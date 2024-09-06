import matplotlib.pyplot as plt

# Dict para trazer o mes correspondente dos numeros nas datas.
meses = {1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril", 5: "Maio", 6: "Junho",
         7: "Julho", 8: "Agosto", 9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"}

# Valida se contem somente números.
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
                print("Ano fora do intervalo ou menor que o ano de inicio!\n")
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
    """Apresentação das opções retornando somente quando valor esperado no intervalo."""
    opt = "10"
    print("\n1 - Para mostrar todos os dados \n\
2 - Mostrar somente a precipitação \n\
3 - mostrar somente a temperatura \n\
4 - mostrar somente a umidade e vento\n")

    while len(opt) > 1 or len(opt) < 1 or opt not in validos or int(opt) > 4 or int(opt) < 1:
        opt = input("Digite a opção: ")
    return opt


def validaMes(mes):
    """Valida a formatação do mes e ano digitado como: MM/AAAA, incluindo a barra."""
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


def calcTempMin(dict, data, temp):
    """Função para leitura e armazenamento dos dados correspondentes
    ao mes selecionado pelo usuário."""
    if data[1]+data[2] not in dict:
        return [temp, 1]
    else:
        dict[data[1]+data[2]][0] += temp
        dict[data[1]+data[2]][1] += 1

    return [dict[data[1]+data[2]][0], dict[data[1]+data[2]][1]]


print("\nProjeto Meteorológico! \n\
      Intervalos de consulta válidos: \n\
        Ano entre 1961 e 2016 \n\
        Meses entre 1 a 12 \n\
        Para o ano de 2016, o ultimo mês foi", meses[6], "\n")

inicio = input(
    "Qual mês e ano de inicio? \n(utilize MM/AAAA - exemplo: 01/2002): ")
while validaMesAno(inicio, 1, 1961, 6, 2016):
    inicio = input(
        "Qual mês e ano de inicio? \n(utilize MM/AAAA - exemplo: 01/2002): ")

fim = input(
    "Qual mês e ano de Fim? \n(utilize MM/AAAA - exemplo: 01/2002): ")
while validaMesAno(fim, int(inicio[:2]), int(inicio[3:7]), 6, 2016):
    fim = input(
        "Qual mês e ano de Fim? \n(utilize MM/AAAA - exemplo: 01/2002): ")

opt = int(opcoes())

mes = input(
    "\nDigite o mes para consultar a temperatura mínima média:\n02 para fevereiro... ")
while validaMes(mes):
    mes = input(
        "\nDigite o mes para consultar a temperatura mínima média:\n02 para fevereiro... ")

# Transformando as datas de inicio em uma lista com mes e ano
inicio = [inicio.split("/")[0], inicio.split("/")[1]]
fim = [fim.split("/")[0], fim.split("/")[1]]

somaTemp = 0

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
            mesTempMin[mes+ano] = calcTempMin(mesTempMin, data, tempMin)

        # Armazenamento dos meses mais chuvosos de cada ano
        if ano not in mesesChuvosos:
            mesesChuvosos[ano] = dados
            mesesChuvosos[ano][1] = precip
        elif precip > mesesChuvosos[ano][1]:
            mesesChuvosos[ano] = dados
            mesesChuvosos[ano][1] = precip

        # Verificação se a data corresponde ao intervalo solicitado
        if verifMesAno([data[1], data[2]], inicio, fim):
            if opt == 1:
                tabela.append(dados)
            elif opt == 2:
                tabela.append(dados[:2])
            elif opt == 3:
                tabela.append([dados[0], dados[5]])
            elif opt == 4:
                tabela.append([dados[0], dados[6], dados[7]])

# Recebendo o mês mais chuvoso
mesMaisChuvoso = sorted(mesesChuvosos.items(),
                        key=lambda x: x[1][1], reverse=True)[0]

# Apresentação dos dados
if opt == 1:
    print(" - ".join(cabecalho))
elif opt == 2:
    print(f"{cabecalho[:2]}")
elif opt == 3:
    print(f"{cabecalho[0]} - {cabecalho[5]}")
elif opt == 4:
    print(f"{cabecalho[0]} - {cabecalho[6]} - {cabecalho[7]}")

# --- Apresentou valor em float mesmo que em todo momento tenha sido tratado como string.
for i in tabela:
    i[1] = str(i[1])
    print(" - ".join(i))

# Dict para coletar os meses mais chuvosos no período digitado pelo usuário.
maiorPeriodo = {}
for i in mesesChuvosos:
    if i >= inicio[1] and i <= fim[1]:
        maiorPeriodo[i] = mesesChuvosos[i]

# Requisito A
print("\nMeses mais chuvosos do período selecionado: ")
for c, v in sorted(maiorPeriodo.items(), key=lambda x: x[1][1], reverse=True)[:10]:
    print(
        f"{c} -> a precipitação foi {v[1]} no mês de {meses[int(v[0].split("/")[1])]}")

# Requisito B
print("\nMês mais chuvoso em todo o período: ")
print(f"{mesMaisChuvoso[0]} -> a precipitação foi {mesMaisChuvoso[1][1]} \
no mês de {meses[int(mesMaisChuvoso[1][0].split("/")[1])]}")

# Requisito C
print(f"\nTemperatura mínima média entre 2006 e 2016 do mês de \
{meses[int(mes)]}")
if mes+"2016" not in mesTempMin.keys():
    print(f"\n2016 não possui dados para o mês de {meses[int(mes)]}")
for c, v in sorted(mesTempMin.items(), key=lambda x: x[0], reverse=True)[:11]:
    print(
        f"{c[2:]} -> a temperatura mínima média foi {v[0]/v[1]:.3f}")

# Requisito D
# Coleta dos dados para o gráfico x e y.
listay = [round(mesTempMin[i][0]/mesTempMin[i][1], 3)
          for i in mesTempMin.keys()]
listax = [int(i[2:]) for i in mesTempMin.keys()]

# Configuração do gráfico - visual
# gráfico de barra pode não ficar muito adequado
# Para o volume de dados, porém optei por ele por conta que é melhor de visualizar
# Os anos relacionados aos dados. Pensei em usar o .plot para gráfico de linha, porém
# achei que ficou confuso.
fig, ax = plt.subplots()
ax.bar(listax, listay, label='Temperaturas mínimas média')
ax.set_title(f"Temperaturas mínimas média entre 2006 e 2016 do mês de \
{meses[int(mes)]}", fontsize=12)
ax.set_ylabel("Temperaturas mínimas", fontsize=10)
ax.set_xlabel("Anos", fontsize=10)


# Inserindo rótulos para as colunas
for idx, val in enumerate(listay):
    txtTop = f'{val:.2f}º'
    yCoord = val + 0.07
    xCoord = idx + 1961
    ax.text(x=xCoord, y=yCoord, s=txtTop, fontsize=7,
            horizontalalignment='center', rotation=60)
    ax.yaxis.set_visible(False)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)

# Ajustando para melhor visualização. Para windows, irá ficar em tela cheia.
# Não vi necessidade de colocar legenda, pois só tem um tipo de informação e não necessita - porém coloquei da mesma forma conforme Critério 5
plt.legend()
# Contrastar com as barras.
plt.xticks(range(listax[1], listax[-1], 4))
plt.get_current_fig_manager().window.state('zoomed')
plt.show()


# Requisito E
# Media total do mes selecionado de todos os anos.
# É necessário fechar o gráfico para visualizar essas apresentações.
media = 0
for c, v in sorted(mesTempMin.items(), key=lambda x: x[1]):
    media += v[0]/v[1]
print(f"\nMédia mínima do mês escolhido:  {media/len(mesTempMin):.2f}")

# - Detalhe nessa apresentação:
# Coloquei na função lambda o float porque um unico valor se apresentava como sting e eu
# não tenho a mínima idéia do porque aconteceu isso. O valor que constou como string foi a preciptação
# de 2002 no dia 9 de janeiro. Basta usar a chave mesesChuvosos.items()[1][1]. Aconteceu algo selemelhante
# Na etapa de apresentação de dados, na leitura da variavel i na lista da tabela, deixarei marcado para melhor
# percepção.
# Se puder me retornar a respeito disso eu agradeceria. Obrigado!
print("\nTop 10 meses mais chuvosos: ")
for c, v in sorted(mesesChuvosos.items(), key=lambda x: float(x[1][1]), reverse=True)[:10]:
    print(
        f"{c} -> a precipitação foi {v[1]} no mês de {meses[int(v[0].split("/")[1])]}")
#
print("\nUltimos 10 anos: ")
for c, v in sorted(mesesChuvosos.items(), key=lambda x: x[0], reverse=True)[:10]:
    print(
        f"{c} -> a precipitação foi {v[1]} no mês de {meses[int(v[0].split("/")[1])]}")
