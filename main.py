# -*- coding: utf-8 -*-
# Importando os modulos / Bot

from src.classBot import Bot 

bot = Bot()

def receive_hours():
    date = bot.return_hours().split(" ")

    return date

def verify_hours():

    hour = receive_hours()

    hour = hour[1]
    
    if(hour):
        return True
    else:
        return False

def main():

    print("""
    
            \tPublicações do dia """ + str(receive_hours()[0]) + """
    

        \033[1;31m[\033[1;33m!\033[1;31m] \033[1;33m Todos os registros do dia serão exibidos aqui\033[1;31m.
    """)

'''while 1:
        try:
            bot.bot_clear()
            print("\n\n\t\t\t\033[1;31m[\033[1;33m!\033[1;31m] \033[1;33mPrograma está em fase de desenvolvimento ainda, por favor aguarde até o lançamento final do produto\033[1;31m!")

            time.sleep(0.5)
        except KeyboardInterrupt: 
            print("\n\t\t\tObrigado por utilizar os nossos serviços \n")
            break
        except Exception as error:

            print("Erro found: {error}")

        finally:
            print("\033[0;00m") # Remove a formatação imposta no script do bot
'''        



if __name__ == '__main__':
    main()

#bot.extract_info('https://www.tecmundo.com.br/voxel/208761-solitairica-gratis-epic-games-store.htm')
#https://www.theenemy.com.br/pc/respawn-nova-ip-titanfall-apex-legends
#https://g1.globo.com/pop-arte/games/noticia/2020/12/28/a-misteriosa-morte-de-bilionario-chines-dono-de-gigante-dos-games.ghtml
'''

    Montagem do bot em passos:

        1 - Irá receber as noticias por meio de uma api flask
        2 - Todos os links serão enviados para o programa que irá salvar na tabela "links_not_publicated" 
        3 - O bot terá 2 horários programadas para realizar as publicações, sendo elas: 

            10:00 - Manhã
            15:00 - Tarde

        4 - Após dar o horário o bot irá realizar a conexão com o banco, requisitar a noticia, fazer a extração de informações do link e enviar para um array temporário
        5 - Logo após será realizada as verificações de horário e enviar se for válida a condição irá realizar a publicação por meio de um token de acesso com o facebook developers
        6 - Se a publicação for realizada com sucesso, será gravada uma mensagem no arquivo de "access.log" e em uma tabela especifica do banco.
        
'''