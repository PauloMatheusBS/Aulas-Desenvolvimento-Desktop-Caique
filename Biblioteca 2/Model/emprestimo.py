class Emprestimo:
    def __init__(self, id_livro, id_usuario, id_emprestimo=None):
        self.id_livro = id_livro
        self.id_usuario = id_usuario
        self.id_emprestimo = id_emprestimo  # O id_emprestimo pode ser None até ser salvo no banco

    def create(self):
        # Usando placeholders para prevenir SQL Injection
        return 'INSERT INTO emprestimo(id_livro, id_usuario) VALUES(%s, %s);'

    def delete(self):
        if not self.id_emprestimo:
            raise ValueError("Não é possível excluir um empréstimo sem o ID.")
        # Usando placeholder para evitar SQL Injection
        return 'DELETE FROM emprestimo WHERE id_emprestimo = %s;'

    def select(self):
        # Usando placeholder para evitar SQL Injection
        return 'SELECT * FROM emprestimo WHERE id_livro = %s AND id_usuario = %s;'

    def select_all(self):
        # Consultar todos os empréstimos
        return 'SELECT * FROM emprestimo;'
    
#///////////////////////////////////////////////////////////////////////////////////////////

    # Supondo que você tenha uma conexão com o banco de dados aberta:
db = Database(host="10.28.2.59", user="suporte", password="suporte", database="biblioteca")
db.conectar()

# Criando um empréstimo
emprestimo = Emprestimo(id_livro=1, id_usuario=2)

# Inserindo o empréstimo no banco de dados
sql_create = emprestimo.create()
db.executar_query(sql_create, (emprestimo.id_livro, emprestimo.id_usuario))

# Consultando um empréstimo específico
sql_select = emprestimo.select()
db.executar_query(sql_select, (emprestimo.id_livro, emprestimo.id_usuario))

# Excluindo um empréstimo (supondo que o id_emprestimo seja conhecido)
emprestimo.id_emprestimo = 1  # ID do empréstimo após inserção
sql_delete = emprestimo.delete()
db.executar_query(sql_delete, (emprestimo.id_emprestimo,))

# Consultando todos os empréstimos
sql_select_all = emprestimo.select_all()
db.executar_query(sql_select_all)

# Fechando a conexão
db.desconectar()


