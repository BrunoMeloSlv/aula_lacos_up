# ============================================================================
# ARQUIVO : exemplo_erro_proposital.py
# O QUE FAZ: Simulador de Poupanca (WHILE) com um ERRO PROPOSITAL de logica,
#            para ser depurado AO VIVO diante da banca. O programa RODA sem erro
#            de sintaxe, mas em tempo de execucao entra em LOOP INFINITO.
# AULA    : Lacos de Repeticao em Python | Universidade Positivo | Prof. Bruno Melo
# ----------------------------------------------------------------------------
# >>> NOTA PARA O PROFESSOR (nao ler em voz alta):
#     erro comum proposital para corrigir na hora.
#
# SINTOMA (ao rodar): o programa NUNCA para (loop infinito) e imprime sempre
#          "acumulado: R$ 0.00", com o contador de meses subindo indefinidamente.
#          Interrompa com Ctrl+C.
#
# CAUSA:   a variavel de controle da condicao (`total`) NAO e atualizada dentro
#          do laco. Como `total` permanece 0 e a meta e positiva, a condicao
#          (total < meta) e SEMPRE verdadeira -> loop infinito. Erro classico:
#          um laco condicionado precisa alterar, no corpo, a variavel testada
#          (DOWNEY, 2016).
#
# COMO CORRIGIR AO VIVO: descomente a linha marcada com [FIX].
#
# VARIANTE opcional (off-by-one) para discutir: no `for`, usar range(1, 12)
#          em vez de range(1, 13) faria o programa contar so 11 meses.
# EXECUTAR : python exemplo_erro_proposital.py
# ============================================================================

print("=== Simulador de Poupanca (VERSAO COM BUG) ===")
mensal = float(input("Quanto voce consegue economizar por mes? R$ "))
meta   = float(input("Qual e a sua meta? R$ "))

total = 0.0
meses = 0
while total < meta:
    # BUG: a variavel de controle (total) nao e atualizada -> loop infinito
    # total += mensal    # <-- [FIX] descomente esta linha ao vivo
    meses += 1
    print(f"Mes {meses:2d} -> acumulado: R$ {total:.2f}")

print(f"\nMeta atingida em {meses} meses! Total: R$ {total:.2f}")
