#declarando variaveis
colheita_total = 0.0
colheita = 0.0
perda_manual = 0.0
perda_maquina = 0.0
perda_manual_total = 0.0
perda_maquina_total = 0.0

print('Insira as toneladas colhidas por mês: ')
for volta in range(1, 13):
    #verificação para se caso o usuário não digitar nada.
    while True:
        colheita = (input(f'\n Mês {volta}: '))
        if colheita == "":
            print('Valor inválido. Por favor, insira o número em toneladas.')
        else:
            colheita = float(colheita)
            break

    perda_manual = colheita * 0.05
    perda_maquina = colheita * 0.15

    colheita_total += colheita
    perda_manual_total += perda_manual
    perda_maquina_total += perda_maquina

    print(f'\n Perda manual: {perda_manual:.2f} \n Perda com máquina: {perda_maquina:.2f}')


print(f'\n RELATÓRIO CONSOLIDADO: \n\n Colheita do ano: {colheita_total} \n\n Projeção de desperdício: \n   Manual: {perda_manual_total} \n   Com máquina: {perda_maquina_total}')
