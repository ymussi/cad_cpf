import MySQLdb

def conexao_db():
    connection = MySQLdb.connect(user='task', passwd='task', db='cpf2', host='localhost')
    return connection

    connection.close()



