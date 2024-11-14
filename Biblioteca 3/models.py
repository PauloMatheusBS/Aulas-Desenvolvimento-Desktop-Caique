import sqlite3
from datetime import datetime

# Função para criar a conexão com o banco de dados
def get_connection():
    return sqlite3.connect('biblioteca.db')

# Função para criar as tabelas no banco de dados
def create_tables():
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS livros (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        titulo TEXT NOT NULL,
                        autor TEXT NOT NULL,
                        isbn TEXT UNIQUE NOT NULL,
                        genero TEXT,
                        disponivel BOOLEAN DEFAULT 1)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL,
                        email TEXT UNIQUE NOT NULL,
                        senha TEXT NOT NULL,
                        cpf TEXT UNIQUE NOT NULL,
                        administrador BOOLEAN DEFAULT 0)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS emprestimos (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        usuario_id INTEGER,
                        livro_id INTEGER,
                        data_emprestimo TEXT,
                        data_devolucao TEXT,
                        status TEXT DEFAULT 'pendente',
                        FOREIGN KEY(usuario_id) REFERENCES usuarios(id),
                        FOREIGN KEY(livro_id) REFERENCES livros(id))''')
    
    conn.commit()
    conn.close()

# Model para Livro
class Livro:
    def __init__(self, id, titulo, autor, isbn, genero, disponivel=True):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.genero = genero
        self.disponivel = disponivel

    @staticmethod
    def cadastrar_livro(titulo, autor, isbn, genero):
        conn = get_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute("INSERT INTO livros (titulo, autor, isbn, genero) VALUES (?, ?, ?, ?)",
                           (titulo, autor, isbn, genero))
            conn.commit()
        except sqlite3.IntegrityError:
            print("Erro: ISBN já cadastrado.")
        finally:
            conn.close()

    @staticmethod
    def consultar_livro(isbn=None, titulo=None, autor=None, genero=None):
        conn = get_connection()
        cursor = conn.cursor()
        
        query = "SELECT * FROM livros WHERE"
        params = []
        
        if isbn:
            query += " isbn = ?"
            params.append(isbn)
        if titulo:
            query += " titulo LIKE ?"
            params.append('%' + titulo + '%')
        if autor:
            query += " autor LIKE ?"
            params.append('%' + autor + '%')
        if genero:
            query += " genero LIKE ?"
            params.append('%' + genero + '%')

        cursor.execute(query, params)
        livros = cursor.fetchall()
        conn.close()
        return livros

    @staticmethod
    def atualizar_livro(id, titulo=None, autor=None, genero=None):
        conn = get_connection()
        cursor = conn.cursor()
        
        if titulo:
            cursor.execute("UPDATE livros SET titulo = ? WHERE id = ?", (titulo, id))
        if autor:
            cursor.execute("UPDATE livros SET autor = ? WHERE id = ?", (autor, id))
        if genero:
            cursor.execute("UPDATE livros SET genero = ? WHERE id = ?", (genero, id))
        
        conn.commit()
        conn.close()

    @staticmethod
    def excluir_livro(id):
        conn = get_connection()
        cursor = conn.cursor()
        
        # Verifica se o livro está emprestado antes de excluir
        cursor.execute("SELECT * FROM emprestimos WHERE livro_id = ? AND status = 'pendente'", (id,))
        if cursor.fetchone():
            print("Erro: Livro não pode ser excluído, pois está emprestado.")
        else:
            cursor.execute("DELETE FROM livros WHERE id = ?", (id,))
            conn.commit()
        
        conn.close()

# Model para Usuário
class Usuario:
    def __init__(self, id, nome, email, senha, cpf, administrador=False):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha
        self.cpf = cpf
        self.administrador = administrador

    @staticmethod
    def cadastrar_usuario(nome, email, senha, cpf, administrador=False):
        conn = get_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute("INSERT INTO usuarios (nome, email, senha, cpf, administrador) VALUES (?, ?, ?, ?, ?)",
                           (nome, email, senha, cpf, administrador))
            conn.commit()
        except sqlite3.IntegrityError:
            print("Erro: Email ou CPF já cadastrados.")
        finally:
            conn.close()

    @staticmethod
    def consultar_usuario(nome=None, email=None, cpf=None):
        conn = get_connection()
        cursor = conn.cursor()
        
        query = "SELECT * FROM usuarios WHERE"
        params = []
        
        if nome:
            query += " nome LIKE ?"
            params.append('%' + nome + '%')
        if email:
            query += " email = ?"
            params.append(email)
        if cpf:
            query += " cpf = ?"
            params.append(cpf)

        cursor.execute(query, params)
        usuarios = cursor.fetchall()
        conn.close()
        return usuarios

    @staticmethod
    def atualizar_usuario(id, nome=None, email=None, senha=None):
        conn = get_connection()
        cursor = conn.cursor()
        
        if nome:
            cursor.execute("UPDATE usuarios SET nome = ? WHERE id = ?", (nome, id))
        if email:
            cursor.execute("UPDATE usuarios SET email = ? WHERE id = ?", (email, id))
        if senha:
            cursor.execute("UPDATE usuarios SET senha = ? WHERE id = ?", (senha, id))
        
        conn.commit()
        conn.close()

    @staticmethod
    def excluir_usuario(id):
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM emprestimos WHERE usuario_id = ? AND status = 'pendente'", (id,))
        if cursor.fetchone():
            print("Erro: Usuário não pode ser excluído, pois tem empréstimos pendentes.")
        else:
            cursor.execute("DELETE FROM usuarios WHERE id = ?", (id,))
            conn.commit()
        
        conn.close()

# Model para Empréstimo
class Emprestimo:
    def __init__(self, id, usuario_id, livro_id, data_emprestimo, status):
        self.id = id
        self.usuario_id = usuario_id
        self.livro_id = livro_id
        self.data_emprestimo = data_emprestimo
        self.status = status

    @staticmethod
    def realizar_emprestimo(usuario_id, livro_id):
        conn = get_connection()
        cursor = conn.cursor()
        
        # Verifica se o livro está disponível e se o usuário tem menos de 3 livros emprestados
        cursor.execute("SELECT disponivel FROM livros WHERE id = ?", (livro_id,))
        livro = cursor.fetchone()
        
        if livro and livro[0] == 1:
            cursor.execute("SELECT COUNT(*) FROM emprestimos WHERE usuario_id = ? AND status = 'pendente'", (usuario_id,))
            count = cursor.fetchone()[0]
            
            if count < 3:
                data_emprestimo = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                cursor.execute("INSERT INTO emprestimos (usuario_id, livro_id, data_emprestimo, status) VALUES (?, ?, ?, 'pendente')",
                               (usuario_id, livro_id, data_emprestimo))
                cursor.execute("UPDATE livros SET disponivel = 0 WHERE id = ?", (livro_id,))
                conn.commit()
            else:
                print("Erro: Usuário já tem 3 livros emprestados.")
        else:
            print("Erro: Livro não disponível.")
        
        conn.close()

    @staticmethod
    def devolver_emprestimo(emprestimo_id):
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute("UPDATE emprestimos SET status = 'devolvido' WHERE id = ?", (emprestimo_id,))
        cursor.execute("UPDATE livros SET disponivel = 1 WHERE id = (SELECT livro_id FROM emprestimos WHERE id = ?)", (emprestimo_id,))
        conn.commit()
        conn.close()

# Inicializa o banco de dados e cria as tabelas
create_tables()
