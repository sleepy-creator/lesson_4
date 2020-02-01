#1) Напишите функцию (F): на вход список имен и целое число N; на выходе список длины N случайных имен из первого списка (могут повторяться, можно взять значения: количество имен 20, N = 100, рекомендуется использовать функцию random)
import random
def choice_name(Names, N):
    return random.choices(Names, k=N)

names=['Nikita', 'John', 'Mark', 'Liza', 'Vika', 'Andrew', 'Kolya', 'Kate', 'Peter', 'Bill', 'Bob', 'Liza', 'Maria', 'Alex', 'Nastya', 'Vova', 'Veronika', 'Kate', 'Nikita', 'Lena']

new_list = choice_name(names, N=100)

print(new_list)

# 2) Напишите функцию вывода самого частого имени из списка на выходе функции F
def popular_name(listname):
    dict = {}
    for name in listname:
        dict[name] = dict.get(name,0) + 1
    dict = list(dict.items())
    dict.sort(key=lambda x: x[1], reverse=True)

    return dict[0][0]

print(popular_name(new_list))

# 3) Напишите функцию вывода самой редкой буквы, с которого начинаются имена в списке на выходе функции F

def rare_name(list2):
    new_dict = {}
    for name in list2:
        for char in name:
            if char.isupper():
                new_dict[char] = new_dict.get(char, 0) + 1
            else: continue
    new_dict = list(new_dict.items())
    new_dict.sort(key=lambda x: x[1])
    return new_dict[0][0]
print(rare_name(new_list))