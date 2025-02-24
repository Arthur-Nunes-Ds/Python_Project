import csv
colunas = ["login", "senha"]
Conjuntos_de_logins = [{"login": "test", "senha": "123"},
                       {"login": "user", "senha": "adm"}]

arquivo = open("logins.csv", "w", newline='')
escrita = csv.DictWriter(arquivo, fieldnames= colunas)
escrita.writeheader()
escrita.writerows(Conjuntos_de_logins)