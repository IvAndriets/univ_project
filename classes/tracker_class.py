from app import db


class Time(db.Model):
    __tablename__ = 'time'

    id = db.Column(db.String, primary_key=True)
    staff_id = db.Column(db.String, db.ForeignKey('staff.id'))
    staff_surname = db.relationship("Staff", backref="time_staff")
    project_id = db.Column(db.String, db.ForeignKey('project.id'))
    project_name = db.relationship("Project", backref="time_project")
    time = db.Column(db.String)

    def __init__(self, id, staff_id, project_id, time):
        self.id = id
        self.staff_id = staff_id
        self.project_id = project_id
        self.time = time

    @property
    def serialize(self):
        return {
            'id': self.id,
            'staff_id': self.staff_id,
            'staff_surname': self.staff_surname.surname,
            'project_id': self.project_id,
            'project_name': self.project_name.name,
            'time': self.time
        }
