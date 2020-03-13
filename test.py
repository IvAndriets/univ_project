class Person:
    def __init__(self, per_id, name, second_name, surname):
        self.id = per_id
        self.name = name
        self.second_name = second_name
        self.surname = surname

    def get_info(self):
        return {self.id: [self.name, self.second_name, self.surname]}


staff_list = [
    Person(11111111, 'name1', 'second_name1', 'surname1'),
    Person(11111112, 'name2', 'second_name2', 'surname2'),
    Person(11111113, 'name3', 'second_name3', 'surname3'),
    Person(11111114, 'name4', 'second_name4', 'surname4'),
    Person(11111115, 'name5', 'second_name5', 'surname5')

]
x = [i.get_info() for i in staff_list]
if Person(11111115, 'name5', 'second_name5', 'surname5').get_info() in x:
    print('inc')
else:
    print("not inc")

print(x)
