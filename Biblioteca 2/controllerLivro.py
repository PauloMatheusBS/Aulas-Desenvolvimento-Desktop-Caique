from livros import Livros
from main import Database

class ControllerLivro:
    def cadastrarLivro():
        bd = Database()
        bd.conectar()

        livro = Livros()
        bd.cursor.execute(livro.create())