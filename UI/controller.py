import flet as ft
from UI.view import View
from model.biblioteca_DTO import Biblioteca
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    # POPOLA DROPDOWN
    # TODO
    def popola_dropdown(self):
        self._view.dropdown_genere.options.append(ft.dropdown.Option("Nessun filtro"))
        self._view.dropdown_biblioteca.options.append(ft.dropdown.Option("Nessun filtro"))
        for g in self._model.get_generi():
            self._view.dropdown_genere.options.append(ft.dropdown.Option(g))
        for b in self._model.get_biblioteche():
            self._view.dropdown_biblioteca.options.append(ft.dropdown.Option(key=str(b.id), text=b.nome))
        self._view.page.update()
    # CALLBACKS DROPDOWN
    # TODO
    def handle_genere(self,e):
        genere = e.control.value
        if genere is not None:
            self.genere_selezionato = genere
        if genere == "Nessun filtro":
            self.genere_selezionato = None
    def handle_biblioteca(self, e):
        biblioteca = e.control.value
        if biblioteca is not None:
            self.biblioteca_selezionata = biblioteca
        if biblioteca == "Nessun filtro":
            self.biblioteca_selezionata = None
    # AZIONE: MOSTRA LIBRI
    # TODO
    def handle_libri(self,e):
        self._view.libri.controls.clear()
        libri = self._model.get_libri_filtrati(self.biblioteca_selezionata, self.genere_selezionato)
        for libro in libri:
            self._view.libri.controls.append(ft.TextField(str(libro)))
        self._view.page.update()