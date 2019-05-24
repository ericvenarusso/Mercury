import os
import boto3

class AWSTools:


    def __init__(self, service, acces_key, secret_key):
        """
        Instantiate AWS client object.
        
        Parameters
        ----------
        service : string
            String that indentify the AWS service.
        
        acces_key: string
            String that indentify the AWS acess key.

        secret_key: string
            String that indentify the AWS secret key.
        """
        
        self.client = boto3.client(
            service,
            aws_access_key_id=acces_key,
            aws_secret_access_key=secret_key,
        )

    def upload(self, file_path, bucket_name, file_name):
        """
        Upload a file to AWS S3.
        
        Parameters
        ----------
        file_path : string
            String that indetify the file path.
        
        bucket_name: string
            String that indentify AWS S3 Bucket.

        file_name: string
            String that identify the name of the file that
            will be upload on S3.
        """

        self.client.upload_file(file_path, bucket_name, file_name)