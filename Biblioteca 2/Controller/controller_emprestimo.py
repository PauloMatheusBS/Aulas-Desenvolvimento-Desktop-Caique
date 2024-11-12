from Model.emprestimo import Emprestimo
from Model.main import Database

class ControllerEmprestimo:
    def cadastrarEmprestimo(self):
        bd = Database("10.28.2.59", "suporte", "suporte", "biblioteca")
        bd.conectar()

        emprestimo = Emprestimo(id_livro=1, id_usuario=1)  
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

        emprestimo = Emprestimo(id_livro=1, id_usuario=1)  
        emprestimo.id_emprestimo = 1  
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

        emprestimo = Emprestimo(id_livro=1, id_usuario=1)  
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

        emprestimo = Emprestimo(id_livro=None, id_usuario=None)  
        try:
            bd.cursor.execute(emprestimo.select_all())
            resultado = bd.cursor.fetchall()
            for linha in resultado:
                print(linha)
        except Exception as e:
            print(f"Erro ao consultar todos os empréstimos: {e}")
        finally:
            bd.desconectar()



controladora_emprestimo = ControllerEmprestimo()


controladora_emprestimo.cadastrarEmprestimo()


controladora_emprestimo.consultarTodosEmprestimos()


controladora_emprestimo.consultarEmprestimos()


controladora_emprestimo.excluirEmprestimo()

