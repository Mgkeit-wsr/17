import telebot

token='5113124651:AAFwke0IXKpOlMVHKLA3GNLWdDjwYfXRtB4'
bot=telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,'�������� ����. �������?')
    bot.send_message(message.chat.id,'(���������� ����������,������,�����)')

@bot.message_handler(content_types=["text"])
def inst(message):
    if message.text == '���������� ����������' or message.text == '���������� ����������' or message.text == '���������� ����������' or message.text == '���������� ����������':
        bot.send_message(message.chat.id,'�������������:')
        bot.send_message(message.chat.id,'���������(����� ������������� - ��������������,�������)')
        bot.send_message(message.chat.id,'���������� �����������(������������� ����� - �����������)')
        bot.send_message(message.chat.id,'�������� ���� �������������')
    if message.text=='���������' or message.text=='���������':
            bot.send_message(message.chat.id,'���������-������������� �������� ��� ���Ȼ')
            bot.send_message(message.chat.id,'������� ��������� ���� - 76.7')
            bot.send_message(message.chat.id,'��������� �����- 448 (�� ���� ���)')
            bot.send_message(message.chat.id,'https://www.inei.mpei.ru/')

            bot.send_message(message.chat.id,'���������� ��������������� �������� ����������� - ���� ����� �.�. ����������')
            bot.send_message(message.chat.id,'������� ��������� ���� - 63.1')
            bot.send_message(message.chat.id,'��������� �����- 3055 (�� ���� ���)')
            bot.send_message(message.chat.id,'https://www.timacad.ru/?/&ysclid=l1ypbxoulq')

            bot.send_message(message.chat.id,'������������ ����������������� ����������� ������� ����� ��������� (��� ���)')
            bot.send_message(message.chat.id,'������� ��������� ���� - 72')
            bot.send_message(message.chat.id,'��������� ����- 2055 (�� ���� ���)')
            bot.send_message(message.chat.id,'https://www.hse.ru')
    if message.text=='���������� �����������'  or message.text=='���������� �����������': 
            bot.send_message(message.chat.id,'������ ��������� �������� ������� ����������� ��������������� ��������� ��������������� ���������� ������� ����������� ���������� ����������� ����������� ����� � �����������')
            bot.send_message(message.chat.id,'��������� ���� - 176')
            bot.send_message(message.chat.id,'��������� ����- 1192 (�� ���� ���)')
            bot.send_message(message.chat.id,'https://mtuci.ru/?ysclid=l1yu6pn3er')
            
            bot.send_message(message.chat.id,'���������� ����� ����������� (������)')
            bot.send_message(message.chat.id,'��������� ���� - 185')
            bot.send_message(message.chat.id,'��������� ����- 65 (�� ���� ���)')
            bot.send_message(message.chat.id,'https://rosnou.ru/?ysclid=l1yu9kmb6j')

            bot.send_message(message.chat.id,'���������� ��������������� ����������� ����������� ��. �.�. �������')
            bot.send_message(message.chat.id,'������� ��������� ���� - 79.9')
            bot.send_message(message.chat.id,'��������� ����- 8848 (�� ���� ���)')
            bot.send_message(message.chat.id,'https://bmstu.ru/')
                
    if message.text == '������' or message.text == '������':
        bot.send_message(message.chat.id,'�������������:')
        bot.send_message(message.chat.id,'�����-������� ')
        bot.send_message(message.chat.id,'�����-������� ')
        bot.send_message(message.chat.id,'�����-������������ ')
        bot.send_message(message.chat.id,'�������� ���� �������������')
    if message.text=='�����-�������' or message.text=='�����-�������':

            bot.send_message(message.chat.id,'���������� ��������������� �����������')
            bot.send_message(message.chat.id,'������� ��������� ���� -73.4')
            bot.send_message(message.chat.id,'��������� ����- 2 483 (�� ���� ���)')
            bot.send_message(message.chat.id,'https://mospolytech.ru/')

            bot.send_message(message.chat.id,'���������� ��������������� ����������� ����������� ��. �.�. �������')
            bot.send_message(message.chat.id,'������� ��������� ���� - 79.9')
            bot.send_message(message.chat.id,'��������� ����- 8848 (�� ���� ���)')
            bot.send_message(message.chat.id,'https://bmstu.ru/')

            bot.send_message(message.chat.id,'������������ ����������������� ����������� "���"')
            bot.send_message(message.chat.id,'������� ��������� ���� - ')
            bot.send_message(message.chat.id,'��������� ����-2678  (�� ���� ���)')
            bot.send_message(message.chat.id,'https://mpei.ru/?ysclid=l1ysoj361v')

    if message.text=='�����-�������' or message.text=='�����-�������':

            bot.send_message(message.chat.id,'������������ ����������������� ������� ����������� ����Ȼ')
            bot.send_message(message.chat.id,'��������� ���� - 274')
            bot.send_message(message.chat.id,'��������� ����- 840 (�� ���� ���)')
            bot.send_message(message.chat.id,'https://mephi.ru/?ysclid=l1yprkj0vp')

            bot.send_message(message.chat.id,'���������-������������� �������� ��� ���Ȼ')
            bot.send_message(message.chat.id,'������� ��������� ���� - 76.7')
            bot.send_message(message.chat.id,'��������� �����- 448 (�� ���� ���)')
            bot.send_message(message.chat.id,'https://www.inei.mpei.ru/')

            bot.send_message(message.chat.id,'���������� ��������������� ����������� ����������� ��. �.�. �������')
            bot.send_message(message.chat.id,'������� ��������� ���� - 79.9')
            bot.send_message(message.chat.id,'��������� ����- 8848 (�� ���� ���)')
            bot.send_message(message.chat.id,'https://bmstu.ru/')

    if message.text=='�����-������������' or message.text=='�����-������������':

            bot.send_message(message.chat.id,'������������ ����������������� ��������������� ����������� ����� ')
            bot.send_message(message.chat.id,'������� ��������� ���� - 83 ')
            bot.send_message(message.chat.id,'��������� ����- 832 (�� ���� ���)')
            bot.send_message(message.chat.id,'https://misis.ru/')
            
            bot.send_message(message.chat.id,'��� ��. �. �. ����������, ��������� ���� � ����������')
            bot.send_message(message.chat.id,'��������� ���� - 201')
            bot.send_message(message.chat.id,'��������� ����- 4005 (�� ���� ���)')
            bot.send_message(message.chat.id,'http://www.fnm.msu.ru/')

            bot.send_message(message.chat.id,'���������� ������-����������� ��������')
            bot.send_message(message.chat.id,'������� ��������� ���� - 96.9')
            bot.send_message(message.chat.id,'��������� ����- 1044 (�� ���� ���)')
            bot.send_message(message.chat.id,'https://mipt.ru/?ysclid=l1ytp922ra')



    if message.text == '�����' or message.text == '�����':
        bot.send_message(message.chat.id,'�������������:')
        bot.send_message(message.chat.id,'�����-������������')
        bot.send_message(message.chat.id,'��������')
        bot.send_message(message.chat.id,'�����-�����������.')

        bot.send_message(message.chat.id,'����-')

        bot.send_message(message.chat.id,'����� � ���������� ��������������� �����������')
        bot.send_message(message.chat.id,'������� ��������� ���� - 78.1')
        bot.send_message(message.chat.id,'��������� ����- 3 868 (�� ���� ���)')
        bot.send_message(message.chat.id,'https://www.mirea.ru/')

        bot.send_message(message.chat.id,'���������� ������-��������������� ����������� ����� �.�. ����������')
        bot.send_message(message.chat.id,'������� ��������� ���� -73.1 ')
        bot.send_message(message.chat.id,'��������� ����- 5 202 (�� ���� ���)')
        bot.send_message(message.chat.id,'https://www.muctr.ru/?ysclid=l1ysxj3bte')

        bot.send_message(message.chat.id,'���������� ������������ ����������������� ����������� ����������� ����� �.�. ��������')
        bot.send_message(message.chat.id,'������� ��������� ���� - 85.6 ')
        bot.send_message(message.chat.id,'��������� ����- 1 663 (�� ���� ���)')
        bot.send_message(message.chat.id,'https://rsmu.ru/')
        
bot.infinity_polling()
