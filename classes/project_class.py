from app import db
import datetime


class Project(db.Model):
    __tablename__ = 'project'

    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    create_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'createAt': self.create_at,
            'updateAt': self.updated_at
        }

    def __init__(self, project_id, project_name):
        self.id = project_id
        self.name = project_name
