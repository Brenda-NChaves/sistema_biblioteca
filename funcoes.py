
#classe que organiza os dados do livro
class Livro:
    titulo = None
    autor = None
    ano = None
    id = None
    status = 'DISPONÍVEL'
    #chat usado aq pra entender seu eu podia colocar o status disponível direto aq sem precisar mexer nele no cadastro

#como essa estrutura foi muito repetida durante o código, o bucsra por id virou função também
def existe_id(lista,id):
    
    existe = False

    for i in range (len(lista)):
        if lista[i].id == id:
            existe = True
            break

    return existe

#no momento, não existe nada escrito no input para facilitar colocar as informações nos testes e demonstrações, mas o ideal é que em cada input exista uma frase que informe ao usuário que informação ele deve digitar 
def cadastro(lista):
    book = Livro()
    book.titulo = input().upper()
    book.autor = input().upper()
    book.ano = int(input())
    book.id = int(input())

    existe = existe_id(lista,book.id)

    if existe  == True:
        print('Já existe um livro cadastrado com esse código')
        print()
    
    else:
        lista.append(book)
        print('Livro cadastrado com sucesso')
        print()
        
            #tinha esquecido que aq tinha que deixar o caminho todo claro pra ele poder comparar, aí pedi ajuda do gpt pra entender pq n tava funcionando

#função que mostra todas as informações sobre o livro que será consultado           
def allinfo(lista):
    print('Título = ',lista.titulo)
    print('Autor = ',lista.autor)
    print('Ano = ',lista.ano)
    print('Código = ',lista.id)
    print('Status = ',lista.status)
    print('-----------------')

#função para consultar os livros por autor(retorna todos os livros cadastrados daquele autor) ou por código (só retorna um livro, pois o id é único)
def consultar(lista):
    print('Digite:\n1-Consultar por autor\n2-Consultar por código')

    busca = int(input())

    if busca != 1 and busca != 2:
        print('Número inválido')
        print()

    else: 
        existe = False

        if busca == 1:
            nome = input('Autor = ').upper()
            print()
            for i in range (len(lista)):
                if lista[i].autor == nome:
                    existe = True
                    allinfo(lista[i])
                    
        
        else:
            cod = int(input('Código = '))
            print()
            for j in range (len(lista)):
                if lista[j].id == cod:
                    existe = True
                    allinfo(lista[j]) 
                    break

        if existe == False:
            print('Livro não encontrado')
            print()

#função para aletrar as informações de um livro já cadastrado (título e/ou autor e/ou ano de publicação)
def alterar(lista):
    id = int((input('Código do livro que deseja alterar os dados: ')))
    
    existe = existe_id(lista,id)
    
    if existe == False:
            print('Livro não encontrado')
            print()
    
    else:
        print('O que será alterado? (digite "s" para o que será alterado e "n" para o que não será alterado)')

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
                break
        
    
#remove todas as informações de um livro cadastrado
def remover(lista):
    id = int(input('Código do livro que deseja remover da biblioteca: '))
    
    existe = existe_id(lista,id)
    
    if existe == False:
            print('Livro não encontrado')
            print()
    else:
        for e in range (len(lista)):
            if lista[e].id == id:
                lista.pop(e)
                print('Remoção realizada com sucesso')
                print()
                break
    
#lista o título e ano de publicação de todos os livros
def printall(lista):
    for i in range(len(lista)):
        print ('Título = ',lista[i].titulo)
        print ('Ano de publicação = ',lista[i].ano)
        print('-----------------')


#verifica se o livro está ou não disponível para empréstimo e, se estiver, muda o status do livro
def emprestimo(lista):
    id = int((input('Código do livro que deseja pegar emprestado: ')))
    
    
    existe = existe_id(lista,id)
    
    if existe == False:
            print('Livro não encontrado')
            print()
    else:
        for e in range(len(lista)):
            if lista[e].id == id:

                if lista[e].status == 'DISPONÍVEL':
                    lista[e].status = 'INDISPONÍVEL'
                    print('Empéstimo realizado com sucesso')
                    print()
                    break

                else:
                    if lista[e].status == 'INDISPONÍVEL':
                        print('Esse livro não está disponível para empréstimo')
                        print()
                        break


#verifica se o livro está ou não emprestado e, se estiver, muda o status do livro
def devolver(lista):
    id = int((input('Código do livro que deseja devolver: ')))
    
    
    existe = existe_id(lista,id)
    
    if existe == False:
            print('Livro não encontrado.')
            print()
    else:
        for e in range(len(lista)):
            if lista[e].id == id:

                if lista[e].status == 'INDISPONÍVEL':
                    lista[e].status = 'DISPONÍVEL'
                    print('Devolução feita com sucesso!')
                    print()
                    break

                else:
                    if lista[e].status == 'DISPONÍVEL':
                        print('Esse livro não estava emprestado')
                        print()
                        break
