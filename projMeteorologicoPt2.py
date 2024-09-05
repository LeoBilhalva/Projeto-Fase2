from texttable import Texttable

meses = {1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril", 5: "Maio", 6: "Junho",
         7: "Julho", 8: "Agosto", 9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"}

validos = "0123456789"


def verif(data, inicio, fim):
    if data[1] >= inicio[0] and data[2] >= inicio[1]:
        if data[1] <= fim[0] and data[2] <= fim[1]:
            return True

def valida(valor):
    if len(valor) != 7:
        # Posição do mes
        print("Erro tamanho!\n")
        return True
    elif valor[2] != "/":
        print("Erro formato!\n")
        return True
    else:
        for i in valor[:2]:
            if i not in validos:
                print("Erro mês!\n")
                return True
        for i in valor[3:7]:
            if i not in validos:
                print("Erro ano!\n")
                return True
        mes = int(valor[:2])
        ano = int(valor[3:7])

        if mes < 1 or mes > 12:
            print("Mes inválido!\n")
            return True
        else:
            if ano < 1961 or ano > 2016:
                print("Ano fora do intervalo!\n")
                return True
            if ano == 2016 and mes > 6:
                print(f"O ultimo mês de 2016 vai até {meses[6]}!\n")
                return True
        return False

def inicioFim():
    inicio = input(
        "Qual mês e ano de inicio? \n(utilize MM/AAAA - exemplo: 01/2002): ")
    while valida(inicio):
        inicio = input(
            "Qual mês e ano de inicio? \n(utilize MM/AAAA - exemplo: 01/2002): ")

    fim = input(
        "Qual mês e ano de Fim? \n(utilize MM/AAAA - exemplo: 01/2002): ")
    while valida(fim):
        fim = input(
            "Qual mês e ano de Fim? \n(utilize MM/AAAA - exemplo: 01/2002): ")

    if int(inicio[:2]+inicio[3:7]) > int(fim[:2]+fim[3:7]):
        print("Data de inicio não deve ser maior que a data do fim!\n")
        return False

    return inicio, fim

def opcoes():
    opt = "10"
    print("\n1 - Para mostrar todos os dados \n\
2 - Mostrar somente a precipitação \n\
3 - mostrar somente a temperatura \n\
4 - mostrar somente a umidade e vento\n")

    while len(opt) > 1 or opt not in validos or int(opt) > 4 or int(opt) < 1:
        opt = input("Digite a opção: ")
    return opt


print("\nProjeto Meteorológico! \n\
      Intervalos de consulta válidos: \n\
        Ano entre 1961 e 2016 \n\
        Meses entre 1 a 12 \n\
        Para o ano de 2016, o ultimo mês foi", meses[6], "\n")

# inicio, fim = inicioFim()
opt = int(opcoes())

inicio = "01/2002"
fim = "01/2002"

inicio = [int(inicio.split("/")[0]), int(inicio.split("/")[1])]
fim = [int(fim.split("/")[0]), int(fim.split("/")[1])]

with open("Faculdade\\dados.csv") as csv:
    cabecalho = csv.readline()[:-1].split(",")
    t = Texttable()
    t.set_precision(2)

    tabela = []
    mesChuvoso = {}

    for linha in csv.readlines():
        dados = linha[:-1].split(",")
        data = dados[0].split("/")
        mes = data[1]+data[2]
        precip = float(dados[1])
        
        if mes not in mesChuvoso:
            mesChuvoso[mes] = precip
        elif precip > mesChuvoso[mes]:
            mesChuvoso[mes] = precip
            
        data = [int(data[0]), int(data[1]), int(data[2])]

        

        # Verifica se a data corresponde ao intervalo solicitado
        if verif(data, inicio, fim) == True:
            if opt == 1:
                tabela.append(dados)
            elif opt == 2:
                tabela.append(dados[:2])
            elif opt == 3:
                tabela.append([dados[0], dados[5]])
            elif opt == 4:
                tabela.append([dados[0], dados[6], dados[7]])

        if data[2] > fim[1]:
            if opt == 2:
                tabela.insert(0, cabecalho[:2])
            elif opt == 3:
                tabela.insert(0, [cabecalho[0], cabecalho[5]])
            elif opt == 4:
                tabela.insert(0, [cabecalho[0], cabecalho[6], cabecalho[7]])
            t.add_rows(tabela)
            print(t.draw())

            print("Top 10 meses mais chuvosos: ")   
            for c, v in sorted(mesChuvoso.items(), key = lambda x: x[1], reverse=True)[:10]:
                
                print(f"{c[:2]+"/"+c[2:]} -> {v}")
            break
