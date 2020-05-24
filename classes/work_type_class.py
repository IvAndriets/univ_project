from app import db


class WorkType(db.Model):
    __tablename__ = 'work_types'

    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    salary_mod = db.Column(db.String)

    def __init__(self, id, name, salary_mod):
        self.id = id
        self.name = name
        self.salary_mod = salary_mod

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'salaryMod': self.salary_mod
        }
