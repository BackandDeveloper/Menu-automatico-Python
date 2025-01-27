#Exemplo simples do Match, com a finalizade de realizar estudos.

codigo = int(input)("Digite o código do produto:")
qtde = int(input)("Digite a qtde:")
                  
match codigo:
    case 1:
        print (f'Total = {qtde * 4.00}')
    case 2:
        print (f'Total = {qtde * 4.50}')
    case 3:
        print (f'Total = {qtde * 5.00 }')
    case 4:
        print (f'Total = {qtde * 2.00 }')
    case 5:
        print (f'Total = {qtde * 1.50 }')
    case 6:
        print("Código Inválido!")