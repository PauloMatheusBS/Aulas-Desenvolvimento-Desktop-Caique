from Model.emprestimo import Emprestimo
from Model.main import Database

class ControllerEmprestimo:
    def cadastrarEmprestimo(self):
        bd = Database("10.28.2.59", "suporte", "suporte", "biblioteca")
        bd.conectar()

        emprestimo = Emprestimo(id_livro=1, id_usuario=1)  # Exemplo de empréstimo do livro com ID 1 para o usuário com ID 1
        try:
            bd.cursor.execute(emprestimo.create())
            bd.conexao.commit()
            print("Empréstimo cadastrado com sucesso!")
        except Exception as e:
            print(f"Erro ao cadastrar empréstimo: {e}")
            bd.conexao.rollback()
        finally:
            bd.desconectar()

    def excluirEmprestimo(self):
        bd = Database("10.28.2.59", "suporte", "suporte", "biblioteca")
        bd.conectar()

        emprestimo = Emprestimo(id_livro=1, id_usuario=1)  # Exemplo de exclusão de empréstimo para o livro com ID 1 e usuário com ID 1
        emprestimo.id_emprestimo = 1  # ID do empréstimo a ser excluído
        try:
            bd.cursor.execute(emprestimo.delete())
            bd.conexao.commit()
            print("Empréstimo excluído com sucesso!")
        except Exception as e:
            print(f"Erro ao excluir empréstimo: {e}")
            bd.conexao.rollback()
        finally:
            bd.desconectar()

    def consultarEmprestimos(self):
        bd = Database("10.28.2.59", "suporte", "suporte", "biblioteca")
        bd.conectar()

        emprestimo = Emprestimo(id_livro=1, id_usuario=1)  # Exemplo de consulta de empréstimo do livro com ID 1 para o usuário com ID 1
        try:
            bd.cursor.execute(emprestimo.select())
            resultado = bd.cursor.fetchall()
            for linha in resultado:
                print(linha)
        except Exception as e:
            print(f"Erro ao consultar empréstimos: {e}")
        finally:
            bd.desconectar()

    def consultarTodosEmprestimos(self):
        bd = Database("10.28.2.59", "suporte", "suporte", "biblioteca")
        bd.conectar()

        emprestimo = Emprestimo(id_livro=None, id_usuario=None)  # Não estamos filtrando por livro ou usuário aqui
        try:
            bd.cursor.execute(emprestimo.select_all())
            resultado = bd.cursor.fetchall()
            for linha in resultado:
                print(linha)
        except Exception as e:
            print(f"Erro ao consultar todos os empréstimos: {e}")
        finally:
            bd.desconectar()


# Teste da ControllerEmprestimo
controladora_emprestimo = ControllerEmprestimo()

# Cadastro de um empréstimo
controladora_emprestimo.cadastrarEmprestimo()

# Consulta de todos os empréstimos
controladora_emprestimo.consultarTodosEmprestimos()

# Consulta de um empréstimo específico
controladora_emprestimo.consultarEmprestimos()

# Exclusão de um empréstimo
controladora_emprestimo.excluirEmprestimo()

