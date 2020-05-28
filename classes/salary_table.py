from app import db
import datetime


class TableSalary(db.Model):
    __tablename__ = 'salary_table'

    id = db.Column(db.String, primary_key=True)
    person_id = db.Column(db.String,  db.ForeignKey('staff.id'))
    person = db.relationship('Staff', backref="salary_staff")
    salary = db.Column(db.INT)
    periodstart = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    periodend = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    create_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self, id, person_id, salary, period_start, period_end):
        self.id = id
        self.person_id = person_id
        self.salary = salary
        self.periodstart = period_start
        self.periodend = period_end

    @property
    def serialize(self):
        return {
            'id': self.id,
            'personId': self.person_id,
            'surname': self.person.surname,
            'salary': self.salary,
            'periodStart': self.periodstart,
            'periodEnd': self.periodend
        }
