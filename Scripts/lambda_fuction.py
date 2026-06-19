import boto3

glue = boto3.client("glue")

def lambda_handler(event, context):

    response = glue.start_job_run(
        JobName="music-etl-job"
    )

    print(response)

    return {
        "statusCode": 200,
        "jobRunId": response["JobRunId"]
    }