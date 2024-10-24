from Livros import Livro
from Usuarios import Usuario



rafaela = Usuario("Rafaela", "501651651065","654645654645")
print(vars(rafaela))
    
don_casmurro = Livro("Don Casmurro","Machado de Assis", "Drama", "2165165165")
print(vars(don_casmurro))            
        
rafaela.pegar_emprestado(don_casmurro)
print(vars(rafaela))






# crie uma classe usuario com seus atributos e com uma constante de MAX_EMPRESTIMO para identificar a quantidade maxima permitida.
# crie uma classe para livros que tenha os metodos de emprestimo, cadastro, listar e atributos
# crie uma classe estatica que implemente uma Bibliotecaque consiga realizar o emprestimo e devolução
# defina uma interface que para realizar o CRUD tanto de usuario quanto de livro        

# emprestimo1 = Biblioteca()
# emprestimo1.gerenciaremprestimo()

###################################################################################################################

# class Usuario:
#     MAX_EMPRESTIMO = 5

#     def __init__(self, nome, id_usuario):
#         self.nome = nome
#         self.id_usuario = id_usuario
#         self.emprestimos = []

#     def emprestar(self, livro):
#         if len(self.emprestimos) < Usuario.MAX_EMPRESTIMO:
#             self.emprestimos.append(livro)
#             return True
#         return False

#     def devolver(self, livro):
#         if livro in self.emprestimos:
#             self.emprestimos.remove(livro)
#             return True
#         return False

# class Livro:
#     def __init__(self, titulo, autor, id_livro):
#         self.titulo = titulo
#         self.autor = autor
#         self.id_livro = id_livro
#         self.disponivel = True

#     def cadastrar(self):
#         return {"titulo": self.titulo, "autor": self.autor, "id_livro": self.id_livro}

# class Biblioteca:
#     usuarios = []
#     livros = []

#     @staticmethod
#     def cadastrar_usuario(nome, id_usuario):
#         usuario = Usuario(nome, id_usuario)
#         Biblioteca.usuarios.append(usuario)

#     @staticmethod
#     def cadastrar_livro(titulo, autor, id_livro):
#         livro = Livro(titulo, autor, id_livro)
#         Biblioteca.livros.append(livro)

#     @staticmethod
#     def listar_usuarios():
#         return [usuario.nome for usuario in Biblioteca.usuarios]

#     @staticmethod
#     def listar_livros():
#         return [livro.cadastrar() for livro in Biblioteca.livros]

#     @staticmethod
#     def emprestar_livro(id_usuario, id_livro):
#         usuario = next((u for u in Biblioteca.usuarios if u.id_usuario == id_usuario), None)
#         livro = next((l for l in Biblioteca.livros if l.id_livro == id_livro), None)

#         if usuario and livro and livro.disponivel:
#             if usuario.emprestar(livro):
#                 livro.disponivel = False
#                 return True
#         return False

#     @staticmethod
#     def devolver_livro(id_usuario, id_livro):
#         usuario = next((u for u in Biblioteca.usuarios if u.id_usuario == id_usuario), None)
#         livro = next((l for l in Biblioteca.livros if l.id_livro == id_livro), None)

#         if usuario and livro and not livro.disponivel:
#             if usuario.devolver(livro):
#                 livro.disponivel = True
#                 return True
#         return False

# class Interface:
#     @staticmethod
#     def criar_usuario(nome, id_usuario):
#         Biblioteca.cadastrar_usuario(nome, id_usuario)

#     @staticmethod
#     def criar_livro(titulo, autor, id_livro):
#         Biblioteca.cadastrar_livro(titulo, autor, id_livro)

#     @staticmethod
#     def listar_usuarios():
#         return Biblioteca.listar_usuarios()

#     @staticmethod
#     def listar_livros():
#         return Biblioteca.listar_livros()

#     @staticmethod
#     def emprestar_livro(id_usuario, id_livro):
#         return Biblioteca.emprestar_livro(id_usuario, id_livro)

#     @staticmethod
#     def devolver_livro(id_usuario, id_livro):
#         return Biblioteca.devolver_livro(id_usuario, id_livro)
