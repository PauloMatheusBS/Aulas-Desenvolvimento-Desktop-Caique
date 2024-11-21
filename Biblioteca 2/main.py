from Controller.controller_usuario import ControllerUsuario
from Controller.controller_livro import ControllerLivro
from Model.main import Database


def main():
    # Exemplo de uso da controladora de usuários
    controlador_usuario = ControllerUsuario()

    # Cadastrar um novo usuário
    print("Cadastrando usuário...")
    controlador_usuario.cadastrar_usuario(nome="João Silva", cpf="123.456.789-00", telefone="99999-8888")

    # Consultar um usuário pelo ID (suponha que o ID 1 existe)
    print("\nConsultando usuário com ID 1...")
    controlador_usuario.consultar_usuario(id_usuario=1)

    # Atualizar informações de um usuário
    print("\nAtualizando usuário com ID 1...")
    controlador_usuario.atualizar_usuario(id_usuario=1, novo_nome="João Silva Jr.", novo_telefone="98765-4321")

    # Excluir um usuário pelo ID
    print("\nExcluindo usuário com ID 1...")
    controlador_usuario.excluir_usuario(id_usuario=1)

    # Exemplo de uso da controladora de livros
    controlador_livro = ControllerLivro()

    # Cadastrar um novo livro
    print("\nCadastrando livro...")
    controlador_livro.cadastrarLivro(titulo="Dom Casmurro", autor="Machado de Assis", genero="Suspense", codigo=123)

    # Consultar um livro pelo ID (suponha que o ID 123 existe)
    print("\nConsultando livro com ID 123...")
    controlador_livro.consultarLivro(id_livro=123)

    # Atualizar informações de um livro
    print("\nAtualizando livro com ID 123...")
    controlador_livro.atualizarLivro(id_livro=123, novo_titulo="Dom Casmurro - Edição Atualizada", novo_status="Indisponível")

    # Excluir um livro pelo ID
    print("\nExcluindo livro com ID 123...")
    controlador_livro.excluirLivro(id_livro=123)


if __name__ == "__main__":
    print("Iniciando aplicação...")
    main()

