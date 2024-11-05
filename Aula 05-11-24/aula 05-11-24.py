# Crie uma classe Database, a mesma deve instanciar um novo objeto utilizando o mysql connector;
# Deve ter um metodo para conectar e desconectar 
import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self, host, user, password, database):
        """
        Inicializa a classe Database com as credenciais de acesso.
        
        :param host: O endereço do servidor MySQL (por exemplo, 'localhost').
        :param user: O nome de usuário para autenticação no MySQL.
        :param password: A senha do usuário para autenticação.
        :param database: O nome do banco de dados para se conectar.
        """
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        """
        Conecta ao banco de dados MySQL utilizando as credenciais fornecidas.
        """
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )

            if self.connection.is_connected():
                print(f"Conectado ao banco de dados {self.database} com sucesso.")
        except Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            self.connection = None

    def disconnect(self):
        """
        Desconecta do banco de dados MySQL se estiver conectado.
        """
        if self.connection is not None and self.connection.is_connected():
            self.connection.close()
            print(f"Desconectado do banco de dados {self.database}.")
        else:
            print("Nenhuma conexão ativa para desconectar.")

# Exemplo de uso da classe
if __name__ == "__main__":
    # Defina suas credenciais de acesso ao banco de dados
    db = Database(host='localhost', user='root', password='sua_senha', database='nome_do_banco')

    # Conectando ao banco de dados
    db.connect()

    # Desconectando do banco de dados
    db.disconnect()




