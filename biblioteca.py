from funcoes import *
#n sabia como funcionava pra referenciar algode outra pasta aí a IA do google disse como


#TO DO LIST
#Falta testar os casos de erro

#falta colocar no git
#transformar a verificação se o livro tá na lista em função
#adiconar comentários que organizem o código


#usei ia pra acahar erros que eram de variável errada



biblioteca = []


while True:
    print(f'Digite:\n1-Cadastrar livro\n2-Consultar livro\n3-Alterar dados\n4-Remover livro\n5-Listar todos\n6-Realizar empréstimo\n7-Realizar devolução\n8-Sair')
    num = int(input())
    possibilidades = [1,2,3,4,5,6,7,8]

    if num not in possibilidades:
        print('Número invalido, digite novamente')
        
    
    else:
        if num == 8:
            break
        else:
            if num == 1:
                cadastro(biblioteca)
            else:
                if num == 2:
                    consultar(biblioteca)
                else:
                    if num == 3:
                        alterar(biblioteca)
                    else:
                        if num == 4:
                            remover(biblioteca)
                        else:
                            if num == 5:
                                printall(biblioteca)
                            else:
                                if num == 6:
                                    emprestimo(biblioteca)
                                else:
                                    if num == 7:
                                        devolver(biblioteca)



