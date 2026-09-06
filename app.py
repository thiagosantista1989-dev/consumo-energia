nome_aparelho = input("Digite o nome do aparelho: ")
print("aparelho", nome_aparelho)

potencia = float(input("Qual a potencia do aparelho em watts? "))
uso_diario = float(input("Qual o tempo médio de uso diário em horas? "))

consumo_mensal = (potencia * uso_diario * 30) / 1000
print(f"O consumo mensal do {nome_aparelho} é {consumo_mensal} KWH." )
custo_mensal = (consumo_mensal * 0.75)
print(f"O valor mensal gasto é de: {custo_mensal:.2f} reais por mes. ")