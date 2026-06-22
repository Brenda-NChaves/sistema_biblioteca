nome = ['ana','amanda','anaa','brenda','fernanda','dulce','carmem','elena',]


alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


#selection sort com nums

'''nums = [1,5,6,7,2]

for i in range (len(nums)):
    menor = i

    for c in range (i+1,len(nums)):
        if nums[c] < nums[menor]:
            menor = c
    
    temp = nums[menor]
    nums[menor] = nums[i]
    nums[i] = temp

print(nums)'''


'''for i in range (len(nome)):
    numcorresponde = None

    for j in range (len(alfabeto)):
        if nome[i][0] == alfabeto[j]:
                numcorresponde = j
                break
                

    variavel = numcorresponde
    posicao = i
    for f in range (i+1,len(nome)):
            

        for l in range (len(alfabeto)):
            if nome[f][0] == alfabeto[l]:
                if l < variavel:
                    variavel = l
                    posicao = f
                    break
   
                    
    if variavel < numcorresponde:                
        temp = nome[i]
        nome[i] = nome[posicao]
        nome[posicao] = temp
                    

print(nome)'''



for i in range (len(nome)):
   
    
    valor_letra = 0
    posicao = i

    
    for f in range (i+1,len(nome)):
        inicio = 0
        #acha aonde começa a comparação
        while inicio != len(nome[i])-1 and inicio != len(nome[f])-1:
            if nome[i][inicio] == nome[f][inicio]:
                inicio += 1
            else:
                break


        #acha o valor da letra analisada da primeira palavra da lista em relação as outras
        for j in range (len(alfabeto)):
            if nome[i][inicio] == alfabeto[j]:
                valor_letra = j
       
        #confere se a letra da palavra comparada tem um valor menor que o valor da primeira 
        for l in range (len(alfabeto)):
            if nome[f][inicio] == alfabeto[l]:
                if l < valor_letra:
                    valor_letra = l
                    posicao = f
                    break

                #o caso desse else seria se as duas palavras tivesssem terminado sempre iguais(tipo "ana" e "anaa", nesse caso a menor tem que ser colocada primeiro)
                else:
                    if l == valor_letra:
                        menor = None
                        if len(nome[f]) <= len(nome[i]):
                            menor = f
                        else:
                            menor = i
                        
                        #posicao é alterada
                        posicao = menor
               
    temp = nome[i]
    nome[i] = nome[posicao]
    nome[posicao] = temp

print(nome)



     #encontra a letra diferente 

  
        

                     
                
            

