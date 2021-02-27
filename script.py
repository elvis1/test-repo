from os import rename

import requests

# print(sys.executable)


# def greet(who_to_greet):
#     greeting = "hello, {}".format(who_to_greet)
#     return greeting


# print (greet('Juan'))


# def saludo (a_quien_saludar):
#     saludos = 'hola {}'.format(a_quien_saludar)
#     return saludo


# print (saludo('Juan'))


# def saludar (pasar_variable_de_a_quien_saludar):
#     saludos = 'Hola {}'.format(pasar_variable_de_a_quien_saludar)
#     return saludos

# print (saludar('Juan'))


# def hola(valores_que_toma):
#     test1 = "Estoy tomando este valor {}".format(valores_que_toma)
#     return test1


# # print (hola ( '...SOY ESE VALOR') )

# r = requests.get("https://infobae.com")
# print(r.status_code)

# name = input("Your name ?")
# print("Hello, ", (name))


# def greet(who_to_greet):
#     greeting = "hello {}".format(who_to_greet)
#     return greeting

#     print(greet("Juan"))


r = requests.get("infobae.com")
print(r.status_code)
