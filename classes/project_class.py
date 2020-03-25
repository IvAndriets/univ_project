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

    def get_id(self):
        return self.project_id

    def get_name(self):
        return self.project_name

    def gat_project_rate(self):
        return self.project_rate

    def get_date(self):
        return self.update_date

    def update(self, staff_class):
        self.project_id = staff_class.get_id()
        self.project_name = staff_class.get_name()
        self.project_rate = staff_class.gat_project_rate()
        self.update_date = staff_class.get_date()

    def get_all_info(self):
        return {'project_id': self.project_id, 'project_name': self.project_name, 'project_rate': self.project_rate}


def in_projects_search(project, list_to_search):
    for i in list_to_search:
        if i.get_name() == project:
            return False
    return Exception


def in_project_search_by_id(project_id, list_to_search):
    for i in list_to_search:
        if i.get_id() == project_id:
            return i
    return Exception


def search_project_for_index(project_id, list_to_search):
    for i in range(len(list_to_search)):
        if list_to_search[i].get_id() == project_id:
            return i
    return Exception
