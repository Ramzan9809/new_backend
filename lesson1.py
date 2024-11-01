#1
def bonus_time(salary, bonus):
    return '${}'.format(salary * (10 if True else 1))

print(bonus_time(5000, True))

#2
def points(games):
    count = 0
    for i in games:
        res = i.split(':')
        if res[0]>res[1]:
            count += 3
        elif res[0] == res[1]:
            count += 1
    return count

print(points)

#3
def string_to_array():
    pass

print(string_to_array)

#4
def count_sheep(sheep):
    return sheep.count(True)

print(count_sheep)

#5
def reverse_words(s):
    str1 = ''
    s = s.split()
    s.reverse()
    return ' '.join(s)

print(reverse_words("hello world!"))
    


