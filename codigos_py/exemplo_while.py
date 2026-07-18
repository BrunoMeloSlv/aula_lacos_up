# ============================================================================
# ARQUIVO : exemplo_while.py
# O QUE FAZ: Simulador de Poupanca usando WHILE (repeticao CONDICIONADA).
#            Pergunta o valor economizado por mes e a META (ex: um notebook) e
#            calcula em quantos meses a meta e atingida, mostrando o total
#            acumulado a cada iteracao.
# AULA    : Lacos de Repeticao em Python | Universidade Positivo | Prof. Bruno Melo
# ----------------------------------------------------------------------------
# CONCEITO
#   O laco `while` repete ENQUANTO uma condicao for verdadeira. Nao sabemos
#   quantos meses serao necessarios: o laco para quando a META e atingida
#   -> repeticao condicionada. A condicao e avaliada ANTES do corpo (DOWNEY,
#   2016); se a meta ja estivesse satisfeita, o corpo nao executaria nenhuma vez.
#   OBS.: exigimos `mensal > 0` para evitar laco infinito quando o usuario
#   informa 0 (o total nunca cresceria e a meta nunca seria atingida).
# Referencias: DOWNEY (2016); ASCENCIO; CAMPOS (2012).
# EXECUTAR : python exemplo_while.py
# ============================================================================

print("=== Simulador de Poupanca (WHILE - ate a meta) ===")
mensal = float(input("Quanto voce consegue economizar por mes? R$ "))
meta   = float(input("Qual e a sua meta (ex: notebook)? R$ "))

if mensal <= 0:                    # protecao contra laco infinito
    print("O valor mensal precisa ser maior que zero.")
    raise SystemExit

total = 0.0                        # total acumulado
meses = 0                          # contador de meses gastos

# Repeticao CONDICIONADA: enquanto NAO atingir a meta
while total < meta:                # condicao testada ANTES de cada volta
    total += mensal                # corpo: acumula a economia do mes
    meses += 1                     # atualiza a variavel de controle
    print(f"Mes {meses:2d} -> acumulado: R$ {total:.2f}")

print(f"\nMeta atingida em {meses} meses! Total: R$ {total:.2f}")
