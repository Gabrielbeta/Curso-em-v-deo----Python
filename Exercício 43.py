#
# Sistemas de pagamento de uma loja
#

compra = float(input("Valor da compra: "))

pagamento = int(input("""Selecione a forma de pagamento abaixo:
[1] À vista - Dinheiro/Cheque
[2] À vista - Cartão débito/ crédito
[3] Parcelado - Cartão de Crédito
"""))

if pagamento == 1:
    desconto = compra - (compra * 0.10)
    print(f"Com a compra à vista você recebe um desconto de 10%:\nTotal R${desconto:.2f}")
elif pagamento == 2:
    desconto = compra - (compra * 0.05)
    print(f"Com a compra à vista você recebe um desconto de 5%:\nTotal R${desconto:.2f}")
elif pagamento == 3:
    vezes = int(input("Digite a quantidade de parcelas: "))
    if vezes < 3:
        print(f"""Ótima compra!
Total: R${compra:.2f}
Quantidade de Parcelas: {vezes} Parcela(s) de R${compra / vezes:.2f}""")


        