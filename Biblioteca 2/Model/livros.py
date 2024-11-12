class Livros:
    def __init__(self, titulo, autor, genero, codigo):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.codigo = codigo
        self.id_livro = None  
        self.status = "Disponivel"

    def create(self):
        return f'INSERT INTO livro(titulo, autor, genero, status, codigo) VALUES("{self.titulo}", "{self.autor}", "{self.genero}", "{self.status}", {self.codigo});'

    def delete(self):
        return f'DELETE FROM livro WHERE id_livro = {self.id_livro};'

    def update(self, novo_titulo=None, novo_autor=None, novo_genero=None, novo_status=None):
        set_clause = []
        
        if novo_titulo:
            set_clause.append(f'titulo = "{novo_titulo}"')
        if novo_autor:
            set_clause.append(f'autor = "{novo_autor}"')
        if novo_genero:
            set_clause.append(f'genero = "{novo_genero}"')
        if novo_status:
            set_clause.append(f'status = "{novo_status}"')
        
        set_clause_str = ", ".join(set_clause)
        return f'UPDATE livro SET {set_clause_str} WHERE id_livro = {self.id_livro};'

    def select(self):
        return f'SELECT * FROM livro WHERE id_livro = {self.id_livro};'




    
