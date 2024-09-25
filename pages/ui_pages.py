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


class UITest:
    
    
    def auth(self, browser: WebDriver, test_data: DataProvider):
        index_page = IndexPage(browser)
        index_page.open()
        index_page.click_sign_in()
        
        team_page = TeamPage(browser)
        team_page.set_email(test_data.get('email'))
        team_page.set_password(test_data.get('password'))
        team_page.login()
        assert test_data.get('email') == 'verarodkina1999@yandex.ru'
            

       
    def add_project(
        self, 
        auth_browser: WebDriver, 
        test_data: dict, 
        project_api: ProjectApi,
        delete_utility_project: dict
    ):
        team_page = TeamPage(auth_browser)
        team_page.open()

        team_page.click_add_project()
        
        
        prefix_id = str(random.randint(0, 99999))    
        project_title = test_data.get('project_title') + ' ' + prefix_id
              
        team_page.set_project_title(project_title)
        team_page.set_prefix_id_task(prefix_id)
        
        ui_btn_bg_color = team_page.get_bg_action_color()

        team_page.click_create_project(project_title)
        
        ui_title = team_page.get_project_title()
        ui_prefix = team_page.get_prefix_id_task()
        
        api_projects = project_api.get_projects().json()
        project_titles = []
        project_id = ''
        for proj in api_projects['content']:
            project_titles.append(proj['title'])
            if proj['title'] == project_title:
                project_id = proj['id']
        api_project_titles = ''.join(project_titles)
        
        delete_utility_project['project_id'] = project_id
        
        
        assert test_data.get('bg_active_color') == ui_btn_bg_color
        assert project_title == ui_title 
        assert prefix_id == ui_prefix
        assert project_title in api_project_titles
    
         
    def delete_project(
        self, 
        auth_browser, 
        test_data: DataProvider,
        project_api: ProjectApi, 
        user_api: UserApi,
        generate_random_str: str
    ):
        
        project_title = 'Проект ' + generate_random_str + ' ' + str(random.randint(0, 99999))
        admin_id = user_api.get_user_id(test_data.get('email'))
        user_dict = {admin_id: "admin"}
        project_id = project_api.create_project(project_title, users_dict=user_dict).json()['id']
        
        team_page = TeamPage(auth_browser)
        team_page.open()
        
        team_page.click_three_dot(project_title)
        team_page.click_trash()
        team_page.click_delete(project_title)
        
        project_api_data = project_api.get_project_by_id(project_id).json()
        
        ui_project_card_titles = team_page.get_project_section_text()

        
        assert not project_title in ui_project_card_titles
        if project_api_data['deleted'] is True:
            assert True
        else:
            assert False
        
           
    def create_task(
        self,
        auth_browser, 
        test_data: dict,
        user_api: UserApi,
        project_api: ProjectApi, 
        board_api: BoardApi,
        column_api: ColumnApi,
        task_api: TaskApi,
        generate_random_str: str,
        delete_utility_project: dict,
        delete_utility_board: dict,
        delete_utility_column: dict,
        delete_utility_task: dict
    ):
        
        project_title = 'Проект ' + generate_random_str + ' ' + str(random.randint(0, 99999))
        admin_id = user_api.get_user_id(test_data.get('email'))
        user_dict = {admin_id: "admin"}
        project_id = project_api.create_project(project_title, users_dict=user_dict).json()['id']
                
        board_title = 'Доска ' + generate_random_str
        board_id = board_api.create_board(board_title, project_id).json()['id']
        
        column_title = 'Колонка ' + generate_random_str
        column_id = column_api.create_column(column_title, board_id).json()['id']
        
        team_page = TeamPage(auth_browser)
        team_page.open()

        team_page.click_project_card(project_title)

        project_page = ProjectPage(auth_browser)
        project_page.click_board(board_title)

        project_page.click_add_task(column_title)
        project_page.add_task(test_data.get('task_title'))

        ui_task_titles = ''.join(project_page.get_task_titles(column_title)) 
        
        api_tasks = task_api.get_tasks_by_column(column_id).json()['content']
        
        task_id = ''
        task_titles = []
        for task in api_tasks:
            task_titles.append(task['title'])
            if test_data.get('task_title') in task['title']:
                task_id = task['id']
        api_task_titles = ''.join(task_titles)

        delete_utility_project['project_id'] = project_id
        delete_utility_board['board_id'] = board_id
        delete_utility_column['column_id'] = column_id
        delete_utility_task['task_id'] = task_id
        
        
        assert test_data.get('task_title') in ui_task_titles
        assert test_data.get('task_title') in api_task_titles
    
    
    def complete_task(
        self, 
        auth_browser,
        test_data: dict,
        user_api: UserApi,
        project_api: ProjectApi, 
        board_api: BoardApi,
        column_api: ColumnApi,
        task_api: TaskApi,
        generate_random_str: str,
        delete_utility_project: dict,
        delete_utility_board: dict,
        delete_utility_column: dict,
        delete_utility_task: dict
    ):        
        
        project_title = 'Проект ' + generate_random_str + ' ' + str(random.randint(0, 99999))
        admin_id = user_api.get_user_id(test_data.get('email'))
        user_dict = {admin_id: "admin"}
        project_id = project_api.create_project(project_title, users_dict=user_dict).json()['id']

        board_title = 'Доска ' + generate_random_str
        board_id = board_api.create_board(board_title, project_id).json()['id']
        
        column_title = 'Колонка ' + generate_random_str
        column_id = column_api.create_column(column_title, board_id).json()['id']
        
        task_title = 'Задача ' + generate_random_str
        task_id = task_api.create_task(task_title, column_id).json()['id']
        
        team_page = TeamPage(auth_browser)
        team_page.open()

        team_page.click_project_card(project_title)
        
        project_page = ProjectPage(auth_browser) 
        
        project_page.click_board(board_title)
        project_page.click_three_dot(column_title, task_title)
        project_page.click_mark_completed()
        
        ui_title_status_color = project_page.get_title_status_color(column_title, task_title)
        
        task_response = task_api.get_task_by_id(task_id)
        
        delete_utility_project['project_id'] = project_id
        delete_utility_board['board_id'] = board_id
        delete_utility_column['column_id'] = column_id
        delete_utility_task['task_id'] = task_id

       
        assert test_data.get('completed_task_title_color') == ui_title_status_color
        assert task_response.json()['completed']