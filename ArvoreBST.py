class No:
     def __init__(self, chave):
          self.item = chave
          self.direita = None
          self.esquerda = None

class Binaria:
     def __init__(self, raiz = None):
          self.raiz = No(raiz)
          
     def inserir(self, binarios, raiz, caractere):
          cont = 0
          aux = ''
          aux2 = ''
          for bin in binarios:
               if len(binarios) == 1:
                    if bin == '1':
                         raiz.direita = No(caractere)
                         return
                    elif bin == '0':
                         raiz.esquerda = No(caractere)
                         return
               elif bin == '1':
                    if aux2 == '0':
                         return self.inserir(aux, raiz.esquerda, caractere)
                    elif raiz.direita == None:
                         raiz.direita = No('1')
                    elif aux2 == bin:
                         return self.inserir(aux, raiz.direita, caractere)
               elif bin == '0':
                    if aux2 == '1':
                         return self.inserir(aux, raiz.direita, caractere)
                    if raiz.esquerda ==  None:
                         raiz.esquerda = No('0')
                    elif aux2 == bin:
                         return self.inserir(aux, raiz.esquerda, caractere)
               aux2 = bin
               cont += 1
               aux = ''
               for contador_normal in range(len(binarios)):
                    if contador_normal+cont < len(binarios):
                         aux += binarios[contador_normal+cont]

     def preOrdem(self, raiz, string):
          if raiz != None:
               string.append(raiz.item)
               self.preOrdem(raiz.esquerda, string)
               self.preOrdem(raiz.direita, string)
          return string

     def inserirPreordem(self, preordem, raiz):
          preordem = preordem[1:]
          ordem_2 = ''
          ordem = ''
          for i in range(len(preordem)):
               if preordem[i] == '0' or preordem[i] == '1':
                    if len(ordem) < 4:
                         ordem += preordem[i]
                    else:
                         ordem_2 += preordem[i]
                         if preordem[i+1] != '1' and preordem[i+1] != '0':
                              valor = len(ordem_2)
                              ordem_3 = ''
                              for aux in range(4):
                                   if valor + aux == 4:
                                        ordem_3 += ordem_2
                                   elif valor + aux < 4:
                                        ordem_3 += ordem[aux]
                              ordem = ordem_3
                              ordem_2 = ''
               elif preordem[i] != '0' and preordem[i] != '1':
                    if preordem[i-1] == '0' or preordem[i-1] == '1':
                         binarios = ordem + '0'
                         self.inserir(binarios, raiz, preordem[i])
                    else:
                         binarios = ordem + '1'
                         self.inserir(binarios, raiz, preordem[i])
     
     def buscar(self, chave, raiz):
          if raiz.item == None:
               return None
          if raiz.esquerda == None and raiz.direita == None:
               return raiz.item
          aux = chave[1:]
          if chave[0] == '1':
               return self.buscar(aux, raiz.direita)
          elif chave[0] == '0':
               return self.buscar(aux, raiz.esquerda)
