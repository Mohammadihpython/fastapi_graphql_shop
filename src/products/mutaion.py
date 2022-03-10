import shutil
import uuid

from graphene_file_upload.scalars import Upload
import graphene
from db_conf import db_session
import models
from werkzeug.utils import secure_filename
from .types import ProductType
db = db_session.session_factory()


class CreateProduct(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        total = graphene.Int(required=True)
        description = graphene.String(required =True)
        image = Upload(required=True)
        price = graphene.String(requied=True)

    success = graphene.Boolean()

    @staticmethod
    def mutate(self, info, image, **kwargs):
        try:
            filename = f"media/product_image/{uuid.uuid1()}_{secure_filename(image.filename)}"
            db_product = models.Products(
                name = kwargs["name"],
                description = kwargs["description"],
                total = kwargs["total"],
                price =kwargs["price"],
                image = filename
            )
            with open(f"{filename}",'wd') as buffer:
                shutil.copyfileobj(image.file,buffer)
            db.add(db_product)
            db.commit()
            db.refresh(db_product)
            success = True
            return CreateProduct(success=success)
        except ValueError:
            return  CreateProduct(success=False)


class ProductMutation(graphene.ObjectType):
    create_product = CreateProduct.Field()
