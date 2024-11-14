from Model.livros import Livros
from Model.main import Database

class ControllerLivro:
    def __init__(self):
        """Inicializa a conexão com o banco de dados."""
        self.bd = Database("10.28.2.59", "suporte", "suporte", "biblioteca")

    def conectar_bd(self):
        """Método para conectar ao banco de dados."""
        self.bd.conectar()

    def desconectar_bd(self):
        """Método para desconectar do banco de dados."""
        self.bd.desconectar()

    def cadastrarLivro(self, titulo, autor, genero, codigo):
        """Cadastrar um novo livro."""
        livro = Livros(titulo, autor, genero, codigo)
        self.conectar_bd()
        try:
            self.bd.cursor.execute(livro.create())
            self.bd.conexao.commit()
            print(f"Livro '{titulo}' cadastrado com sucesso!")
        except Exception as e:
            print(f"Erro ao cadastrar livro: {e}")
            self.bd.conexao.rollback()
        finally:
            self.desconectar_bd()

    def excluirLivro(self, id_livro):
        """Excluir um livro pelo ID."""
        livro = Livros(titulo=None, autor=None, genero=None, codigo=None)
        livro.id_livro = id_livro
        self.conectar_bd()
        try:
            self.bd.cursor.execute(livro.delete())
            self.bd.conexao.commit()
            print(f"Livro de ID {id_livro} excluído com sucesso!")
        except Exception as e:
            print(f"Erro ao excluir livro: {e}")
            self.bd.conexao.rollback()
        finally:
            self.desconectar_bd()

    def atualizarLivro(self, id_livro, novo_titulo=None, novo_autor=None, novo_genero=None, novo_status=None):
        """Atualizar informações de um livro."""
        livro = Livros(titulo=None, autor=None, genero=None, codigo=None)
        livro.id_livro = id_livro
        self.conectar_bd()
        try:
            self.bd.cursor.execute(livro.update(novo_titulo, novo_autor, novo_genero, novo_status))
            self.bd.conexao.commit()
            print(f"Livro de ID {id_livro} atualizado com sucesso!")
        except Exception as e:
            print(f"Erro ao atualizar livro: {e}")
            self.bd.conexao.rollback()
        finally:
            self.desconectar_bd()

    def consultarLivro(self, id_livro):
        """Consultar um livro pelo ID."""
        livro = Livros(titulo=None, autor=None, genero=None, codigo=None)
        livro.id_livro = id_livro
        self.conectar_bd()
        try:
            self.bd.cursor.execute(livro.select())
            resultado = self.bd.cursor.fetchall()
            if resultado:
                for linha in resultado:
                    print(linha)
            else:
                print(f"Nenhum livro encontrado com o ID {id_livro}.")
        except Exception as e:
            print(f"Erro ao consultar livro: {e}")
        finally:
            self.desconectar_bd()



controladora_livro = ControllerLivro()


controladora_livro.cadastrarLivro(titulo="Dom Casmurro", autor="Machado de Assis", genero="Suspense", codigo=123) # Cadastrar livro


controladora_livro.consultarLivro(id_livro=123) # Consultar livro


controladora_livro.atualizarLivro(id_livro=123, novo_titulo="Dom Casmurro - Edição Atualizada", novo_status="Indisponível") # Atualizar livro


controladora_livro.excluirLivro(id_livro=123) # Excluir livro
