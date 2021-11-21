from matplotlib import pyplot
from ObtenerDatos import consola, jugadores

colores = ('red', 'blue', 'black', 'green')  # Colores que se van a aplicar en el gráfico

pyplot.rcParams['toolbar'] = 'None'  # Oculta la toolbar de pyplot

_, _, texto = pyplot.pie(jugadores, colors=colores, labels=consola, autopct='%1.1f%%', startangle=90)  # Instrucciones para generar el gráfico

for tex in texto:
    tex.set_color('white')  # Cambia las letras dentro de los colores a blanco

pyplot.axis('equal')  # Convierte al gráfico en un círuclo perfecto
pyplot.title('Gráfico circular de la cantidad de jugadores por consola')  # Agrega un título
pyplot.show()  # Muestra el gráfico

pyplot.savefig('graficoqueryb.png')  # Guarda el gráfico como imagen
