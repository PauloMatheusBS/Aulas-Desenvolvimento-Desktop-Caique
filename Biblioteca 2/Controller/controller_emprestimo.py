from Model.emprestimo import Emprestimo
from Model.main import Database

class ControllerEmprestimo:
    def __init__(self):
        # Conexão com o banco de dados
        self.bd = Database("10.28.2.59", "suporte", "suporte", "biblioteca")

    def conectar_bd(self):
        """Método centralizado para conectar ao banco de dados."""
        self.bd.conectar()

    def desconectar_bd(self):
        """Método centralizado para desconectar do banco de dados."""
        self.bd.desconectar()

    def cadastrarEmprestimo(self, id_livro, id_usuario):
        """Cadastrar um novo empréstimo de livro para um usuário."""
        emprestimo = Emprestimo(id_livro, id_usuario)
        self.conectar_bd()
        try:
            self.bd.cursor.execute(emprestimo.create())
            self.bd.conexao.commit()
            print("Empréstimo cadastrado com sucesso!")
        except Exception as e:
            print(f"Erro ao cadastrar empréstimo: {e}")
            self.bd.conexao.rollback()
        finally:
            self.desconectar_bd()

    def excluirEmprestimo(self, id_emprestimo):
        """Excluir um empréstimo existente."""
        emprestimo = Emprestimo(id_livro=None, id_usuario=None)
        emprestimo.id_emprestimo = id_emprestimo
        self.conectar_bd()
        try:
            self.bd.cursor.execute(emprestimo.delete())
            self.bd.conexao.commit()
            print("Empréstimo excluído com sucesso!")
        except Exception as e:
            print(f"Erro ao excluir empréstimo: {e}")
            self.bd.conexao.rollback()
        finally:
            self.desconectar_bd()

    def consultarEmprestimos(self, id_livro=None, id_usuario=None):
        """Consultar empréstimos, podendo filtrar por livro ou usuário."""
        emprestimo = Emprestimo(id_livro, id_usuario)
        self.conectar_bd()
        try:
            if id_livro and id_usuario:
                self.bd.cursor.execute(emprestimo.select())
            elif id_livro:
                emprestimo.id_livro = id_livro
                self.bd.cursor.execute(emprestimo.select())
            elif id_usuario:
                emprestimo.id_usuario = id_usuario
                self.bd.cursor.execute(emprestimo.select())
            else:
                print("Informe pelo menos um parâmetro para consulta (id_livro ou id_usuario).")
                return

            resultado = self.bd.cursor.fetchall()
            if resultado:
                for linha in resultado:
                    print(linha)
            else:
                print("Nenhum empréstimo encontrado.")
        except Exception as e:
            print(f"Erro ao consultar empréstimos: {e}")
        finally:
            self.desconectar_bd()

    def consultarTodosEmprestimos(self):
        """Consultar todos os empréstimos."""
        emprestimo = Emprestimo(id_livro=None, id_usuario=None)
        self.conectar_bd()
        try:
            self.bd.cursor.execute(emprestimo.select_all())
            resultado = self.bd.cursor.fetchall()
            if resultado:
                for linha in resultado:
                    print(linha)
            else:
                print("Nenhum empréstimo registrado.")
        except Exception as e:
            print(f"Erro ao consultar todos os empréstimos: {e}")
        finally:
            self.desconectar_bd()

controladora_emprestimo = ControllerEmprestimo()

# Cadastrar empréstimo
controladora_emprestimo.cadastrarEmprestimo(id_livro=1, id_usuario=1)

# Consultar todos os empréstimos
controladora_emprestimo.consultarTodosEmprestimos()

# Consultar empréstimos filtrados por livro ou usuário
controladora_emprestimo.consultarEmprestimos(id_livro=1)
controladora_emprestimo.consultarEmprestimos(id_usuario=1)

# Excluir um empréstimo
controladora_emprestimo.excluirEmprestimo(id_emprestimo=1)
