#Сколько найдено файлов, не содержащих цифр в названии.
#Кроме этого, программа должна выводить на экран названия всех файлов или папок,
#которые она нашла, без повторов


import os


numbers = '1234567890'


def list_of_folders():
    files = {}
    for f in os.listdir():
        if f in files:
            files[f] += 1
        else:
            files[f] = 1
    return files


def no_numbers(files):
    clean_files = {}
    for f in files:
        t = 0 
        for number in numbers:
            if number in f:
                t += 1
        if f in clean_files and t == 0:
            clean_files[f] += 1
        elif f not in clean_files and t == 0:
            clean_files[f] = 1
    return clean_files
            


def print_out(clean_files, files):
    n = 0
    for f in clean_files:
        n += 1
    print(n)
    for fi in files:
        print(fi)
        


def main():
    files = list_of_folders()
    clean_files = no_numbers(files)
    print_out(clean_files, files)


main()
