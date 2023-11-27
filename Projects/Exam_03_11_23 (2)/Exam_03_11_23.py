from bs4 import BeautifulSoup
import requests
from datetime import date

from aiogram import Bot, Dispatcher, executor, types


def get_html(url: str) -> str:
    """We geting the html markup of particular website by using his url"""
    response = requests.get(url)
    return response.text

def get_soup(html: str) -> BeautifulSoup:
    """We geting the html markup and structure it into bs"""
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def get_article_data(soup):
    """We returning dictionary with data"""
    articles = soup.find('div', class_='Tag--articles')
    article = articles.find_all('div', class_='Tag--article')
    data_list = []

    #looking for only 20 first articles
    for ArticleItem in article[0:20]:
        data = ArticleItem.find('div', class_='ArticleItem--data ArticleItem--data--withImage')

        #name
        name = data.find('a', class_='ArticleItem--name').text.strip()
        
        #descripxon
        descripxon_url = data.find('a', class_='ArticleItem--name').get('href')   #to get a descripxon we need to go deeper
        descripxon_html = requests.get(descripxon_url).text
        descripxon_soup = BeautifulSoup(descripxon_html, 'html.parser')
        Article_text = descripxon_soup.find('div', class_='Article--text')
        container = Article_text.find('div', class_='BbCode')
        descripxon = container.find('p').text.strip()

        #photo
        photo = data.find('a', class_='ArticleItem--image').get('href')

        #finnaly data list
        data_list.append({'Name': name, 'Descripxon': descripxon, 'Photo': photo})

    return data_list


url = 'https://kaktus.media/?lable=8&date=' + str(date.today()) + '&order=time'   # Чтобы находил страницу с новостями сегодняшнего дня
html = get_html(url)
soup = get_soup(html)


TOKEN = '6783369599:AAGNJwmG1LgCGHamk4m2nrDao_L2a6nePU8'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
chosen_article_num = 0


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    """This handler will be called when the user sends the 'start' command"""
    await message.reply('Подождите страничка парсится...')
    if not len(get_article_data(soup)) == 0:
        """Ночью после 00:00 оказывется страница с новостями чиста. Конечно пока не опубликуют новые статьи"""

        response = 'Здесь вы можете прочитать последние новости!\nВыберите статью по номерации\n\n'

        for num, Article in enumerate(get_article_data(soup)): # Добавляем в переменную response 20 заголовков из наших данных
            response += f"{num+1, Article['Name']}\n"

        response += '\nПожалуйста выберите номер статьи которую вы хотите прочесть от 1 до 20 '

        await message.reply(response)

    else:
        await message.reply('Прошу прощения, но на сегодняшную дату пока нет новостей')
        




@dp.message_handler(content_types=['text'])
async def chose_article(message: types.Message):
    
    global chosen_article_num   # Using global. А то chosen_article_num не видно
    num = message.text
    if  num.isdigit():
        """User must chose number of article 1-20"""
        chosen_article_num = int(num)
        response = f'Отлично! Вы выбрали {num}-ю статью.\nВы можете увидеть описание этой новости и фото!\nВыберите Descripxon или Photo!'
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)   # Используем кнопки и ниже добавляем
        keyboard.add(types.KeyboardButton(text="Descripxon"))
        keyboard.add(types.KeyboardButton(text="Photo"))
        keyboard.add(types.KeyboardButton(text='Quit'))
        await message.reply(response, reply_markup=keyboard)
        
    elif not num.isdigit():
        desc_message = message.text
        if desc_message.lower() == 'descripxon':
            await message.reply('Подождите, описание загружается...')
            desc = get_article_data(soup)[chosen_article_num-1]['Descripxon']
            await message.reply(desc)

        photo_message = message.text
        if photo_message.lower() == 'photo':
            await message.reply('Подождите, фото загружается...')
            photo = get_article_data(soup)[chosen_article_num-1]['Photo']
            await message.reply_photo(photo)

        quit_message = message.text
        if quit_message.lower() == 'quit':
            await message.reply('До свидания!')




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)