from flask import Flask
from bson import ObjectId
import json

from flask_cors import CORS

from Routers.persons import persons

class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if (isinstance(obj, ObjectId)):
            return str(obj)
        return json.JSONEncoder.default(self,obj)

app = Flask(__name__)

CORS(app)


app.url_map.strict_slashes = False

app.json_encoder = JSONEncoder


app.register_blueprint(persons, url_prefix="/persons/")

app.run()