from flask_restful import Api
from app.controllers import (
    IndexView
    )

api = Api()

# Index route
api.add_resource(IndexView, '/')
