q = int(input("Quantos alunos serão calculados a média? "))

d = []

for x in range(q):
    nome = input("Nome do aluno:  ")
    n1 = float(input("N1: "))
    n2 = float(input("N2: "))
    n3 = float(input("N3: "))
    print()
    
    d.append({"nome":nome, "media":(n1+n2+n3)/3})


for aluno in d:
    if aluno['media'] >= 7:
        print(f"O aluno {aluno['nome']} foi aprovado com média {aluno['media']:.1f}")
    else:
        print(f"O aluno {aluno['nome']} foi reprovado com média {aluno['media']:.1f}")
