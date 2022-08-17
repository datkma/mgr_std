class Student:

    count = 0

    def __init__(self, id, name):
        self.id = id
        self.name = name
        Student.count += 1

    # def set_id(self, id):
    #    self.id = id

    def get_id(self):
        return self.id

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.id

    def show_infor(self):
        print(f"ID: {self.get_id()}")
        print(f"Tên sinh viên: {self.name}")

