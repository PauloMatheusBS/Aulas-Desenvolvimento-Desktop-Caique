class Livros:
    def __init__(self, titulo, autor, genero, codigo, id_livro=None):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.codigo = codigo
        self.id_livro = id_livro  # O id_livro pode ser None até ser salvo no banco
        self.status = "Disponivel"  

    def create(self):
        return 'INSERT INTO livro(titulo, autor, genero, status, codigo) VALUES(%s, %s, %s, %s, %s);' #placeholder pra não trollar a entrada
  
    def delete(self):
        if not self.id_livro:
            raise ValueError("Não é possível excluir um livro sem o ID.")
        return 'DELETE FROM livro WHERE id_livro = %s;'  #placeholder pra não trollar a entrada

    def update(self, novo_titulo=None, novo_autor=None, novo_genero=None, novo_status=None):
        if not self.id_livro:
            raise ValueError("Não é possível atualizar um livro sem o ID.")
        
        set_clause = []
        
        if novo_titulo:
            set_clause.append('titulo = %s')
        if novo_autor:
            set_clause.append('autor = %s')
        if novo_genero:
            set_clause.append('genero = %s')
        if novo_status:
            set_clause.append('status = %s')

        if not set_clause:
            raise ValueError("Nenhum campo para atualização foi fornecido.")
        
        set_clause_str = ", ".join(set_clause)
        return f'UPDATE livro SET {set_clause_str} WHERE id_livro = %s;'

    def select(self):
        if not self.id_livro:
            raise ValueError("Não é possível consultar um livro sem o ID.")
        # Usando placeholder para evitar SQL Injection
        return 'SELECT * FROM livro WHERE id_livro = %s;'



#////////////////////////////////////////////////////////////////////////////////
# Supondo que você tenha uma conexão com o banco de dados aberta:
db = Database(host="10.28.2.59", user="suporte", password="suporte", database="biblioteca")
db.conectar()

# Criando um livro
livro = Livros(titulo="Dom Casmurro", autor="Machado de Assis", genero="Ficção", codigo=123)

# Executando a consulta de criação do livro
sql_create = livro.create()
db.executar_query(sql_create, (livro.titulo, livro.autor, livro.genero, livro.status, livro.codigo))

# Agora que o livro foi inserido, podemos atualizar, consultar ou excluir

# Atualizando um livro (supondo que o id_livro seja conhecido)
livro.id_livro = 1  # ID do livro após inserção
sql_update = livro.update(novo_status="Indisponível")
db.executar_query(sql_update, ("Indisponível", livro.id_livro))

# Consultando um livro pelo ID
sql_select = livro.select()
db.executar_query(sql_select, (livro.id_livro,))

# Excluindo um livro
sql_delete = livro.delete()
db.executar_query(sql_delete, (livro.id_livro,))

# Fechando a conexão
db.desconectar()



    
