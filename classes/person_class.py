from app import db


class Staff(db.Model):
    __tablename__ = 'staff'

    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    second_name = db.Column(db.String)
    surname = db.Column(db.String)

    def __init__(self, person_id, name, second_name, surname):
        self.id = person_id
        self.name = name
        self.second_name = second_name
        self.surname = surname

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'second_name': self.second_name,
            'surname': self.surname
        }

