###coding###

import random
def weighted_random(values,weights):
    total_weights=sum(weights)
    acum_weights=[w/total_weights for w in weights[:]]
    for i in range(len(weights)-1):
        acum_weights[i+1]+=acum_weights[i]
    #print(acum_weights)
    rand = random.random()
    #print(rand)
    for value, weight in zip(values,acum_weights):
        if weight>rand:
            return value

# En la función que presenta el ejercicio hay un error en aquella parte donde se crea una lista con las probabilidades acumuladas para cada valor.
# Es decir, en la linea número 6 y 7. En primer lugar, como a cada probabilidad quiero sumarle la probabilidad de la izquierda, voy a iterar sobre el largo de la lista menos 1, pues el valor de la posición 0 quedará intacto.
# En la linea siguiente, realice una modificación que busca sumar la probabilidad de un cierta posicion con la probabilidad correcta.
# Esto es, el valor que toma la lista en la posicion i debe ser sumado al valor de la lista en la posicion i+1.
# Asi me aseguro que la parte final del código va a funciona de manera correcta - la lista va tomando valores ascendentes entre 0 y 1 a medida que corremos a la derecha.





###analytics###

# events se queda con una table cuyas columnas son: (1) identificación del usuario;
# (2) el momento en el que el usuario realizo una accion; (3) el momento en el que el usuario realizo la siguiente acción

# per_events toma la diferencia entre las columnas (2) y (3). Y se queda con las columnas:
# (1) identificación del usuario; (2) tiempo transcurrido entre dos eventos realizados por el usuario.

# Por último, el programa se queda con una sola fila por usuario y el tiempo promedio transcurrido entre dos eventos realizados por cada usuario.

# De esta forma eligiendo el id de un cliente, el cual supongo es una apliación (en el ejemplo es el cliente 1), y algún evento en especial
# realizado en la misma, como por ejemplo puede ser una compra dentro de la misma, podemos ver en promedio cuanto tarda cada usuario en la aplicación para repetir el evento.
# Si un cliente entra en la aplcación de cliente 1 con una frecuencia semanal, a este le puede ayudar a tomar decisiones sobre como atraer a ese cliente, cuanto
# dinero destinar a tratar de atraerlo en diferentes momentos. En este ejemplo, el cliente estaría dispuesto a pagar mas para atraerlo 5 días después de su ultimo ingreso a la apliación que al día siguiente.
# Conocer esta información puede ser de utilidad para nuestro cliente el cual podría ofrecer algún tipo de descuento o oferta para incentivar a algunos usuarios a entrar con mayor frecuencia a la aplicación.





###math###

#El primer paso para resolver el ejercicio es encontrar la cantidad de monedas que tiene el capitan Morgan.
# Con la información proveida por el ejercicio podemos ver que en el primer caso, el capitan está repartiendo
# una cantidad de monedas entre 1 y 9 (con 10 o mas se excede de mil). En el segundo caso, esta dando a cada uno
# de los 77 piratas entre 1 y 12 monedas. Cruzando las diferentes opciones encuentro que la cantidad de monedas
# que hay es 645, es el único valor que coincide en ambas situaciones.
# Con un programa analiz las diferentes opciones que tiene el capitán - las diferentes combinaciones de cantidad
# de piratas elegidos, cantidad de monedas para cada uno, y cantidad de monedas restantes para el. Una primera intuición
# es que la cantidad depiratas sería la mitad mas 1, de manera tal que a todos estos les quede una moneda (no alcanzan
# para dar 2 a cada uno) y el capitan se queda con la mitad menos uno. Efectivamente, el programa encuentra que el valor
# máximo que puede quedarse el capitán es 322, para lo cual debe elegir 323 piratas y darle una moneda a cada uno.
# El programa también realiza un gráfico de dispersiónn de manera tal que se puede ver cuanto obtiene el capitan según la
# cantidad de piratas que selecciona - vemos que acorde a lo hallado anteriormente, el punto mas alto se alcanza en las
# coordenadas (x,y)=(323,322).

import matplotlib.pyplot as plt
treasure=645
num_of_pirates=list(range(1,treasure+1))
coins_per_pirate=[int(treasure/i) for i in num_of_pirates]
captain_rest=[treasure-(coins_per_pirate[i]*(i+1)) for i in range(len(coins_per_pirate))]

maxcoins=max(captain_rest)
print('Number of coins the captain gets: ', maxcoins)
pirates=[i for i in num_of_pirates if captain_rest[i-1]==maxcoins]
print('Number of pirates the captain selects: ', pirates)

plt.scatter(num_of_pirates,captain_rest)
plt.xlabel("Number of pirates")
plt.ylabel("Number of coins that the captain gets")
plt.show()