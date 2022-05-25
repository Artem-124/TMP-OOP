from enum import Enum

class Film:
    def __init__(self, type):
        self.title = ''
        self.type = type
        self.void = None

    def get_from_file(self, file):
        self.title = file.readline()
        if self.type == 1:
            self.void = Feature()
            self.director = file.readline()
        if self.type == 2:
            self.void = Cartoon()
            self.wayToCreate = wayToCreate(int(file.readline()))

    def record_to_file(self, file):
        file.write(self.title)
        if self.type == 1:
            file.write("Художественный фильм\n")
            file.write(f"Режиссер: {self.director}")
        if self.type == 2:
            file.write("Мультфильм\n")
            if self.wayToCreate == wayToCreate.drawn:
                file.write("Рисованный\n")
            if self.wayToCreate == wayToCreate.puppet:
                file.write("Кукольный\n")
            if self.wayToCreate == wayToCreate.plasticine:
                file.write("Пластилиновый\n")    
        file.write('\n')     

class Feature:
    def __init__(self):
        self.director = ""

class Cartoon:
    def __init__(self):
        self.wayToCreate = None

class wayToCreate(Enum):
    drawn = 1
    puppet = 2
    plasticine = 3