from Model.usuario import Usuario
from Model.main import Database

class ControllerUsuario:
    def cadastrarUsuario(self):
        bd = Database("10.28.2.59", "suporte", "suporte", "biblioteca")
        bd.conectar()

        usuario = Usuario("João Silva", "123.456.789-00", "99999-8888")
        try:
            bd.cursor.execute(usuario.create())
            bd.conexao.commit()
            print("Usuário cadastrado com sucesso!")
        except Exception as e:
            print(f"Erro ao cadastrar usuário: {e}")
            bd.conexao.rollback()
        finally:
            bd.desconectar()

    def excluirUsuario(self):
        bd = Database("10.28.2.59", "suporte", "suporte", "biblioteca")
        bd.conectar()

        usuario = Usuario("João Silva", "123.456.789-00", "99999-8888")
        usuario.id_usuario = 1  
        try:
            bd.cursor.execute(usuario.delete())
            bd.conexao.commit()
            print("Usuário excluído com sucesso!")
        except Exception as e:
            print(f"Erro ao excluir usuário: {e}")
            bd.conexao.rollback()
        finally:
            bd.desconectar()

    def atualizarUsuario(self):
        bd = Database("10.28.2.59", "suporte", "suporte", "biblioteca")
        bd.conectar()

        usuario = Usuario("João Silva", "123.456.789-00", "99999-8888")
        usuario.id_usuario = 1  
        novo_nome = "João Silva Jr."
        novo_telefone = "98765-4321"
        try:
            bd.cursor.execute(usuario.update(novo_nome=novo_nome, novo_telefone=novo_telefone))
            bd.conexao.commit()
            print("Usuário atualizado com sucesso!")
        except Exception as e:
            print(f"Erro ao atualizar usuário: {e}")
            bd.conexao.rollback()
        finally:
            bd.desconectar()

    def consultarUsuario(self):
        bd = Database("10.28.2.59", "suporte", "suporte", "biblioteca")
        bd.conectar()

        usuario = Usuario("João Silva", "123.456.789-00", "99999-8888")
        usuario.id_usuario = 1  
        try:
            bd.cursor.execute(usuario.select())
            resultado = bd.cursor.fetchall()
            for linha in resultado:
                print(linha)
        except Exception as e:
            print(f"Erro ao consultar usuário: {e}")
        finally:
            bd.desconectar()



controladora_usuario = ControllerUsuario()

controladora_usuario.cadastrarUsuario()
controladora_usuario.consultarUsuario()
controladora_usuario.atualizarUsuario()
controladora_usuario.excluirUsuario()

