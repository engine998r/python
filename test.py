#class chain_sum(int):
#    def __call__(self, addiction = 0):
#        return chain_sum(self + addiction)
#print(chain_sum(5)(8))
#quote = "How can mirrors be real if our eyes aren't real"

#
#def to_jaden_case(string):
#    a = str.split(string)
#    list_new=[]
#    for i in a:
#        n = (str.capitalize(i))
#        list_new.append(n)
#    print(list_new)    
#    list_new = ' '.join(list_new)
#    return(list_new)
#print(to_jaden_case(quote))


#import os
#import sys

#import subprocess
#cp = subprocess.run()
#cp.
#from operator import truediv
#from os import pread
#from re import A
#from typing import KeysView


#n = int(9)
#def fact(n):
#    if n == 0:
#      return 1
#    else:
#      return fact(n-1)*n
#print(fact(n))

#n=5
#fact=1
#index=1
#while index<=n:
#fact=fact*index
#index=index+1
#print(fact)
#stairway_lenght = int(input('Введите число N \n'))
#current_string = 1
#counter = 1
#if stairway_lenght == 1:
#    print(stairway_lenght)
    
#else:
#    while counter <= stairway_lenght:
#        counter = counter + 1
#        l = len(str(current_string))
#        prev_str = str(current_string)[:l-1][::-1]
#        print(str(current_string) + str(prev_str))
#        current_string = str(current_string) + str(counter)
#    counter = stairway_lenght
#    current_string = str(current_string)[:l-1]  
#    while counter > 0:
#        counter = counter - 1
#        l = len(str(current_string))
#        print(str(current_string) + str(current_string)[:l-1][::-1]) 
#        current_string = str(current_string)[:l-1]       
#else:
#    while counter <= stairway_lenght:
#        counter = counter + 1
##        print(str(current_string).rjust(stairway_lenght))
#        current_string = str(current_string) + str(counter)
#        l = len(str(current_string))
#    counter = stairway_lenght
##    current_string = str(current_string)[:l-1] 
#    while counter > 0:
#        counter = counter - 1
#        l = len(str(current_string))
#        print('         ' + str(current_string)[:l-1][::-1].ljust(stairway_lenght)) 
#        current_string = str(current_string)[:l-1] 
#incert(i,a)

#s = [2,9,9,9,9,9,9,5]
#l = len(s)
#position = l-1
#s[position] +=1
#while position !=-1:
#       if s[position] == 10:
#              s[position] = 0
#              s[position-1] +=1
#       position -=1      
#print(s)

#d = {'Hello' : 'Hi', 'Bye' : 'Goodbye', 'List' : 'Array'}

#d = {"a": 1, "b": 2, "c": 3, "d": 4}
#rd = {}
#for k, v in d.items():
#  rd[v] = rd.get(v, []) + [k]
#input = str(input('Введите значение \n'))  
#print(rd[input])

#s = ['abc', 'bcd', 'abc', 'abd', 'abd', 'dcd', 'abc']
#eq_count = 0 #счетчик совпадений
#l = len(s)-1 #сколько элементов проверять
#position=0 #стартовая позиция
#pos=[] #сюда пишем позиции одинаковых значений
#final=[] #сюда пишем все что уже проверили
#fin=[] #сюда пишем кол-во повторений (ответ)
#for i in s: #начали с первого элемента
#       if i not in final: #если значение отсутствует в списке уже проверенных, то гоним цикл
#              while position<=l:            
#                     if i == s[position]: #сравнили с первым
#                            eq_count +=1 #увеличили счетчик
#                            pos.append(position) #добавили в массив позиции одинаковых значений
#                     position +=1 #пошли проверять следующее значение
#              final.append(i)#записали в массив значение которое уже прогнали
#              position = 0 #обнулили позицию
#              fin.append(len(pos)) #записали количество повторений
#              pos = [] #обнулили счетчик одинаковых значений   
#print(fin)

#s1 = [1, 10, 223, 413, 2]
#s2 = [2, 40, 12, 100, 10]
#count = 0
#a1 = set(s1)
#a2 = set(s2)

#a1.intersection_update(a2)

#print(len(a1))
#import sys
#x = int(input('input X \n'))
#y = int(input('input Y \n'))
#z = input('input OPERATOR \n')
#checklist = ['+', '-', '*', '/', '%', '**', '**x']
#def check(z):
#    if z == '/' and y == 0: 
#        return sys.exit(print('unsupported operation'))
#    elif z in checklist:
#        return True
#    else:
#        return sys.exit(print('unsupported operation'))    
#def count(x, y):
#    if check(z) == True:
#        if z == '+':
#            return x + y
#        elif z == '-':
#            return x - y
#        elif z == '*':
#            return x * y
#          return x / y
#        elif z == '%':
#            return str(x / y * 100) + '%'
#        elif z == '**':
#            return x * x
#        elif z == '**x':
#            return x ** y         
#print(count(x, y))
#import email


#f = open('task_file.txt', 'r')
#c = 0
#telephone = []
#list_of_names  = []
#fin = ''
#string = ''

#def email_gen(list_of_names):
#    emails = []
#    for i in list_of_names:
#        letter = 1
#        while i[1] + '.' + i[0][0:letter] + '@company.io' in emails:
#            letter+=1
#        emails.append(i[1] + '.' + i[0][0:letter] + '@company.io')
#    return emails

# for i in f:
#    if -1 < c < len(open('task_file.txt').readlines()):
#        i = i.split(",")
#        emailaddress = i[0].replace(" ","")
#        telephone = i[3].replace(" ","")
#        name = i[1].replace(" ","")
#        surname = i[2].replace(" ","")
#        city = i[4].replace(" ","")
#        if len(telephone) == 7 and len(name)>0 and len(surname)>0 and len(city)>0:
#            list_of_names.append([name,surname])
#            emailaddress = email_gen(list_of_names)[-1]
#            i[0] = emailaddress
#        fin = fin + ','.join(i)
#    c +=1
# print(fin)
# f.close()
# f = open('task_file_new.txt', 'r+')
# f.write(fin)
# f.close()

# from dataclasses import replace
# import re
# import yaml
# from yaml.loader import SafeLoader

# environment_json_customPlaceholder = '\{\{- with secret.*}}'
# environment_json_skipPostCheckParams = '^vault\.hashicorp\.com.*'
# environment_json_path_to_exclude = 'spec.template.metadata.annotations'

# def checkIfAllParametrized(text, ignoreParams):
#     if text == ''.join(ignoreParams):
#         if re.findall(r'\{\{.*?}}', text):            
#             return '####### Validating Error!!! #######' +'\n' +  text
#         else:
#             text = text[:].replace('[[','{{').replace(']]','}}')
#             return '####### PostCHeck Success!!! #######' +'\n' + text
#     return 'the value is outside of [[ ]]'  

# text = ''
# ignoreParams = re.findall(environment_json_customPlaceholder, text)


# path2 = environment_json_path_to_exclude.split('.')

# with open('testSecman.yml') as f:
#     data = yaml.load(f, Loader=SafeLoader)
#     z = len(path2)-1
#     data_to_check = data
#     while z>=0:
#         data_to_check = data_to_check[path2[0]]
#         path2.pop(0)
#         z-=1
#     for k, v in data_to_check.items():
#         skipPostCheckParams = re.findall(environment_json_skipPostCheckParams, k)
#         if k == ''.join(skipPostCheckParams):
#             v = v.replace('\n','').rstrip()
#             ignoreParams = re.findall(environment_json_customPlaceholder, v)
#             if checkIfAllParametrized(v, ignoreParams) != 'the value is outside of [[ ]]':
#                 print(checkIfAllParametrized(v, ignoreParams))

# #               
# #import random
# #from re import A, M
# #pass_lenght = 12 #str(input("Введите длину пароля \n"))
# #reqs = ['1234567890','abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ','!@#$%^&*()-+']
# #def passGen(pass_lenght):
# #    passwrd = ''
# #    while len(passwrd) < int(pass_lenght):
# #        for req in reqs:
# #            passwrd = passwrd + random.choice(req)
# #    return passwrd
# #
# #f = open('task_file.txt', 'r')
# #c = 0
# #telephone = []
# #list_of_names  = []
# #fin = ''
# #string = ''
# #
# #def email_gen(list_of_names):
# #    emails = []
# #    for i in list_of_names:
# #        letter = 1
# #        while i[1] + '.' + i[0][0:letter] + '@company.io' in emails:
# #            letter+=1
# #        emails.append(i[1] + '.' + i[0][0:letter] + '@company.io')
# #    return emails
# #
# #for i in f:
# #    if -1 < c < len(open('task_file.txt').readlines()):
# #        i = i.split(",")
# #        i[4] = i[4].replace('\n','')
# #        i.append(' PASSWORD\n')
# #        emailaddress = i[0].replace(" ","")
# #        telephone = i[3].replace(" ","")
# #        name = i[1].replace(" ","")
# #        surname = i[2].replace(" ","")
# #        city = i[4].replace(" ","")
# #        userpasswdr = i[5].replace(" ","")
# #        if len(telephone) == 7 and len(name)>0 and len(surname)>0 and len(city)>0:
# #            list_of_names.append([name,surname])
# #            emailaddress = email_gen(list_of_names)[-1]
#            userpasswdr = passGen(pass_lenght)
#            i[0] = emailaddress
#            i[5] = ' ' + userpasswdr + '\n'
#        fin = fin + ','.join(i)
#    c +=1
#print(fin)
#f.close()
#f = open('task_file_new.txt', 'r+')
#f.write(fin)
#f.close()

######################################################
#x = int(input())
#def fac(x):
#    if x == 0:
#        return 1
#    else:
#        return x*fac(x-1)
#print(fac(x))
######################################################

#      | \_/ | \_/ | \_/ | \_/ | \_/ |
#        ||E    M    ||E    M    ||E
# import threading
# import random
# import time

# class Phil(threading.Thread):
#     running = True
#     def __init__(self, name, left_fork, right_fork):
#         threading.Thread.__init__(self)
#         self.name = name
#         self.left_fork = left_fork
#         self.right_fork = right_fork

#     def run(self):
#         while self.running:
#             time.sleep(random.uniform(5,10))
#             print("{} is hungry".format(self.name))
#             self.dine()

#     def dine(self):
#         while self.running:
#             self.left_fork.acquire()
#             if not self.right_fork.locked():
#                 self.right_fork.acquire()
#                 break
#             else:
#                 self.left_fork.release()
#         else:
#             return
        
#         self.start_dining()
#         self.left_fork.release()
#         self.right_fork.release()
#         print("{} stop eating, start thinking".format(self.name))

#     def start_dining(self):
#         print("{} start eating".format(self.name))
#         time.sleep(random.uniform(10,20))

        


# def start_phil_act():
#     forks = [threading.Lock() for n in range(5)]
#     phil_names = ['1','2','3','4','5']
#     philos = [Phil(phil_names[i], forks[i%5], forks[(i+1)%5]) for i in range(5)]

#     Phil.running = True
#     for p in philos: p.start()
#     time.sleep(50)
#     Phil.running = False
#     print("FINISH")

# start_phil_act()

# import jinja2, re
# values = {
#     "var1": "",
#     "var2": "",
# #    "common_name": "",
# #    "format1": "",
#     "idmosehashicorpkey": "213234234",
#     "globallufssecretrootpath": "CIXXXXXXXX_CXXXXXXXXX/A/IFT/",
#     "fp_nameosedeploymentsecretpath": "OSH/XXXXX/KV/os_project_name/",
#     "fp_nameosedeploymentsecretcertgeo_cert_name": "egressgateway-certs.ver201"
# }

# extention_point = False
# environment = jinja2.Environment()  #variable_start_string='@=', variable_end_string='=@'
# #template = environment.from_string("{{ '{{' }}- with secret {{ globallufssecretrootpath }}{{ fp_nameosedeploymentsecretpath }}{{ fp_nameosedeploymentsecretcertgeo_cert_name}} }} {{ '{{' }} base64Decode (index .Data tls.key) {{ '}}' }} {{ '{{' }} end {{ '}}' }}")
# #template = environment.from_string("{% raw %}{{- with secret {% endraw %} {{ globallufssecretrootpath }}{{ fp_nameosedeploymentsecretpath }}{{ fp_nameosedeploymentsecretcertgeo_cert_name}} }} {% raw %}{{ base64Decode (index .Data tls.key) }} {{ end }}{% endraw %}")
# #template = environment.from_string("{{'{{- with secret '}} {{ globallufssecretrootpath }}{{ fp_nameosedeploymentsecretpath }}{{ fp_nameosedeploymentsecretcertgeo_cert_name}} }}{{' {{ base64Decode (index .Data tls.key) }} {{ end }}'}}")
# #template = environment.from_string("{{- with secret {{ globallufssecretrootpath }}{{ fp_nameosedeploymentsecretpath }}{{ fp_nameosedeploymentsecretcertgeo_cert_name}} }} {{  base64Decode (index .Data tls.key) }} {{ end }}")
# #template = environment.from_string("{{{ '{{' }} with secret "pki_int/issue/solution-dot-sbt" "common_name=my.solution.sbt" "format=pem" | string }} '}}' }}{{ ('{' + '{ ' + '.Data.certificate' + ' }' + '}') | string}}{{ ('{' + '{ ' + 'end' + ' }' + '}') | string}}")
# #print(template.render(values))
# template = environment.from_string('{% raw %}{{- with secret {% endraw %}"{{ idmosehashicorpkey }}" -}}{% raw %}{{- base64Decode .Data.keystore -}}{{- end -}}{% endraw %}')
# if extention_point == False:
#     text = template.render(values)
#     if re.findall(r'\{\{.*?}}', text):
#         print('!WARNING! Могли остаться нераскрытые параметры',text)
#     else:
#         print(text)
# else:
#     text = template.render(values).replace(' }} {{ base64Decode (index .Data tls.key) }} {{ end }}','').replace('{{- with secret ','')
#     if re.findall(r'\{\{.*?}}', text):
#         print('!!!!!!ERROR!!!!!! Остались нераскрытые переменные в аннотациях secman, проверьте экранирование',text)


# def foo(a=[]):
#     a.append(1)
#     print(a)
# foo()
# foo()
# foo()

# class A:
#     def test(self):
#         print("A")
# class B(A):
#     def test(self):
#         print("B")
#         super().test()
# class C(A):
#     def test(self):
#         print("C")
# class D(B,C):
#     def new_test(self):
#         print("D")   
# obj = D()
# obj.test()

# def test_func(lett, dig):
#     for l in lett:
#         print(l)
#         for d in dig:
#             print(d)
#             return l + d
# lett = ['a','b','c']
# dig = ['1','2','3']
# print(test_func(lett,dig))
# lett = ['a','b','c']
# dig = ['1','2','3']
# for l in lett:
# #    print(l)
#     for d in dig:
# #        print(d)
#         print(l,d)

print([x*2 for x in range(1,9)])
