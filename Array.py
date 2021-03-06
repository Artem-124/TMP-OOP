from Film import Film

class Array:
    def __init__(self, max_size):
        self.size = 0
        self.content = []
        self.max_size = max_size

    def append(self, element):
        if self.size < self.max_size:
            self.size += 1
            self.content.append(element)
        else:
            print("Массив уже заполнен! Элемент не будет записан")

    def clear(self):
        self.size = 0
        self.content = []

    def fill(self, file):
        type = file.readline()
        while type != '' and type != '\n':
            film = Film.get_from_file(int(type), file)
            self.append(film)
            type = file.readline()

    def record_to_file(self, file):
        file.write(f"Записано {self.size} фильмов\n\n")
        for i in range(self.size):
            self.content[i].record_to_file(file)

    def sort(self):
        for j in range(1, self.size):
            for i in range(self.size - j):
                if comparator(self.content[i], self.content[i + 1]):
                    self.content[i], self.content[i + 1] = self.content[i + 1], self.content[i]
    
    def only_one_type_record_to_file(self, file, type):
        if type == 0:
            self.record_to_file(file)
            return
        num = 0
        for i in range(self.size):
            if self.content[i].type == type:
                self.content[i].record_to_file(file)
                num += 1
        if num == 1:
            file.write(f"\nЗаписан {num} фильм\n")
        if num > 1 and num <= 4:
            file.write(f"\nЗаписано {num} фильма\n")
        if num >= 5:
            file.write(f"\nЗаписано {num} фильмов\n")


def comparator(a, b):
    return a.number_of_vowels() > b.number_of_vowels() 