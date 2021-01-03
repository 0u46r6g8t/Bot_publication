# -*- coding: utf-8 -*-
# Importando os modulos / Bot

from src.classBot import Bot 
from function_extra import receive_hours, verify_hours, sleep_pause, banner
import time, sys

bot = Bot()

if __name__ == '__main__':    
    bot.bot_clear()
    try:
        banner(bot)

        print("\n\n\t\033[1;33mLogs do bot\033[1;31m:\033[0;0m\n\n")
        while 1:
            
            if( verify_hours(bot) == False):
                sleep_pause()
                
            else:

                data = bot.get_data("publication_not_published")

                if(len(data) > 0):    
                    bot.setData(data[0][1], data[0][2])
                    
                    bot.delete_publications(data[0][0])
    
                bot.publication()

                bot.success_connection_mysql()
                
            bot.getMessage()
            
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