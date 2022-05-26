from enum import Enum

class Film:
    def __init__(self):
        self.title = ''

    @staticmethod
    def get_from_file(type, file):
        if type == 1:
            film = Feature() 
        if type == 2:
            film = Cartoon()
        if type == 3:
            film = Doсumentary()
        film.read_from_file(file) 
        return film
    
    def record_to_file(self, file):
        pass
   

class Feature(Film):
    def __init__(self):
        super().__init__()
        self.director = ""

    def read_from_file(self, file):
        self.title = file.readline()
        self.director = file.readline()

    def record_to_file(self, file):
        file.write(self.title)
        file.write("Художественный фильм\n")
        file.write(f"Режиссер: {self.director}")
        file.write('\n') 

class Cartoon(Film):
    def __init__(self):
        super().__init__()
        self.wayToCreate = None

    def read_from_file(self, file):
        self.title = file.readline()
        self.wayToCreate = wayToCreate(int(file.readline()))

    def record_to_file(self, file):
        file.write(self.title)
        file.write("Мультфильм\n")
        if self.wayToCreate == wayToCreate.drawn:
            file.write("Рисованный\n")
        if self.wayToCreate == wayToCreate.puppet:
            file.write("Кукольный\n")
        if self.wayToCreate == wayToCreate.plasticine:
            file.write("Пластилиновый\n")
        file.write('\n') 

class Doсumentary:
    def __init__(self):
        super().__init__()
        self.year = 1900

    def read_from_file(self, file):
        self.title = file.readline()
        self.year = int(file.readline())

    def record_to_file(self, file):
        file.write(self.title)
        file.write("Документальный фильм\n")
        file.write(f"Год: {self.year}\n")
        file.write('\n')            

class wayToCreate(Enum):
    drawn = 1
    puppet = 2
    plasticine = 3