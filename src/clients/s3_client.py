import boto3


class S3Client:
    def __init__(self) -> None:
        self.client = boto3.client("s3")

    def upload_file(self, file) -> str:
        self.client.upload_file()
