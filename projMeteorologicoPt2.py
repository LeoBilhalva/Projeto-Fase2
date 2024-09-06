

meses = {1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril", 5: "Maio", 6: "Junho",
         7: "Julho", 8: "Agosto", 9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"}

validos = "0123456789"


def verifMesAno(data, inicio, fim):
    """Entrada de 3 listas com elementos sendo listas de dois elementos, o mes e ano.
    True caso a data esteja no intevalo entre inicio e fim."""

    data = int(data[1]+data[0])
    inicio = int(inicio[1]+inicio[0])
    fim = int(fim[1]+fim[0])

    if data >= inicio and data <= fim:
        return True


def validaMesAno(valor, mesInicio=1, anoInicio=1900, mesFim=12, anoFim=2100):
    """Entrada mes/ano - MM/AAAA para validação da formatação e verificação do intervalo mes e ano inicio e mes e ano fim."""

    # Reutilizei o dicionário para dentro da função para permitir que ela seja reutilizavel em outros programas.
    meses = {1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril", 5: "Maio", 6: "Junho",
             7: "Julho", 8: "Agosto", 9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"}

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
            if ano < anoInicio or ano > anoFim:
                print("Ano fora do intervalo!\n")
                return True
            if ano == anoInicio and mes < mesInicio:
                print(f"O primeiro mês de {anoInicio} vai até\
                      {meses[mesInicio]}!\n")
                return True
            if ano == anoFim and mes > mesFim:
                print(f"O ultimo mês de {anoFim} vai até {meses[mesFim]}!\n")
                return True
        return False


def opcoes():
    opt = "10"
    print("\n1 - Para mostrar todos os dados \n\
2 - Mostrar somente a precipitação \n\
3 - mostrar somente a temperatura \n\
4 - mostrar somente a umidade e vento\n")

    while len(opt) > 1 or len(opt) < 1 or opt not in validos or int(opt) > 4 or int(opt) < 1:
        opt = input("Digite a opção: ")
    return opt


def validaMes(mes):
    if len(mes) != 2:
        print("Tamanho inválido, deve conter dois digitos! ")
        return True
    for l in mes:
        if l not in validos:
            print("Deve conter somente valores numéricos! ")
            return True
    mes = int(mes)
    if mes > 12 or mes == 0:
        print("Fora do intervalo válido!")
        return True
    return False


def entradaTempMin(tempMin, somaTemp, cont):
    somaTemp += tempMin
    cont += 1
    return somaTemp, cont


print("\nProjeto Meteorológico! \n\
      Intervalos de consulta válidos: \n\
        Ano entre 1961 e 2016 \n\
        Meses entre 1 a 12 \n\
        Para o ano de 2016, o ultimo mês foi", meses[6], "\n")

# inicio = input(
#     "Qual mês e ano de inicio? \n(utilize MM/AAAA - exemplo: 01/2002): ")
# while validaMesAno(inicio, 1, 1961, 6, 2016):
#     inicio = input(
#         "Qual mês e ano de inicio? \n(utilize MM/AAAA - exemplo: 01/2002): ")

# fim = input(
#     "Qual mês e ano de Fim? \n(utilize MM/AAAA - exemplo: 01/2002): ")
# while validaMesAno(fim, int(inicio[:2]), int(inicio[3:7]), 6, 2016):
#     fim = input(
#         "Qual mês e ano de Fim? \n(utilize MM/AAAA - exemplo: 01/2002): ")

# inicio, fim = inicioFim()
opt = int(opcoes())

mes = input(
    "\nDigite o mes para consultar a temperatura mínima média:\n02 para fevereiro... ")
while validaMes(mes):
    mes = input(
        "\nDigite o mes para consultar a temperatura mínima média:\n02 para fevereiro... ")


inicio = "01/2002"
fim = "01/2003"

# Transformando as datas de inicio em uma lista com mes e ano
inicio = [inicio.split("/")[0], inicio.split("/")[1]]
fim = [fim.split("/")[0], fim.split("/")[1]]
somaTemp = 0
cont = 1

# Abrindo o arquivo .CSV
with open("Faculdade\\dados.csv") as csv:

    # Armazenando o cabeçalho para reutilizar posteriormente
    cabecalho = csv.readline()[:-1].split(",")

    # Criando uma variavel para criação de tabela utilizando a biblioteca Texttable
    tabela = []  # Lista para armazenar as linhas do intervalo solicitado
    mesesChuvosos = {}  # Dicionário para armazenar a maior precipitação dos meses
    # Dicionário para armazenar as temperaturas mínimas do mês solicitado pelo usuário
    mesTempMin = {}

    # Leitura das linhas do arquivo
    for linha in csv.readlines():
        dados = linha[:-1].split(",")
        data = dados[0].split("/")
        ano = data[2]
        precip = float(dados[1])
        tempMin = float(dados[3])

        if data[1] == mes:
            if int(data[0]) == 1:
                if somaTemp == 0:
                    somaTemp, cont = entradaTempMin(tempMin, somaTemp, cont)
                else:
                    mesTempMin[mes + ano] = somaTemp/cont
                    cont = 1
                    somaTemp = tempMin
            else:
                somaTemp, cont = entradaTempMin(tempMin, somaTemp, cont)

        # Armazenamento dos meses mais chuvosos de cada ano
        if ano not in mesesChuvosos:
            mesesChuvosos[ano] = dados
            mesesChuvosos[ano][1] = precip
        elif precip > mesesChuvosos[ano][1]:
            mesesChuvosos[ano] = dados
            mesesChuvosos[ano][1] = precip

        # Verificação se a data corresponde ao intervalo solicitado
        if verifMesAno([data[1], data[2]], inicio, fim) == True:
            if opt == 1:
                tabela.append(dados)
            elif opt == 2:
                tabela.append(dados[:2])
            elif opt == 3:
                tabela.append([dados[0], dados[5]])
            elif opt == 4:
                tabela.append([dados[0], dados[6], dados[7]])

mesMaisChuvoso = sorted(mesesChuvosos.items(),
                        key=lambda x: x[1][1], reverse=True)[0]

if data[1] == mes:
    mesTempMin[mes + ano] = somaTemp/cont

if opt == 2:
    tabela.insert(0, cabecalho[:2])
elif opt == 3:
    tabela.insert(0, [cabecalho[0], cabecalho[5]])
elif opt == 4:
    tabela.insert(0, [cabecalho[0], cabecalho[6], cabecalho[7]])
else:
    tabela.insert(0, cabecalho)

print("\nTop 10 meses mais chuvosos: ")
for c, v in sorted(mesesChuvosos.items(), key=lambda x: x[1][1], reverse=True)[:10]:
    print(
        f"{c} -> a precipitação foi {v[1]} no mês de {meses[int(v[0].split("/")[1])]}")

print("\nUltimos 10 anos: ")
for c, v in sorted(mesesChuvosos.items(), key=lambda x: x[0], reverse=True)[:10]:
    print(
        f"{c} -> a precipitação foi {v[1]} no mês de {meses[int(v[0].split("/")[1])]}")

print("\nMês mais chuvoso em todo o período: ")
print(f"{mesMaisChuvoso[0]} -> a precipitação foi {mesMaisChuvoso[1][1]} \
no mês de {meses[int(mesMaisChuvoso[1][0].split("/")[1])]}")

maiorPeriodo = {}
for i in mesesChuvosos:
    if i >= inicio[1] and i <= fim[1]:
        maiorPeriodo[i] = mesesChuvosos[i]

print("\nMeses mais chuvosos do período selecionado: ")
for c, v in sorted(maiorPeriodo.items(), key=lambda x: x[1][1], reverse=True)[:10]:
    print(
        f"{c} -> a precipitação foi {v[1]} no mês de {meses[int(v[0].split("/")[1])]}")

print(f"\nTemperatura mínima média entre 2006 e 2016 do mês de {
      meses[int(mes)]}")

if mes+"2016" not in mesTempMin.keys():
    print(f"\n2016 não possi dados do mês de {meses[int(mes)]}")
for c, v in sorted(mesTempMin.items(), key=lambda x: x[0], reverse=True)[:11]:
    print(
        f"{c[2:]} -> a temperatura mínima média foi {v:0.3f}")
