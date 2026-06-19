from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Initialize Spark
spark = SparkSession.builder.appName("MusicETL").getOrCreate()

bucket = "music-etl-pipeline-diva-232621644823-ap-southeast-2-an"

print("Starting ETL pipeline...")

# -------------------------
# Load Data
# -------------------------
songs_df = spark.read.option("header", "true") \
    .option("inferSchema", "true") \
    .csv(f"s3://{bucket}/raw-data/songs1.csv")

artists_df = spark.read.option("header", "true") \
    .option("inferSchema", "true") \
    .csv(f"s3://{bucket}/raw-data/artists1.csv")

print("Datasets loaded successfully.")

# -------------------------
# Select Useful Columns Only
# -------------------------
songs_df = songs_df.select(
    "id",
    "name",
    "album_name",
    "artists",
    "genre"
)

artists_df = artists_df.select(
    "id",
    "name",
    "followers",
    "popularity",
    "genre"
)

# -------------------------
# Remove Duplicates + Nulls
# -------------------------
songs_df = songs_df.dropDuplicates()
artists_df = artists_df.dropDuplicates()

songs_df = songs_df.dropna(subset=["id", "name"])
artists_df = artists_df.dropna(subset=["id", "name"])

# -------------------------
# Validate Data
# -------------------------
print("Songs count:", songs_df.count())
print("Artists count:", artists_df.count())

songs_df.printSchema()
artists_df.printSchema()

# -------------------------
# Write Parquet
# -------------------------
songs_df.write.mode("overwrite").parquet(
    f"s3://{bucket}/processed-data/songs/"
)

artists_df.write.mode("overwrite").parquet(
    f"s3://{bucket}/processed-data/artists/"
)

print("ETL completed successfully.")