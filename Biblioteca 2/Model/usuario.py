class Usuario:
    def __init__(self, nome, cpf, telefone, id_usuario=None):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.id_usuario = id_usuario  

    def create(self):
        # A query para inserir dados no banco
        return 'INSERT INTO usuario(nome, cpf, telefone) VALUES(%s, %s, %s);', (self.nome, self.cpf, self.telefone)

    def delete(self):
        # Verifica se o id_usuario está definido para poder deletar
        if not self.id_usuario:
            raise ValueError("O ID do usuário deve ser definido para exclusão.")
        return 'DELETE FROM usuario WHERE id_usuario = %s;', (self.id_usuario,)

    def update(self, novo_nome=None, novo_cpf=None, novo_telefone=None):
        # Monta a cláusula SET dinamicamente
        set_clause = []
        params = []
        
        if novo_nome:
            set_clause.append('nome = %s')
            params.append(novo_nome)
        if novo_cpf:
            set_clause.append('cpf = %s')
            params.append(novo_cpf)
        if novo_telefone:
            set_clause.append('telefone = %s')
            params.append(novo_telefone)

        if not set_clause:
            raise ValueError("Nenhum campo para atualizar foi fornecido.")

        set_clause_str = ", ".join(set_clause)
        # O ID do usuário sempre deve ser fornecido para atualização
        params.append(self.id_usuario)
        
        return f'UPDATE usuario SET {set_clause_str} WHERE id_usuario = %s;', tuple(params)

    def select(self):
        # O ID do usuário deve ser fornecido para consulta
        if not self.id_usuario:
            raise ValueError("O ID do usuário deve ser definido para consulta.")
        return 'SELECT * FROM usuario WHERE id_usuario = %s;', (self.id_usuario,)


# Exemplo de uso da classe Usuario - Este código pode ser removido após testes.
usuario = Usuario(nome="João Silva", cpf="123.456.789-00", telefone="99999-8888")

# # Exemplo de criação no banco
# sql_create = usuario.create()
# cursor.execute(sql_create, (usuario.nome, usuario.cpf, usuario.telefone))

# # Exemplo de atualização no banco
# sql_update = usuario.update(novo_nome="João Silva Jr.", novo_telefone="98765-4321")
# cursor.execute(sql_update, ("João Silva Jr.", "98765-4321", usuario.id_usuario))

# # Exemplo de exclusão no banco
# sql_delete = usuario.delete()
# cursor.execute(sql_delete, (usuario.id_usuario,))

# # Exemplo de consulta no banco
# sql_select = usuario.select()
# cursor.execute(sql_select, (usuario.id_usuario,))
# resultado = cursor.fetchone()
