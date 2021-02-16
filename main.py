from BotAmino import *
from random import uniform, choice
import os
import sys
import datetime

print("Iniciando")
client = BotAmino()
client.wait = 10
client.prefix = "!"


@client.command("!reload")
def reload(data):
    os.execv(__file__, sys.argv)


@client.command("!entrartd")
def joinall(data):
    print(type(data))
    data.subClient.send_message(chatId=data.chatId, message="Entrando...")
    data.subClient.join_all_chat()
    data.subClient.send_message(chatId=data.chatId, message="Pronto.")
    value = int(''.join(open("value", 'r').readlines()))
    value = value + 1
    print(value)


@client.command("!sairtd")
def leaveall(data):
    data.subClient.send_message(chatId=data.chatId, message="Okay")
    data.subClient.leave_all_chats()
    data.subClient.send_message(chatId=data.chatId, message="Pronto")
    value = int(''.join(open("value", 'r').readlines()))
    value = value + 1
    print(value)


@client.command("!ship")
def ship(data):
    casal = data.message + " null null "
    pessoas = casal.split(" ")
    porcentagem = uniform(0, 100)
    quote = ' '
    if porcentagem <= 10:
        quote = 'Sem chance.'
    elif 10 <= porcentagem <= 25:
        quote = 'Eh...'
    elif 25 <= porcentagem <= 50:
        quote = 'Quem sabe um dia?'
    elif 50 <= porcentagem <= 75:
        quote = 'Meu casal ❤'
    elif 75 <= porcentagem <= 100:
        quote = 'Casal top'
    data.subClient.send_message(chatId=data.chatId, message=f"{pessoas[0]} x {pessoas[1]} tem {porcentagem:.2f}% "
                                                            f"de chance de dar certo.")
    data.subClient.send_message(chatId=data.chatId, message=quote)
    value = int(''.join(open("value", 'r').readlines()))
    value = value + 1
    print(value)


@client.command("!spam")
def spam(data):
    import time
    msg = data.message
    msg = msg.split(" ")
    msg.append(" ")
    msg[1] = ' '.join(msg[1:])
    try:
        num = int(msg[0])
    except (TypeError, ValueError):
        data.subClient.send_message(chatId=data.chatId, message="Digite a quantidade de vezes antes da frase.")
        return False

    for loop in range(1, int(msg[0]) + 1):
        data.subClient.send_message(chatId=data.chatId, message=msg[1])
        time.sleep(1)


@client.command("!cancelar")
def cancel(data):
    msg = data.message
    motivos = ["ser um gostoso(a)", "ser foda", "ser muito gado", "ser corno", "que sim, fodase", "comer o cu de quem "
                                                                                                  "ta lendo",
               'um bostakkk']
    data.subClient.send_message(chatId=data.chatId, message=f"{msg} foi cancelado por {choice(motivos)}")


@client.command("!help")
def help(data):
    data.subClient.send_message(chatId=data.chatId, message="""

[bc]== Comandos ==
[ci]!!reload - Recarrega o bot
[ci]!!entrartd - Entra em todos os chats publicos
[ci]!!sairtd - Sai de todos os chats publicos
[ci]!!ship (Pessoa1, Pessoa2) - Shippa 2 pessoas
[ci]!!spam [vezes] [Texto]- Flooda uma msg especifica em uma quantidade especifica de vezes 
[ci]!!help - Ajuda
[ci]!!cancelar [Pessoa] - Cancela alguém
[ci]!!entrar_em [link ou id] - Entra no chat 
[ci]!!vsfbot - Manda o bot se fuder
[ci]!!copypasta - Envia uma copypasta
[ci]!!google [pesquisa]- Pesquisa no google

    """)


@client.command("!entrar_em")
def joinchat(data):
    data.subClient.send_message(chatId=data.chatId, message="Entrando, por favor aguarde...")
    data.subClient.join_chatroom(data.message)
    data.subClient.send_message(chatId=data.chatId, message=f"Pronto.")


@client.command("!vsfbot")
def vsfbot(data):
    data.subClient.send_message(chatId=data.chatId, message="vai tomar no cu")


@client.command("!google")
def joinchat(data):
    msg = data.message.split(" ")
    msg = '+'.join(msg)
    data.subClient.send_message(chatId=data.chatId, message=f"https://www.google.com/search?q={msg}")


client.launch()
