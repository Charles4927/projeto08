from django.shortcuts import render
from .models import Filme
# import pyodbc


# Create your views here.
def homepage(request):
    return render(request, "homepage.html")

# def valores_do_bco(request):
#     context = {}
#
#     dados_conexao = ("Driver={MySQL ODBC 8.0 Unicode Driver};"
#                      "Server=10.11.1.10;"
#                      "Database=cdtmes;"
#                      "UID=admin;"
#                      "PWD=Admin@Condutec;")
#     conexao = pyodbc.connect(dados_conexao)
#     cursor = conexao.cursor()
#
#     cursor.execute("SELECT Hora FROM luxor_producao")
#
#     ultimo_ciclo = cursor.fetchall()
#     # valor_anterior = None
#     # if valores[-1:] != valor_anterior:
#     # valores_mostrados['text'] = str(valores[-1:][0][0])
#     cursor.close()
#     conexao.close()
#
#     context['ultimo_ciclo'] = str(ultimo_ciclo[-1:][0][0])
#     return render(request, "homepage.html", context)
