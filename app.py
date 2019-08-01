import re
import json
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app, prefix='/api')
class DefangResource(Resource):
    def get(self, path):
        defang = path.replace('http', 'hxxp', 1).replace('.', '[.]').replace('//', '||')
        return {'path': path, 'defang': defang}

class RefangResource(Resource):
    def get(self, path):
        refang = path.replace('hxxp', 'http', 1).replace('[.]', '.').replace('||', '//')
        return {'path': path, 'refang': refang}

api.add_resource(DefangResource, '/defang/<path:path>')
api.add_resource(RefangResource, '/refang/<path:path>')

if __name__ == '__main__':
    app.run(debug=True)