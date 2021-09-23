#!/usr/bin/python
# coding=utf-8
import sys

shopping_car = []
product_list_title = 'Product list'
welcome = 'Welcome to the shopping'
product_list = [
    ('iphone', 3888),
    ('thinkpad', 4888),
    ('coffee', 18),
    ('mac', 6888)
]
print(welcome)
salary = int(input('Please input your salary:'))
while True:
    print(product_list_title)
    for item in product_list:
        print(product_list.index(item) + 1, item)
    print("0. exit")
    choice = input('Please input the name of goods:')
    if choice.isdigit():
        choice = int(choice)
        if choice > 4 or choice < 0:
            print('no such goods,please reselect')
            continue
        elif 4 >= choice >= 1:
            if salary < product_list[choice - 1][1]:
                print('Account balance is insufficient, please buy other products or quit')
                continue
            else:
                shopping_car.append(product_list[choice - 1])  # 将商品添加到购物车
                print('The goods you had buy')
                for goods in shopping_car:
                    print(goods[0], goods[1])
                salary = salary - product_list[choice - 1][1]
                print('Your account balance is %s' % salary)
        elif choice == 0:
            print('Your goods is ')
            for goods in shopping_car:
                print(goods[0], goods[1])
            print('Your balance is', salary)
            sys.exit('Program exit!!!')
    else:
        print("输入有误！")
        continue
