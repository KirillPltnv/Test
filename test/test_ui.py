import allure
import random
from selenium.webdriver.remote.webdriver import WebDriver
from web_pages.IndexPage import IndexPage
from web_pages.TeamPage import TeamPage
from web_pages.ProjectPage import ProjectPage
from api_client.UserApi import UserApi
from api_client.ProjectApi import ProjectApi
from api_client.BoardApi import BoardApi
from api_client.ColumnApi import ColumnApi
from api_client.TaskApi import TaskApi
from testdata.DataProvider import DataProvider
from pages.ui_pages import UITest 

@allure.epic('Тестирование интерфейса сервиса YouGile')
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite('UI-тесты на авторизацию, управлению проектами и задачами')
@allure.id('YG-1')
@allure.story('Позитивные проверки авторизации')
@allure.title('Авторизация ранее зарегистрированного пользователя')
@allure.description('Выполнить авторизацию ранее зарегистрированного пользователя')
@allure.feature('AUTHORIZE')   
def test_auth():
    ui_page = UITest
    ui_page.auth
            

@allure.id('YG-4')
@allure.story('Позитивные проверки по управлению проектами')
@allure.title('Добавление проекта компании')
@allure.description('Добавить новый проект компании через кнопку Добавить проект')
@allure.feature('Кнопка Добавить проект')     
def test_add_project():
    ui_page = UITest
    ui_page.add_project

    
@allure.id('YG-5')
@allure.story('Позитивные проверки по управлению проектами')
@allure.title('Удаление проекта компании')
@allure.description('Удалить проект компании через кнопку Удалить в контекстном меню проекта')
@allure.feature('Кнопка Удалить в контекстном меню проекта')      
def test_delete_project():
    ui_page = UITest
    ui_page.delete_project
        
@allure.id('YG-6')
@allure.story('Позитивные проверки по управлению задачами')
@allure.title('Добавление задачи')
@allure.description('Добавить задачу через заполнение и отправку формы Ввода названивания задачи')
@allure.feature('Поле Ввести названивание задачи')         
def test_create_task():
    ui_page = UITest
    ui_page.create_task
    
@allure.id('YG-7')
@allure.story('Позитивные проверки по управлению задачами')
@allure.title('Отметить задачу выполненной')
@allure.description('Нажать кнопку Отметить выполненной в контекстном меню задачи')
@allure.feature('Кнопка Отметить выполненной в контекстном меню задачи')   
def test_complete_task():
    ui_page = UITest
    ui_page.complete_task