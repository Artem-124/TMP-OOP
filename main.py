import sys
from Array import Array

if len(sys.argv) != 3:
    print('\nФайлы ввода/вывода не выбраны! Будут использованы стандартные in.txt и out.txt\n')
    infile = 'in.txt'
    outfile = 'out.txt'
else:
    infile = sys.argv[1]
    outfile = sys.argv[2]

infile = open(infile, 'r', encoding = "utf-8")
a = Array(12)
a.fill(infile)
print(f"В контейнер записано {a.size} фильмов\n")
infile.close()
a.sort()

outfile = open(outfile, 'w', encoding = "utf-8")
a.only_one_type_record_to_file(outfile, 2) #0 - вывод всех типов
outfile.close()
a.clear()