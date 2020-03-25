from app import db


class Time(db.Model):
    __tablename__ = 'time'

    id = db.Column(db.String, primary_key=True)
    per_id = db.Column(db.String)
    pro_id = db.Column(db.String)
    time = db.Column(db.String)

    def __init__(self, id, per_id, pro_id, time):
        self.id = id
        self.per_id = per_id
        self.pro_id = pro_id
        self.time = time

    @property
    def serialize(self):
        return {
            'id': self.id,
            'per_id': self.per_id,
            'pro_id': self.pro_id,
            'time': self.time
        }
