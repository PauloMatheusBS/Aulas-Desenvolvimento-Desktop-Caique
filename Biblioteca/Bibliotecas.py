from Livros import Livro
from Usuarios import Usuario


class Biblioteca:
    Acervo = []
    @staticmethod
    def emprestar(usuario:Usuario, livro:list(Livro)):
        for item in livro:
            item.emprestar_livro(usuario)
            usuario.pegar_emprestado(livro)
    
    # @staticmethod
    # def devolver(livro:Livro , usuario:Usuario):
    #     livro.devolver_livro