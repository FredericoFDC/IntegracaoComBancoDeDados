import pyodbc


def conecta_ao_banco(
    driver="SQL Server Native Client 11.0",
    server="DESKTOP-VG9IMGD\SQLEXPRESS",
    database="seven_ORA",
    username="sa",
    password="aimare306090",
    trusted_connection="yes",
):
    string_conexao = f"DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password};TRUSTED_CONNECTION={trusted_connection}"

    conexao = pyodbc.connect(string_conexao)
    cursor = conexao.cursor()

    return conexao, cursor


conexao, cursor = conecta_ao_banco()
# print( cursor.execute("SELECT * FROM dbo.UserInfo").fetchall())  # mostra as contas criadas no sql.


cursor.execute("INSERT INTO dbo.UserInfo VALUES ('test4', 'null', '0', '0', 'null', '11/08/2023', '11/08/2023', '11/08/2023', '11/08/2023', '11/08/2023', 'null', 'ffdc@gmail.com', 'null', 'null', 'null', 'null', 'null', 'null', 'True', 'True', 'e10adc3949ba59abbe56e057f20f883e', 'null', 'null', 'null', 'null', '11/08/2023', '768', 'null', 'null', 'null', 'null', 'null', 'null', '0', 'null', 'null', 'null', 'null', 'null', '11/08/2023', 'null', 'null')") #forma correta de cadastrar membros no sql do irose onlympus.

conexao.commit()

conexao.close()
# lista_usuarios = [ ('João', 'Maria', '2022-11-10'), ('João2', 'Maria2', '2022-11-11'), ]

# try:
# cursor.executemany(f"INSERT asda usuarios VALUES (?, ?, ?)", lista_usuarios)
# conexao.commit()
# except pyodbc.DatabaseError as e:
# print(e)
# conexao.rollback()
# finally:
# conexao.close()
