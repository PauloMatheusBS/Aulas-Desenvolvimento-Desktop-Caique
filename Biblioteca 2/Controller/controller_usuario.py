from Model.usuario import Usuario
from Model.main import Database

class ControllerUsuario:
    def __init__(self):
        # Conexão com o banco de dados
        self.bd = Database("10.28.2.59", "suporte", "suporte", "biblioteca")

    def cadastrar_usuario(self, nome, cpf, telefone):
        """Cadastrar um novo usuário na base de dados."""
        usuario = Usuario(nome, cpf, telefone)
        self.bd.conectar()
        try:
  
            self.bd.cursor.execute(usuario.create())
            self.bd.conexao.commit()
            print("Usuário cadastrado com sucesso!")
        except Exception as e:
            print(f"Erro ao cadastrar usuário: {e}")
            self.bd.conexao.rollback()
        finally:
            self.bd.desconectar()

    def excluir_usuario(self, id_usuario):
        """Excluir um usuário existente."""
        usuario = Usuario(nome=None, cpf=None, telefone=None)  
        usuario.id_usuario = id_usuario
        self.bd.conectar()
        try:
            self.bd.cursor.execute(usuario.delete())
            self.bd.conexao.commit()
            print("Usuário excluído com sucesso!")
        except Exception as e:
            print(f"Erro ao excluir usuário: {e}")
            self.bd.conexao.rollback()
        finally:
            self.bd.desconectar()

    def atualizar_usuario(self, id_usuario, novo_nome=None, novo_cpf=None, novo_telefone=None):
        """Atualizar dados de um usuário."""
        usuario = Usuario(nome=novo_nome, cpf=novo_cpf, telefone=novo_telefone)
        usuario.id_usuario = id_usuario
        self.bd.conectar()
        try:
            self.bd.cursor.execute(usuario.update(novo_nome, novo_cpf, novo_telefone))
            self.bd.conexao.commit()
            print("Usuário atualizado com sucesso!")
        except Exception as e:
            print(f"Erro ao atualizar usuário: {e}")
            self.bd.conexao.rollback()
        finally:
            self.bd.desconectar()

    def consultar_usuario(self, id_usuario):
        """Consultar um usuário pelo ID."""
        usuario = Usuario(nome=None, cpf=None, telefone=None)
        usuario.id_usuario = id_usuario
        self.bd.conectar()
        try:
            self.bd.cursor.execute(usuario.select())
            resultado = self.bd.cursor.fetchone()
            if resultado:
                print(f"Usuário encontrado: ID = {resultado[0]}, Nome = {resultado[1]}, CPF = {resultado[2]}, Telefone = {resultado[3]}")
            else:
                print("Usuário não encontrado.")
        except Exception as e:
            print(f"Erro ao consultar usuário: {e}")
        finally:
            self.bd.desconectar()

    def listar_usuarios(self):
        """Listar todos os usuários cadastrados."""
        self.bd.conectar()
        try:
            self.bd.cursor.execute("SELECT * FROM usuario;")
            resultado = self.bd.cursor.fetchall()
            if resultado:
                print("Lista de usuários cadastrados:")
                for usuario in resultado:
                    print(f"ID = {usuario[0]}, Nome = {usuario[1]}, CPF = {usuario[2]}, Telefone = {usuario[3]}")
            else:
                print("Nenhum usuário encontrado.")
        except Exception as e:
            print(f"Erro ao listar usuários: {e}")
        finally:
            self.bd.desconectar()
