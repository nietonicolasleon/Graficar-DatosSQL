from matplotlib import pyplot
from ObtenerDatos import consola, jugadores

colores = ('red', 'blue', 'cyan', 'green')

pyplot.rcParams['toolbar'] = 'None'

_, _, texto = pyplot.pie(jugadores, colors=colores, labels=consola, autopct='%1.1f%%', startangle=90)

for tex in texto:
    tex.set_color('white')

pyplot.axis('equal')
pyplot.title('Gráfico circular de la cantidad de jugadores por consola')
pyplot.show()
