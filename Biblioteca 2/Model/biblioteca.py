from Model.livros import Livros
from Model.usuario import Usuario

class Biblioteca:
    def __init__(self):
        # Inicializa um acervo vazio de livros para cada instância de Biblioteca
        self.acervo = []

    def adicionar_livro(self, livro: Livros):
        """Método para adicionar livros ao acervo da biblioteca."""
        self.acervo.append(livro)

    @staticmethod
    def emprestar(usuario: Usuario, livros: list[Livros]):
        """Método para emprestar livros a um usuário."""
        for item in livros:
            # Verifica se o usuário já atingiu o limite de empréstimos
            if len(usuario.lista_livros) >= usuario.MAX_EMPRESTIMO:
                print(f"Usuário {usuario.nome} atingiu o limite de empréstimos.")
                return  # Não permite mais empréstimos
            
            # Verifica se o livro está disponível
            if item.status != "Disponivel":
                print(f"O livro '{item.titulo}' não está disponível para empréstimo.")
                continue  # Pula para o próximo livro, caso o livro não esteja disponível
            
            # Registra o empréstimo no usuário e no livro
            usuario.pegar_emprestado(item)
            item.emprestar_livro(usuario)
            print(f"Livro '{item.titulo}' emprestado com sucesso para {usuario.nome}.")
            
    def listar_livros(self):
        """Método para listar todos os livros no acervo da biblioteca."""
        for livro in self.acervo:
            print(f"Livro: {livro.titulo}, Autor: {livro.autor}, Status: {livro.status}")

#//////////////////////////////////////////////////////////////////////////////////////////
# Criando uma instância de biblioteca
biblioteca = Biblioteca()

# Criando livros
livro1 = Livros(titulo="Dom Casmurro", autor="Machado de Assis", genero="Ficção", codigo=123)
livro2 = Livros(titulo="1984", autor="George Orwell", genero="Distopia", codigo=124)

# Adicionando livros ao acervo da biblioteca
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)

# Criando um usuário
usuario1 = Usuario(nome="João", cpf="12345678901", telefone="987654321")

# Emprestando livros para o usuário
biblioteca.emprestar(usuario1, [livro1, livro2])

# Listando livros emprestados pelo usuário
print(f"Livros emprestados por {usuario1.nome}:")
for livro in usuario1.lista_livros:
    print(f" - {livro.titulo}")




    # @staticmethod
    # def devolver(livro: Livros, usuario: Usuario):
    #     livro.devolver_livro()
    #     usuario.