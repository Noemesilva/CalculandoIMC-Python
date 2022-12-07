import sqlite3

conexao = sqlite3.connect('calculo_imc.db')

c = conexao.cursor()

c.execute(''' CREATE TABLE IF NOT EXISTS paciente (
               id int PRIMARY KEY  NOT NULL,
                nome text NOT NULL,
                endereco text NOT NULL,
                peso float NOT NULL,
                altura float NOT NULL,
                resultadoIMC float NOT NULL)
''')

conexao.commit()
conexao.close()
