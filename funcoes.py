class Livro:
    titulo = None
    autor = None
    ano = None
    id = None
    status = 'Disponível'
    #chat usado aq pra entender seu eu podia colocar o status disponível direto aq sem precisar mexer nele no cadastro

def cadastro(lista):
    book = Livro()
    book.titulo = input().upper()
    book.autor = input().upper()
    book.ano = input()
    book.id = int(input())

    existe = False
    for i in range (len(lista)):
        if lista[i].id == book.id:
            existe = True
    
    if existe == True:
        print('Já existe um livro com esse código')
    
    else:
        lista.append(book)
        
            #tinha esquecido que aq tinha que deixar o caminho todo claro pra ele poder comparar, aí pedi ajuda do gpt pra entender pq n tava funcionando
            


def consultar(lista):
    print('digite:\n1-Consultar por autor\n2-Consultar por código')
    busca = int(input())
    if busca != 1 and busca != 2:
        print('Número invalido')
    else:  #ver se é obrigatório vir primeiro o autor e depois o codigo ou whatever
        existe = False
        if busca == 1:
            nome = input('Autor = ').upper()
            for i in range (len(lista)):
                if lista[i].autor == nome:
                    existe = True
                    allinfo(lista[i]) #ajeitar oq vai nesse print
        
        else:
            cod = int(input('Código = '))
            for j in range (len(lista)):
                if lista[j].id == cod:
                    existe = True
                    allinfo(lista[j]) #ajeitar oq vai nesse print

        if existe == False:
            print('Livro não encontrado')


def alterar(lista):
    id = int((input('Código do livro que deseja alterar os dados: ')))
    
    existe = False
    for i in range (len(lista)):
        if lista[i].id == id:
            existe = True
    
    if existe == False:
            print('Livro não encontrado')
    
    else:
        print('O que será alterado? (digite "s" para oq será alterado e "n" para o que não será alterado)')

        t = input('Título: ')
        a = input('Autor: ')
        ap = input('Ano de publicação: ')

        for l in range (len(lista)):
            if lista[l].id == id:     
                if t == 's':
                    lista[l].titulo = input('Novo título = ').upper()
                if a == 's':
                    lista[l].autor = input('Novo autor = ').upper()
                if ap == 's':
                    lista[l].ano = int(input('Novo ano de publicação = '))
        
    

def remover(lista):
    id = int(input('Código do livro que deseja remover da biblioteca: '))
    
    existe = False
    for i in range (len(lista)):
        if lista[i].id == id:
            existe = True
            break
    
    if existe == False:
            print('Livro não encontrado')
    else:
        for e in range (len(lista)):
            if lista[e].id == id:
                lista.pop(e)
                print('Remoção realizada com sucesso')
                break
    

def printall(lista):
    for i in range(len(lista)):
        print ('Título = ',lista[i].titulo)
        print ('Ano de publicação = ',lista[i].ano)
        print('-----------------')

def emprestimo(lista):
    id = int((input('Código do livro que deseja pegar emprestado: ')))
    
    existe = False
    for i in range (len(lista)):
        if lista[i].id == id:
            existe = True
    
    if existe == False:
            print('Livro não encontrado')
    else:
        for e in range(len(lista)):
            if lista[e].id == id:

                if lista[e].status == 'DISPONÍVEL':
                    lista[e].status = 'INDISPONÍVEL'
                    print('Empéstimo feito com sucesso!')
                    break
                else:
                    if lista[e].status == 'INDISPONÍVEL':
                        print('Esse livro não está disponível para empréstimo')
                        break



def devolver(lista):
    id = int((input('Código do livro que deseja devolver: ')))
    
    existe = False
    for i in range (len(lista)):
        if lista[i].id == id:
            existe = True
    
    if existe == False:
            print('Livro não encontrado.')
    else:
        for e in range(len(lista)):
            if lista[e].id == id:

                if lista[e].status == 'INDISPOÍVEL':
                    lista[e].status = 'DISPONÍVEL'
                    print('Devolução feita com sucesso!')
                    break
                else:
                    if lista[e].status == 'DISPONÍVEL':
                        print('Esse livro não estava emprestado')
                        break

def allinfo(lista):
    print('Título = ',lista.titulo)
    print('Autor = ',lista.autor)
    print('Ano = ',lista.ano)
    print('Código = ',lista.id)
    print('Status = ',lista.status)
    print('-----------------')
