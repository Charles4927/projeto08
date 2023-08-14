from django.shortcuts import render
# from .models import Filme
import pyodbc


# Create your views here.



def homepage(request):
    context = {}

    # dados_conexao = ("Driver={MySQL ODBC 8.0 Unicode Driver};"
    #                  "Server=10.11.1.10;"
    #                  "Database=cdtmes;"
    #                  "UID=admin;"
    #                  "PWD=Admin@Condutec;")

    dados_conexao = ("Driver={MySQL ODBC 8.1 Unicode Driver};"
                     "Server=177.47.167.82;"
                     "Database=cdtmes;"
                     "UID=admin;"
                     "PWD=Admin@Condutec;")

    conexao = pyodbc.connect(dados_conexao)

    cursor = conexao.cursor()

    cursor.execute("SELECT Hora FROM luxor_producao")

    ultimo_ciclo = cursor.fetchall()
    # valor_anterior = None
    # if valores[-1:] != valor_anterior:
    # valores_mostrados['text'] = str(valores[-1:][0][0])
    cursor.close()
    conexao.close()

    # ultimo_ciclo = ["Não definido", "Não definido",]

    context['ultimo_ciclo'] = str(ultimo_ciclo[-1:][0][0])
    return render(request, "homepage.html", context)



# def my_function(request):
#     conexao = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=177.47.167.82;DATABASE=cdtmes;UID=admin;PWD=Admin@Condutec')
#     cursor = conexao.cursor()
#     cursor.execute('SELECT * FROM cdtmes.luxor_resumo where data = "09/08/2023"')
#     results = cursor.fetchall()
#     return results



# def homepage(request):
#     context = {}
#
#     conexao = pyodbc.connect(
#         'DRIVER={ODBC Driver 17 for SQL Server};SERVER=177.47.167.82;DATABASE=cdtmes;UID=admin;PWD=Admin@Condutec')
#     cursor = conexao.cursor()
#     cursor.execute("SELECT Hora FROM luxor_producao")
#     ultimo_ciclo = cursor.fetchall()
#
#     context['ultimo_ciclo'] = str(ultimo_ciclo[-1:][0][0])
#     return render(request, "homepage.html", context)



