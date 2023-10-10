import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='3371',
    database='bdyoutube',
)

cursor = conexao.cursor()

# CRUD

# CREATE
#nome_produto = "todynho"
#valor = 5
#comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
#cursor.execute(comando)
#conexao.commit() # editar o banco de dados
# resultado = cursor.fetchall() # ler o banco de dados

# READ
#comando = f'SELECT * FROM vendas;'
#cursor.execute(comando)
# conexao.commit() # editar o banco de dados
#resultado = cursor.fetchall() # ler o banco de dados
#print(resultado)

# UPDATE
#nome_produto = "todynho"
#valor = 7
#comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
#cursor.execute(comando)
#conexao.commit() # editar o banco de dados

# DELETE

nome_produto = "todynho"
comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit() # editar o banco de dados


cursor.close()
conexao.close()
