
import random

from api_client.AuhtApi import AuthApi
from api_client.ProjectApi import ProjectApi
from api_client.BoardApi import BoardApi
from api_client.ColumnApi import ColumnApi
from testdata.DataProvider import DataProvider


class APITest:
    
    def create_project(
        self,
        project_api: ProjectApi, 
        test_data: DataProvider, 
        delete_utility_project: dict, 
    ):
       
        project_title = test_data.get('project_title') + str(random.randint(0, 99999))
            
        len_before = len(project_api.get_projects().json()['content'])
        api_response = project_api.create_project(project_title)
        
        
        new_project = project_api.get_project_by_id(api_response.json()['id']).json()

        len_after = len(project_api.get_projects().json()['content'])
        
        delete_utility_project['project_id'] = api_response.json()['id']
        
        
            
        assert api_response.status_code == 201
           
        assert api_response.json().get('id', None) != None
            
        assert new_project['title'] == project_title
            
        assert len_after - len_before == 1
    
          
    def get_active_project(
        self, 
        project_api: ProjectApi, 
        generate_random_str: str,
        delete_utility_project: dict
    ):
        actual_project_id = project_api.create_project(f'1. {generate_random_str}').json()['id']
        deleted_project_id = project_api.create_project(f'1. {generate_random_str}').json()['id']
        
        project_api.delete_project(deleted_project_id)

        api_response = project_api.get_projects()
        
        
        api_ids = []
        for proj in api_response.json()['content']:
            api_ids.append(proj['id'])
        
        delete_utility_project['project_id'] = actual_project_id

        
        assert api_response.status_code == 200
        
        assert not deleted_project_id in api_ids
            
        assert actual_project_id in api_ids
    
    
    def update_column(
        project_api: ProjectApi, 
        board_api: BoardApi, 
        column_api: ColumnApi, 
        create_utility_project: dict,
        delete_utility_project: dict,
        delete_utility_board: dict,
        delete_utility_column: dict,
        test_data: DataProvider,
        generate_random_str: str
    ):
        project_id = create_utility_project['project_id']
        
        first_board_id = board_api.create_board(f'1 {generate_random_str}', project_id).json()['id']
            
        second_board_id = board_api.create_board(f'2 {generate_random_str}', project_id).json()['id']
        
        
        column_id = column_api.create_column(f'Колонка {generate_random_str}', first_board_id).json()['id']
        
        body = {
            'title': test_data.get('new_column_title'),
            'color': test_data.get('new_column_color'),
            'boardId': second_board_id
        }
        api_response = column_api.update_column(column_id, body)

        updated_column = column_api.get_column_by_id(column_id).json()
        
        delete_utility_project['project_id'] = project_id 
        delete_utility_board['first_board_id'] = first_board_id
        delete_utility_board['second_board_id'] = second_board_id
        delete_utility_column['column_id'] = column_id

       
        assert api_response.status_code == 200
            
        assert api_response.json()['id'] == column_id
            
        assert test_data.get('new_column_title') in updated_column['title']
            
        assert test_data.get_int('new_column_color') == updated_column['color']
            
        assert second_board_id == updated_column['boardId']  
                          
    
    def create_project_empty_title(self, project_api: ProjectApi, test_data: DataProvider):
        
        len_before = len(project_api.get_projects().json()['content'])
            
        api_response = project_api.create_project('')
        
        
        len_after = len(project_api.get_projects().json()['content'])

        error_msg = test_data.get('error_description_empty_project_title')
        
        
        assert api_response.status_code == 400
            
        assert api_response.json()['statusCode'] == 400
            
        assert error_msg in api_response.json()['message']
            
        assert test_data.get('error_bad_request') == api_response.json()['error']
           
        assert len_before == len_after
        
       
    def create_project_deleted_api_key(
        self, 
        auth_api: AuthApi, 
        project_api: ProjectApi, 
        test_data: DataProvider
    ):
        
        len_before = len(project_api.get_projects().json()['content'])
        
        key_resp = auth_api.create_api_key(test_data.get('company_id'))
        key = key_resp.json()['key']
        auth_api.delete_api_key(key)
        auth_api.get_api_keys(test_data.get('company_id'))
        
        api_response = project_api.create_project('test', key)
        
        
        len_after = len(project_api.get_projects().json()['content'])
        
        error_msg = test_data.get('error_description_unauth')
        error = test_data.get('error_unauth')
          
        
        assert api_response.status_code == 401
            
        assert api_response.json()['statusCode'] == 401
            
        assert error_msg == api_response.json()['message']
            
        assert error == api_response.json()['error']
           
        assert len_before == len_after