# Lista para armazenar os dados dos alunos
alunos = []

# Cadastro dos alunos
while True:
    nome = input("Nome do aluno: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    alunos.append([nome, [nota1, nota2], (nota1 + nota2) / 2])
    
    continuar = input("Deseja continuar? [S/N] ").strip().upper()
    if continuar == 'N':
        break

# Exibindo o boletim
print("\n{:<4} {:<20} {:>10}".format("No.", "Nome", "Média"))
print("-" * 36)
for i, aluno in enumerate(alunos):
    print("{:<4} {:<20} {:>10.1f}".format(i, aluno[0], aluno[2]))

# Mostrar notas individuais
while True:
    opc = int(input("\nMostrar notas de qual aluno? (999 para sair): "))
    if opc == 999:
        break
    if 0 <= opc < len(alunos):
        print(f"Notas de {alunos[opc][0]} são: {alunos[opc][1]}")
    else:
        print("Número inválido. Tente novamente.")
