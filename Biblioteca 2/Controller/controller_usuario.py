from Model.usuario import Usuario
from Model.main import Database

class ControllerUsuario:
    def __init__(self):
        self.bd = Database("10.28.2.59", "suporte", "suporte", "biblioteca")  # Conexão com o banco de dados

    def _executar_query(self, query, params):
        """Método auxiliar para executar queries com tratamento de exceções."""
        try:
            self.bd.conectar()
            self.bd.cursor.execute(query, params)
            self.bd.conexao.commit()
        except Exception as e:
            print(f"Erro ao executar query: {e}")
            self.bd.conexao.rollback()
            return False
        finally:
            self.bd.desconectar()
        return True

    def cadastrar_usuario(self, nome, cpf, telefone):
        """Cadastrar um novo usuário na base de dados."""
        usuario = Usuario(nome, cpf, telefone)
        query, params = usuario.create()
        if self._executar_query(query, params):
            print("Usuário cadastrado com sucesso!")
        else:
            print("Erro ao cadastrar usuário.")

    def excluir_usuario(self, id_usuario):
        """Excluir um usuário existente."""
        usuario = Usuario(nome=None, cpf=None, telefone=None, id_usuario=id_usuario)  # Passando o id_usuario
        query, params = usuario.delete()
        if self._executar_query(query, params):
            print("Usuário excluído com sucesso!")
        else:
            print("Erro ao excluir usuário.")

    def atualizar_usuario(self, id_usuario, novo_nome=None, novo_cpf=None, novo_telefone=None):
        """Atualizar dados de um usuário."""
        usuario = Usuario(nome=novo_nome, cpf=novo_cpf, telefone=novo_telefone, id_usuario=id_usuario)
        query, params = usuario.update(novo_nome, novo_cpf, novo_telefone)
        if self._executar_query(query, params):
            print("Usuário atualizado com sucesso!")
        else:
            print("Erro ao atualizar usuário.")

    def consultar_usuario(self, id_usuario):
        """Consultar um usuário pelo ID."""
        usuario = Usuario(nome=None, cpf=None, telefone=None, id_usuario=id_usuario)
        query, params = usuario.select()
        try:
            self.bd.conectar()
            self.bd.cursor.execute(query, params)
            resultado = self.bd.cursor.fetchone()
            if resultado:
                print(f"Usuário encontrado: ID = {resultado[0]}, Nome = {resultado[1]}, CPF = {resultado[2]}, Telefone = {resultado[3]}")
            else:
                print(f"Usuário com ID {id_usuario} não encontrado.")
        except Exception as e:
            print(f"Erro ao consultar usuário: {e}")
        finally:
            self.bd.desconectar()


    def listar_usuarios(self):
        """Listar todos os usuários cadastrados."""
        try:
            self.bd.conectar()
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

    def _executar_query(self, query: str, params: tuple) -> bool:
        """Método auxiliar para executar queries com tratamento de exceções."""
        try:
            self.bd.conectar()
            self.bd.cursor.execute(query, params)
            self.bd.conexao.commit()
        except Exception as e:
            print(f"Erro ao executar query: {e}")
            self.bd.conexao.rollback()
            return False
        finally:
            self.bd.desconectar()
        return True
