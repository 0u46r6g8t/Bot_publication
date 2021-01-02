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
import os
import platform as pl
import facebook # Biblioteca responsável pela comunicação entre o bot utilizando o token
import urllib.request # Utilizada para fazer o request no site
import mysql.connector # Utilizada para conseguir se comunicar e interagir com o banco
from datetime import datetime # Biblioteca Responsável para trabalhar com data/hora/minutos:segundos
from bs4 import BeautifulSoup # Biblioteca para conseguir fazer o web Scraping nos sites solicitados

class Bot():

    info = []

    class_found = ['content-title__content__title', 'content-head__title', 'tec--article__header__title']
    class_phrases = []
    # Inicia a variaveis para realizar a comunicação com o banco de dados


    def __init__(self):

        self.message = {}
        self.id = ""
        self.port = 3306
        self.nameDB = 'bot_python'
        self.password = 'Leontechh@15'
        self.host = 'localhost'
        self.page = '908493739185235'
        self.token = 'EAALVbVPZCmzUBAPk3xo2ZCEP1C2b4u2ykismIwOcja1tTFeVzQPhgGkSNQlA7s0kT02rZATWp9ydQ1m89nAtcJdKSiXLXtY0PTawARjFgDUPJkiptObAj8MLWnmrmInQKQjYle8lRGIBAdASlZB5ZAG8GBFt15V7i0ewFqGdpW50dy0gUXURkubsFvNDHAojWZBsOnGYzhmwZDZD'
        self.connection = mysql.connector.connect(host='localhost', user='root', password='Leontechh@15', database='bot_python') 

    def return_hours(self):
        try:
            dateNow = datetime.now()
            
            dateNow = dateNow.strftime("%d/%m/%Y %H:%M")

            return dateNow

        except Exception as error:

            self.message = {
                "MessageError": "Erro ao retornar a hora",
                "error": error
            }

            return self.message

    def bot_clear(self):
        
        try:
            system = pl.system()

            if(system == 'Windows'):

                os.system('cls')

            else:

                os.system('clear')
                
        except Exception as error:

            self.message = {
                "MessageError": "Erro ao limpar a tela, não foi possível identificar o sistema a ser utilizado",
                "error": error
            }    

            return self.message

    # Responsável por organizar o receber as publicações antes de serem publicadas
    def publication_waiting(self, data):

        try:

            sql = self.connection.cursor()
            
            dateNow = self.return_hours()

            query = "INSERT INTO publication_not_published( news, link, created_time ) VALUES ( %s, %s, %s )"
            
            values = (data['title'], data['link'], dateNow)

            sql.execute(query, values)

            self.connection.commit()
            
        except Exception as error:
            
            return {
                "messageError": error
            }


    # Função responsável por deletar os itens das tabelas
    def delete_publications(self, id):
        try: 
    
            sql = self.connection.cursor()

            query = "DELETE FROM publication_not_published where id = ( %s )"

            sql.execute(query, id)

            self.connection.commit()

        except Exception as error:
            
            return {
                "messageError": error
            }
    # É a função responsável por enviar os dados para a tabela
    def success_connection_mysql(self, data):
        try:

            sql = self.connection.cursor() 

            dateNow = self.return_hours() 
    
            query = "INSERT INTO publication ( news, link, id_publication, created_time ) VALUES ( %s, %s, %s, %s )"
            
            values = (data['title'], data['link'], data['id'], dateNow)

            sql.execute(query, values)

            self.connection.commit()

        except Exception as error:

            return {
                "messageError": error
            }

    # Função responsável por reaizar a publicação atráves do token de acesso com o facebook developed

    def publication(self, news):
        try:        
            if((news['title'] and news['link']) != ""):
                
                graph = facebook.GraphAPI(self.token)
                messageReturn = graph.put_object(parent_object=self.page, connection_name='feed', message=news['title'], link=news['link'])
                
                self.link = news['link']

                news['id'] = messageReturn['id']

                self.message = {
                    "id_publication": messageReturn['id'],
                    "MessageSuccess": "Postagem realizada com sucesso"
                }

                self.success_connection_mysql(news)

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
                            'id': "",
                            'link': url,
                            'title': list_item.text.strip()
                        }

                        self.info.append(info_extrated)
                    else:
                        pass
                
                
                self.publication(info_extrated)

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