class Livros:
    def __init__(self, titulo, autor, genero, codigo, id_livro=None):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.codigo = codigo
        self.id_livro = id_livro  # O id_livro pode ser None até ser salvo no banco
        self.status = "Disponível"  # Status inicial do livro

    def create(self):
        # Query de inserção no banco
        return 'INSERT INTO livro(titulo, autor, genero, status, codigo) VALUES(%s, %s, %s, %s, %s);', (
            self.titulo, self.autor, self.genero, self.status, self.codigo)

    def delete(self):
        # Verifica se o id_livro está definido
        if not self.id_livro:
            raise ValueError("Não é possível excluir um livro sem o ID.")
        return 'DELETE FROM livro WHERE id_livro = %s;', (self.id_livro,)

    def update(self, novo_titulo=None, novo_autor=None, novo_genero=None, novo_status=None):
        if not self.id_livro:
            raise ValueError("Não é possível atualizar um livro sem o ID.")
        
        set_clause = []
        params = []

        if novo_titulo:
            set_clause.append('titulo = %s')
            params.append(novo_titulo)
        if novo_autor:
            set_clause.append('autor = %s')
            params.append(novo_autor)
        if novo_genero:
            set_clause.append('genero = %s')
            params.append(novo_genero)
        if novo_status:
            set_clause.append('status = %s')
            params.append(novo_status)

        if not set_clause:
            raise ValueError("Nenhum campo para atualização foi fornecido.")
        
        set_clause_str = ", ".join(set_clause)
        params.append(self.id_livro)  # Inclui o id_livro no final dos parâmetros
        
        return f'UPDATE livro SET {set_clause_str} WHERE id_livro = %s;', tuple(params)


    def select(self):
        if not self.id_livro:
            raise ValueError("Não é possível consultar um livro sem o ID.")
        return 'SELECT * FROM livro WHERE id_livro = %s;', (self.id_livro,)
    
    def create(self) -> tuple:
        return 'INSERT INTO livro(titulo, autor, genero, status, codigo) VALUES(%s, %s, %s, %s, %s);', (
            self.titulo, self.autor, self.genero, self.status, self.codigo)

