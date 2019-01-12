from conexao import conexao_db, conexao_db_ext
from flask import Flask
import tratacpf

db = conexao_db_ext()
app = Flask("projeto")


@app.route("/api/cadastrar/<nome>/<cpf>")
def cadastrar_cpf(nome, cpf):
    cursor = db.cursor()
    # cpfint = cpf
    cursor.execute(f"insert into cad (nome, cpf) values('{nome}', '{cpf}')")
    cursor.execute(f"select nome, cpf from cad where cpf = '{cpf}'")
    cadnome = cursor.fetchone()
    cursor.execute(f"select cpf from cad where cpf = '{cpf}'")
    cadcpf = cursor.fetchone()
    return tratacpf.trata_cadastro_cpf(cadnome, cadcpf)


@app.route("/api/consultar/<cpf>")
def consultar_cpf(cpf):
    cursor = db.cursor()
    cpfint = cpf
    cursor.execute(f"select nome from cad where cpf = {cpfint} ")
    cpfreturn = cursor.fetchone()
    cursor.execute(f"select cpf from cad where cpf = {cpfint}")
    cpff = cursor.fetchone()
    return tratacpf.trata_consulta_cpf(cpfreturn, cpff)


@app.route("/api/atualizar/<cpf>/<novocpf>/<novonome>")
def atualiza_cpf(cpf, novonome, novocpf):
    cursor = db.cursor()
    cpfint = cpf
    cpfnew = novocpf
    nomenew = novonome
    cursor.execute(f"update cad set cpf = '{cpfnew}', nome = '{nomenew}' where cpf = '{cpfint}'")
    cpfreturn = cursor.fetchone()
    return tratacpf.trata_atualiza_cpf(cpfreturn)


@app.route("/api/excluir/<cpf>")
def exclui_cpf(cpf):
    cursor = db.cursor()
    cpfint = cpf
    cursor.execute(f"delete from cad where cpf = {cpfint} ")
    cpfreturn = cursor.fetchone()
    return tratacpf.trata_exclui_cpf(cpfreturn)


@app.route("/api/listar/")
def listar_cads():
    cursor = db.cursor()
    cursor.execute("select * from cad")
    listarCads = cursor.fetchall()
    return tratacpf.trata_listar_cads(listarCads)

@app.route("/api/delete_all/")
def delete_cads():
    cursor = db.cursor()
    cursor.execute("TRUNCATE TABLE cad")
    return tratacpf.limpar_table()

app.run(use_reloader=True)
