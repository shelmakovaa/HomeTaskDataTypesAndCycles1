# Мы делаем MVP dating-сервиса, и у нас есть список парней и девушек.
# Выдвигаем гипотезу: лучшие рекомендации мы получим, если просто отсортируем имена по алфавиту и познакомим людей с одинаковыми индексами после сортировки! Но мы не будем никого знакомить, если кто-то может остаться без пары:
#
# Примеры работы программы:
# 1.
#
# boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
# girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
# Результат:
#
# Идеальные пары:
# Alex и Emma
# Arthur и Kate
# John и Kira
# Peter и Liza
# Richard и Trisha
# boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard', 'Michael']
# for i in range(len(boys)):
#     print(sorted(boys)[i])
# girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
# Результат:
# Внимание, кто-то может остаться без пары!

boys = list(input('Введите имена парней через пробел: ').split())
girls = list(input('Введите имена девушек через пробел: ').split())

if len(boys) != len(girls):
    print('Внимание, кто-то может остаться без пары!')
else:
    print('Идеальные пары:')
    for i in range(len(boys)):
        print(sorted(boys)[i], ' и ', sorted(girls)[i])