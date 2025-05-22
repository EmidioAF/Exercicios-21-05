# Exercicios 21/05 #

# 1. #
matriz = []

for i in range(5):
    for i in range(5):
        matriz.append(1 if i == i else 0)
    print(matriz)


# 2. #

matriz = []
for i in range(4):
    matriz.append([int(input()) for j in range(4)])
for l in matriz:
    print(l)
maior = matriz[0][0]
lin = col = 0
for i in range(4):
    for j in range(4):
        if matriz[i][j] > maior:
            maior = matriz[i][j]
            lin, col = i, j
print("Maior:", maior, "Posicao:", lin, col)


# 3. #

alunos = [] 
maior_nota_final = -1
matricula_maior_nota = 0

for i in range(5):
    print(f"\nAluno {i + 1}:")
    matricula = int(input("Matricula: "))
    media_provas = int(input("Media das provas: "))
    media_trabalhos = int(input("Media dos trabalhos: "))
    nota_final = media_provas + media_trabalhos

    alunos.append([matricula, media_provas, media_trabalhos, nota_final])

    if nota_final > maior_nota_final:
        maior_nota_final = nota_final
        matricula_maior_nota = matricula
        
print(f"\nA matricula do aluno com maior nota final e: {matricula_maior_nota}")
