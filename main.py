from tabelaHash import Hash
from ArvoreBST import Binaria

def geradorChave():
     # lendo caracteres
     arquivo_caracteres = open('caracteres.txt', 'r')
     caracteres_txt = arquivo_caracteres.readline()
     caracteres_ascii = []
     for i in caracteres_txt:
          caracteres_ascii.append(i)
     arquivo_caracteres.close()
     print(f'Caracteres: {caracteres_ascii}\n')

     # transforma os caracteres em ASCII e converte em binário
     arquivo_chave = open('chave.txt', 'w')
     tab_hash = Hash(len(caracteres_ascii))
     for elemento in range(len(caracteres_ascii)):
          ordenar = ord(caracteres_ascii[elemento])
          print(f'{caracteres_ascii[elemento]} - {ordenar}', end='    ')
          tab_hash.inserir(ordenar)
     arquivo_chave.writelines(tab_hash.formataBinario())
     arquivo_chave.close()

def codificadorSenha():
     # Pegando a senha;
     arquivo_senha = open('senha.txt', 'r')
     senha = arquivo_senha.readline()
     senhaLista = []
     for i in senha:
          senhaLista.append(i)
     arquivo_senha.close()
     print(f'\n\nprintando a senha: {senha}\n')

     #  Lendo arquivo chave;
     arquivo_chave = open('chave.txt', 'r')
     chave = arquivo_chave.readlines()
     arquivo_chave.close()
     print('chave: {}'.format(chave))

     # Codificando a senha
     senhaCodificada = ''
     percorreChave = percorreSenha = subposicao = 0
     while(1):
          if chave[percorreChave][0] == senhaLista[percorreSenha]:
               for subposicao in range(3,8):
                    senhaCodificada += chave[percorreChave][subposicao]
               percorreSenha += 1
          percorreChave += 1

          if percorreChave == len(chave):
               percorreChave = 0
          if percorreSenha == len(senhaLista):
               break
     arquivo_senha_codificada = open('senhacodificada.txt', 'w')
     arquivo_senha_codificada.writelines(senhaCodificada)
     arquivo_senha_codificada.close()

# arvore BST
def arvore():
     Arvore = Binaria('0')
     arquivo_chave = open('chave.txt', 'r')
     chave_arquivo = arquivo_chave.readlines()
     arvListaBinario = []
     arvListaCaractere = []
     for elemento in chave_arquivo:
          arvListaCaractere.append(elemento[0])
          arvListaBinario.append(elemento[3:8])
     print('\n', arvListaCaractere)
     print('\n', arvListaBinario)

     for elemento2 in range(len(arvListaBinario)):
          Arvore.inserir(arvListaBinario[elemento2], Arvore.raiz, arvListaCaractere[elemento2])

     arquivo_preordem = open('preordem.txt', 'w')
     arquivo_preordem.writelines(Arvore.preOrdem(Arvore.raiz, []))
     arquivo_preordem.close()

# decodificando Senha
def decodificar():
     arquivo_decodificador = open('preordem.txt', 'r')
     arvore_preordem = Binaria('0')
     decodificador = arquivo_decodificador.readline()
     print(decodificador)
     arvore_preordem.inserirPreordem(decodificador, arvore_preordem.raiz)
     arquivo_decodificador.close()
     
     arquivo_senha_descodificada = open('senhacodificada.txt', 'r')
     senhaDecodificada = arquivo_senha_descodificada.readline()
     senhaDecodificadaLista = []
     for contador in senhaDecodificada:
          senhaDecodificadaLista.append(contador)
     print(f'\n{senhaDecodificadaLista}')
     arquivo_senha_descodificada.close()
     lista = []
     string2 = ''
     for i in range(len(senhaDecodificadaLista)):
          lista.append(senhaDecodificadaLista[i])
          if len(lista) == 5:
               string2 += arvore_preordem.buscar(lista, arvore_preordem.raiz)
               lista = []
     print(f'\nSenha descodificada: {string2}\n')


# main
geradorChave()
codificadorSenha()
arvore()
decodificar()