import pymysql

class BDD:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='torneo'
        )

        self.cursor = self.connection.cursor()

        print("Conexión Exitosa con la base de datos")

    def obtenerqueryb(self):
        consola = []
        jugadores = []
        sql = 'select c.modelo, count(pcv.codparticipante) as "Cantidad de usuarios" from consola c, ParCV pcv where c.CodConsola = pcv.codconsola group by c.CodConsola'

        try:
            self.cursor.execute(sql)
            datos = self.cursor.fetchall()
            for dato in datos:
                print(str(dato[0]) + " " + str(dato[1]))
                consola.append(str(dato[0]))
                jugadores.append(int(dato[1]))
            print(consola)
            print(jugadores)
        except Exception as e:
            raise


baseDeDatos = BDD()
baseDeDatos.obtenerqueryb()
