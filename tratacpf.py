
def trata_cpf(cpf):
    if len(str(cpf)) == 11:
        print('CPF Válido.')
        return True
    else:
        print('CPF Inválido.')
        return False


def trata_consulta_cpf(cpfreturn, cpff):
    try:
        return "Consulta realisada com sucesso!<br>Seu nome é : {}<br> Seu CPF é : {}".format(cpfreturn[0], cpff[0])
    except:
        return 'CPF Inválido.'


def trata_cadastro_cpf(cadnome, cadcpf):
    try:
        return f"Cadastro realisado com sucesso!<br><br>Nome cadastrado: {cadnome[0]}<br>CPF Cadastrado: {cadcpf[0]}"

    except:
        return 'CPF Inválido.'


def trata_atualiza_cpf(cpfreturn):
    try:
        return "Cadastro Atualizado com sucesso!<br>"
    except:
        return 'CPF Inválido.'


def trata_exclui_cpf(cpfreturn):
    try:
        return "Cadastro excluido com sucesso!<br>"
    except:
        return 'CPF Inválido.'

def trata_listar_cads(listarCads):
    try:
        return f'Consulta realizada com Sucesso! {listarCads}'
    except:
        return 'Erro ao consultar o Banco de Dados.'

def limpar_table():
    try:
        return 'Cadastros Excluidos com Sucesso!'
    except:
        return 'Erro ao excluir os cadastros.'


