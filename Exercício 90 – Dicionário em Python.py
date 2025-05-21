aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média de {aluno['nome']}:'))
if aluno['média'] >= 7:
    aluno['siatuação'] = 'Aprovado'