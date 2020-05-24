from app import db
import datetime


class Staff(db.Model):
    __tablename__ = 'staff'

    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    position_id = db.Column(db.String, db.ForeignKey('position.id', ondelete='RESTRICT'))
    position = db.relationship("Position", backref="position_staff")
    surname = db.Column(db.String)

    create_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self, person_id, name, surname, position_id):
        self.id = person_id
        self.name = name
        self.position_id = position_id
        self.surname = surname

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'surname': self.surname,
            'position': self.position.name,
            'positionId': self.position_id,
            'createAt': self.create_at,
            'updateAt': self.updated_at
        }
