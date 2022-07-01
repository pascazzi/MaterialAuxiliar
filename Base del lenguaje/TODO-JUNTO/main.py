print("++++++++++++++++++++MIS FUNCIONES 2");
global_a = '   global_a presente'


def pxp_multiplesretornos_cuadrado(a, b, c):
    x_squared = a * a
    y_squared = b * b
    z_squared = c * c
    print(global_b)
    print(global_c)
    # Return all three values:
    return x_squared, y_squared, z_squared


global_b = '   global_b presente'


#---------------------------------------
def pxp_if_ready_for_school(backpack, pencil_case):
    if (backpack == 'full' and pencil_case == 'full'):
        print("  I'm ready for school!")
        return 'yes'
    else:
        print('  No estoy listo para esto')
        return 'no'


#---------------------------------------
def pxp_defaultparam_greet_customer(special_item,
                                    grocery_store="Cooperativa defaulteada"):
    print("Welcome to " + grocery_store + ".")
    print("   Our special is " + special_item + ".")


#---------------------------------------
def pxp_forloop(numero):
    sum = 0
    for x in range(numero):
        print('   loop:' + str(x))
        sum += x
    return sum


print('Inicio cuerpo del programa')
#variables globales definidas ANTES del llamado de las funciones que la usaran aunque sea debajo del cuerpo de las funciones.
global_c = '   global_c presente'
CuadradoA, CuadradoB, CuadradoC = pxp_multiplesretornos_cuadrado(3, 4, 5)

print('Cuadrado de tres %i es el resultado' % CuadradoA)
res = pxp_if_ready_for_school('full', 'nofull')
print(' resultado: ' + res)
pxp_defaultparam_greet_customer('Banana')
pxp_defaultparam_greet_customer('Criollitas', 'Bagley')
resloop = pxp_forloop(5)
print(resloop)
print('fin')


#-------------------------------------------------
# pruebas de orden de parametros
def findvolume(length=1, width=2, depth=3):
    print("Length = " + str(length))
    print("  Width = " + str(width))
    print("    Depth = " + str(depth))
    return length * width * depth


findvolume(10, 20, 30)
findvolume(length=100, depth=300, width=200)
findvolume(1000, depth=3000, width=2000)
findvolume()
#------------------------------------------------

print("+++++++++++++++++++PrimerosPasosHelloworld")
#name = input('What is your name?\n')
#print('Hi, %s.' % name)
print('inicio2')
resto = 17 % 3
print(resto)
resto += 1000
print(resto)

# Example integer numbers
chairs = 4
broken_chairs = -2

# Non-integer numbers
lights = 2.5
left_overs = 0.0

first = "Hello "
second = 'Fucking World'  #pueden ser simples tambien
result = first + second
long_result = first + second + "!"
print(long_result)

longer = "This string is broken up \
over multiple lines"

print(longer)
#----------------------------------------------
print("+++++++++++++++++++++ESTILO LIBRE")


def edad():
    nacimiento = int(input('Anio de nacimiento: '))
    print(2021 - nacimiento)


edad()


def pideValor():
    mivalor = input('Valor?')
    return mivalor


lista = []
vale = pideValor()
while vale != '0':
    lista.append(vale)
    vale = pideValor()

lista.sort()
print(list(lista))

for i in range(len(lista)):
    print(lista[i] + '/', end='')

print('')
print('otra forma mas python')
for num in lista:
    print(num + '/', end='')
print('')
print('--------------------')

print(list(enumerate(lista, 700)))

for indice, item in enumerate(lista, 700):
    print("Elemento %d: %s." % (indice, str(item)))

datos = ['pablo', 'pasca', '1972']
nombre, apellido, edad = datos
print('Apellido: ' + apellido)

#--------------------------------------
print("+++++++++++++++++Modulos")
import datetime

nacimiento = datetime.date(1972, 11, 18)
hoy = datetime.date.today()
dentrodeunasemana = hoy + datetime.timedelta(days=7)

print("Hoy {hh}  nacimiento {nn} ".format(hh=hoy, nn=nacimiento))
print("dentro de Una SemaNa  " + str(dentrodeunasemana))
print('Dentro de una semana ' + dentrodeunasemana.strftime("%d/%m/%Y"))

anio = hoy.year
cumple = datetime.date(year=anio, month=nacimiento.month, day=nacimiento.day)
if (cumple < hoy):
    #esto serviria para sumar un año o mes
    #pip install python-dateutil
    #cumple=cumple+relativedelta(years=1, weeks=1)
    cumple = cumple + datetime.timedelta(days=365)
print(cumple)

##
import calendar as c


def mirar(texto):
    print('*******' + texto)
    print(c.weekday(cumple.year, cumple.month, cumple.day))
    print(cumple.isoweekday())
    print('dia de la semana formateado: ' + cumple.strftime("%A"))
    print('Mes nombre ' + c.month_name[cumple.month])
    print(c.month(cumple.year, cumple.month))


mirar("default ")
import locale
print(locale.getlocale())
locale.setlocale(locale.LC_ALL, ('en_US', 'UTF-8'))
mirar('segunda vez')
'''
locale -a muestra en consola que idiomas hay
To install a new locale use:
sudo apt-get install language-pack-id
where id is the language code  
After you have installed the locale you should follow Julien Palard advice and reconfigure the locales with:
sudo dpkg-reconfigure locales
'''
##########################################################################

import random
print("Tiremos los dados: ", end=' - ')
for x in range(30):
    dado = random.randint(1, 6)
    print(str(dado), end=' - ')
print("")

# Prints a random element from a sequence
seq = ["a", "b", "c", "d", "e"]
r2 = random.choice(seq)
print(r2)  # Random element in the sequence

print("Usando comillas 'dentro' de una frase parte 1")
print('Usando comillas "dentro" de una frase parte 2')
print('Usando comillas \'dentro\' de una frase parte 3')

import archivo2
archivo2.FuncionSegundoArchivo("Hello World segundo archivo")

import Tercero
Tercero.FuncionTercerArchivo("Tercer archivo")

#otra manera
# from module import *
#function()

#-------------------------------------
print("+++++++++++++++++++++++Diccionarios")
MiDiccionario1 = {"Lunes": "Monday", "Martes": "Tuesday"}
MiDiccionario1["Lunes"] = "Montag"  #existia lo pisa
MiDiccionario1["Miercoles"] = "Mittwoch"  #no existia lo agrega
MiDiccionario2 = {"Lunes": "Lundi", "Jueves": "Donnerstag", "Viernes": 5}

MiDiccionario1.update(MiDiccionario2)

print(MiDiccionario1["Lunes"])
print(MiDiccionario1["Martes"])
print(MiDiccionario1["Miercoles"])
print(MiDiccionario1["Jueves"])
print(MiDiccionario1["Viernes"])

print('-------- 2 ----------')
print(MiDiccionario1.get("Viernes"))
print(MiDiccionario1.get("Sabado"))  #no existe y no tengo default
print(MiDiccionario1.get("Domingo",
                         "Domingo No existe"))  #existe y tengo default

MiDiccionario1.update({"Enero": "January"})
print(MiDiccionario1.get("Enero", "Enero No existe"))
MiDiccionario1.pop("Enero")  #borro
print(MiDiccionario1.get("Enero", "Enero No existe"))

#Las claves solop ueden ser numeros int, float o strings.
MiDic3 = {
    1: 'hello',
    'two': True,
    '3': [1, 2, 3],
    'Four': {
        'fun': 'addition'
    },
    5.0: 5.5
}
print('----------- 3 ------------')
print(MiDiccionario1.keys())
print(MiDiccionario1.values())
print(MiDiccionario1.items())

print('----------- 4 ------------')
for k in MiDiccionario1.keys():
    if (MiDiccionario1[k] == 5):
        print("  Es cinco  :)")
        continue
    print(MiDiccionario1[k])

#----------------------------------------------------
print("+++++++++++++++++++++FILES")

with open('Notas.txt') as file_object:
    print('**file_object')
    print(file_object)  #datos del archivo, encoding etc.
    print('**READLINE')
    print(file_object.readline())

with open('Notas.txt') as file_object:
    file_data = file_object.readlines()
    text_data = file_object.read()

print('**file data*')
print(file_data)
print('**text data*')
print(text_data)

print('**Recorrer filedata*')
for ren in file_data:
    print(ren)

import random
with open('dados.txt', 'w') as dados:
    dados.write("Nuevo archivo\n")  #Lo abro con w entonces lo pisa

with open(
        'dados.txt', 'a'
) as dados:  #Lo abro con #a para agregar contenido. Si no existia esto lo crea
    for x in range(1, 10):
        tirada = random.randint(1, 6)
        print(tirada, end=' - ')
        dados.write(str(tirada) + " - ")
print(' ')
print('**************** JSON ***********************')
import json
with open('file.json') as json_file:
    python_dict = json.load(json_file)

print(python_dict.get('profesion'))
print(python_dict.get('nombreYAp'))

print(python_dict.get('empleados')[1])
print(len(python_dict.get('empleados')))
for empi in python_dict.get('empleados'):
    print(empi)
    print('El apellido es: ' + empi.get('apellido'))

print('***************** dictwriter *************')
# An example of csv.DictWriter
import csv

with open('companies.csv', 'w') as csvfile:
    fieldnames = ['name', 'type']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'name': 'Codecademy', 'type': 'Learning'})
    writer.writerow({'name': 'Google', 'type': 'Search'})

with open('mascotas.csv', 'w') as miArchivo:
    campos = ['Nombre', 'Duenio', 'Apodo']
    writer = csv.DictWriter(miArchivo, fieldnames=campos)
    writer.writeheader()
    writer.writerow({'Nombre': 'Baisha', 'Duenio': 'Pablo', 'Apodo': 'Negra'})
    writer.writerow({'Duenio': 'Flor', 'Apodo': 'Lolona', 'Nombre': 'Lola'})
#---------------------------------
print("+++++++++++++++++++++Clase")
class Perro:
    nombre = 'Sin nombre aun'

    def __init__(self, nombre):
        self.nombre = nombre
        self.apellido = "no tiene apellido"

    def CambiarNombre(self, nuevonombre):
        self.nombre = nuevonombre

    def bark(self):
        print(self.nombre + " guau guau")

print("aeiou")
print(dir())
print('----------------------')
print(dir(Perro))
print('----------------------')
lola = Perro('Lola')
baisha = Perro('Baisha')

print(lola.nombre)
lola.CambiarNombre("Lolona")
print(lola.nombre)
lola.bark()

print(baisha.nombre)
print(baisha.apellido)
print(type(baisha))

print(dir())
print("  ")
print(dir(baisha))

print("---------------------------")
print(
    type(baisha)
)  #main: This means that the class CoolClass was defined in the current script file.

import anexo
puntito = anexo.Punto(1, 2)
print(type(puntito))

p1 = anexo.Punto(1, 10)
p2 = anexo.Punto(2, 20)
p3 = p1 + p2
print(p3)

#esto dispara exception a proposito:
try:
    print('* paso 1')
    puntito = anexo.Punto(1, 2)
    print('* paso 2')
    puntito = anexo.Punto(1, 'a')
    print('* paso 3')
    puntito = anexo.Punto(1, 2)
except IOError:
    print('error de io')
except ZeroDivisionError:
    print('division por cero no va')
except anexo.FuckException:
    print('    ..........Atrapo fuck exception')
except:
    print('salio algo mal pero no se que')
finally:
    print('* paso finally')

#############################

import herencia
boeing = herencia.avion('Boeing', 2)
boeing.definite()
boeing.categorias()
jumbo = herencia.avion('jumbo', 2)
jumbo.definite()
print(jumbo)

fiat = herencia.auto('fiat siena', 4)
fiat.definite()
print(fiat)

print(fiat + boeing)  #sumo ruedas 6

print(issubclass(herencia.avion, herencia.vehiculo))  # True
print(issubclass(herencia.auto, herencia.vehiculo))  # True
print(issubclass(herencia.auto, herencia.avion))  # falso

import MiBeep
MiBeep.beep()
#--------------------------------------
print("+++++++++++++++++++++ArgumentosFunciones")


# Here, an empty list is used as a default argument of the function.
def append(number, number_list=[]):
    number_list.append(number)
    print(number_list)
    return number_list


def funcionConReturn():
    print('En funcionConReturn')
    return 'funcionConReturn'


def funcionSinReturn():
    print('En funcionSinReturn')


# Below are 3 calls to the `append` function and their expected and actual outputs:
append(5)  # expecting: [5], actual: [5]
append(7)  # expecting: [7], actual: [5, 7]
append(2)  # expecting: [2], actual: [5, 7, 2]

print

lista1 = [100, 200, 300]
lista2 = lista1
#mismo objetos con dos nombres

lista1.append(5000)
print(lista1)
print(lista2)
#si funcion no retorna nada, retorna igual algo llamado none
print(funcionConReturn())
print(funcionSinReturn())

# Variable check for None (usar mayusculas)
variable_name = None
if variable_name is None:
    print("variable is None")
else:
    print("variable is NOT None")


#Llamado con argumentos
# The function will take arg1 and arg2
def func_with_args(arg1, arg2):
    print(arg1 + ' ' + arg2)


func_with_args('First', 'Second')
# Prints:
# First Second

func_with_args(arg2='Second', arg1='First')
# Prints
# First Second
#--------------------------------------------


