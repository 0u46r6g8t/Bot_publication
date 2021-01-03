from src.classBot import Bot 
import time, sys

def receive_hours(bot):
    date = bot.return_hours().split(" ")

    return date

def verify_hours(bot):
    
    hour = receive_hours(bot)
    c = 0
    hour = hour[1]
    if(((hour > "13:00:00" and hour < "13:00:10" ) or (hour > "20:00:00" and hour < "20:01:00" )) and (c == 0)):
        c = 1
        return True
    else:
        c = 0
        return False

def sleep_pause():

    for i in range(0,10):
        time.sleep(1)

def banner(bot):

    print("""
    
            \tPublicações do dia """ + str(receive_hours(bot)[0]) + """
    

         \033[1;33m Todos os registros do dia serão exibidos aqui\033[1;31m.    
    """)

