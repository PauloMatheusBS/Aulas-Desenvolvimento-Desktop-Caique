from Model.livros import Livros
from Model.usuario import Usuario

class Biblioteca:
    def __init__(self):
        self.acervo = [] #starta a lista vazia

    def adicionar_livro(self, livro: Livros):
        """Método para adicionar livros ao acervo da biblioteca."""
        self.acervo.append(livro)

    @staticmethod
    def emprestar(usuario: Usuario, livros: list[Livros]):
        """Método para emprestar livros a um usuário."""
        for item in livros:
            if len(usuario.lista_livros) >= usuario.MAX_EMPRESTIMO: #consulta limite
                print(f"Usuário {usuario.nome} atingiu o limite de empréstimos.")
                return  #aqui se bater ele so sai e é isso
            
            if item.status != "Disponivel": #confere o status
                print(f"O livro '{item.titulo}' não está disponível para empréstimo.")
                continue  #se tiver indisponivel, pula
            
            usuario.pegar_emprestado(item) #deu bom
            item.emprestar_livro(usuario)
            print(f"Livro '{item.titulo}' emprestado com sucesso para {usuario.nome}.")
            
    def listar_livros(self):
        """Método para listar todos os livros no acervo da biblioteca."""
        for livro in self.acervo:
            print(f"Livro: {livro.titulo}, Autor: {livro.autor}, Status: {livro.status}")

#//////////////////////////////////////////////////////////////////////////////////////////
# Criando uma instância de biblioteca
biblioteca = Biblioteca()


livro1 = Livros(titulo="Dom Casmurro", autor="Machado de Assis", genero="Ficção", codigo=123) #criou
livro2 = Livros(titulo="1984", autor="George Orwell", genero="Distopia", codigo=124) #criou


biblioteca.adicionar_livro(livro1) #add livro
biblioteca.adicionar_livro(livro2) #add livro


usuario1 = Usuario(nome="João", cpf="12345678901", telefone="987654321") #add user


biblioteca.emprestar(usuario1, [livro1, livro2]) #ta com erro ainda mas vai emprestar


print(f"Livros emprestados por {usuario1.nome}:") #aqui ele lista o que esta com o usuario, não ta pronto ainda
for livro in usuario1.lista_livros:
    print(f" - {livro.titulo}")




    # @staticmethod
    # def devolver(livro: Livros, usuario: Usuario):
    #     livro.devolver_livro()
    #     usuario.