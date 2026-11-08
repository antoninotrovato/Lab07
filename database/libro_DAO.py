from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass
    def get_libro(self, id_biblioteca, genere):
        cnx = DBConnect.get_connection()
        if cnx is None:
            return []
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT * 
                        FROM libro 
                        WHERE id_biblioteca = COALESCE(%s, id_biblioteca)
                        AND genere = COALESCE(%s, genere)"""
        cursor.execute(query, (id_biblioteca, genere))
        lista_libri = []
        for libro in cursor:
            l = Libro(id= libro["id"],
                      titolo=libro["titolo"],
                      autore = libro["autore"],
                      genere=libro["genere"],
                      anno_pubblicazione=libro["anno_pubblicazione"],
                      id_biblioteca=libro["id_biblioteca"])
            lista_libri.append(l)
        cursor.close()
        cnx.close()
        return lista_libri

