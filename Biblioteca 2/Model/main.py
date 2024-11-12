import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conexao = None
        self.cursor = None

    def conectar(self):
        try:
            self.conexao = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.conexao.is_connected():
                self.cursor = self.conexao.cursor()
                print("Conexão com o banco de dados estabelecida com sucesso.")
        except Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            self.conexao = None
            self.cursor = None

    def desconectar(self):
        """Fecha a conexão e o cursor se estiverem abertos."""
        if self.cursor:
            self.cursor.close()
        if self.conexao and self.conexao.is_connected():
            self.conexao.close()
        print("Conexão com o banco de dados fechada.")

    def executar_query(self, query, params=None):
        """Executa uma query no banco de dados."""
        try:
            if self.cursor:
                self.cursor.execute(query, params or ())
                self.conexao.commit()  # Commit as mudanças
            else:
                print("Erro: Nenhuma conexão com o banco de dados estabelecida.")
        except Error as e:
            print(f"Erro ao executar a query: {e}")
            self.conexao.rollback()  # Em caso de erro, faz rollback



    
        
# rafaelatonta = Database("192.168.0.59","suporte","suporte","biblioteca")     
# rafaelatonta.conectar()
# print(vars(rafaelatonta.conexao))
# rafaelatonta.cursor.execute("select * from livro")
# print(rafaelatonta.cursor.fetchall())

# # print(vars(rafaelatonta.conexao))
# rafaelatonta.desconectar()
# print(vars(rafaelatonta.conexao))

# criar uma classe ControllerLivro
# sera responsavel por executar as querys SQL chamando o banco de dados e o livro
# ajustar a classe livro para que implemente um crud (a classe )
#/////////////////////////////////////////////////////////////
# Instanciando o objeto de conexão com o banco de dados
db = Database(host="10.28.2.59", user="suporte", password="suporte", database="biblioteca")

# Conectando ao banco de dados
db.conectar()

# Criando um novo livro
livro = Livros("Dom Casmurro", "Machado de Assis", "Ficção", 123)

# Executando a query de criação de livro
sql_create = livro.create()
db.executar_query(sql_create, (livro.titulo, livro.autor, livro.genero, livro.status, livro.cod_livro))

# Consultando um livro específico
sql_select = livro.select()
db.executar_query(sql_select)

# Desconectando do banco de dados
db.desconectar()
