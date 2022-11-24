import time
from io import StringIO

import boto3


class S3Client:
    def __init__(self, aaki, asak) -> None:
        self.client = boto3.client("s3", aws_access_key_id=aaki, aws_secret_access_key=asak)

    def upload_df(self, df) -> None:
        csv_buffer = StringIO()
        df.to_csv(csv_buffer, index=False)
        self.client.put_object(
            Bucket="game-scanner113112",
            Key=f"{int(time.time())}_games.csv",
            Body=csv_buffer.getvalue(),
        )
