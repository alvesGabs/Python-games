import easygui
import random

# Lista de palavras (ou você pode descomentar a leitura do arquivo se preferir)
# with open("forca.txt") as arquivo:
#     palavras = arquivo.readlines()
# palavraSorteada = random.choice(palavras).strip()

Palavras = ["velha", "animal", "tentativas", "rodeio", "cirurgia"]
palavraSorteada = random.choice(Palavras).lower()

espacoBranco = "_" * len(palavraSorteada)
letrasEscolhidas = []

desafios = ["Normal", "Tormento", "Inferno", "Nightmare"]
tentativas = 0

# Boas-vindas
easygui.msgbox("EAI, VACILÃO, VAI FRANGAR OU VAI JOGAR?", "FORCA OF MADNESS SPECIAL EDITION", "VAM'BORA!")

dificuldade = easygui.choicebox("Escolha a dificuldade:", "FORCA OF MADNESS SPECIAL EDITION", desafios)

if dificuldade == "Normal":
    tentativas = 6
elif dificuldade == "Tormento":
    tentativas = 4
elif dificuldade == "Inferno":
    tentativas = 2
elif dificuldade == "Nightmare":
    tentativas = 1

easygui.msgbox(f"O sofrimento escolhido foi: {dificuldade}\nVocê pode cometer {tentativas} erro(s).", 
               "FORCA OF MADNESS SPECIAL EDITION")

# Loop principal
while True:
    mensagem = f"Palavra: {espacoBranco}\n\nLetras usadas: {' '.join(letrasEscolhidas)}\nErros restantes: {tentativas}"
    letra = easygui.enterbox(mensagem, "FORCA OF MADNESS SPECIAL EDITION")

    if not letra or len(letra) != 1 or not letra.isalpha():
        easygui.msgbox("Digite apenas **UMA** letra válida!", "FORCA OF MADNESS SPECIAL EDITION")
        continue

    letra = letra.lower()

    if letra in letrasEscolhidas:
        easygui.msgbox(f"A letra '{letra}' já foi tentada, vacilão.", "FORCA OF MADNESS SPECIAL EDITION")
        continue

    letrasEscolhidas.append(letra)

    if letra in palavraSorteada:
        nova_palavra = ""
        for i in range(len(palavraSorteada)):
            if palavraSorteada[i] == letra:
                nova_palavra += letra
            else:
                nova_palavra += espacoBranco[i]
        espacoBranco = nova_palavra

        if "_" not in espacoBranco:
            easygui.msgbox(f"ACERTOU, SEU MIZERA!\nA palavra era: '{palavraSorteada}'", 
                           "FORCA OF MADNESS SPECIAL EDITION")
            break
    else:
        tentativas -= 1
        if tentativas == 0:
            easygui.msgbox(f"PERDESTE!\nA palavra era: '{palavraSorteada}'", 
                           "FORCA OF MADNESS SPECIAL EDITION")

            def principal():
                opcao = easygui.indexbox("Continuar jogando?", 
                                         "FORCA OF MADNESS SPECIAL EDITION",
                                         choices=["Sim", "Não"])
                if opcao == 0:
                    easygui.msgbox("OK! REVIVAM ELE PARA QUE POSSAMOS ENFORCÁ-LO DE NOVO!")
                    exec(open(__file__).read())  # reinicia o script atual
                else:
                    easygui.msgbox("LEVEM ELE!! ESSE FOI REQUISITADO PELO VASCO!!")

            principal()
            break