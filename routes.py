from flask import request, jsonify

from models import Person
from app import ma


class PeopleSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Person
        load_instance = True


peopleSchema = PeopleSchema()
peopleSchemaMany = PeopleSchema(many=True)


def register_routes(app, db):
    @app.route('/', methods = ['GET', 'POST'])
    def index():
        if request.method == 'POST':
            person = Person(request.json['name'], request.json['age'], request.json['job'])
            db.session.add(person)
            db.session.commit()
            return peopleSchema.jsonify(person)
        elif request.method == 'GET':
            people = Person.query.all()
            result = peopleSchemaMany.dump(people)
            return jsonify(result)

    @app.route('/<user_id>', methods=['PUT', 'GET', 'DELETE'])
    def user_operations(user_id):
        if request.method == 'PUT':
            person = Person.query.get(user_id)
            person.name = request.json['name']
            person.age = request.json['age']
            person.job = request.json['job']
            db.session.commit()
            return peopleSchema.jsonify(person)
        elif request.method == 'GET':
            person = Person.query.get(user_id)
            return peopleSchema.jsonify(person)
        elif request.method == 'DELETE':
            person = Person.query.get(user_id)
            db.session.delete(person)
            db.session.commit()
            return jsonify({"msg": f"Deleted User {user_id}"})



