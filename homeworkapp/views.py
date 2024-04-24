import logging
from django.shortcuts import render
# Create your views here.

logger = logging.getLogger(__name__)


def index(request):
    logger.info('Страница "Главная страница" была посещена') 
    
    html = """
    <h1>Главная страница</h1>
    <h2>Фреймворк Django - Домашнее задание 1.</h2>
    <p>Задание:</p>
    <p>Создайте пару представлений в вашем первом приложении:</p>
    <p> — главная страница</p>
    <p> — о себе.</p>
    <p>Внутри каждого представления должна быть переменная html — многострочный текст с HTML-вёрсткой 
    и данными о вашем первом Django-сайте и о вас.</p>
    <p>Сохраняйте в логи данные о посещении страниц.</p>
    """
    title = "Главная страница"
    return render(request, 'index.html', {'html': html, 'title': title})

def about(request):
    logger.info('Страница "О себе" была посещена')

    html = """
    <h1>О себе</h1>
    <h2>Представление</h2>
    <p>Добрый день</p>
    <p>Хотел бы рассказать о себе: меня зовут Сокол Константин.</p>
    <p>Был опыт прохождения блоков в образовательной платформе 'GeekBrains'</p>
    <p>А именно:</p>
    <p>* Введение в WEB технологии.</p>
    <p>* Работа с Git and Github</p>
    <p>* Полный курс по языку программирования Python.</p>
    <p>* Flask and FastAPI</p> 
    <h2>Это домашнее задание по Django.</h2>
    """
    title = "О себе"
    return render(request, 'about.html', {'html': html, 'title': title})