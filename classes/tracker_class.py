class Time:
    def __init__(self, per_id, pro_id, time):
        self.per_id = per_id
        self.pro_id = pro_id
        self.time = time

    def per_id(self):
        return self.per_id

    def pro_id(self):
        return self.pro_id

    def time(self):
        return self.time

    def get_all_info(self):
        return {"person_id": self.per_id, "project_id": self.pro_id, "hours_worked": self.time}
