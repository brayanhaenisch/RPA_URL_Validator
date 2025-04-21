import requests
import csv
import os
import pyodbc

conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=localhost\SQLTESTEURL;'
    'DATABASE=TesteURL;'
    'UID=sa;'
    'PWD=senha;'
)

cursor = conn.cursor()

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def url_testar():

    resultados = []
    sucesso = 0
    erro = 0
    falha = 0

    with open('urls.txt', 'r') as file:
        urls = file.readlines()

    total = len(urls)

    print('-------------')

    for i, url in enumerate(urls, start=1):
         print(f'Processando URL {i}/{total}...')
         
       
    for url in urls:
        url = url.strip()
        
        try:
            response = requests.get(url, timeout=5)
            status_code = response.status_code

            if response.status_code == 200:
                status = 'OK'
                observacao = 'URL validada com sucesso'
                sucesso += 1

            if 400 <= response.status_code < 600:
                status = 'ERRO'
                observacao = 'Ocorreu um erro ao validar a URL'
                erro += 1
            
            

        except requests.exceptions.RequestException as e:
                status = 'FALHA'
                observacao = str(e) 
                status_code = '-'
                falha += 1

        resultados.append([url, status, status_code, observacao])

        cursor.execute(
             "INSERT INTO ResultadosLinks (URL, Status, StatusCode, Observacao) VALUES (?, ?, ?, ?)",
             url, status, status_code, observacao
        )
        conn.commit()

    with open('resultados.csv', 'w', newline='', encoding='utf-8') as csvfile:
         escritor = csv.writer(csvfile)
         escritor.writerow(['URL', 'STATUS', 'STATUS_CODE','OBSERVACAO'])
         escritor.writerows(resultados)
    print(f'-------------\nResultados salvos em "resultados.csv"')
    print(f'-------------\nTotal: {total}')
    print(f'Sucesso: {sucesso}') 
    print(f'Erro: {erro}')
    print(f'Falha: {falha}\n-------------')
    print("Todos os dados foram inseridos no banco!")


limpar_terminal()
url_testar()
cursor.close()
conn.close()