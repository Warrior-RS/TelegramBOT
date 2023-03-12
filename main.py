import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CallbackContext, CommandHandler, CallbackQueryHandler, ContextTypes

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)




async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Создаем клавиатуру
    keyboard = [
        [InlineKeyboardButton("Мобильные Операторы", callback_data='option1')],
        [InlineKeyboardButton("Поиск жилья", callback_data='option2')],
        [InlineKeyboardButton("Поиск работы", callback_data='option3')],
        [InlineKeyboardButton("Транспорт", callback_data='option4')],
        [InlineKeyboardButton("Доставка еды", callback_data='option5')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Отправляем сообщение с клавиатурой
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Please choose an option:",
                                   reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()


    if query.data == 'option1':
        # Создаем клавиатуру для опции 1
        keyboard = [
            [InlineKeyboardButton("T-mobile", url='https://www.t-mobile.com')],
            [InlineKeyboardButton("Orange", url='https://www.orange.pl')],
            [InlineKeyboardButton("Plus", url='https://www.plus.pl')],
            [InlineKeyboardButton("Virgin Mobile", url='https://virginmobile.pl')],
            [InlineKeyboardButton("Play", url='https://www.play.pl')],
            [InlineKeyboardButton("Lyca Mobile", url='https://www.lycamobile.pl')],
            [InlineKeyboardButton("Back", callback_data='back')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        # Редактируем сообщение с новой клавиатурой
        await query.edit_message_text(text="You chose Мобильные операторы. Please choose a suboption:",
                                      reply_markup=reply_markup)

    elif query.data == 'option2':
        # Создаем клавиатуру для опции 2
        keyboard = [
            [InlineKeyboardButton("OLX.pl", url='https://www.olx.pl/d/nieruchomosci/')],
            [InlineKeyboardButton("Otodom.pl", url='https://www.otodom.pl')],
            [InlineKeyboardButton("Gratka.pl", url='https://gratka.pl/nieruchomosci')],
            [InlineKeyboardButton("Domiporta.pl", url='https://www.domiporta.pl')],
            [InlineKeyboardButton("Oferty.pl", url='https://www.oferty.net/mieszkania/')],
            [InlineKeyboardButton("Flagma.pl", url='https://flagma.pl/ru/products/nedvizhimost/')],
            [InlineKeyboardButton("Domy.pl", url='https://domy.pl')],
            [InlineKeyboardButton("Lento.pl", url='www.lento.pl/nieruchomosci')],
            [InlineKeyboardButton("Morizon.pl", url='https://www.morizon.pl')],
            [InlineKeyboardButton("GetHome.pl", url='https://gethome.pl')],
            [InlineKeyboardButton("Okolica.pl", url='https://www.okolica.pl/')],
            [InlineKeyboardButton("Back", callback_data='back')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        # Редактируем сообщение с новой клавиатурой
        await query.edit_message_text(text="You chose Option 2. Please choose a suboption:", reply_markup=reply_markup)


    elif query.data == 'option3':
        # Создаем клавиатуру для опции 3
        keyboard = [
            [InlineKeyboardButton("Pracuj.pl", url='https://www.pracuj.pl/praca')],
            [InlineKeyboardButton("Flagma.pl", url='https://flagma.pl/ru/vacancies/')],
            [InlineKeyboardButton("Praca.pl", url='https://www.praca.pl')],
            [InlineKeyboardButton("Jobs.pl", url='https://www.jobs.pl/praca')],
            [InlineKeyboardButton("InfoPraca.pl", url='https://www.infopraca.pl')],
            [InlineKeyboardButton("OLX.pl", url='https://www.olx.pl/d/praca/')],
            [InlineKeyboardButton("E-Delo.pl", url='https://e-delo.pl')],
            [InlineKeyboardButton("PolandPraca-UA.com", url='http://polandpraca-ua.com')],
            [InlineKeyboardButton("LayBoard.com", url='https://layboard.com/vakansii/rabota-v-polshe')],
            [InlineKeyboardButton("JobRapido", url='https://pl.jobrapido.com/')],
            [InlineKeyboardButton("Back", callback_data='back')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        # Редактируем сообщение с новой клавиатурой
        await query.edit_message_text(text="You chose. Please choose a suboption:", reply_markup=reply_markup)

    elif query.data == 'option4':
        # Создаем клавиатуру для опции 4
        keyboard = [
            [InlineKeyboardButton("Общественный транспорт", url='https://jakdojade.pl/', callback_data='jakdojade')],
            [InlineKeyboardButton("Поезда", callback_data='train')],
            [InlineKeyboardButton("Такси Online", callback_data='taxi')],
            [InlineKeyboardButton("Back", callback_data='back')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        # Редактируем сообщение с новой клавиатурой
        await query.edit_message_text(text="You chose Option 4. Please choose a suboption:", reply_markup=reply_markup)
    elif query.data == 'train':
        # Создаем клавиатуру для train
        keyboard = [
            [InlineKeyboardButton("PKP.pl", url='https://www.pkp.pl/pl/')],
            [InlineKeyboardButton("Intercity.pl", url='https://www.intercity.pl/')],
            [InlineKeyboardButton("PolRail", url='https://www.polrail.com/ru')],
            [InlineKeyboardButton("Koleo.pl", url='https://koleo.pl/ru/')],
            [InlineKeyboardButton("Back", callback_data='option4')]
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        # Редактируем сообщение с новой клавиатурой
        await query.edit_message_text(text="You chose Suboption 88. Please choose a train:", reply_markup=reply_markup)

    elif query.data == 'taxi':
        # Создаем клавиатуру для taxi
        keyboard = [
            [InlineKeyboardButton("ITaxi.pl", url='https://itaxi.pl/pobierz/')],
            [InlineKeyboardButton("EleTaxi.pl", url='https://aplikacja.eletaxi.pl')],
            [InlineKeyboardButton("Free-Now.com", url='https://www.free-now.com/pl/download-app-qr-code')],
            [InlineKeyboardButton("Uber", url='https://www.uber.com/pl/ru/')],
            [InlineKeyboardButton("Bolt", url='https://bolt.eu')],
            [InlineKeyboardButton("Back", callback_data='option4')]
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        # Редактируем сообщение с новой клавиатурой
        await query.edit_message_text(text="You chose Suboption 88. Please choose a train:", reply_markup=reply_markup)


    elif query.data == 'option5':
        # Создаем клавиатуру для опции 5
        keyboard = [
            [InlineKeyboardButton("Доставка из супермаркетов", url='https://pl.everli.com')],
            [InlineKeyboardButton("Lisek", url='https://sklep.lisek.app')],
            [InlineKeyboardButton("Allegro.pl", url='https://allegro.pl')],
            [InlineKeyboardButton("Inpost Fresh", url='https://inpostfresh.pl')],
            [InlineKeyboardButton("Доставка еды из ресторанов", callback_data='restoran')],
            [InlineKeyboardButton("Back", callback_data='back')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        # Редактируем сообщение с новой клавиатурой
        await query.edit_message_text(text="You chose. Please choose a suboption:", reply_markup=reply_markup)

    elif query.data == 'restoran':
        # Создаем клавиатуру для restoran
        keyboard = [

            [InlineKeyboardButton("Pyszne (Android)",
                            url='https://play.google.com/store/apps/details?id=com.yourdelivery.pyszne&hl=en&gl=US')],
            [InlineKeyboardButton("Pyszne (iOS)",
                                  url='https://apps.apple.com/us/app/pyszne-pl/id1039818673')],
            [InlineKeyboardButton("Glovo (Androind)",
                                  url='https://play.google.com/store/apps/details?id=com.glovo&hl=en&gl=US')],
            [InlineKeyboardButton("Glovo (iOS)",
                                  url='https://apps.apple.com/us/app/glovo-more-than-food-delivery/id951812684')],
            [InlineKeyboardButton("Uber Eats (Android)",
                                  url='https://play.google.com/store/apps/details?id=com.ubercab.eats&hl=en&gl=US')],
            [InlineKeyboardButton("Uber Eats (iOS)",
                                  url='https://apps.apple.com/us/app/uber-eats-food-delivery/id1058959277')],
            [InlineKeyboardButton("Bolt Food (Android)",
                            url='https://play.google.com/store/apps/details?id=com.bolt.deliveryclient&hl=en&gl=US')],
            [InlineKeyboardButton("Bolt Food (iOS)",
                                  url='https://apps.apple.com/us/app/bolt-food/id1451492388')],
            [InlineKeyboardButton("Wolt Delivery (Android)",
                                  url='https://play.google.com/store/apps/details?id=com.wolt.android&hl=en&gl=US')],
            [InlineKeyboardButton("Wolt Delivery (iOS)",
                                  url='https://apps.apple.com/us/app/wolt-delivery-food-and-more/id943905271')],


            [InlineKeyboardButton("Back", callback_data='option5')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        # Редактируем сообщение с новой клавиатурой
        await query.edit_message_text(text="You chose. Please choose a suboption:", reply_markup=reply_markup)



    elif query.data == 'back':
        # Создаем клавиатуру главного меню
        keyboard = [
            [InlineKeyboardButton("Мобильные Операторы", callback_data='option1')],
            [InlineKeyboardButton("Поиск жилья", callback_data='option2')],
            [InlineKeyboardButton("Поиск работы", callback_data='option3')],
            [InlineKeyboardButton("Транспорт", callback_data='option4')],
            [InlineKeyboardButton("Доставка еды", callback_data='option5')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        # Редактируем сообщение с главным меню
        await query.edit_message_text(text="Please choose an option:", reply_markup=reply_markup)




if __name__ == '__main__':
    application = ApplicationBuilder().token('5967895265:AAHbAcrpglNi3-vY0j7zet0pRVxwyen5ZnU').build()

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    button_handler = CallbackQueryHandler(button)
    application.add_handler(button_handler)



    application.run_polling()

