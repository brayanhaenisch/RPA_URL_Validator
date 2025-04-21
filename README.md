# Projeto: Verificador de Links Quebrados (Broken Link Checker)

## Objetivo
Criar um script em Python que leia uma lista de URLs, faça requisições HTTP a cada uma e gere um relatório indicando:
- Quais estão funcionando (status 200)  
- Quais retornam erro (4xx/5xx)  
- Quais não puderam ser acessadas (timeout, DNS etc.)  

## Por que é útil para QA?
- *Automatiza* uma tarefa comum de verificação de links em sites, documentação ou relatórios.  
- Ensina *file I/O, **laços, **tratamento de exceções, uso de **módulos externos* (como requests) e *formatos de saída* (CSV/JSON).  
- Proporciona experiência prática em como usar Python para validar a *qualidade de conteúdo*.  

## Funcionalidades mínimas (MVP)

1. *Leitura de URLs*  
   - O script recebe como parâmetro um arquivo de texto (urls.txt), com uma URL por linha.

2. *Requisição HTTP*  
   - Para cada URL, faz um GET (ou HEAD) usando o módulo requests.

3. *Tratamento de respostas*  
   - status_code == 200 → OK  
   - 400 ≤ status_code < 600 → Erro: Código XX  
   - Exceções (timeout, conexão recusada etc.) → Falha: <motivo>

4. *Geração de relatório*  
   - Salva um CSV (relatorio.csv) com colunas:  
     
     URL,Status,StatusCode,Observação
     

5. *Feedback no console*  
   - Mostrar progresso (e.g. “Verificando link 3/10…”)  
   - Ao final, exibir resumo:  
     - Total verificados  
     - Quantos OK  
     - Quantos com erro  
     - Quantos falharam  

## Tecnologias / Bibliotecas
- *Python 3.x*  
- *requests* (pip install requests)  
- Módulos da Stdlib: csv, argparse, time (para pausas), logging (opcional)