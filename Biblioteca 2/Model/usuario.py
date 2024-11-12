from main import Database
from Controller import controller_usuario

class Usuario:
    def __init__(self, nome, cpf, telefone, id_usuario=None):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.id_usuario = id_usuario  

    def create(self):
        return 'INSERT INTO usuario(nome, cpf, telefone) VALUES(%s, %s, %s);'

    def delete(self):
        if not self.id_usuario:
            raise ValueError("O ID do usuário deve ser definido para exclusão.")
        return 'DELETE FROM usuario WHERE id_usuario = %s;'

    def update(self, novo_nome=None, novo_cpf=None, novo_telefone=None):
        set_clause = []
        
        if novo_nome:
            set_clause.append(f'nome = %s')
        if novo_cpf:
            set_clause.append(f'cpf = %s')
        if novo_telefone:
            set_clause.append(f'telefone = %s')

        if not set_clause:
            raise ValueError("Nenhum campo para atualizar foi fornecido.")

        set_clause_str = ", ".join(set_clause)
        return f'UPDATE usuario SET {set_clause_str} WHERE id_usuario = %s;'

    def select(self):
        if not self.id_usuario:
            raise ValueError("O ID do usuário deve ser definido para consulta.")
        return 'SELECT * FROM usuario WHERE id_usuario = %s;'


#/////////////////////////////////////////////////////////////////////////////////////////////////
usuario = Usuario(nome="João Silva", cpf="123.456.789-00", telefone="99999-8888")

# Criar no banco
sql_create = usuario.create()
cursor.execute(sql_create, (usuario.nome, usuario.cpf, usuario.telefone))
# Após a execução, o banco de dados atribui automaticamente o id_usuario

# Atualizar no banco
sql_update = usuario.update(novo_nome="João Silva Jr.", novo_telefone="98765-4321")
cursor.execute(sql_update, ("João Silva Jr.", "98765-4321", usuario.id_usuario))

# Excluir no banco
sql_delete = usuario.delete()
cursor.execute(sql_delete, (usuario.id_usuario,))


#//////////////////////////////////////////////////////////
# Criação do controlador de usuários
controladora_usuario = ControllerUsuario()

# Cadastrar um novo usuário
controladora_usuario.cadastrar_usuario(nome="Maria", cpf="12345678901", telefone="999999999")

# Listar todos os usuários cadastrados
controladora_usuario.listar_usuarios()

# Consultar um usuário pelo ID
controladora_usuario.consultar_usuario(id_usuario=1)

# Atualizar dados de um usuário
controladora_usuario.atualizar_usuario(id_usuario=1, novo_nome="Maria Silva", novo_telefone="888888888")

# Excluir um usuário pelo ID
controladora_usuario.excluir_usuario(id_usuario=1)
