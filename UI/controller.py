import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def calcola_anagrammi(self, e):
        word = self._view.txt_word.value
        anagrammi = self._model.calcola_anagrammi(word)
        for anagramma in anagrammi:
            self._view.lst_correct.controls.append(ft.Text(anagramma))
        self._view.update_page()

    def reset(self, e):
        pass
