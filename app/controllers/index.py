from flask_restful import Resource


class IndexView(Resource):

    def get(self):
        return dict(status="success", message="Welcome to the API")
