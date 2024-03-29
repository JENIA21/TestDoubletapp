import io

from datetime import timedelta

from minio import Minio

from src.config.minio_config import settings_minio


def connect_to_minio():

    client = Minio("minio:9000",
                   access_key=settings_minio.ACCESS_KEY,
                   secret_key=settings_minio.SECRET_KEY,
                   secure=False
                   )
    return client


def get_files_minio(file: str, bucket_name: str = "img"):

    client = connect_to_minio()
    return client.presigned_get_object(bucket_name, file, expires=timedelta(hours=3))


def creat_files_minio_files(file: object, filename: str, bucket_name: str = "img"):
    client = connect_to_minio()
    client.put_object(bucket_name, filename, io.BytesIO(file), length=io.BytesIO(file).getbuffer().nbytes)
    url = client.presigned_get_object(bucket_name, filename, expires=timedelta(hours=3))
    return url


def delete_files_minio_files(filename: object, bucket_name: str = "img"):
    client = connect_to_minio()
    for name_img in filename:
        client.remove_object(bucket_name, name_img.id_photo)
