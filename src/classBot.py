##################################################################################################
##################################################################################################
###
###   Name of student: Gustavo Silva
###   University: Universidade Técnologica Federal do Paraná
###   half: 4°
###   Research project: LAMIA - Laboratório de Aprendizado e Imagens aplicados à indústria
###   Campus: Santa Helena
###
##################################################################################################
##################################################################################################

# Importando as libs necessárias 

import facebook # Biblioteca responsável pela comunicação entre o bot utilizando o token
import urllib.request # Utilizada para fazer o request no site
import mysql.connector # Utilizada para conseguir se comunicar e interagir com o banco
from datetime import datetime # Biblioteca Responsável para trabalhar com data/hora/minutos:segundos
from bs4 import BeautifulSoup # Biblioteca para conseguir fazer o web Scraping nos sites solicitados

class Bot():

    info = []
    class_found = ['content-title__content__title', 'content-head__title']

    # Inicia a variaveis para realizar a comunicação com o banco de dados
    def __init__(self):

        self.link = ""
        self.message = message = {}
        self.id = ""
        self.port = 3306
        self.nameDB = 'bot_python'
        self.password = 'Leontechh@15'
        self.host = 'localhost'
        self.page = '908493739185235'
        self.token = 'EAALVbVPZCmzUBAMNr9KhglZBwMxOrkEeY67DYziQw0KlNsH4DRK2fEsEtSHS3Td64bqxUJqOVSj0DmDeGpz9WspDXcEa3nOr6OsbV3KRZBnqE8lq6t3RyFkX80qxoS6OqCGkiZAizhpb6O9ef1sUBESSJZBL7C3QOl31TbbzkgiTOwOVCAnMvall0W71WdAg06agtikx6tgZDZD'
        self.connection = mysql.connector.connect(host='localhost', user='root', password='Leontechh@15', database='bot_python') 

    # É a função responsável por enviar os dados para a tabela
    def success_connection_mysql(self):
        try:

            sql = self.connection.cursor() 

            self.connection.cursor()

            dateNow = datetime.now()
            
            dateNow = dateNow.strftime("%Y-%m-%d %H:%M")
            
            query = "INSERT INTO publication ( news, link, id_publication, created_time ) VALUES ( %s, %s, %s, %s )"
            
            values = (self.link, 'link.com.br', self.id, dateNow)

            sql.execute(query, values)

            self.connection.commit()

        except Exception as error:

            return {
                "messageError": error
            }

    # Função responsável por reaizar a publicação atráves do token de acesso com o facebook developed

    def publication(self, news, localpage):
        
        try:        
            if(news['news'] != ""):
    
                graph = facebook.GraphAPI(self.token)

                messageReturn = graph.put_object(self.page, localpage, message=news['news'])

                self.link = news['news']

                self.id = messageReturn['id']

                self.message = {
                    "id_publication": messageReturn['id'],
                    "MessageSuccess": "Postagem realizada com sucesso"
                }

                return self.message

        except Exception as error:

            self.message = {
                "MessageError": error
            }

            return self.message

    # Responsável por extrair os dados como link, text, etc do link passado
    def extract_info(self, url):

        try:
            # Se a variavel estiver contendo um link e não estiver vázio
            if(url != ' '):

                page = urllib.request.urlopen(url)

                soup = BeautifulSoup(page, 'html5lib')

                for class_item in self.class_found:

                    list_item = soup.find('h1', attrs={'class': class_item})

                    if(list_item != None and list_item != ''):
                        info_extrated = {
                            'link': url,
                            'title': list_item.text.strip()
                        }

                        self.info.append(info_extrated)
                    else:
                        pass
                return self.info
            else:

                self.message = {
                    "MessageError": "Not url found"
                }
                return self.message

        # Casos em que o bot irá retornar um erro para o código MAIN

        # Primeiro caso: Caso seja interrompido no meio do processo
        except KeyboardInterrupt:

            self.message = {
                "MessageError": 'You stoped this program'
            }

            return self.massage

        # Segundo caso, outro erro desconhecido surja no meio da execução
        except Exception as error:
            self.message = {
                "MessageError": error
            }

            return self.message