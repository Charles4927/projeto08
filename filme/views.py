from datetime import datetime, timedelta
import time
from django.shortcuts import render
# from .models import Filme
import requests
import mysql.connector
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.utf-8')


# Create your views here.



# def homepage(request):
#     context = {}
#     link = 'https://apiluxorproducao.charlesoliveir9.repl.co'
#     ciclos = requests.get(link)
#     context['ultimo_ciclo'] = ciclos.json()
#     return render(request, "homepage.html", context)




def homepage(request):
    context = {}

    dados_conexao = mysql.connector.connect(
        host='177.47.167.82',
        user='admin',
        password='Admin@Condutec',
        database='cdtmes',
    )

    cursor = dados_conexao.cursor()
    cursor.execute(f"SELECT Data, Hora FROM luxor_producao")
    valores_ultimo_ciclo = cursor.fetchall()

    # Data e horario atuais que se atualizam (penas para usar para sabem o tempo parado de máquina)
    data_hora_atual_str = (time.strftime("%Y-%m-%d %H:%M:%S"))  # Aqui está em str
    data_hora_atual_date = datetime.strptime(data_hora_atual_str, "%Y-%m-%d %H:%M:%S")
    # print("data_hor_atual_str:", data_hora_atual_str)
    # print("data_hora_atual_date:", data_hora_atual_date)

    data_atual = data_hora_atual_str[8:10] + '/' + data_hora_atual_str[5:7] + '/' + data_hora_atual_str[0:4]
    # print("data_atual:", data_atual)

    data_ultimo_ciclo = valores_ultimo_ciclo[-1][0]
    # print("data_ultimo_ciclo:", data_ultimo_ciclo)
    hora_ultimo_ciclo = valores_ultimo_ciclo[-1][1]
    # print("hora_ultimo_ciclo:", hora_ultimo_ciclo)

    comando_ciclos_do_dia_atual = (f"SELECT Data, Hora FROM luxor_producao where Data = '{data_atual}'")
    # print("comando_ciclos_do_dia_atual:", comando_ciclos_do_dia_atual)
    cursor.execute(comando_ciclos_do_dia_atual)
    valores_ciclos_do_dia_atual = cursor.fetchall()
    # print("valores_ciclos_do_dia_atual:", valores_ciclos_do_dia_atual)

    qtde_ciclos_do_dia_atual = len(valores_ciclos_do_dia_atual)
    # qtde_ciclos_do_dia_atual = ("{:,.3f}".format(float(qtde_ciclos_do_dia_atual0)))
    # print("qtde_ciclos_do_dia_atual:", qtde_ciclos_do_dia_atual)
    # data_ultimo_ciclo_do_dia_atual = valores_ciclos_do_dia_atual[-1][0]
    data_ultimo_ciclo_do_dia_atual = data_atual
    # print("data_ultimo_ciclo_do_dia_atual:", data_ultimo_ciclo_do_dia_atual)

    try:
        hora_primeiro_ciclo_do_dia_atual = valores_ciclos_do_dia_atual[0][1]
    except:
        hora_primeiro_ciclo_do_dia_atual = str("Não houve")
    # print("hora_primeiro_ciclo_do_dia_atual:", hora_primeiro_ciclo_do_dia_atual)

    # Apenas para usar para sabem o tempo parado de máquina:
    try:
        data_hora_ultimo_ciclo_do_dia_atual0 = str(valores_ciclos_do_dia_atual[-1])
        data_hora_ultimo_ciclo_do_dia_atual1 = data_hora_ultimo_ciclo_do_dia_atual0[
                                               2:-14] + " " + data_hora_ultimo_ciclo_do_dia_atual0[-10:-2]
        data_hora_ultimo_ciclo_do_dia_atual = datetime.strptime(data_hora_ultimo_ciclo_do_dia_atual1,
                                                                "%d/%m/%Y %H:%M:%S")
        # print("data_hora_ultimo_ciclo_do_dia_atual:", data_hora_ultimo_ciclo_do_dia_atual)

        tempo_entre_datas = abs(data_hora_atual_date - data_hora_ultimo_ciclo_do_dia_atual).seconds
        # print("tempo_entre_datas:", tempo_entre_datas)

        status_de_producao = ()
        if tempo_entre_datas > 30:
            status_de_producao = "Parada"
        else:
            status_de_producao = "Produzindo"
        # print("status_de_producao:", status_de_producao)
    except:
        status_de_producao = "Parada"


    context['mostrar_data_ultimo_ciclo_do_dia_atual'] = str(data_ultimo_ciclo_do_dia_atual)

    context['mostrar_hora_primeiro_ciclo_do_dia_atual'] = str(hora_primeiro_ciclo_do_dia_atual)

    context['mostrar_data_ultimo_ciclo'] = str(data_ultimo_ciclo)

    context['mostrar_hora_ultimo_ciclo'] = str(hora_ultimo_ciclo)

    qtde_ciclos_do_dia_atual = locale.format_string('%d', qtde_ciclos_do_dia_atual, grouping=True)
    context['mostrar_qtde_ciclos_do_dia_atual'] = str(qtde_ciclos_do_dia_atual)



    return render(request, "homepage.html", context)




# def get_luxor():
# 	return Luxor.objects.all()




# def homepage(request):
#     context = {}
#
#
#     # dados_conexao = ("Driver={MySQL ODBC 8.0 Unicode Driver};"
#     #                  "Server=10.11.1.10;"
#     #                  "Database=cdtmes;"
#     #                  "UID=admin;"
#     #                  "PWD=Admin@Condutec;")
#
#     # dados_conexao = ("Driver={MySQL ODBC 8.1 Unicode Driver};"
#     #                  "Server=177.47.167.82;"
#     #                  "Database=cdtmes;"
#     #                  "UID=admin;"
#     #                  "PWD=Admin@Condutec;")
#
#
#     # conexao = pyodbc.connect(dados_conexao)
#     #
#     # cursor = conexao.cursor()
#     #
#     # cursor.execute("SELECT Hora FROM luxor_producao")
#     #
#     # ultimo_ciclo = cursor.fetchall()
#     # # valor_anterior = None
#     # # if valores[-1:] != valor_anterior:
#     # # valores_mostrados['text'] = str(valores[-1:][0][0])
#     # cursor.close()
#     # conexao.close()
#
#     ultimo_ciclo = ["Não definido", "Não definido",]
#
#     context['ultimo_ciclo'] = str(ultimo_ciclo[-1:][0][0])
#     return render(request, "homepage.html", context)
