import pymysql

consola = []  # Lista donde se guarda la primera columna
jugadores = []  # Lista donde se guarda la segunda columna

class BDD:
    """Clase Base de Datos. Posee dos métodos"""
    def __init__(self):
        """Método que se ejecuta al inicio. Conecta con la base de datos"""
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='torneo'
        )

        self.cursor = self.connection.cursor()

        print("Conexión Exitosa con la base de datos")

    def obtenerqueryb(self):
        """Método que realiza una query. Los datos son guardados en listas."""
        sql = 'select c.modelo, count(pcv.codparticipante) as "Cantidad de usuarios" from consola c, ParCV pcv where c.CodConsola = pcv.codconsola group by c.CodConsola'  # La consulta

        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchall()
            for dato in datos:
                print(str(dato[0]) + " " + str(dato[1]))  # Se imprimen todos los datos como string
                consola.append(str(dato[0]))  # Se alamacenan los datos en la lista como string
                jugadores.append(int(dato[1]))  # Se alamacenan los datos en la lita como int
        except Exception as e:
            raise


baseDeDatos = BDD()
baseDeDatos.obtenerqueryb()
# Se imprimen las listas
print(consola)
print(jugadores)
