from enum import Enum

class Film:
    def __init__(self):
        self.title = ''
        self.country = ''
        self.type = 0

    @staticmethod
    def get_from_file(type, file):
        if type == 1:
            film = Feature() 
        if type == 2:
            film = Cartoon()
        if type == 3:
            film = Doсumentary()
        film.type = type
        film.read_from_file(file) 
        return film
    
    def read_from_file_general(self, file):
        self.title = file.readline()
        self.country = file.readline()

    def record_to_file_general(self, file):
        file.write(self.title)
        file.write(f"Страна: {self.country}")
        file.write(f"Количество гласных в названии: {self.number_of_voves()}\n")

    def number_of_voves(self):
        voves = 'аеёиоуыэюя'
        num = 0
        for letter in self.title:
            if letter in voves:
                num += 1
        return num      

class Feature(Film):
    def __init__(self):
        super().__init__()
        self.director = ""

    def read_from_file(self, file):
        super().read_from_file_general(file)
        self.director = file.readline()

    def record_to_file(self, file):
        super().record_to_file_general(file)
        file.write("Художественный фильм\n")
        file.write(f"Режиссер: {self.director}")
        file.write('\n') 

class Cartoon(Film):
    def __init__(self):
        super().__init__()
        self.wayToCreate = None

    def read_from_file(self, file):
        super().read_from_file_general(file)
        self.wayToCreate = wayToCreate(int(file.readline()))

    def record_to_file(self, file):
        super().record_to_file_general(file)
        file.write("Мультфильм\n")
        if self.wayToCreate == wayToCreate.drawn:
            file.write("Рисованный\n")
        if self.wayToCreate == wayToCreate.puppet:
            file.write("Кукольный\n")
        if self.wayToCreate == wayToCreate.plasticine:
            file.write("Пластилиновый\n")
        file.write('\n') 

class Doсumentary(Film):
    def __init__(self):
        super().__init__()
        self.year = 1900

    def read_from_file(self, file):
        super().read_from_file_general(file)
        self.year = int(file.readline())

    def record_to_file(self, file):
        super().record_to_file_general(file)
        file.write("Документальный фильм\n")
        file.write(f"Год: {self.year}\n")
        file.write('\n')            

class wayToCreate(Enum):
    drawn = 1
    puppet = 2
    plasticine = 3