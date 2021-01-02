# Montagem do bot em passos:

1. Irá receber as noticias por meio de uma api flask
2. Todos os links serão enviados para o programa que irá salvar na tabela "links_not_publicated" 
3. O bot terá 2 horários programadas para realizar as publicações, sendo elas: 

> 10:00 - Manhã.··
> 15:00 - Tarde.

4. Após dar o horário o bot irá realizar a conexão com o banco, requisitar a noticia, fazer a extração de informações do link e enviar para um array temporário.

5. Logo após será realizada as verificações de horário e enviar se for válida a condição irá realizar a publicação por meio de um token de acesso com o facebook developers.

6. Se a publicação for realizada com sucesso, será gravada uma mensagem no arquivo de "access.log" e em uma tabela especifica do banco.