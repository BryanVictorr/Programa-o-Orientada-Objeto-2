import sqlite3

conexao = sqlite3.connect("teste.sql")
cursor = conexao.cursor()

sql = """CREATE TABLE IF NOT EXISTS usuarios(id integer PRIMARY KEY, nome text NOT NULL,email text NOT NULL);"""

nome = 'Bryan'
email = 'Bryan@gmail.com'

cursor.execute(sql)
for i in range(5):
    cursor.execute('INSERT INTO usuarios (nome, email) VALUES (?,?)', (nome,email))

nome = 'Breno'
email = 'breno@gmail.com'

for i in range(5):
    cursor.execute('INSERT INTO usuarios (nome, email) VALUES (?,?)', (nome,email))

cursor.execute('SELECT * from usuarios WHERE nome = "Breno"')

for c in cursor:
    print(c)

conexao.commit()
conexao.close()