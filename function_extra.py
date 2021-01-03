from src.classBot import Bot 
import time, sys

def receive_hours(bot):
    date = bot.return_hours().split(" ")

    return date

def verify_hours(bot):
    
    hour = receive_hours(bot)
    hour = hour[1]
    if(hour == "10:00" or hour == "20:00"):
        return True
    else:
        return False

def sleep_pause():

    for i in range(0,60):
        time.sleep(1)

def banner(bot):

    print("""
    
            \tPublicações do dia """ + str(receive_hours(bot)[0]) + """
    

         \033[1;33m Todos os registros do dia serão exibidos aqui\033[1;31m.
    
    """)

def message_bot(bot):

    data = bot.getMessage()

    for value in data:

        if(value['status'] == 2):
           print("     \033[0;0m[\033[1;32m!\033[0;0m] -> {0}".format(value['message']))
        else:
            print("    [\033[1;31m!\033[0;0m] -> {0}".format(value['message']))
