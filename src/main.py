import graphene
from fastapi import FastAPI
from starlette.graphql import GraphQLApp
from products.mutaion import ProductMutation
app = FastAPI()

app.add_route("/graphql",GraphQLApp(schema=graphene.Schema(mutation=ProductMutation)))
