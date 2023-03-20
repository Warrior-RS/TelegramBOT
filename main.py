import logging, asyncio, os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CallbackContext, CommandHandler, CallbackQueryHandler, ContextTypes
from dotenv import load_dotenv

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
        [InlineKeyboardButton("Доставка еды", callback_data='option5')],
        [InlineKeyboardButton("Скидки и Купоны", callback_data='option6')],
        [InlineKeyboardButton("Польские новостные и справочные порталы", callback_data='option7')],
        [InlineKeyboardButton("Красота и Здоровье", callback_data='option8')],
        [InlineKeyboardButton("Досуг", callback_data='option9')],
        [InlineKeyboardButton("Банки Польши", callback_data='option10')],
        [InlineKeyboardButton("Почта, посылки, пачкоматы", callback_data='option11')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Отправляем сообщение с клавиатурой
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Здесь собраны основные Польские сервисы и приложения, что бы облегчить ваше пребывание и адаптацию в Польше",
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
        await query.edit_message_text(text="Польские Мобильные Операторы",
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
        await query.edit_message_text(text="Список сайтов для поиска жилья:", reply_markup=reply_markup)

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
        await query.edit_message_text(text="Список сайтов для поиска работы", reply_markup=reply_markup)

    elif query.data == 'option4':
        # Создаем клавиатуру для опции 4
        keyboard = [
            [InlineKeyboardButton("JakDojade", url='https://jakdojade.pl/')],
            [InlineKeyboardButton("BusNavi", url='https://play.google.com/store/apps/details?id=pl.mobicore.mobilempk&hl=en_US&gl=US')],
            [InlineKeyboardButton("Поезда", callback_data='train')],
            [InlineKeyboardButton("Такси Online", callback_data='taxi')],
            [InlineKeyboardButton("Back", callback_data='back')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        # Редактируем сообщение с новой клавиатурой
        await query.edit_message_text(text="  JakDojade - Комплексный инструмент для планирования поездок на общественном"
                                           "транспорте. Обязательное для скачивания приложение."
                                           "  BusNavi - это расписание общественного транспорта, планировщик поездок, карта - все, что нужно для поездки на общественном транспорте.\n"
                                           "После установки приложение может работать в автономном режиме и не требует подключения к Интернету.",
                                      reply_markup=reply_markup)

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
        await query.edit_message_text(text="Сервисы по покупке билетов на поезда", reply_markup=reply_markup)

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
        await query.edit_message_text(text="Приложения для  вызова Taxi онлайн", reply_markup=reply_markup)

    elif query.data == 'option5':
        # Создаем клавиатуру для опции 5
        keyboard = [
            [InlineKeyboardButton("Доставка из супермаркетов Everli", url='https://pl.everli.com')],
            [InlineKeyboardButton("Lisek", url='https://sklep.lisek.app')],
            [InlineKeyboardButton("Allegro.pl", url='https://allegro.pl')],
            [InlineKeyboardButton("Inpost Fresh", url='https://inpostfresh.pl')],
            [InlineKeyboardButton("Доставка еды из ресторанов", callback_data='restoran')],
            [InlineKeyboardButton("Back", callback_data='back')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        # Редактируем сообщение с новой клавиатурой
        await query.edit_message_text\
            (text="Сервис Everli работает с: Carrefour, Auchan, Netto, Spar, Lidl, Biedronka.\n"
                  "У сервиса доставки продуктов Lisek, вроде бы есть алкоголь в ассортименте ^_^\n"
                  "Allegro доставляет вообще всё, это что то вроде Aliexpress'a\n"
                  "Inpost - сеть пачкоматов, но еще они занимаются доставкой еды из Marko и Carrefour"
                  "",
             reply_markup=reply_markup)

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
        await query.edit_message_text(text="Ссылки на официальные приложения доставки еды в Польше", reply_markup=reply_markup)

    elif query.data == 'option6':
        # Создаем клавиатуру для опции 6
        keyboard = [
            [InlineKeyboardButton("Газетки и промо-акции", url='https://mojagazetka.com')],
            [InlineKeyboardButton("Купоны фастфуда + скидки в магазинах + cashback", url='https://goodie.pl')],
            [InlineKeyboardButton("Купоны на услуги: мед.обслуживание, спорт, учеба", url='https://www.groupon.pl/')],
            [InlineKeyboardButton("Купоны на одежду, технику и тд.", url='https://rabatio.com/')],
            [InlineKeyboardButton("Купоны на всё", url='https://www.newsweek.pl/kupony-rabatowe/sklepy')],
            [InlineKeyboardButton("Back", callback_data='back')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        # Редактируем сообщение с новой клавиатурой
        await query.edit_message_text(text="Купоны и скидки", reply_markup=reply_markup)

    elif query.data == 'option7':
        # Создаем клавиатуру для опции 7
        keyboard = [
            [InlineKeyboardButton("Polskieradio", url='https://www.polskieradio.pl/397')],
            [InlineKeyboardButton("Novosti PL", url='https://novosti.sprosi.eu')],
            [InlineKeyboardButton("Новости + статьи по адаптации и легализации", url='https://in-poland.com')],
            [InlineKeyboardButton("Справочник по вузам, фирмам, отелям, бизнесу ...", url='https://polsha24.com')],
            [InlineKeyboardButton("Туризм в Польше", url='https://www.polscha.travel/uk')],
            [InlineKeyboardButton("Русскоязычное издание о Польше", url='https://novayapolsha.pl')],
            [InlineKeyboardButton("Новости и события в Варшаве", url='https://www.the-warsaw.com')],
            [InlineKeyboardButton("Все про образование в Польше", url='https://mojaedukacja.com/ru/')],
            [InlineKeyboardButton("UkrainianInPoland", url='https://www.ukrainianinpoland.pl/ru/)],')],
            [InlineKeyboardButton("Back", callback_data='back')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        # Редактируем сообщение с новой клавиатурой
        await query.edit_message_text(text="Новостные и справочные порталы для эмигрантов", reply_markup=reply_markup)

    elif query.data == 'option8':
        # Создаем клавиатуру для опции 8
        keyboard = [
            [InlineKeyboardButton("Красота", callback_data='beauty')],
            [InlineKeyboardButton("Медицина", callback_data='medical')],
            [InlineKeyboardButton("Back", callback_data='back')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        # Редактируем сообщение с новой клавиатурой
        await query.edit_message_text(text="Красота и здоровье", reply_markup=reply_markup)

    elif query.data == 'beauty':
        # Создаем клавиатуру для beauty
        keyboard = [
            [InlineKeyboardButton("Booksy", url='https://booksy.com/uk-pl/')],
            [InlineKeyboardButton("Lookinwell", url='https://www.lookinwell.com/ru/search')],
            [InlineKeyboardButton("Back", callback_data='option8')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        # Редактируем сообщение с новой клавиатурой
        await query.edit_message_text(text="Стрижки, Маникюр, Макияж и т.п.", reply_markup=reply_markup)

    elif query.data == 'medical':
        # Создаем клавиатуру для beauty
        keyboard = [
            [InlineKeyboardButton("Украино и русскоговорящие доктора", url='https://polandlek.pl/doctor/')],
            [InlineKeyboardButton("Бесплатная помощь для беженцев", url='https://www.dimedic-ukrayina.eu')],
            [InlineKeyboardButton("Поиск рус/укр говорящих врачей ", url='https://lekarzedlaukrainy.pl/ru')],
            [InlineKeyboardButton("Поиск укр/рус говорящих врачей ", url='https://www.znanylekarz.pl')],
            [InlineKeyboardButton("Крупнейший медицинский центр в Польше ", url='https://www.medicover.pl')],
            [InlineKeyboardButton("Back", callback_data='option8')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        # Редактируем сообщение с новой клавиатурой
        await query.edit_message_text(text="Поиск врачей и медицинских услуг", reply_markup=reply_markup)

    elif query.data == 'option9':
        # Создаем клавиатуру для опции 9
        keyboard = [
            [InlineKeyboardButton("Going", url='https://goingapp.pl')],
            [InlineKeyboardButton("Orange Smile", url='https://www.orangesmile.com/destinations/poland/')],
            [InlineKeyboardButton("Booking", url='https://www.booking.com/attractions/')],
            [InlineKeyboardButton("Tripadvisor", url='https://www.tripadvisor.ru/Tourism-g274723-Poland-Vacations.html')],
            [InlineKeyboardButton("Кинотеатры", callback_data='kino')],
            [InlineKeyboardButton("Back", callback_data='back')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        # Редактируем сообщение с новой клавиатурой
        await query.edit_message_text(text="Тургиды и сервисы поиску досуга в Польше", reply_markup=reply_markup)

    elif query.data == 'kino':
        # Создаем клавиатуру для beauty
        keyboard = [
            [InlineKeyboardButton("Helios", url='https://www.helios.pl/')],
            [InlineKeyboardButton("MultiKino", url='https://multikino.pl')],
            [InlineKeyboardButton("Cinema city", url='https://www.cinema-city.pl/')],
            [InlineKeyboardButton("Back", callback_data='option9')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        # Редактируем сообщение с новой клавиатурой
        await query.edit_message_text(text="Польские сети кинотеатров.\n"
                                           "В основном эти сети позывают фильмы на польском и английском языках\n"
                                           "Но переодически проходят показы для Украино говорящей аудитории.\n"
                                           "Все зависит от конкретного города и кинотеатра.", reply_markup=reply_markup)

    elif query.data == 'option10':
        # Создаем клавиатуру для опции 10
        keyboard = [
            [InlineKeyboardButton("PKO", callback_data='PKO')],
            [InlineKeyboardButton("Pekao", callback_data='Pekao')],
            [InlineKeyboardButton("Millenium", callback_data='Millenium')],
            [InlineKeyboardButton("ING", callback_data='ING')],
            [InlineKeyboardButton("Santander", callback_data='Santander')],
            [InlineKeyboardButton("Alior", callback_data='Alior')],
            [InlineKeyboardButton("Онлайн-банки", callback_data='online-bank')],
            [InlineKeyboardButton("Back", callback_data='back')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        # Редактируем сообщение с новой клавиатурой
        await query.edit_message_text(text="Банки Польши + условия открытия счета", reply_markup=reply_markup)

    elif query.data == 'PKO':
        keyboard = [
            [InlineKeyboardButton("PKO", url='https://www.pkobp.pl')],
            [InlineKeyboardButton("Back", callback_data='back')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await query.edit_message_text(text="Проще всего будет открыть банковский счёт в банке PKO Bank Polski."
                                           " Для этого будет достаточно паспорта с визой и вам даже необязательно иметь PESEL."
                                           " Помимо паспорта подходит: \n"
                                           " 1. Польский вид на жительство \n"
                                           " 2. ВНЖ ЕС, удостоверение личности страны ЕС \n"
                                           " 3. Удостоверение личности польского иностранца \n"
                                           " 4. Польский проездной документ для иностранца \n"
                                           " 5. Временный польский проездной документ для иностранца \n"
                                           " 6. Временное удостоверение личности иностранца \n"
                                           "Счёт может быть как в злотых, так и валютный.", reply_markup=reply_markup)
    elif query.data == 'Pekao':
        keyboard = [
            [InlineKeyboardButton("Pekao", url='https://www.pekao.com.pl')],
            [InlineKeyboardButton("Back", callback_data='back')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await query.edit_message_text(text="Открыть счёт в банке Pekao могут как резиденты, так и нерезиденты Польши.\n"
                                           "Какие нужны документы:\n"
                                           "Документ, подтверждающий личность - паспорт или вид на дительство + PESEL \n"
                                           "Счёт может быть как в злотых, так и валютный.", reply_markup=reply_markup)
    elif query.data == 'Millenium':
        keyboard = [
            [InlineKeyboardButton("Millenium", url='https://www.bankmillennium.pl')],
            [InlineKeyboardButton("Back", callback_data='back')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await query.edit_message_text(text="В банке Millenium открыть банковский счёт только с визой или с международной защитой не получится.\n"
                                           "Какие нужны документы:\n"
                                           "Паспорт; документы, подтверждающие необходимость открытия счёта \n"
                                           "(трудовой договор на срок минимум шесть месяцев, студенческий билет, вид на жительство) \n"
                                           "Счёт может быть как в злотых, так и валютный. \n"
                                           "Для семьи есть возможность открытия общего банковского счёта.", reply_markup=reply_markup)
    elif query.data == 'ING':
        keyboard = [
            [InlineKeyboardButton("ING", url='https://www.ing.pl')],
            [InlineKeyboardButton("Back", callback_data='back')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await query.edit_message_text(text="В банке ING также не смогут открыть счёт только на основании польской визы или международной защиты.\n"
                                           " Для открытия счёта будут необходимы дополнительные документы, подтверждающие легальность пребывания в Польше и источник дохода.\n"
                                           "Какие нужны документы: \n"
                                           "паспорт или вид на жительство, выданный Польшей;\n"
                                           "документ о пребывании (вид на жительство в Польше или виза);\n"
                                           "документ, подтверждающий приобретение денежных средств в Польше (трудовой договор, справка от работодателя, подтверждение получения стипендии, подтверждение ведения собственного бизнеса);\n"
                                           "Также нужно будет предоставить свой идентификационный номер налогоплательщика, если у вас нет польского налогового резидентства.",
                                      reply_markup=reply_markup)
    elif query.data == 'Santander':
        keyboard = [
            [InlineKeyboardButton("Santander", url='https://www.santander.pl/')],
            [InlineKeyboardButton("Back", callback_data='back')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await query.edit_message_text(text="Иностранцы, не являющиеся гражданами Европейского Союза, должны иметь следующие документы:\n"
                                           "Паспорт и постоянный или временный вид на жительство в Польше.\n"
                                           "В некоторых случаях банк также может потребовать подтверждение о постоянных поступлений на счёт.\n"
                                           "Речь здесь идет о выплатах по зарплате, пенсии или стипендии.\n"
                                           "Открыть счёт можно в отделении банка и онлайн.",
                                      reply_markup=reply_markup)
    elif query.data == 'Alior':
        keyboard = [
            [InlineKeyboardButton("Alior", url='https://www.aliorbank.pl')],
            [InlineKeyboardButton("Back", callback_data='back')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await query.edit_message_text(
            text="Для открытия счета в Alior Bank. Необходимо иметь с собой ОДИН из следующих документов + PESEL:\n"
                 "1. Действительный паспорт.\n"
                 "2. Польский документ под названием Karta pobytu (Разрешение на проживание).\n"
                 "3. Польский документ под названием Tymczasowe zaświadczenie tożsamości cudzoziemca \n"
                 "(Временное удостоверение личности иностранца).\n"
                 "4. Временный польский проездной документ, который выдается иностранцам.\n"
                 "Открыть счёт можно в отделении банка и онлайн.",
            reply_markup=reply_markup)
    elif query.data == 'online-bank':
        keyboard = [
            [InlineKeyboardButton("Revolut", url='https://www.revolut.com')],
            [InlineKeyboardButton("Paysera", url='https://www.paysera.pl/')],
            [InlineKeyboardButton("Back", callback_data='back')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await query.edit_message_text(
            text="Revolut — британо-литовский банк и компания финансовых технологий, предлагающая банковские услуги.\n"
                 "Revolut Bank UAB имеет лицензию банка Европейского центрального банка и регулируется Банком Литвы. \n"
                 "Вы можете открыть счёт в Revolut, если проживает на территории стран, где он легален\n"
                 " (Revolut в Польше работает).\n"
                 "Для открытия счёта вам необходимо:\n"
                 "Иметь официального работодателя на территории, где Revolut легален (необязательно);\n"
                 "Визу типа D этой страны или вид на жительство;\n"
                 "Номер телефона с ее кодом.\n"
                 "Если все условия соблюдены, вы можете заказать пластиковую карту Revolut с доставкой домой. \n"
                 "Но будьте осторожны с Revolut: он сохраняет за собой право блокировать счёта.\n"
                 "------------------------------------------------------------------------------------------\n"
                 "Paysera — это платежная система Литвы для осуществления платежей через интернет,\n"
                 " которая предоставляет свои услуги в более чем 180 стран по всему миру.\n "
                 "Вы можете открыть счёт в банке Paysera, если проживает на территории стран, где он легален \n"
                 "(Paysera в Польше работает). \n"
                 "Для открытия счёта вам необходимо:\n"
                 "Иметь официального работодателя на территории, где легален банк Paysera (необязательно)\n"
                 "Визу типа D этой страны или вид на жительство;\n"
                 "Номер телефона с ее кодом.\n"
                 "Если все условия соблюдены, вы можете заказать пластиковую карту Paysera с доставкой домой.", reply_markup=reply_markup)

    elif query.data == 'option11':
        # Создаем клавиатуру для опции 11
        keyboard = [
            [InlineKeyboardButton("Poczta Polska", callback_data='Poczta Polska')],
            [InlineKeyboardButton("InPost", callback_data='InPost')],
            [InlineKeyboardButton("DPD", callback_data='DPD')],
            [InlineKeyboardButton("Furgonetka", callback_data='Furgonetka')],
            [InlineKeyboardButton("UPS", callback_data='UPS')],
            [InlineKeyboardButton("Back", callback_data='back')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        # Редактируем сообщение с новой клавиатурой
        await query.edit_message_text(text="Cуществуют следующие способы отправки посылок в Польше:\n"
                                           "Отправить посылку курьером.\n"
                                           "Отправить посылку с помощью почтомата.\n"
                                           "Отправить посылку через почтовое отделение.", reply_markup=reply_markup)
    elif query.data == 'Poczta Polska':
        keyboard = [
            [InlineKeyboardButton("Poczta Polska", url='https://www.poczta-polska.pl')],
            [InlineKeyboardButton("Back", callback_data='back')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await query.edit_message_text(text="Poczta Polska — национальный почтовый оператор, который предлагает вид доставки Pocztex\n"
                                           " — это курьерская служба, которая доставляет посылки на дом \n"
                                           "или в одну из 17 000 точек самовывоза.\n"
                                           " Среди них есть почтоматы, которые расположены в супермаркетах Biedronka, Lewiatan, Zabka, Arhelan\n"
                                           " Одно из преимуществ Pocztex в том, что половина точек самовывоза работают в выходные и посылку можно забрать в любой день.", reply_markup=reply_markup)

    elif query.data == 'InPost':
        keyboard = [
            [InlineKeyboardButton("InPost", url='https://inpost.pl/ua')],
            [InlineKeyboardButton("InPost Mobile Android", url='https://play.google.com/store/apps/details?id=pl.inpost.inmobile')],
            [InlineKeyboardButton("InPost Mobile iOS", url='https://apps.apple.com/pl/app/inpost-mobile/id1437787639')],
            [InlineKeyboardButton("Back", callback_data='back')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await query.edit_message_text(text="InPost — польская компания, которая делает акцент на развитии сети почтоматов (Paczkomat).\n"
                                           "Почтоматы работают как полноценное почтовое отделение и используются для получения или отправки посылок,\n"
                                           "работающих круглосуточно и без выходных", reply_markup=reply_markup)
    elif query.data == 'DPD':
        keyboard = [
            [InlineKeyboardButton("DPD", url='https://www.dpd.com/pl/pl/')],
            [InlineKeyboardButton("Back", callback_data='back')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await query.edit_message_text(text="DPD - это международная курьерская служба,которая предлагает широкий спектр услуг по доставке,\n"
                                           " включая экспресс-доставку, стандартную доставку и доставку тяжелых грузов.\n"
                                           " Компания также предоставляет услуги по отслеживанию грузов, подписке на уведомления о статусе доставки,\n"
                                           " а также предоставляет возможность выбора точки самовывоза и оплаты за товар при получении.", reply_markup=reply_markup)
    elif query.data == 'Furgonetka':
        keyboard = [
            [InlineKeyboardButton("Furgonetka", url='https://furgonetka.pl')],
            [InlineKeyboardButton("Back", callback_data='back')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await query.edit_message_text(text="Furgonetka — логистическая компания, работающая в Польше с 2010 года.\n"
                                           " Сервис выполняет роль почтового агрегатора и предоставляет возможность отправки с помощью 12 разных операторов.\n"
                                           " Оформить посылку можно прямо на сайте, а после ее заберет курьер. Также у компании есть свои курьерские пункты и почтоматы Furgonetka BOX.\n"
                                           " Сервис предлагает индивидуальные тарифы для интернет-магазинов, а стоимость отправки зависит от количества посылок, которые вы отправляете за месяц.", reply_markup=reply_markup)
    elif query.data == 'UPS':
        keyboard = [
            [InlineKeyboardButton("UPS", url='https://wwwapps.ups.com/time?loc=en_PL')],
            [InlineKeyboardButton("Back", callback_data='back')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await query.edit_message_text(text="UPS — глобальная компания со штаб-квартирой в США, которая работает в 220 странах.\n"
                                           " У UPS неудобный сайт, где нужно просчитывать отдельно каждую посылку.\n"
                                           " Калькулятор для расчета стоимости содержит большое количество полей. \n"
                                           "Отправителю нужно пройти три этапа заполнения данных и начинать каждый расчет с чистого листа. \n"
                                           "В результате вы получите от 3 до 10 тарифов для разных типов доставок.\n"
                                           "Большинство тарифов UPS дороже, чем у других польских операторов, и только некоторые из них соответствуют среднерыночным.\n"
                                           " Например, есть тарифы стоимостью в тысячи евро за небольшую посылку.", reply_markup=reply_markup)

    elif query.data == 'back':
        # Создаем клавиатуру главного меню
        keyboard = [
            [InlineKeyboardButton("Мобильные Операторы", callback_data='option1')],
            [InlineKeyboardButton("Поиск жилья", callback_data='option2')],
            [InlineKeyboardButton("Поиск работы", callback_data='option3')],
            [InlineKeyboardButton("Транспорт", callback_data='option4')],
            [InlineKeyboardButton("Доставка еды", callback_data='option5')],
            [InlineKeyboardButton("Скидки и Купоны", callback_data='option6')],
            [InlineKeyboardButton("Польские новостные и справочные порталы", callback_data='option7')],
            [InlineKeyboardButton("Красота и Здоровье", callback_data='option8')],
            [InlineKeyboardButton("Досуг", callback_data='option9')],
            [InlineKeyboardButton("Банки Польши", callback_data='option10')],
        [InlineKeyboardButton("Почта, посылки, пачкоматы", callback_data='option11')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        # Редактируем сообщение с главным меню
        await query.edit_message_text(text="Выберите интересующий вас раздел", reply_markup=reply_markup)



if __name__ == '__main__':

    load_dotenv()
    application = ApplicationBuilder().token(os.getenv('TOKEN')).build()

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    button_handler = CallbackQueryHandler(button)
    application.add_handler(button_handler)

    asyncio.run(application.run_polling())


