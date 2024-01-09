import io
import os
from datetime import timedelta
from dotenv import load_dotenv

from minio import Minio

from schemas.pet_schema import PhotoCreate


def connect_to_minio():
    load_dotenv('src')
    print(os.getenv('ACCESSKEY'))
    MY_ENV_VAR = os.getenv('MY_ENV_VAR')
    client = Minio("localhost:9000",
                   access_key="nyjnzw6WYUd5xSUAzUvc",
                   secret_key="L8tMNjLno5hGXuOZMDi6w7aFizK78l8n3QwiE7Rw",
                   secure=False
                   )
    return client


def get_files_minio(file: str, bucket_name: str = "img"):

    client = connect_to_minio()
    return client.presigned_get_object(bucket_name, file, expires=timedelta(hours=3))


def creat_files_minio_files(file: PhotoCreate, filename: str, bucket_name: str = "img"):
    client = connect_to_minio()
    client.put_object(bucket_name, filename, io.BytesIO(file), length=io.BytesIO(file).getbuffer().nbytes)
    url = client.presigned_get_object(bucket_name, filename, expires=timedelta(hours=3))
    return url
