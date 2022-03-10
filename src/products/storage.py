import functools

from sqlalchemy_media import StoreManager, FileSystemStore
import json

from sqlalchemy import TypeDecorator, Unicode


TEMP_PATH = '/tmp/sqlalchemy-media'
StoreManager.register(
    'fs',
    functools.partial(FileSystemStore, TEMP_PATH, 'http://static.example.org/'),
    default=True
)



class Json(TypeDecorator):
    impl = Unicode

    def process_bind_param(self, value, engine):
        return json.dumps(value)

    def process_result_value(self, value, engine):
        if value is None:
            return None

        return json.loads(value)
    
    
from sqlalchemy_media import Image, ImageAnalyzer, ImageValidator, ImageProcessor

class ProfileImage(Image):
    __pre_processors__ = [
        ImageAnalyzer(),
        ImageValidator(
            minimum=(80, 80),
            maximum=(800, 600),
            min_aspect_ratio=1.2,
            content_types=['image/jpeg', 'image/png','image/jpg']
        ),
        ImageProcessor(
            fmt='jpeg',
            width=120,
            crop=dict(
                left='10%',
                top='10%',
                width='80%',
                height='80%',
            )
        )
    ]    