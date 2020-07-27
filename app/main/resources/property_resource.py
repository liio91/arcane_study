from flask_restful import Resource

# from ..models.property_model import Property, properties_schema


class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String())

    def __repr__(self):
        return '<Property %s>' % self.title


class PropertySchema(ma.Schema):
    class Meta:
        fields = ("id", "title", "content")


property_schema = PropertySchema()
properties_schema = PropertySchema(many=True)


class PropertyListResource(Resource):
    def get(self):
        properties = Property.query.all()
        return properties_schema.dump(properties)
