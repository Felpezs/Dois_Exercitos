import time
import random
from datetime import datetime, timedelta

# Decidir se o mensageiro foi capturado ou não
def decisão(probabilidade):
    return random.random() < probabilidade

# Gerar o tempo em que o mensageiro levou e atualizar a variável timestamp
def enviarMensageiro(tempo, corMensageiro, captura):

    # Se não foi capturado, soma o tempo randômico entre 60 e 70 minutos
    if(captura == False):
        # Tempo randômico de 60 a 70 minutos convertido em segundos
        tempoViagem = random.randint(60, 70) * 60
        print(f"\nSISTEMA: Tempo de travessia do mensageiro {corMensageiro} foi de: {tempoViagem}")
        tempo += timedelta(seconds = tempoViagem)

    # Se foi capturado, soma o tempo máximo de travessia
    else:
        tempo += timedelta(seconds = 4200)
        print(f"\nSISTEMA: Tempo de travessia do mensageiro {corMensageiro}(capturado) foi de: 4200")

    return tempo

def mensageiroCapturado(tempo, tempoMax, corMensageiro, corExército, qntdMensageiros):
    
    chegou = False
    tempo = enviarMensageiro(tempo, corMensageiro, True)
    print(f"\nSISTEMA: Mensageiro {corMensageiro} capturado!")
    tempoViagem = 4200
    qntdMensageiros -= 1

    if(qntdMensageiros > 0):

        while (tempoViagem < tempoMax):
            # Se o msg chegar no exército
            if decisão(0.55) :
                tempo = enviarMensageiro(tempo, corMensageiro, False)
                print(f"\nSISTEMA: Mensageiro {corMensageiro} chegou no Exército {corExército}!")
                chegou = True 
                break  
            else:
                qntdMensageiros -= 1
                tempoViagem += 4200
                tempo = enviarMensageiro(tempo, corMensageiro, True)
                if(qntdMensageiros >= 0):
                    print(f"\nSISTEMA: Mensageiro {corMensageiro} capturado!")
                else:
                    break
        else:
            chegou = False
            print(f"\nSISTEMA: Se passaram {tempoMax/60} minutos e o mensageiro do Exército {corExército} não chegou, enviaremos um outro Mensageiro")
        
    return tempo, qntdMensageiros, chegou

# Código

msgs_vermelho = 5
msgs_azul     = 10
exsAzulAceitar = False
msgsAzulChegou = False
msgsVermelhoChegou = False

# Pegar a timestamp atual
timestamp = time.mktime(datetime.now().timetuple())
timestamp = datetime.fromtimestamp(timestamp)
print("*Timestamp atual*")
print("timestamp =", timestamp.hour, ":" ,timestamp.minute, ":" ,timestamp.second)

while(msgsAzulChegou == False):

    # Se os msgs_azul ou msgs_vermelho acabarem, sai do loop
    if(msgs_azul == 0 or msgs_vermelho == 0):
        print("\nSISTEMA: Todos os mensageiros azuis foram capturados e assassinados brutalmente!")
        print("\nSISTEMA: Os exércitos perderam!")
        break

    # Se o msgs_Vermelho chegar no exército Azul
    if decisão(0.55):
        timestamp = enviarMensageiro(timestamp, 'Vermelho', False)
        print("\nSISTEMA: Mensageiro vermelho chegou no Azul!")
        msgsVermelhoChegou = True
        exsAzulAceitar = decisão(0.99)

    # Se o msgs_Vermelho não chegar no exército Azul
    else:
        var_aux = mensageiroCapturado(timestamp, 12600, 'Vermelho', 'Azul', msgs_vermelho)
        timestamp, msgs_vermelho, msgsVermelhoChegou = var_aux
        
        if  msgsVermelhoChegou:
            exsAzulAceitar = decisão(0.99)

    # Se o exército azul aceitar o horário
    if(exsAzulAceitar == True and msgsVermelhoChegou == True):
        print("\nSISTEMA: Exercito Azul aceitou horario")

        # Se o msgs_azul fez a travessia
        if decisão(0.55):
            msgsAzulChegou = True
            timestamp = enviarMensageiro(timestamp, 'Azul', False)
            print("\nSISTEMA: Mensageiro azul chegou no vermelho!")

        # Se o msgs_azul não fez a travessia
        else:
            var_aux = mensageiroCapturado(timestamp, 16800, 'Azul', 'Vermelho', msgs_azul)
            timestamp, msgs_azul, msgsAzulChegou = var_aux
    
    # Se o exército azul não aceitar o horário
    elif(exsAzulAceitar == False and msgsVermelhoChegou == True):

        print("\nSISTEMA: O exército Azul recusou o horário de ataque!")   
        #Se o msgs_azul fez a travessia
        if decisão(0.55):
            timestamp = enviarMensageiro(timestamp, 'Azul', False)
            print("\nSISTEMA: Mensageiro Azul chegou no Exército Vermelho pedindo um novo horário")
            msgsAzulChegou = False

        # Se o msgs_azul não fez a travessia
        else:
            var_aux = mensageiroCapturado(timestamp, 12600, 'Azul', 'Vermelho', msgs_azul)
            timestamp, msgs_azul, msgsAzulChegou = var_aux
            
            if  msgsAzulChegou:
                msgsAzulChegou = False
                print("\nSISTEMA: Mensageiro Azul pediu um novo horário")

    #msgs_azul chegou no exército vermelho com o horário do ataque
else:
    print("\nSISTEMA: O sinalizador foi disparado! Os Exércitos venceram a batalha e dominaram o castelo!")

print("\n*Timestamp FINAL*")

print(f"timestamp = {timestamp.hour}:{timestamp.minute}:{timestamp.second}")
print(f"\nMensageiros vermelhos restantes = {msgs_vermelho}")
print(f"Mensageiros azuis restantes = {msgs_azul}")
input()