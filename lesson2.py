# def calc(num1, num2, simbol):
#     if simbol == '+':
#         return f'ответ: {num1+num2}'
#     elif simbol == '-':
#         return f'ответ: {num1-num2}'
    
# print(calc(10, 5, '+'))



# from homework_1 import descending_order

# print(descending_order(72097126891))




# dictSlovar = {
#     'apple': 'яблоко',
#     'pen': 'ручка', 
#     'car': 'машина',
# }
# def SearchWord():
#     word = input('Введите слово: ')
#     if word in dictSlovar.keys():
#         return f'слово: {word} перевод: {dictSlovar[word]}'
#     else:
#         return 'нет такого слова'

# def AddWord():
#     k = input('слово на англ: ')
#     v = input('слово на русс: ')
#     dictSlovar[k]=v
#     return dictSlovar

# def deleteWord():
#     d = input('слово которое удаляем: ')
#     if d in dictSlovar:
#         print(f'удалено "{dictSlovar[d]}"')
#         del dictSlovar[d]
#         return dictSlovar
    
# while True:
#     print('* 1: перевести слово')
#     print('* 2: добвавить слово')
#     print('* 3: удалить слово')
#     print('* 4: завершить')
#     x = int(input('Введите число вашего выбора: '))
#     if x == 1:
#       print(SearchWord())
#     elif x == 2:
#         print(AddWord())
#     elif x == 3:
#         print(deleteWord())
#     elif x == 4:
#         print('Завершение программы!')
#         break

cart = {}

pizza = {
    'Пеперони': 250,
    '4 Сыра': 280,
    'Маргарита': 360,
    'Грибная': 230, 
}

def Order():
    o = input('Вы собираетесь сделать заказ?') 
    if o == 'да':
        return True
    elif o == 'нет':
        return False
    
def AddCart():
    pizza_list = list(pizza.keys())[0], [1], [2], [3]
    a = input(f'Наш осортимент: {pizza_list}')
    for i in pizza:
        i = input(f'Хотели бы вы заказать {pizza[0]}?')
        if i == 'да':
            return cart[i] == pizza.value()
        else:
            print(Order())
    return i

def repeatOrder():
    r = input(f'Такой ли вы сделали заказ: {cart}?')
    if r == 'да':
        return True
    elif r == 'нет':
        print(Order())

def Result():
    for i in res:
        res = cart.keys() * cart.values()
    return res

Order()
AddCart()
repeatOrder()
Result()
