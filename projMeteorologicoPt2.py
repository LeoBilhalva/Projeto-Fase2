def verif(data, inicio, fim):
    if data[1] >= inicio[0] and data[2] >= inicio[1]:
        if data[1] <= fim[0] and data[2] <= fim[1]:
            return True

meses = {1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril", 5: "Maio", 6: "Junho",
         7: "Julho", 8: "Agosto", 9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"}

# opc 1: todos os dados; opc 2: precipitação; opc 3: temperatura; opc 4: umidade e vento


# inicio = int(input("Qual mês e ano de inicio? (exemplo: 01/2002) "))
inicio = "01/2002"
# fim = int(input("Qual mês e ano de fim? "))
fim = "02/2002"






inicio = [int(inicio.split("/")[0]), int(inicio.split("/")[1])]
fim = [int(fim.split("/")[0]), int(fim.split("/")[1])]
with open("Faculdade\\dados.csv") as csv:
    csv.readline().split(",")

    for linha in csv.readlines():
        dados = linha.split(",")[:-1]
        data = dados[0].split("/")
        data = [int(data[0]), int(data[1]), int(data[2])]

        # Verifica se a data corresponde ao intervalo solicitado
        if verif(data,inicio,fim) == True:
            if data[0] == 1:
                print("\n", meses[data[1]])
            for l in dados:
                print(l, " ", end="")
            print("\n", end="")
