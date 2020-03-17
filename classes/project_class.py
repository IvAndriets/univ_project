class Project:
    def __init__(self, project_id, project_name, project_rate):
        self.project_id = project_id
        self.project_name = project_name
        self.project_rate = project_rate

    def get_id(self):
        return self.project_id

    def get_name(self):
        return self.project_name

    def gat_project_rate(self):
        return self.project_rate

    def get_all_info(self):
        return {self.project_id: [self.project_name, self.project_rate]}
