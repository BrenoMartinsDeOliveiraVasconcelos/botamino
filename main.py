from BotAmino import *
from random import uniform, choice, randint

print("Iniciando")
client = BotAmino()
client.wait = 2


@client.command("entrartd")
def joinall(data):
    print(type(data))
    data.subClient.send_message(chatId=data.chatId, message="Entrando...")
    data.subClient.join_all_chat()
    data.subClient.send_message(chatId=data.chatId, message="Pronto.")
    value = int(''.join(open("value", 'r').readlines()))
    value = value + 1
    print(value)


#@client.command("sairtd")
#def leaveall(data):
    #data.subClient.send_message(chatId=data.chatId, message="Okay")
    #data.subClient.leave_all_chats()
    #data.subClient.send_message(chatId=data.chatId, message="Pronto")
    #value = int(''.join(open("value", 'r').readlines()))
    #value = value + 1
    #print(value)


@client.command("ship")
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


@client.command("spam")
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


@client.command("cancelar")
def cancel(data):
    msg = data.message
    motivos = ["ser um gostoso(a)", "ser foda", "ser muito gado", "ser corno", "que sim, fodase",
               'ser um bostakkk', 'ser sensato', 'gostar do Felipe Neto']
    data.subClient.send_message(chatId=data.chatId, message=f"{msg} foi cancelado por {choice(motivos)}")


@client.command("help")
def help(data):
    data.subClient.send_message(chatId=data.chatId, message="""

[bc]== Comandos ==
[ci]!reload - Recarrega o bot
[ci]!entrartd - Entra em todos os chats publicos
[ci]!sairtd - Sai de todos os chats publicos
[ci]!ship (Pessoa1, Pessoa2) - Shippa 2 pessoas
[ci]!spam [vezes] [Texto]- Flooda uma msg especifica em uma quantidade especifica de vezes 
[ci]!help - Ajuda
[ci]!cancelar [Pessoa] - Cancela alguém
[ci]!entrar_em [link ou id] - Entra no chat 
[ci]!vsfbot - Manda o bot se fuder
[ci]!copypasta - Envia uma copypasta
[ci]!google [pesquisa]- Pesquisa no google
[ci]!kid [TEXTO] - fAz O tExTo FiCaR AsSiM
[ci]!pvp [rounds, player1, player2] - Pvp.

[bc]GumBot feito pela Gumball Amino ©2021

    """)


@client.command("entrar_em")
def joinchat(data):
    data.subClient.send_message(chatId=data.chatId, message="Entrando, por favor aguarde...")
    data.subClient.join_chatroom(data.message)
    data.subClient.send_message(chatId=data.chatId, message=f"Pronto.")


@client.command("vsfbot")
def vsfbot(data):
    data.subClient.send_message(chatId=data.chatId, message="vai tomar no cu")


@client.command("copypasta")
def copypasta(data):
    copypasta = ["""Meu avô fumou a vida inteira. Eu tinha uns 10 anos quando minha mãe lhe disse, "Se você pensa em 
    ver seus netos se formarem, você tem que parar imediatamente". Uma lágrima escorreu dos olhos dele quando 
    entendeu exatamente o que estava em jogo. Ele parou na hora. Três anos depois ele faleceu de câncer de pulmão. 
    Foi muito triste e me deixou completamente sem chão. Minha mãe me disse "Nunca fume. Por favor, não faça sua 
    família sofrer do jeito que seu avô nos fez". Eu obedeci. Aos 28, eu nunca sequer encostei num cigarro. Mas devo 
    dizer, eu sinto um leve arrependimento por nunca ter feito isso, por que seu post me deu câncer mesmo assim.""",
                 """Eu acho hilário vocês falando merda do OP. Vocês não falariam isso pra ele na lan, ele é bolado. 
                 Além disso, ele veste as roupas mais descoladas, come nos restaurantes mais picas e anda com os 
                 caras mais gostosos. Vocês são patéticos rs""", """Em caso de investigação policial, eu declaro que 
                 não tenho envolvimento com este grupo e não sei como estou no mesmo, provavelmente fui inserido por 
                 terceiros, declaro que estou disposto a colaborar com as investigações e estou disposto a me 
                 apresentar a depoimento se necessário.""", """MERMÃO, EU TOMO MONSTER, TENDEU? M-O-N-S-T-E-R!!! A 
                 MELHOR BEBIDA JA FEITA PELA HUMANIDADE, ÓBVIO QUE TU NÃO VAI CONHECER PQ TU É VELHO, MAS EU, 
                 EU SOU ADOLESCENTE MODERNO TA LIGADO???? EU PEGO 8 CONTO EM TROCO E VO NO MERCADO, FAZER O QUE?? 
                 COMPRAR UM MONSTER PORRA, ADOLESCENTE MODERNO SÓ TOMA MONSTER E POSTA FOTO MESMO, PRA ESCULACHAR 
                 NESSA TUA CARA DE VELHO QUE TOMA BEBIDA ALCOÓLICA E DOLLY, QUE MONSTER TA COM TUDO E VOCÊS COM 
                 NADA!!!!!!!!!!!! AH E SÓ PRA TU SABER, TUA BEBIDA COM GOSTO DE NADA QUE AINDA É FORTE, É 400 VEZES 
                 MAIS CARO QUE MEU MONSTER E 1 MILHÃO DE VEZES PIOR, ENQUANTO MEU MONSTER É VARIADO EM SABORES E UM 
                 MELHOR QUE O OUTRO, ALÉM DE QUE NÃO TE DEIXAM FORA E NÃO DA DESGOSTO PROS TEUS PAIS. TENDEU NESSA 
                 PORRA?????? MONSTER É TUDO, POSTO FOTO MESMO E COMPRO QUANDO QUERO, PQ MONSTER NUNCA SERÁ SUPERADO, 
                 RED BULL É COISA DE BAITOLA CHUPA ROLA, MONSTER É COISA DE CABRA MACHO, MACHO ALFA, HOMEM, 
                 SUJEITO MACHO, CAMPEÃO!!!!!!!!!!! AGORA DA LICENÇA QUE TENHO QUE IR COMPRAR MEU MONSTER DE HOJE E 
                 POSTAR MAIS UMA FOTO PRA TU FICAR COM RECALQUE DE MIM QUE SOU UM ADOLESCENTE MODERNO ENQUANTO TU É 
                 SÓ UM FUDIDO.""", """team🇧🇷VAI TOMAR NO CU MAMACO🇧🇷
ŚE TEM PODERZIN È PRÅ ŪSÅ 🦖🦖🦖‼‼‼ ................./¯/)............(\¯
.............../¯ ./............... ¯
............./. . /................ \ . .
......../´¯/' . '/´¯•¸,....,•´¯' . '\´¯
..../' /. ./ . ./ . ./¯../¯. . . . . .\ '
..( . ( . ( . ( ¯ ./' . ')..(' . '. ¯ ) . ) . ) . ) ...\ . . . . . . . . . . ./.... . . . . . . . . . ./ .....\ . . . . . . . . ./....... . . . . . . . . / .....(. . . . . . . . . ......./. . . . . . . . . ) 🔥🦖🦖🦖ÅŤÅQŮ Ę ĐØ§ LAGARTO ĽØĶØ🦖🦖🦖🔥 👉😎👉 👉😎👉 AGORA É NOIS QUE MANDA NESSA PORRA ☣☣☣👿 🦖🦖🤝🦖🦖 OS SOLADORES DE MAMACO ESTÃO PASSANDO POR VOCÊ 🐒🐒🐒 ▬▬▬.◙.▬▬▬ ═▂▄▄▓▄▄▂ ◢◤ █▀🦎▀████▄▄▄▄◢◤ █▄ █ー ███▀▀▀▀▀▀▀╬ ◥█████◤ ══╩══╩═ Desafiamos todos os mamaquinho ╬╬ ╬╬ ╬╬ ╬╬// A DESAFIAR O GRANDE DEUS ZILLA 🦖🦖🔥🔥🔥 MITOOOOOOOOOO GOD 👉😎👉 SEGUE A RISADA DO LAGARTO: KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK MAMAQUINHO TEM QUE SE FODER E ACABOU PORRA 🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🦖🦖🦎🦎🦎🦖🦖🦖 ▕▇▇▇◤▔▔▔▔▔▔▔◥▇▇▇ ▕▇▇▇▏◥▇◣┊◢▇◤▕▇▇▇ ▕▇▇▇▏▃▆▅▎▅▆▃▕▇▇▇ ▕▇▇▇▏╱▔▕▎▔▔╲▕▇▇▇ ▕▇▇▇◣◣▃▅▎▅▃◢◢▇▇▇ ▕▇▇▇▇◣◥▅▅▅◤◢▇▇▇▇ ▕▇▇▇▇▇◣╲▇╱◢▇▇▇▇▇ ▕▇▇▇▇▇▇◣▇◢▇▇▇▇▇▇ unhe unhe unhe unhe unhe unhe unhe unhe unhe unhe unhe unhe unhe unhe unhe unhe unhe unhe unhe unhe unhe unhe unhe unhe unhe unhe unhe unhe unhe unhe unhe unhe unhe unhe unhe unhe unhe unhe unhe unhe unhe unhe unhe unhe unhe unhe unhe unhe unhe unhe unhe unhe unhe unhe unhe unhe unhe unhe unhe unhe unhe unhe unhe unhe unhe unhe unhe unhe unhe unhe unhe unhe unhe unhe unhe unhe unhe unhe Facção ZILLA 💪🏼 O bonde dos lagarto ataca novamente 🦖🦖🦖 vai chorar 🐒? 😭😭 GOD acima de tudo, ZILLA encima de todos ✊✊ tá em shock ⚡⚡ 😯😯😳😳😳😳😳 fica Flinstons aí Kong corn0👋👋🥗🥗 Avante Zilla 🏁🏁🏁🏁🏁🏁VAI TOMA NO CU KONG ................./¯/)............(\¯
.............../¯ ./............... ¯
............./. . /................ \ . .
......../´¯/' . '/´¯•¸,....,•´¯' . '\´¯
..../' /. ./ . ./ . ./¯../¯. . . . . .\ '
..( . ( . ( . ( ¯ ./' . ')..(' . '. ¯ ) . ) . ) . ) ...\ . . . . . . . . . . ./.... . . . . . . . . . ./ .....\ . . . . . . . . ./....... . . . . . . . . / .....(. . . . . . . . . ......./. . . . . ."""]
    data.subClient.send_message(chatId=data.chatId, message=choice(copypasta))


@client.command("google")
def google(data):
    msg = data.message.split(" ")
    msg = '+'.join(msg)
    data.subClient.send_message(chatId=data.chatId, message=f"https://www.google.com/search?q={msg}")


@client.command("kid")
def sarcasmo(data):
    msg = data.message
    res = []
    for loop in msg:
        if randint(0, 1) == 1:
            res.append(loop.upper())
        else:
            res.append(loop)

    res = ''.join(res)
    data.subClient.send_message(chatId=data.chatId, message=res)


@client.command("pvp")
def pvp(data):
    import time
    msg = data.message + " null null "
    msg = msg.split(" ")
    try:
        rounds = int(msg[0])
    except (TypeError, ValueError):
        rounds = 5
        msg[2] = msg[1]
        msg[1] = msg[0]
        msg[0] = 5
    data.subClient.send_message(chatId=data.chatId, message=f"Iniciando o pvp entre {msg[1]} e {msg[2]}...")
    win1 = 0
    win2 = 0
    round = 0
    agess = ''
    defens = ''
    for pvp in range(0, rounds):
        round = round + 1
        data.subClient.send_message(chatId=data.chatId, message=f"[bc]Round {round}/{rounds}")
        punch = randint(0, 1)
        if punch == 0:
            win1 = win1 + 1
            agress = msg[1]
            defens = msg[2]
        else:
            win2 = win2 + 1
            agress = msg[2]
            defens = msg[1]
        time.sleep(4)
        data.subClient.send_message(chatId=data.chatId, message=f"[ic] {agress} deu um locaute em {defens}!")
    if win1 > win2:
        data.subClient.send_message(chatId=data.chatId, message=f"[bcu]{msg[1]} ganhou!")
    elif win1 < win2:
        data.subClient.send_message(chatId=data.chatId, message=f"[bcu]{msg[2]} ganhou!")
    elif win1 == win2:
            data.subClient.send_message(chatId=data.chatId, message=f"[iC]Empate.")



client.launch()
