# -*- coding: utf-8 -*-
# Importando os modulos / Bot

from src.classBot import Bot 
from function_extra import receive_hours, verify_hours, sleep_pause, banner, message_bot
import time, sys

bot = Bot()

if __name__ == '__main__':    
    try:
        while 1:

            if( verify_hours(bot) == False):
                bot.bot_clear()
                print("""
                    \n\n\t\t\t\033[1;31m[\033[1;33m!\033[1;31m] \033[1;33mPrograma está em fase de desenvolvimento ainda, por favor aguarde
                    \t\t         até o lançamento final do produto\033[1;31m!
                """)
                sleep_pause()
                
            else:
                banner(bot)
                
                bot.extract_info("https://www.theenemy.com.br/pc/respawn-nova-ip-titanfall-apex-legends")
                
                datas = bot.get_data()
                
                message_bot(bot)
            
    except KeyboardInterrupt: 

        bot.setMessage("Obrigado por utilizar os nossos serviços", 0)

    except Exception as error:

        bot.setMessage(error, 3)
        
    finally:

        print("\033[0;00m") # Remove a formatação imposta no script do bot
        bot.getMessage()
#Montagem do bot em passos:

#   1 - Irá receber as noticias por meio de uma api flask
#    2 - Todos os links serão enviados para o programa que irá salvar na tabela "links_not_publicated" 
#    3 - O bot terá 2 horários programadas para realizar as publicações, sendo elas: 

#        10:00 - Manhã
#        15:00 - Tarde

#    4 - Após dar o horário o bot irá realizar a conexão com o banco, requisitar a noticia, fazer a extração de informações do link e enviar para um array temporário
#    5 - Logo após será realizada as verificações de horário e enviar se for válida a condição irá realizar a publicação por meio de um token de acesso com o facebook developers
#    6 - Se a publicação for realizada com sucesso, será gravada uma mensagem no arquivo de "access.log" e em uma tabela especifica do banco.