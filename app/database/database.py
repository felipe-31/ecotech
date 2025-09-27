import mysql 

DB_NAME = "ecotech.db"

def conectar():

    return mysql.connect(DB_NAME)
def criar_tabelas():

    con = conectar()
    cur = con.cursor()


    cur.execute(""" 
                 CREATE TABLE IF NOT EXISTS gestor(
                id INT PRIMARY KEY AUTOINCREMENT,
                nome VARCHAR(45) NOT NULL,
                data_nasc_prod DATE NOT NULL,
                )
                """)
    
    cur.execute()