import MySQLdb


def conexao_db_ext():
    connection = MySQLdb.connect(user='casedecom_tomatico', passwd='tomatico', db='casedecom_cpf', host='185.201.10.1')
    return connection

    connection.close()



def conexao_db():
    connection = MySQLdb.connect(user='task', passwd='task', db='cpf2', host='localhost')
    return connection

    connection.close()



