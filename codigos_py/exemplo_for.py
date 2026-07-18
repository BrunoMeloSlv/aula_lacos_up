# ============================================================================
# ARQUIVO : exemplo_for.py
# O QUE FAZ: Simulador de Poupanca usando FOR (repeticao CONTADA).
#            Pergunta quanto o usuario economiza por mes e mostra, mes a mes,
#            o total acumulado em EXATAMENTE 12 meses.
# AULA    : Lacos de Repeticao em Python | Universidade Positivo | Prof. Bruno Melo
# ----------------------------------------------------------------------------
# CONCEITO
#   O laco `for` em Python percorre os elementos de uma sequencia. Para repetir
#   um numero CONHECIDO de vezes, iteramos sobre um range(): repeticao contada.
#       for variavel in range(inicio, fim):    # 'fim' NAO entra
#           corpo
#   - range(1, 13) gera 1, 2, ..., 12 (o 13 fica de fora);
#   - a variavel de controle recebe cada valor e AVANCA sozinha (nao ha 'mes++');
#   - o corpo e delimitado por INDENTACAO, nao por chaves.
# Referencias: DOWNEY (2016); ASCENCIO; CAMPOS (2012).
# EXECUTAR : python exemplo_for.py
# ============================================================================

MESES = 12                       # horizonte FIXO de 12 meses

print("=== Simulador de Poupanca (FOR - 12 meses) ===")
mensal = float(input("Quanto voce consegue economizar por mes? R$ "))

total = 0.0                      # total acumulado

# Repeticao CONTADA: range(1, 13) -> 1, 2, ..., 12
for mes in range(1, MESES + 1):
    total += mensal              # corpo: acumula a economia do mes
    print(f"Mes {mes:2d} -> acumulado: R$ {total:.2f}")

print(f"\nEm {MESES} meses voce tera R$ {total:.2f}")
