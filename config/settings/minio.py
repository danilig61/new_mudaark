from config.settings import logging
from config.settings.env import env
from minio import Minio

logger = logging.getLogger(__name__)


AWS_ACCESS_KEY_ID = env.str('AWS_ACCESS_KEY_ID', default='')
AWS_SECRET_ACCESS_KEY = env.str('AWS_ACCESS_KEY_ID', default='')
AWS_STORAGE_BUCKET_NAME = env.str('AWS_STORAGE_BUCKET_NAME')
AWS_S3_ENDPOINT_URL = env.str('AWS_S3_ENDPOINT_URL')
AWS_S3_FILE_OVERWRITE = env.bool('AWS_S3_FILE_OVERWRITE', default=False)
AWS_DEFAULT_ACL = env.str('AWS_DEFAULT_ACL', default=None)
AWS_QUERYSTRING_AUTH = env.bool('AWS_QUERYSTRING_AUTH', default=False)


# Инициализация клиента MinIO
minio_client = Minio(
    'minio:9000',
    access_key=env.str('AWS_ACCESS_KEY_ID'),
    secret_key=env.str('AWS_ACCESS_KEY_ID'),
    secure=False
)

# Проверка наличия бакета
if not minio_client.bucket_exists(AWS_STORAGE_BUCKET_NAME):
    minio_client.make_bucket(AWS_STORAGE_BUCKET_NAME)
    logger.info(f"Bucket {AWS_STORAGE_BUCKET_NAME} created.")
else:
    logger.info(f"Bucket {AWS_STORAGE_BUCKET_NAME} already exists.")
