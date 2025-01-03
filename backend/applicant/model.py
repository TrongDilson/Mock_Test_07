class Applicant:
    def __init__(self, name, age, classes):
        self.name = name
        self.age = age
        self.classes = classes

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "classes": self.classes
        }
