from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass

    # TODO
    def get_biblioteche(self):
        cnx = DBConnect.get_connection()
        if cnx is None:
            return []
        cursor = cnx.cursor(dictionary=True)
        query = "SELECT * FROM biblioteca"
        cursor.execute(query)
        lista_biblioteche = []
        for biblioteca in cursor:
            b = Biblioteca(id=biblioteca["id"], nome=biblioteca["nome"], indirizzo=biblioteca["indirizzo"])
            lista_biblioteche.append(b)
        cursor.close()
        cnx.close()
        return lista_biblioteche