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
