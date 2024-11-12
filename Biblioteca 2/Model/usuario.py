class Usuario:
    def __init__(self, nome, cpf, telefone):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.id_usuario = None  

    def create(self):
        return f'INSERT INTO usuario(nome, cpf, telefone) VALUES("{self.nome}", "{self.cpf}", "{self.telefone}");'

    def delete(self):
        return f'DELETE FROM usuario WHERE id_usuario = {self.id_usuario};'

    def update(self, novo_nome=None, novo_cpf=None, novo_telefone=None):
        set_clause = []
        
        if novo_nome:
            set_clause.append(f'nome = "{novo_nome}"')
        if novo_cpf:
            set_clause.append(f'cpf = "{novo_cpf}"')
        if novo_telefone:
            set_clause.append(f'telefone = "{novo_telefone}"')
        
        set_clause_str = ", ".join(set_clause)
        return f'UPDATE usuario SET {set_clause_str} WHERE id_usuario = {self.id_usuario};'

    def select(self):
        return f'SELECT * FROM usuario WHERE id_usuario = {self.id_usuario};'

