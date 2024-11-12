import mysql.connector
from mysql.connector import Error

try:
    conn = mysql.connector.connect(
        host="10.28.2.59",  
        user="suporte",       
        password="suporte",       
        database="biblioteca"  
    )
    if conn.is_connected():
        print("Conectado ao MySQL com sucesso!")
except Error as e:
    print(f"Erro ao conectar ao MySQL: {e}")
finally:
    if conn.is_connected():
        conn.close()
