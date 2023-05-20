# -*- coding: utf-8 -*-
"""aula3_sql.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Y7hQGmNWskIzcbhI5EwLsx9HVo4JH1ZB
"""

#!pip install flask

import sqlite3
conn = sqlite3.connect('meuBanco.db')
print('Conexão aberta!')
conn.execute('''
CREATE TABLE IF NOT EXISTS alunos(
  matricula integer,
  nome string,
  nota integer
);
''')
conn.commit()
print('Tabela criada com sucesso!')

conn.execute('INSERT INTO alunos VALUES(1, "Antonio", 5);')
conn.execute('INSERT INTO alunos VALUES(2, "Eduardo", 4);')
conn.execute('INSERT INTO alunos VALUES(3, "Bruno", 7);')
conn.execute('INSERT INTO alunos VALUES(4, "Hugo", 3);')
conn.execute('INSERT INTO alunos VALUES(5, "Juan", 3);')
conn.execute('INSERT INTO alunos VALUES(6, "Allan", 3);')
conn.execute('INSERT INTO alunos VALUES(7, "Rodrigo", 3);')

conn.commit()
print('Dados Inseridos!!!')

alunos_encontrados = conn.execute('''
  SELECT matricula, nome, nota
  FROM alunos
''')

for linha in alunos_encontrados:
    print('Matricula: ' + str(linha[0]))
    print('Nome: ' + linha[1])
    print('Nota: ' + str(linha[2]) + '\n')

import pandas as pd

pedido = 'SELECT * FROM alunos'

estruturaDeDados = pd.read_sql_query(pedido, conn)
estruturaDeDados