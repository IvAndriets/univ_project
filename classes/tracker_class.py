from app import db
import datetime


class TimeTracker(db.Model):
    __tablename__ = 'time_tracker'

    id = db.Column(db.String, primary_key=True)
    staff_id = db.Column(db.String, db.ForeignKey('staff.id', ondelete='RESTRICT'))
    staff_surname = db.relationship("Staff", backref="time_staff")
    project_id = db.Column(db.String, db.ForeignKey('project.id', ondelete='RESTRICT'))
    project_name = db.relationship("Project", backref="time_project")
    position_id = db.Column(db.String, db.ForeignKey('position.id', ondelete='RESTRICT'))
    position = db.relationship("Position", backref="time_position")
    work_type_id = db.Column(db.String, db.ForeignKey('work_types.id', ondelete='RESTRICT'))
    work_type = db.relationship("WorkType", backref="time_work_type")

    time = db.Column(db.String)
    create_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    head_id = db.Column(db.String, db.ForeignKey('month_salary_timesheet.id', ondelete='CASCADE'))

    def __init__(self, id, staff_id, project_id, work_type_id, position_id, time, head_id):
        self.id = id
        self.staff_id = staff_id
        self.project_id = project_id
        self.work_type_id = work_type_id
        self.position_id = position_id
        self.time = time
        self.head_id = head_id

    @property
    def serialize(self):
        return {
            'id': self.id,
            'staffId': self.staff_id,
            'staffSurname': self.staff_surname.surname,
            'projectId': self.project_id,
            'workTypeId': self.work_type_id,
            'workType': self.work_type.name,
            'workTypeMod': self.work_type.salary_mod,
            'projectName': self.project_name.name,
            'positionId': self.position_id,
            'positionSalary': self.position.salary,
            'createAt': self.create_at,
            'time': self.time,
            'headId': self.head_id
        }
