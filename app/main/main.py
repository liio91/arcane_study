from flask import Flask
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# from .resources.property_resource import PropertyListResource
# from .resources.property_resource import PropertyListResource

application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///arcane.db'
db = SQLAlchemy(application)
ma = Marshmallow(application)
api = Api(application)


class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String())
    type = db.Column(db.Integer)

    def __repr__(self):
        return '<Property %s>' % self.title


class PropertySchema(ma.Schema):
    class Meta:
        fields = ("id", "title", "content", "type")


property_schema = PropertySchema()
properties_schema = PropertySchema(many=True)


class PropertyListResource(Resource):
    def get(self):
        properties = Property.query.all()
        return properties_schema.dump(properties)


api.add_resource(PropertyListResource, '/properties')

if __name__ == '__main__':
    application.run(debug=True)
