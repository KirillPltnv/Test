import allure
import pytest
import random

from api_client.AuhtApi import AuthApi
from api_client.ProjectApi import ProjectApi
from api_client.BoardApi import BoardApi
from api_client.ColumnApi import ColumnApi
from testdata.DataProvider import DataProvider
from pages.api_page import APITest 

@allure.epic('Тестирование функционала REST API сервиса YouGile')
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite('API-тесты по управлению проектами и колонками')
@allure.id('YG-9')
@allure.story('Позитивные проверки по управлению проектами')
@allure.title('Добавление проекта компании')
@allure.description('Добавление нового проекта в компанию')
@allure.feature('CREATE')
def test_create_project():
    api_page = APITest
    api_page.create_project
    
@allure.id('YG-10')
@allure.story('Позитивные проверки по управлению проектами')
@allure.title('Получение списка актуальных проектов')
@allure.description('Получить список актуальных проектов компании, у которых нет атрибута deleted:true')
@allure.feature('GET')          
def test_get_active_project():
    api_page = APITest
    api_page.get_active_project
    
@allure.id('YG-12')
@allure.story('Позитивные проверки по управлению колонками')
@allure.title('Редактирование колонки')
@allure.description('Изменить атрибуты колонки - название, цвет, родительскую доску')
@allure.feature('PUT') 
def test_update_column():
    api_page = APITest
    api_page.update_column
                          
@allure.id('YG-8')
@allure.story('Негативные проверки по управлению проектами')
@allure.title('Добавление проекта с пустой строкой в названии')
@allure.description('Проверка обработки запроса на добавление проекта с пустой строкой в названии')
@allure.feature('GET') 
def test_create_project_empty_title():
    api_page = APITest
    api_page.create_project_empty_title
        
@allure.id('YG-11')
@allure.story('Негативные проверки по управлению проектами')
@allure.title('Добавление проекта с удаленном ключом API')
@allure.description('Проверка обработки запроса на добавление проекта с удаленном ключом API')
@allure.feature('POST')     
def test_create_project_deleted_api_key():
    api_page = APITest
    api_page.update_column