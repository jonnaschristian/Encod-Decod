class Hash:
     # construtor
     def __init__ (self, tamanho):
          self.tamanho = tamanho
          self.posicoes = [None] * self.tamanho
          self.cont = 0

     # função para inserir na tabela e encontrar o hash
     def inserir (self, chave):
          aux = 0
          while True:
               if aux == 0:
                    calculo_hash = chave % self.tamanho
               if self.posicoes[calculo_hash] == None:
                    self.posicoes[calculo_hash] = chave
                    break
               else:
                    if calculo_hash == self.tamanho:
                        calculo_hash = 0
                    calculo_hash += 1
                    aux += 1

     # função para imprimir a tabela hash
     def formataBinario(self):
          binarioformatado = ''
          for i in range(self.tamanho):
               binario = f'{i:b}'
               for k in range(4):
                    if len(binario) < 5:
                         binario = '0' + binario
               binarioformatado += (f'{chr(self.posicoes[i])}, {binario}\n')
          return binarioformatado

     def imprimir(self):
          for i in range(len(self.posicoes)):
               print(f"Hash: {i} - Chave: {self.posicoes[i]}")