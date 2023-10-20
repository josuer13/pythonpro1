print("Bienvenido, en este programa puedes aprender las palabras modernas que no sepas. Puedes realizar 5 búsquedas.")
meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "ROFL": "Una respuesta a una broma",
            "SHEESH": "Ligera desaprobación",
            "CREEPY": "Aterrador, siniestro",
            "AGGRO": "Ponerse agresivo/enojado",
            }
i=0            
while i != 5:    
    print("")
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
    if word in meme_dict.keys():
        print("Significa: ", meme_dict[word])
    else:
        print("Esa palabra no existe")
    i=i+1
print("Gracias por usar nuestro servicio! Hasta la próxima!")
