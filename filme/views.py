from datetime import datetime, timedelta
import time
from django.shortcuts import render
# from .models import Filme
import requests
import mysql.connector
# import locale
# locale.setlocale(locale.LC_ALL, 'pt_BR.utf-8')


# Create your views here.



# def homepage(request):
#     context = {}
#     link = 'https://apiluxorproducao.charlesoliveir9.repl.co'
#     ciclos = requests.get(link)
#     context['ultimo_ciclo'] = ciclos.json()
#     return render(request, "homepage.html", context)




# def homepage(request):
#
#     context = {}
#
#     dados_conexao = mysql.connector.connect(
#         host='10.11.1.10',
#         # host='177.47.167.82',
#         user='admin',
#         password='Admin@Condutec',
#         database='cdtmes',
#     )
#
#     cursor = dados_conexao.cursor()
#     cursor.execute(f"SELECT Data, Hora FROM luxor_producao")
#     valores_ultimo_ciclo = cursor.fetchall()
#
#     # Data e horario atuais que se atualizam (penas para usar para sabem o tempo parado de máquina)
#     data_hora_atual_str = (time.strftime("%Y-%m-%d %H:%M:%S"))  # Aqui está em str
#     data_hora_atual_date = datetime.strptime(data_hora_atual_str, "%Y-%m-%d %H:%M:%S")
#     # print("data_hor_atual_str:", data_hora_atual_str)
#     # print("data_hora_atual_date:", data_hora_atual_date)
#
#     data_atual = data_hora_atual_str[8:10] + '/' + data_hora_atual_str[5:7] + '/' + data_hora_atual_str[0:4]
#     # print("data_atual:", data_atual)
#
#     data_ultimo_ciclo = valores_ultimo_ciclo[-1][0]
#     # print("data_ultimo_ciclo:", data_ultimo_ciclo)
#     hora_ultimo_ciclo = valores_ultimo_ciclo[-1][1]
#     # print("hora_ultimo_ciclo:", hora_ultimo_ciclo)
#
#     comando_ciclos_do_dia_atual = (f"SELECT Data, Hora FROM luxor_producao where Data = '{data_atual}'")
#     # print("comando_ciclos_do_dia_atual:", comando_ciclos_do_dia_atual)
#     cursor.execute(comando_ciclos_do_dia_atual)
#     valores_ciclos_do_dia_atual = cursor.fetchall()
#     # print("valores_ciclos_do_dia_atual:", valores_ciclos_do_dia_atual)
#
#     qtde_ciclos_do_dia_atual = len(valores_ciclos_do_dia_atual)
#     # qtde_ciclos_do_dia_atual = ("{:,.3f}".format(float(qtde_ciclos_do_dia_atual0)))
#     # print("qtde_ciclos_do_dia_atual:", qtde_ciclos_do_dia_atual)
#     # data_ultimo_ciclo_do_dia_atual = valores_ciclos_do_dia_atual[-1][0]
#     data_ultimo_ciclo_do_dia_atual = data_atual
#     # print("data_ultimo_ciclo_do_dia_atual:", data_ultimo_ciclo_do_dia_atual)
#
#     try:
#         hora_primeiro_ciclo_do_dia_atual = valores_ciclos_do_dia_atual[0][1]
#     except:
#         hora_primeiro_ciclo_do_dia_atual = str("Não houve")
#     # print("hora_primeiro_ciclo_do_dia_atual:", hora_primeiro_ciclo_do_dia_atual)
#
#     # Apenas para usar para sabem o tempo parado de máquina:
#     try:
#         data_hora_ultimo_ciclo_do_dia_atual0 = str(valores_ciclos_do_dia_atual[-1])
#         data_hora_ultimo_ciclo_do_dia_atual1 = data_hora_ultimo_ciclo_do_dia_atual0[
#                                                2:-14] + " " + data_hora_ultimo_ciclo_do_dia_atual0[-10:-2]
#         data_hora_ultimo_ciclo_do_dia_atual = datetime.strptime(data_hora_ultimo_ciclo_do_dia_atual1,
#                                                                 "%d/%m/%Y %H:%M:%S")
#         # print("data_hora_ultimo_ciclo_do_dia_atual:", data_hora_ultimo_ciclo_do_dia_atual)
#
#         tempo_entre_datas = abs(data_hora_atual_date - data_hora_ultimo_ciclo_do_dia_atual).seconds
#         # print("tempo_entre_datas:", tempo_entre_datas)
#
#         status_de_producao = ()
#         if tempo_entre_datas > 30:
#             status_de_producao = "Parada"
#         else:
#             status_de_producao = "Produzindo"
#         # print("status_de_producao:", status_de_producao)
#     except:
#         status_de_producao = "Parada"
#
#     context['mostrar_data_ultimo_ciclo_do_dia_atual'] = str(data_ultimo_ciclo_do_dia_atual)
#
#     context['mostrar_hora_primeiro_ciclo_do_dia_atual'] = str(f"Primeiro Ciclo: {hora_primeiro_ciclo_do_dia_atual}")
#
#     context['mostrar_data_ultimo_ciclo'] = str(data_ultimo_ciclo)
#
#     context['mostrar_hora_ultimo_ciclo'] = str(f"Último Ciclo: {hora_ultimo_ciclo}")
#
#     # qtde_ciclos_do_dia_atual = locale.format_string('%d', qtde_ciclos_do_dia_atual, grouping=True)
#     context['mostrar_qtde_ciclos_do_dia_atual'] = str(f"Peças: {qtde_ciclos_do_dia_atual}")
#
#     context['mostrar_status_de_producao'] = str(f"Status: {status_de_producao}")
#
#
#     return render(request, "homepage.html", context)







class Dados_Producao:
    def __init__(self):
        pass
    def dados(self, tabela_producao):
        self.tabela_producao = tabela_producao

        context = {}

        dados_conexao = mysql.connector.connect(
            # host='10.11.1.10',
            host='177.47.167.82',
            user='admin',
            password='Admin@Condutec',
            database='cdtmes',
        )

        cursor = dados_conexao.cursor()
        cursor.execute(f"SELECT Data, Hora FROM {self.tabela_producao}")
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

        comando_ciclos_do_dia_atual = (f"SELECT Data, Hora FROM {tabela_producao} where Data = '{data_atual}'")
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

        context[f'{self.tabela_producao}_mostrar_data_ultimo_ciclo_do_dia_atual'] = str(data_ultimo_ciclo_do_dia_atual)

        context[f'{self.tabela_producao}_mostrar_hora_primeiro_ciclo_do_dia_atual'] = str(f"Primeiro Ciclo: {hora_primeiro_ciclo_do_dia_atual}")

        context[f'{self.tabela_producao}_mostrar_data_ultimo_ciclo'] = str(data_ultimo_ciclo)

        context[f'{self.tabela_producao}_mostrar_hora_ultimo_ciclo'] = str(f"Último Ciclo: {hora_ultimo_ciclo}")

        # qtde_ciclos_do_dia_atual = locale.format_string('%d', qtde_ciclos_do_dia_atual, grouping=True)
        context[f'{self.tabela_producao}_mostrar_qtde_ciclos_do_dia_atual'] = str(f"Peças: {qtde_ciclos_do_dia_atual}")

        context[f'{self.tabela_producao}_mostrar_status_de_producao'] = str(f"Status: {status_de_producao}")

        return context




def homepage(request):
    lista_tabelas = ["luxor_producao", "lam04_producao", "lam05_producao", "dc04_producao", "ds03_producao", "dw02_producao", "dw03_producao"]
    lista_dados = {}
    for item in lista_tabelas:
        lista_dados.update(Dados_Producao().dados(item))
    # print(lista_dados)
    return render(request, "homepage.html", lista_dados)

# homepage(request=1)
