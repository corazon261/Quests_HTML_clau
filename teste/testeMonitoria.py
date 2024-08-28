def aplicar_inflacao(nomes, precos, porcentagem_inflacao):
    for i in range(len(precos)):
        novo_preco = precos[i] * (1 + porcentagem_inflacao / 100)
        precos[i] = round(novo_preco, 2)

nomes_itens = ["Arroz", "Feijão", "Macarrão", "Azeite", "Leite"]
precos_itens = [20.00, 8.50, 5.75, 25.90, 4.30]

print("Preços originais:")
for i in range(len(nomes_itens)):
    print(f"{nomes_itens[i]}: R$ {precos_itens[i]}")
inf = float(input())
aplicar_inflacao(nomes_itens, precos_itens, inf)

print("\nPreços após inflação de ",inf," %")
for i in range(len(nomes_itens)):
    print(f"{nomes_itens[i]}: R$ {precos_itens[i]}")
