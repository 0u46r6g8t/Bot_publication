# -*- coding: utf-8 -*-
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

        self.data = ""
        self.message = []
        self.page = '908493739185235'
        self.token = ''
        self.connection = mysql.connector.connect(host='localhost', user='root', password='Leontechh@15', database='bot_python') 

    # Reponsável por retornar a data e hora
    def return_hours(self):
        try:
            dateNow = datetime.now()
            
            dateNow = dateNow.strftime("%d/%m/%Y %H:%M:%S")

            return dateNow

        # Cases de erros
        except Exception as error:

            self.setMessage("Erro ao retornar a hora",0)


    # Criando apenas para limpar a tela
    def bot_clear(self):
        
        try:
            system = pl.system()

            if(system == 'Windows'):

                os.system('cls')

            else:

                os.system('clear')
                
        except Exception as error:

            self.setMessage("Erro ao limpar a tela, não foi possível identificar o sistema a ser utilizado", 0)

    # Responsável por organizar o receber as publicações antes de serem publicadas
    def publication_waiting(self):

        try:
        
            sql = self.connection.cursor()
            sql.charset = "utf8"
            dateNow = self.return_hours()
            
            query = "INSERT INTO publication_not_published( news, link, created_time ) VALUES ( %s, %s, now() )"
            
            values = (self.data['title'], self.data['link'])
            
            sql.execute(query, values)

            self.connection.commit()
            
            sql.close()

            self.setMessage("A noticia foi adicionada a lista de espera com sucesso.", 2)
        # Segundo caso, outro erro desconhecido surja no meio da execução
        except Exception as error:
            
            self.setMessage(error, 3)

    def get_data(self, table = "publication"):
        
        try: 
    
            sql = self.connection.cursor()
            
            query = "SELECT id, news, link from {0}".format(table)

            sql.execute(query)

            self.data = sql.fetchall()
            
            if(len(self.data) > 0):
                self.setMessage("Dados encontrados na lista: '{0}' e retornados para o cliente.".format(table), 2)
            else:
                self.setMessage("Não foram encontrados dados na lista de espera: '{0}'.".format(table), 0)

            sql.close()
            
            return self.data

        # Segundo caso, outro erro desconhecido surja no meio da execução
        except Exception as error:
            
            self.setMessage(error, 3)

    # Função responsável por deletar os itens das tabelas
    def delete_publications(self, id):
        try: 
            if(id > 0):
                sql = self.connection.cursor()

                query = "DELETE FROM publication_not_published where id = ( {0} )".format(id)

                sql.execute(query)
                
                self.connection.commit()

                sql.close()

                self.setMessage("Dado removido com sucesso da lista de espera.", 2)
            else:
                self.setMessage("Não foi identificado nenhum dado na lista de espera.", 3)

        # Segundo caso, outro erro desconhecido surja no meio da execução
        except Exception as error:
                
            self.setMessage(error, 3)
            
    # É a função responsável por enviar os dados para a tabela
    def success_connection_mysql(self):
        try:

            sql = self.connection.cursor() 
            sql.charset = "utf8"
            dateNow = self.return_hours() 
    
            query = "INSERT INTO publication (news, link, id_publication, created_time ) VALUES ( '{0}', '{1}', '{2}', now() )".format(self.data['title'], self.data['link'], self.data['id'])

            sql.execute(query)

            self.connection.commit()

            sql.close()

            self.setMessage("A noticia foi adicionada com sucesso a lista de noticias publicadas", 2)
        # Segundo caso, outro erro desconhecido surja no meio da execução
        except Exception as error:
            
            self.setMessage(error, 3)
    # Função responsável por reaizar a publicação atráves do token de acesso com o facebook developed

    def publication(self):
        try:        
            if((self.data['title'] and self.data['link']) != ""):

                graph = facebook.GraphAPI(self.token)
                messageReturn = graph.put_object(parent_object=self.page, connection_name='feed', message=self.data['title'], link=self.data['link'])
                
                print(messageReturn)
                self.link = self.data['link']

                self.data['id'] = messageReturn['id']

                self.message("Postagem realizada com sucesso", 2)
                
        # Segundo caso, outro erro desconhecido surja no meio da execução
        except Exception as error:
            
            self.setMessage(error, 1)

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
                        
                self.data = info_extrated

                #self.publication(info_extrated)
                self.setMessage("As informações foram extraidas com sucesso da url.", 2)

            else:

                self.setMessage("Not url found", 0)

        # Casos em que o bot irá retornar um erro para o código MAIN

        # Primeiro caso: Caso seja interrompido no meio do processo
        except KeyboardInterrupt:

            self.message('You stoped this program', 3)

        # Segundo caso, outro erro desconhecido surja no meio da execução
        except Exception as error:
            
            self.setMessage(error, 3)

    def getMessage(self):
        
        data = self.message
        
        for value in data:
            
            if(value['status'] == 2):
                print(" \033[0;0m* [\033[1;32m{0}\033[0;0m] -> {1}".format(value['status'], value['message']))
            else:
                print(" * [\033[1;31m{0}\033[0;0m] -> {1}".format(value['status'], value['message']))

        self.message = []

    def setMessage(self, message, status):
        
        data = {
            "message": message,
            "status": status
        }

        self.message.append(data)

    # Códigos de message
    #
    #  0 - erro de funções básicas 
    #  1 - Erro de api
    #  2 - Mensagens de successo
    #  3 - Erro no servidor mysql

    def setData(self, message, link):

        self.data = {
            'title': message,
            'link': link
        }

        self.setMessage('Dado setados para a váriavel responsável pela publicação pela API e inserção no DataBase. ', 2)
