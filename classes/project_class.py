from app import db


class Project(db.Model):
    __tablename__ = 'project'

    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    rate = db.Column(db.String)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'rate': self.rate
        }

    def __init__(self, project_id, project_name, project_rate):
        self.id = project_id
        self.name = project_name
        self.rate = project_rate
