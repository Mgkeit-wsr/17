import telebot

token='5113124651:AAFwke0IXKpOlMVHKLA3GNLWdDjwYfXRtB4'
bot=telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,'Выбирете проф. предмет?')
    bot.send_message(message.chat.id,'(Профильная математика,физика,химия)')

@bot.message_handler(content_types=["text"])
def inst(message):
    if message.text == 'Профильная Математика' or message.text == 'Профильная математика' or message.text == 'профильная математика' or message.text == 'профильная Математика':
        bot.send_message(message.chat.id,'Специальности:')
        bot.send_message(message.chat.id,'Экономика(нужно дополнительно - обществознание,русский)')
        bot.send_message(message.chat.id,'Прикладная информатика(дополнительно нужно - информатика)')
        bot.send_message(message.chat.id,'Напишите вашу специальность')
    if message.text=='экономика' or message.text=='Экономика':
            bot.send_message(message.chat.id,'Инженерно-экономический институт НИУ «МЭИ»')
            bot.send_message(message.chat.id,'Средний проходной балл - 76.7')
            bot.send_message(message.chat.id,'бюджетные места- 448 (на весь ВУЗ)')
            bot.send_message(message.chat.id,'https://www.inei.mpei.ru/')

            bot.send_message(message.chat.id,'Российский государственный аграрный университет - МСХА имени К.А. Тимирязева')
            bot.send_message(message.chat.id,'Средний проходной балл - 63.1')
            bot.send_message(message.chat.id,'бюджетные места- 3055 (на весь ВУЗ)')
            bot.send_message(message.chat.id,'https://www.timacad.ru/?/&ysclid=l1ypbxoulq')

            bot.send_message(message.chat.id,'Национальный исследовательский университет «Высшая школа экономики» (НИУ ВШЭ)')
            bot.send_message(message.chat.id,'Средний проходной балл - 72')
            bot.send_message(message.chat.id,'бюджетные мест- 2055 (на весь ВУЗ)')
            bot.send_message(message.chat.id,'https://www.hse.ru')
    if message.text=='прикладная информатика'  or message.text=='Прикладная информатика': 
            bot.send_message(message.chat.id,'Ордена Трудового Красного Знамени федеральное государственное бюджетное образовательное учреждение высшего образования Московский технический университет связи и информатики')
            bot.send_message(message.chat.id,'проходной балл - 176')
            bot.send_message(message.chat.id,'бюджетные мест- 1192 (на весь ВУЗ)')
            bot.send_message(message.chat.id,'https://mtuci.ru/?ysclid=l1yu6pn3er')
            
            bot.send_message(message.chat.id,'Российский новый университет (РосНОУ)')
            bot.send_message(message.chat.id,'проходной балл - 185')
            bot.send_message(message.chat.id,'бюджетные мест- 65 (на весь ВУЗ)')
            bot.send_message(message.chat.id,'https://rosnou.ru/?ysclid=l1yu9kmb6j')

            bot.send_message(message.chat.id,'Московский государственный технический университет им. Н.Э. Баумана')
            bot.send_message(message.chat.id,'Средний проходной балл - 79.9')
            bot.send_message(message.chat.id,'бюджетные мест- 8848 (на весь ВУЗ)')
            bot.send_message(message.chat.id,'https://bmstu.ru/')
                
    if message.text == 'Физика' or message.text == 'физика':
        bot.send_message(message.chat.id,'Специальности:')
        bot.send_message(message.chat.id,'Физик-инженер ')
        bot.send_message(message.chat.id,'Физик-ядерщик ')
        bot.send_message(message.chat.id,'Физик-материаловед ')
        bot.send_message(message.chat.id,'Напишите вашу специальность')
    if message.text=='Физик-инженер' or message.text=='физик-инженер':

            bot.send_message(message.chat.id,'Московский политехнический университет')
            bot.send_message(message.chat.id,'Средний проходной балл -73.4')
            bot.send_message(message.chat.id,'бюджетные мест- 2 483 (на весь ВУЗ)')
            bot.send_message(message.chat.id,'https://mospolytech.ru/')

            bot.send_message(message.chat.id,'Московский государственный технический университет им. Н.Э. Баумана')
            bot.send_message(message.chat.id,'Средний проходной балл - 79.9')
            bot.send_message(message.chat.id,'бюджетные мест- 8848 (на весь ВУЗ)')
            bot.send_message(message.chat.id,'https://bmstu.ru/')

            bot.send_message(message.chat.id,'Национальный исследовательский университет "МЭИ"')
            bot.send_message(message.chat.id,'Средний проходной балл - ')
            bot.send_message(message.chat.id,'бюджетные мест-2678  (на весь ВУЗ)')
            bot.send_message(message.chat.id,'https://mpei.ru/?ysclid=l1ysoj361v')

    if message.text=='Физик-ядерщик' or message.text=='физик-ядерщик':

            bot.send_message(message.chat.id,'Национальный исследовательский ядерный университет «МИФИ»')
            bot.send_message(message.chat.id,'проходной балл - 274')
            bot.send_message(message.chat.id,'бюджетные мест- 840 (на весь ВУЗ)')
            bot.send_message(message.chat.id,'https://mephi.ru/?ysclid=l1yprkj0vp')

            bot.send_message(message.chat.id,'Инженерно-экономический институт НИУ «МЭИ»')
            bot.send_message(message.chat.id,'Средний проходной балл - 76.7')
            bot.send_message(message.chat.id,'бюджетные места- 448 (на весь ВУЗ)')
            bot.send_message(message.chat.id,'https://www.inei.mpei.ru/')

            bot.send_message(message.chat.id,'Московский государственный технический университет им. Н.Э. Баумана')
            bot.send_message(message.chat.id,'Средний проходной балл - 79.9')
            bot.send_message(message.chat.id,'бюджетные мест- 8848 (на весь ВУЗ)')
            bot.send_message(message.chat.id,'https://bmstu.ru/')

    if message.text=='Физик-материаловед' or message.text=='физик-материаловед':

            bot.send_message(message.chat.id,'Национальный исследовательский технологический университет МИСиС ')
            bot.send_message(message.chat.id,'Средний проходной балл - 83 ')
            bot.send_message(message.chat.id,'бюджетные мест- 832 (на весь ВУЗ)')
            bot.send_message(message.chat.id,'https://misis.ru/')
            
            bot.send_message(message.chat.id,'МГУ им. М. В. Ломоносова, факультет наук о материалах')
            bot.send_message(message.chat.id,'проходной балл - 201')
            bot.send_message(message.chat.id,'бюджетные мест- 4005 (на весь ВУЗ)')
            bot.send_message(message.chat.id,'http://www.fnm.msu.ru/')

            bot.send_message(message.chat.id,'Московский физико-технический институт')
            bot.send_message(message.chat.id,'Средний проходной балл - 96.9')
            bot.send_message(message.chat.id,'бюджетные мест- 1044 (на весь ВУЗ)')
            bot.send_message(message.chat.id,'https://mipt.ru/?ysclid=l1ytp922ra')



    if message.text == 'Химия' or message.text == 'химия':
        bot.send_message(message.chat.id,'Специальности:')
        bot.send_message(message.chat.id,'Химик-материаловед')
        bot.send_message(message.chat.id,'Медицина')
        bot.send_message(message.chat.id,'Химик-биотехнолог.')

        bot.send_message(message.chat.id,'ВУЗы-')

        bot.send_message(message.chat.id,'МИРЭА — Российский технологический университет')
        bot.send_message(message.chat.id,'Средний проходной балл - 78.1')
        bot.send_message(message.chat.id,'бюджетные мест- 3 868 (на весь ВУЗ)')
        bot.send_message(message.chat.id,'https://www.mirea.ru/')

        bot.send_message(message.chat.id,'Российский химико-технологический университет имени Д.И. Менделеева')
        bot.send_message(message.chat.id,'Средний проходной балл -73.1 ')
        bot.send_message(message.chat.id,'бюджетные мест- 5 202 (на весь ВУЗ)')
        bot.send_message(message.chat.id,'https://www.muctr.ru/?ysclid=l1ysxj3bte')

        bot.send_message(message.chat.id,'Российский национальный исследовательский медицинский университет имени Н.И. Пирогова')
        bot.send_message(message.chat.id,'Средний проходной балл - 85.6 ')
        bot.send_message(message.chat.id,'бюджетные мест- 1 663 (на весь ВУЗ)')
        bot.send_message(message.chat.id,'https://rsmu.ru/')
        
bot.infinity_polling()
