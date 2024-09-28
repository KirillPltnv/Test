import random
import json
import allure

#from test.test_api import test_create_project
#from pages.api_page import APITest
from api_client.ProjectApi import ProjectApi
from testdata.DataProvider import DataProvider
from pages.api_page import APITest

company_id = "64c4160e-2202-4f6b-89a0-b5eba1dce2c3"
api_key = "Z9H0gopqKIwdPMFcY3abHEGQbgiJMTDCEwK3a4lkqNmmDaim+nKjseI5hOk-F5Uj"
base_url = 'https://yougile.com/api-v2'


#title = DataProvider().get('project_title')
#a = {}
#print(ProjectApi(base_url, api_key).get_projects())
#ProjectApi(base_url, api_key).create_project(title)
#a = APITest()
#APITest.create_project(a, ProjectApi(base_url, api_key), DataProvider())

@allure.epic('Тестирование функционала REST API сервиса YouGile')
@allure.severity(allure.severity_level.BLOCKER)
@allure.suite('API-тесты по управлению проектами и колонками')
@allure.id('YG-9')
@allure.story('Позитивные проверки по управлению проектами')
@allure.title('Добавление проекта компании')
@allure.description('Добавление нового проекта в компанию')
@allure.feature('CREATE')
def test_create_project():
    #api_page = APITest
    #api_page.create_project

    #начинка из класса тестов метода create_project, printы для души
    delete_utility_project = {}

    test_data = DataProvider()
    project_api = ProjectApi(base_url, api_key)

    project_title = str(test_data.get('project_title')) + str(random.randint(0, 99999))
    print(project_title)

    len_before = len(project_api.get_projects().json()['content'])
    print(len_before)

    api_response = project_api.create_project(project_title)
    print(api_response)

    new_project = project_api.get_project_by_id(api_response.json()['id']).json()
    print(new_project)

    len_after = len(project_api.get_projects().json()['content'])

    delete_utility_project['project_id'] = api_response.json()['id']

    assert api_response.status_code == 201

    assert api_response.json().get('id', None) != None

    assert new_project['title'] == project_title

    assert len_after - len_before == 1

    some_inf = {'status': api_response.status_code, 'id': api_response.json().get('id')}

    APITest().create_project_info_dicts(some_inf)

    print('Thats all')
