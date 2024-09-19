# 1- Faca um for loop no dicionario e exiba os valores de cada tipo: 
tipos_cores = {
    'primaria': ['vermelho', 'azul', 'amarelo'],
    'secundaria': ['verde', 'laranja', 'roxo'],
    }
#foi ultilido uma loof com (key, value) entre (tipo, cores), onde o .itens() foi usado para lista as variáveis de um dicionário no formato (key, value).
#', '.join(cores) junta todos os itens da lista cores em uma única string, separando os itens por uma vírgula e espaço. Por exemplo, para a lista ['vermelho', 'azul', 'amarelo'], o resultado será "vermelho, azul, amarelo".

for tipo, cores in tipos_cores.items():
    print(f"{tipo.capitalize()}: {', '.join(cores)}")

#foi usado o for(loop) ouxar uma key correspondente a um value no dicionário tipos_cores, onde o itens foi utilizado para 
for key, value in tipos_cores.items():
    print(key)
    print(value)














# 2 - Faca um for loop na lista e mostre qual tipo ela é
lst_cores = ['vermelho', 'roxo', 'preto'] 

for cor in lst_cores:
    if cor in tipos_cores['primaria']:
        print(f"{cor} é primária")
    elif cor in tipos_cores['secundaria']:
        print(f"{cor} é secundaria")
    else:
        print(f"{cor} é outro tipo")














# 3 – Verifique o total da compra baseado no preco
precos = {
    'camiseta': 100.00,
    'tenis': 900.00,
    'meia': 45.00,
    'blusa': 245.00,
    'calça': 145.00,
    'luva': 18.00,
    }

compra = ['luva', 'blusa', 'tenis']

valor_compra = precos['luva'] + precos['blusa'] + precos['tenis']
print(f"O valor da compra é {valor_compra}")



















# 4 – Faca uma funcao que entre 3 notas e calcule a media final de acordo com o crirterio de nota do ibmec
# Crie uma pasta meu_pacote e grava essa funcao la dentro
# Importe a funcao, e chame ela, calculando a media final
p1 = 8.5
p2 = 9.0
ac = 1.0

from meu_pacote.modulo import calcular_nota
nota_final = calcular_nota(p1, p2, ac)
print(f"A nota final foi {nota_final}")