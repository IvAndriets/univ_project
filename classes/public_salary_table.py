from app import db
import datetime


class MonthTimeSheet(db.Model):
    __tablename__ = 'month_salary_timesheet'

    id = db.Column(db.String, primary_key=True)
    person_id = db.Column(db.String, db.ForeignKey('staff.id', ondelete='RESTRICT'))
    person = db.relationship('Staff', backref="month_timesheet_staff")
    salary = db.Column(db.String)
    period_start = db.Column(db.String)
    period_end = db.Column(db.String)
    create_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self, id, person_id, period_start, period_end, salary):
        self.id = id
        self.person_id = person_id
        self.salary = salary
        self.period_start = period_start
        self.period_end = period_end

    @property
    def serialize(self):
        return {
            'id': self.id,
            'person': self.person.name,
            'salary': self.salary,
            'pStart': self.period_start,
            'pEnd': self.period_end
        }
