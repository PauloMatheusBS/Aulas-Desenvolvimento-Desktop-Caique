class Emprestimo:
    def __init__(self, id_livro, id_usuario):
        self.id_livro = id_livro
        self.id_usuario = id_usuario
        self.id_emprestimo = None  # Será gerado automaticamente pelo banco (auto_increment)

    def create(self):
        return f'INSERT INTO emprestimo(id_livro, id_usuario) VALUES({self.id_livro}, {self.id_usuario});'

    def delete(self):
        return f'DELETE FROM emprestimo WHERE id_emprestimo = {self.id_emprestimo};'

    def select(self):
        return f'SELECT * FROM emprestimo WHERE id_livro = {self.id_livro} AND id_usuario = {self.id_usuario};'

    def select_all(self):
        return f'SELECT * FROM emprestimo;'
