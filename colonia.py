
                                                                ##============================== Dados atuais da colônia: ==============================##

dados_colonia = {
    "energia" : 30, 
    "consumo" : 70, 
    "reserva" : 100,
    "clima" : {
        "vento" : 10,
        "temperatura" : 22,
        "luminosidade" : 75,

    }
}

sistemas_energeticos = {
    "solar" : 30,
    "eolico" : 25,
}

                                                                ##============================== Dados históricos colônia: ==============================##
                                                        
vento = [4, 6, 8, 10, 12, 14, 16]
geracao_eolica = [10,15, 20, 25, 30, 35, 40]

                                                                                ##============================================================##





def condicionais(energia , consumo):

    if consumo > energia:
        print("\nAtenção! Consumo maior que energia disponível. Iremos utilizar energia dos sistemas de geração de energia. \nSomando...\n")

    
    if energia <= 30 and consumo >= energia:
            print ("priorizar apenas sistemas essenciais, desligar todo o resto.\n")
    

    elif energia > consumo:
        print ("Energia disponível maior que consumo. \nOperação normal. \n")

    elif energia < 50:
        print("Baixa energia.\n")


                                                                                ##============================================================##


condicionais(dados_colonia['energia'] , dados_colonia['consumo'])

sist_en_total = sistemas_energeticos['solar'] + sistemas_energeticos["eolico"]
en_total = sist_en_total + dados_colonia['energia']

print (f"A energia total agora é de {en_total}.\nEla será consumida para o funcionamento da colônia.\n")

en_final = en_total - dados_colonia["consumo"]
print(f"A energia está em {en_final}.")

if en_final < 50:
    print(f"Energia em {en_final}. Iremos utilizar energia da reserva!\nReserva = {dados_colonia['reserva']}")
    while en_final < 100 and dados_colonia['reserva'] > 0:
        dados_colonia["reserva"] = dados_colonia["reserva"] - 1
        en_final = en_final + 1
        if dados_colonia['reserva'] <= 0:
            print("A reserva acabou.")
            break

    print (f"A energia atual está em: {en_final}")
    print (f"A reserva de energia está em: {dados_colonia['reserva']}")    
    print (f"Após somar com a reserva, temos {en_final} de energia disponível.")

if en_final >= 50:
    condicionais(en_final, dados_colonia["consumo"])
else:
    print(f"Energia em {en_final}. Não temos energia o suficiente para sustentar a colônia.")


def calcular_media(a, b, hist):
    x = sum(a)
    y = len(b)


    media = x / y
    
    print(f"A média de {hist} é de {media}")
    return media


media_vento = calcular_media(vento, vento, "vento")
media_eolica = calcular_media(geracao_eolica, geracao_eolica, "geração eólica")
print("")

numerador = 0
denominador = 0


for i in range(len(vento)):
    x = vento[i]
    y = geracao_eolica[i]
    print (x , y)

    numerador += (x - media_vento) * (y - media_eolica)
    denominador += (x - media_vento) ** 2

estimativa = numerador / denominador

print(f"\nA inclinação da regressão linear de energia eólica é de {estimativa}")
estimativa_vento = estimativa * dados_colonia["clima"]['vento']
print(f"A estimativa de geração de energia eólica é de {estimativa_vento}")

sistemas_energeticos['eolico'] = estimativa_vento
sist_en_total = sistemas_energeticos["solar"] +  sistemas_energeticos["eolico"]

print(f"Previsão de geração total de energia: {sist_en_total}")
