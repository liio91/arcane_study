

from flask import Flask, request
from flask_migrate import Migrate
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///arcane.db'
db = SQLAlchemy(application)
migrate = Migrate(application, db)
ma = Marshmallow(application)
api = Api(application)


class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String())
    type = db.Column(db.Integer())
    city_id = db.Column(db.Integer())
    room = db.Column(db.Integer)
    characteristic = db.Column(db.String())
    owner_id = db.Column(db.Integer())

    def __repr__(self):
        return '<Property %s>' % self.title


class PropertySchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "description", "type", "city_id", "room", "characteristic", "owner_id")


property_schema = PropertySchema()
properties_schema = PropertySchema(many=True)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(50))
    lastName = db.Column(db.String(50))
    birthday = db.Column(db.Date())


class UserSchema(ma.Schema):
    class Meta:
        fields = ("id", "firstName", "lastName", "birthday")


user_schema = UserSchema()
users_schema = UserSchema(many=True)


class PropertyListResource(Resource):
    def get(self):
        properties = Property.query.all()
        return properties_schema.dump(properties)

    def post(self):
        if 'name' not in request.json or \
                'description' not in request.json or \
                'type' not in request.json or \
                'city_id' not in request.json or \
                'room' not in request.json or \
                'characteristic' not in request.json or \
                'owner_id' not in request.json:
            return None, 400

        new_property = Property(
            name=request.json['name'],
            description=request.json['description'],
            type=request.json['type'],
            city_id=request.json['city_id'],
            room=request.json['room'],
            characteristic=request.json['characteristic'],
            owner_id=request.json['owner_id']
        )
        db.session.add(new_property)
        db.session.commit()
        return property_schema.dump(new_property), 201


class PropertyResource(Resource):
    def get(self, property_id):
        property = Property.query.get_or_404(property_id)
        return property_schema.dump(property)

    def patch(self, property_id):
        property = Property.query.get_or_404(property_id)

        if 'name' in request.json:
            property.name = request.json['name']
        if 'description' in request.json:
            property.description = request.json['description']
        if 'type' in request.json:
            property.type= request.json['type']
        if 'city_id' in request.json:
            property.city_id = request.json['city_id']
        if 'room' in request.json:
            property.room = request.json['room']
        if 'characteristic' in request.json:
            property.characteristic = request.json['characteristic']

        db.session.commit()
        return property_schema.dump(property)


class UserListResource(Resource):
    def get(self):
        users = User.query.all()
        return users_schema.dump(users)

    def post(self):
        if 'firstName' not in request.json or \
                'lastName' not in request.json or \
                'birthday' not in request.json:
            return None, 400

        try:
            from datetime import datetime
            date = datetime.strptime(request.json['birthday'], '%Y-%m-%d').date()
        except Exception as e:
            return None, 400

        new_user = User(
            firstName=request.json['firstName'],
            lastName=request.json['lastName'],
            birthday=date
        )
        db.session.add(new_user)
        db.session.commit()
        return user_schema.dump(new_user), 201


class UserResource(Resource):
    def get(self, user_id):
        user = User.query.get_or_404(user_id)
        return user_schema.dump(user)

    def patch(self, user_id):
        user = User.query.get_or_404(user_id)

        if 'firstName' in request.json:
            user.firstName = request.json['firstName']
        if 'lastName' in request.json:
            user.description = request.json['lastName']
        if 'birthday' in request.json:
            try:
                from datetime import datetime
                user.birthday = datetime.strptime(request.json['birthday'], '%Y-%m-%d').date()
            except Exception as e:
                return None, 400

        db.session.commit()
        return user_schema.dump(user)


api.add_resource(PropertyListResource, '/properties')
api.add_resource(PropertyResource, '/property/<int:property_id>')
api.add_resource(UserListResource, '/users')
api.add_resource(UserResource, '/user/<int:user_id>')


if __name__ == '__main__':
    application.run(debug=True)
