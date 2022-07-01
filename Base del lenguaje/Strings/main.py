print("+++++++++++++++++++++Strings")
game = "Popular Nintendo Game: Mario Kart"
print("l" in game)  # Prints: True
print("x" in game)  # Prints: False

#concatenar
inicio = 'Desde aqui, '
fin = 'Hasta allá.'
todo = inicio + fin
print(todo)

print("z" in "Hola como estas")
mibool = "z" in "Hola como estas"

box = 'yellow'
print(box[1])  # => 'e'
print(box[2])  # => 'l'
print(box[-1])  # => 'w'
print(box[4:5])  # => 'ow'
print(box[:4])  # => 'yell'
print(box[-3:])  # => 'low'
print(box[-2])  # => 'o'

for c in box:
    print('iterando: ' + c)
print('size:' + str(len(box)))

#formateo de strings
msg1 = 'Fred saco {} de un total de  {} puntos.'
msg1 = msg1.format(3, 10)
print(msg1)

msg2 = 'Pablo {verb} un  {noun} {adjective}.'
msg2 = msg2.format(adjective='verde', verb='compro', noun='auto')
print(msg2)

maxi = 10
for c in range(maxi):
    msg3 = 'Renglon {} de {}'
    msg3 = msg3.format(c, maxi)
    print(msg3)

t1 = '....+++---...Hola que Tal. '
t2 = '    Espero que estes bien. '
print(t1.lower() + t2.upper())
print(t1.capitalize() + t2.title())
print(t1.strip('.+-') + t2.strip())
t3 = t1.strip('.+-') + t2.strip()
print(t3.split('.'))
print(t3.split())
print('aaaaa' + ' '.join(t3.split()))

print(t3.find('tal'))
print(t3.find('Tal'))
print(t3.replace('e ', 'x '))

x = "/".join(["18", "11", "1972"])
print(x)

#-------------------------------------------
