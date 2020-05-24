from app import db


class Position(db.Model):
    __tablename__ = 'position'

    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    salary = db.Column(db.String)
    working_time = db.Column(db.INT)

    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'salary': self.salary,
            'working_time': self.working_time
        }
