# Spotify ETL Pipeline on AWS

## Overview

Built an end-to-end event-driven ETL pipeline on AWS for Spotify music analytics.

## Architecture

CSV Files → Amazon S3 → AWS Lambda → AWS Glue → Parquet Files → Glue Crawler → Athena → Tableau Dashboard

## Tech Stack

* Amazon S3
* AWS Lambda
* AWS Glue
* AWS Glue Crawler
* Amazon Athena
* PySpark
* Tableau Public

## Workflow

1. Raw CSV data uploaded to S3
2. S3 event triggers Lambda
3. Lambda starts Glue ETL job
4. Glue transforms and cleans data
5. Data stored in Parquet format
6. Glue crawler updates schema
7. Athena performs analytics
8. Tableau dashboard visualizes insights

## Key Insights

* Rock has highest song count
* Electronic has highest artist count
* Pop has highest average followers
* Pop has highest average popularity
