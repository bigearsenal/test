"""  Задание 4.3  

Получить из строки CONFIG список VLANов вида: ['1', '3', '10', '20', '30', '100']
Ограничение: Все задания надо выполнять используя только пройденные темы.
Задания
135
CONFIG = 'switchport trunk allowed vlan 1,3,10,20,30,100'"""


CONFIG = 'switchport trunk allowed vlan 1,3,10,20,30,100'

CONFIG = CONFIG.split(' ')

VLAN = CONFIG[4].split(',')

print(VLAN)
