class Livros():
    def __init__(self, titulo, autor, genero, cod_livro):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.cod_livro = cod_livro

        self.status = "Disponivel"
        self.usuario = None

    def create(self):
        return 'insert into livro(titulo, autor, genero) values()'


    
