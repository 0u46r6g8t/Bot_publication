
# Importando os modulos / Bot
import json
from src.classBot import Bot 
from googlesearch import search

bot = Bot()

return_data = bot.extract_info(' ')
#https://www.theenemy.com.br/pc/respawn-nova-ip-titanfall-apex-legends
#https://g1.globo.com/pop-arte/games/noticia/2020/12/28/a-misteriosa-morte-de-bilionario-chines-dono-de-gigante-dos-games.ghtml
print(return_data)