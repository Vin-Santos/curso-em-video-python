frase = 'Curso em Video Python'

# Fatiamento da frase
print (frase[9]) #Letra na posição
print (frase[9:13]) #Frase da posição 9 à 13
print (frase[9:21]) #Frase da posição 9 à 21
print (frase[9:21:2]) #Frase da posição 9 à 21 pulando de 2
print (frase[:5]) #Frase do início até a posição 5
print (frase[15:]) #Frase da posição 15 até o final
print (frase[9::3]) #Frase da posição 9 até o final pulando de 3
print (' ')

# Análise da frase
print (type(frase)) #Mostra tipo primitivo
print (len (frase)) #Me diz quantos caracteres tem
print (frase.count('o')) #Contagem de letra
print (frase.count('o',0,13)) #Contagem de letra numa parte
print (frase.find('deo')) #Encontrar início do que eu mandar
print (frase.find('Android')) #Vai dar -1 porque não tem
print ('Curso' in frase) #Existe na frase ou não
print (' ')

# Transformação da frase
print (frase.replace('Python','Android')) #Substitui
print (frase.upper()) #Tudo maiúsculo
print (frase.lower()) #Tudo minúsculo
print (frase.capitalize()) #Inicial da frase em upper
print (frase.title()) #Inicial da palavras em upper
print (frase)
print (' ')

# Transformação (frase diferente)
print ('Nova frase')
frase2 = '   Aprenda Python  '
print (' ')
print (frase2.strip()) #Tira todos os espaços
print (frase2.rstrip()) #Tira dos espaços de direita
print (frase2.lstrip()) #Tira dos espaços da esquerda
print (frase2)
print (' ')

# Divisão da frase
print (frase.split()) #Separa as palavras em 'frases'
print (' ')

# Junção da frase
print ('-'.join(frase.split())) #Junta com o que eu mandar, nesse caso com -
