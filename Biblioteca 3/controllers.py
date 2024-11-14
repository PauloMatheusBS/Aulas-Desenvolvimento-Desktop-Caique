from models import Livro, Usuario, Emprestimo

def cadastrar_livro(titulo, autor, isbn, genero):
    Livro.cadastrar_livro(titulo, autor, isbn, genero)

def consultar_livro(isbn=None, titulo=None, autor=None, genero=None):
    return Livro.consultar_livro(isbn, titulo, autor, genero)

def atualizar_livro(id, titulo=None, autor=None, genero=None):
    Livro.atualizar_livro(id, titulo, autor, genero)

def excluir_livro(id):
    Livro.excluir_livro(id)

def cadastrar_usuario(nome, email, senha, cpf, administrador=False):
    Usuario.cadastrar_usuario(nome, email, senha, cpf, administrador)

def consultar_usuario(nome=None, email=None, cpf=None):
    return Usuario.consultar_usuario(nome, email, cpf)

def atualizar_usuario(id, nome=None, email=None, senha=None):
    Usuario.atualizar_usuario(id, nome, email, senha)

def excluir_usuario(id):
    Usuario.excluir_usuario(id)

def realizar_emprestimo(usuario_id, livro_id):
    Emprestimo.realizar_emprestimo(usuario_id, livro_id)

def devolver_emprestimo(emprestimo_id):
    Emprestimo.devolver_emprestimo(emprestimo_id)
