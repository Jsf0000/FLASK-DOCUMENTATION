from app import db

class Person(db.Model):

    __tablename__ = 'people'

    pid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    age = db.Column(db.Integer)
    job = db.Column(db.Text)

    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job

# flask db init
# flask db migrate
# flask db upgrade
