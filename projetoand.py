resposta = int(input("Qual é a sua idade:"))

if resposta >=16 and resposta <=65:
    print("Você é obrigado a votar")
elif resposta < 16 or not resposta < 65:
    print("Você não é obrigado a votar")
else: 
    print("Opção inválida")