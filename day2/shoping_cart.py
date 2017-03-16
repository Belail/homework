#-*-coding:utf-8-*-
#env/python3
#folw_chart : https://www.processon.com/view/link/58ca999be4b056e8c628b2bf
from prettytable import PrettyTable
from random import randint

# purse = input('Enter the amount of money you have:')
goods = {'轰炸机':300000000,'坦克':100000000,'直升机':20000000,'迫击炮':100000,'AK-47':5000,'M4':4000}
header = ['SN', 'Name', 'Price','Number']
total_money = 0

def print_goods():
    goods_pt = PrettyTable()
    goods_pt._set_field_names(header)
    for nums,item in enumerate(goods.items(),start=1):
        goods_pt.add_row([nums,item[0],item[1],randint(1,100)])
    print(goods_pt)




print_goods()
