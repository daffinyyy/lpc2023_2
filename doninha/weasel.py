import random

frase_alvo = "METHINKS IT IS LIKE A WEASEL"
chance_mutacao = 5
tamanho_populacao = 100
char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "

def sequencia_aleatoria(frase_alvo, char):
    sequencia = ''
    for i in range(len(frase_alvo)):
        sequencia += char[random.randint(0, len(char)-1)]
    return sequencia

def pontuacao (sequencia, frase_alvo):
    pontos = 0
    for i in range(len(frase_alvo)):
      if frase_alvo[i] == sequencia[i]:
        pontos += 1
    return pontos

def mutacao(sequencia, char):
    resultado_mutacao = ''
    for i in range(len(sequencia)):
      if random.randint(0, tamanho_populacao) <= chance_mutacao:
        resultado_mutacao += char[random.randint(0, len(char)-1)]
      else:
        resultado_mutacao += sequencia[i]
    return resultado_mutacao

def sequencia_mutacoes(sequencia, char):
    lista_seq = []
    for i in range(100):
      lista_seq.append(mutacao(sequencia, char))
    return lista_seq

def funcao_sequencia_modificada(sequencia, frase_alvo, char):
  lista_seq = sequencia_mutacoes(sequencia, char)
  melhor_sequencia = lista_seq[0]
  melhor_fator = pontuacao(melhor_sequencia, frase_alvo)
  for seq in lista_seq:
    fator_gene = pontuacao(seq, frase_alvo)		
    if fator_gene > melhor_fator:
      melhor_fator = fator_gene
      melhor_sequencia = seq
  return melhor_sequencia


def main():
    geracoes = 0
    sequencia_atual = sequencia_aleatoria(frase_alvo, char)
    print("Geração:", geracoes)
    print(sequencia_atual)
    
    while sequencia_atual != frase_alvo:
        sequencia_atual = funcao_sequencia_modificada(sequencia_atual, frase_alvo, char)
        geracoes += 1
        print("Geração:", geracoes)
        print(sequencia_atual)

main()
