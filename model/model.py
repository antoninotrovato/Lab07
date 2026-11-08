from database import libro_DAO
from database.biblioteca_DAO import BibliotecaDAO
from database.libro_DAO import LibroDAO

'''
    MODELLO:
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Si occupa di interrogare il DAO (chiama i metodi di BibliotecaDAO e LibroDAO)
'''

class Model:
    def __init__(self):
        self._biblioteca_dao = BibliotecaDAO()
        self._libro_dao = LibroDAO()

    # --- LIBRI ---
    def get_libri_filtrati(self, biblioteca:str, genere:str):
        """Restituisce la lista di tutti i libri filtrati per biblioteca e/o genere (filtri opzionali)."""
        # TODO
        return self._libro_dao.get_libro(biblioteca, genere)

    def get_generi(self):
        """Restituisce la lista di tutti i generi."""
        # TODO
        lista_libri = self._libro_dao.get_libro(None,None)
        lista_generi= []
        for libro in lista_libri:
            genere = libro.genere
            if genere not in lista_generi:
                lista_generi.append(genere)
        return lista_generi
    # --- BIBLIOTECHE ---
    def get_biblioteche(self):
        """ Restituisce la lista di tutte le biblioteche."""
        # TODO
        return self._biblioteca_dao.get_biblioteche()
