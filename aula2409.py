import os, time

notas = {}
medias = {}

def cadastro():
    os.system('cls')
    print(f'OBS: As notas terão que ser de 0 a 10')
    n = int(input('Insira quantos alunos vai adicionar: '))
    for i in range(1,n+1):
        aluno = input('Insira o nome do aluno: ')
        nota1 = float(input('Insira a primeira nota do aluno: '))
        nota2 = float(input('Insira a segunda nota do aluno: '))
        nota3 = float(input('Insira a terceira nota do aluno: '))
        print(f'Aluno {aluno} cadastrado.')
        notas[i] = {'aluno': aluno, 'nota 1': nota1, 'nota 2': nota2, 'nota 3': nota3}
    print(notas)
    print('Todos os alunos e suas respectivas notas cadastradas com sucesso!')
    time.sleep(3)
    
def media():
    for codigo, valores in notas.items():
        med = (valores['nota 1'] + valores['nota 2'] + valores['nota 3'])/3
        medias[codigo] = {'nome': valores['aluno'], 'media': med}
    os.system('cls')
    print(f'{'-'*30}Médias dos alunos{'-'*30}')
    for codigo,valores in medias.items():
        print(f'Nome do aluno: {valores['nome']}, Média: {valores['media']}')
    time.sleep(3)

def nota_aluno():
    os.system('cls')
    nome = input('Insira o nome do aluno que voçe quer ver as notas e a média: ')
    encontrado = False
    for codigo, valores in notas.items():
        if valores['aluno'] == nome:
            encontrado = True
            print(f'Nome do aluno: {valores['aluno']}, Nota 1: {valores['nota 1']}, Nota 2: {valores['nota 2']}, Nota 3: {valores['nota 3']}')
    if not encontrado:
        print(f'Aluno não encontrado')
    time.sleep(3)
    



def menu():
    while True:
        os.system('cls')
        print(f'{'-'*30}Programa de notas{'-'*30}')
        print(f'Escolha sua opção:')
        print(f'1. Cadastrar alunos')
        print(f'2. Calcular e exibir médias')
        print(f'3. Exibir notas de um aluno')
        print(f'4. Sair')
        print(f'{'-'*77}')
        opcao = input('Insira sua opção: ')

        if opcao == '1':
            cadastro()
        elif opcao == '2':
            media()
        elif opcao == '3':
            nota_aluno()
        elif opcao == '4':
            print(f'Programa finalizado')
            break

menu()
