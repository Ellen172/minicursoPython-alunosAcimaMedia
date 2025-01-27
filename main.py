# função que calcula média, dado as notas que o aluno conseguiu
def calculaMedia(valores) : 
    return (sum (valores)) / len(valores)


# primeiro input: nro de alunos que a turma possui
nAlunos = int ( input ("Entre com o numero de alunos: "))
notas = []

for k in range (1, nAlunos+1 ) :
    # para cada aluno, adicionar sua nota
    notaAluno = float ( input ("Entre com a nota do aluno %s: " %(k)) )
    notas.append(notaAluno) #inclui cada nota dada na lista notas

# calcula a media atraves da função calculaMedia
media = calculaMedia(notas) 

acimaDaMedia = 0
for n in notas : 
    # para todas as notas, verifica quantas são maior que a media
    if n>= media :
        acimaDaMedia += 1


print ("Media da turma: ", media)
print ("Quantidade de alunos acima da media: ", acimaDaMedia)