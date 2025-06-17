def classificacao_infracao(velocidade,velocidade_max):
    if velocidade<=velocidade_max:
        return 'nenhuma',0,0,False
    elif velocidade<=velocidade_max*1.2:
        return 'leve',130.16,0,False
    elif velocidade<=velocidade_max*1.5:
        return 'grave',195.23,5,False
    elif velocidade>velocidade_max*1.5:
        return 'gravissima',880.41,7,True

def verificar_reincidencia(infracao, reincidente, multa):
    if reincidente == "Sim" and infracao in ["grave", "gravissima"]:
        multa=multa*2
        return True, multa
    return False, multa

def aplicar_desconto(pagar, multa):
    if pagar == "Sim":
        return True, multa * 0.8
    return False, multa

def exibir_resultado(placa, nome, velocidade, velocidade_max, infracao, multa, pontos, suspensao, reincidente, pagamento, multa_final):
    print(f"\nPlaca: {placa}")
    print(f"Motorista: {nome}")
    print(f"Velocidade registrada: {velocidade} km/h")
    print(f"Velocidade máxima permitida: {velocidade_max} km/h")

    if infracao == "nenhuma":
        print("Nenhuma infração.")
    else:
        print(f"Infração {infracao.lower()} - Multa de R$ {multa:.2f}, {pontos} pontos na CNH", end='')
        if suspensao:
            print(" e suspensão da carteira.")
        else:
            print(".")

        if reincidente:
            print("Atenção: Multa DOBRADA por reincidência!")

        if suspensao:
            print("Atenção: CNH suspensa! Compareça ao Detran.\nAtenção: Você precisa fazer um curso de reciclagem no Detran.")

        if pagamento:
            print(f"Pagamento realizado! Você recebeu um desconto de 20%. Valor final: R$ {multa_final:.2f}")
        else:
            print(f"Valor final da multa: R$ {multa_final:.2f}")

# --- Início do programa ---
placa = input("Placa do veículo: ")
nome = input("Nome do motorista: ")
velocidade = float(input("Velocidade registrada (km/h): "))
velocidade_max = float(input("Velocidade máxima permitida (km/h): "))
reincidente = input("O motorista já foi multado antes? (Sim/Não): ")
pagar = input("Deseja pagar a multa agora? (Sim/Não): ")

infracao, multa, pontos, suspensao = classificacao_infracao(velocidade, velocidade_max)
reincidente, multa = verificar_reincidencia(infracao, reincidente, multa)
pagamento, multa_final = aplicar_desconto(pagar, multa)

exibir_resultado(placa, nome, velocidade, velocidade_max, infracao, multa, pontos, suspensao, reincidente, pagamento, multa_final)

