from app import db


class Staff(db.Model):
    __tablename__ = 'staff'

    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    second_name = db.Column(db.String)
    surname = db.Column(db.String)

    def __init__(self, person_id, name, second_name, surname):
        self.id = person_id
        self.name = name
        self.second_name = second_name
        self.surname = surname

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'second_nmae': self.second_name,
            'surname': self.surname
        }

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_second_name(self):
        return self.second_name

    def get_surname(self):
        return self.surname

    def get_date(self):
        return self.update_date

    def get_information_about_person(self):
        return {'person_id': self.id, 'name': self.name, 'surname': self.surname, 'second_name': self.second_name}


def in_person_search(surname, list_to_search):
    for i in list_to_search:
        if i.get_surname() == surname:
            return False
    return Exception


def in_person_search_by_id(person_id, list_to_search):
    for i in list_to_search:
        if i.get_id() == person_id:
            return i
    return Exception


def search_for_persons_index(person_id, list_to_search):
    for i in range(len(list_to_search)):
        if list_to_search[i].get_id() == person_id:
            return i
    return Exception


def validator(dict_with_persons_info):
    if 'person_id' in dict_with_persons_info.keys():
        return Exception
    elif dict_with_persons_info["name"] is None:
        return Exception
    elif dict_with_persons_info["second_name"] is None:
        return Exception
    elif dict_with_persons_info["surname"] is None:
        return Exception
