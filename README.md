# Diplon-repo
Проект по автоматизации API и UI тестирования на python для сервиса работы с задачами Yougile
Сервис “Yougile” позволяет планировать и управлять задачами в компании. Для проекта был выбран функционал, доступный в веб-интерфейсе и через REST API. Составлено 5 UI- и 5 API-автотестов, для формирования отчета о проведенных автотестах используется инструмент Allure.



Для выполнения необходимо
склонировать проект,
установить зависимости,
запустить тесты с указанием пути к дирректории результатов тестирования pytest --alluredir allure_files,
сформировать отчет allure generate allure_files -o allure_report,
открыть отчет allure open allure_report.


Стек:
pytest, 
selenium, 
requests, 
allure,
config.


Структура:
./test - тесты, 
/test_api.py - API-тесты, 
/test_ui.py - UI-тесты,
/conftest.py - файл с фикстурами,
./web_pages - описание страниц,
./api_client - хелперы для работы с API,
./configuration - провайдер настроек,
config.ini - настройки для тестов,
./testdata - провайдер тестовых данных,
test_data.json - тестовые данные,
requirements.txt - файл с используемыми зависимостями.

Файл с тестовыми данными (test_data.json):
содержит данные для авторизации,
при смене пользователя необходимо воспользоваться API-документацией Yougile и обновить значения в полях:
email, password, company, user_name, company_id, api_key.
Названия ключей в файле менять нельзя,
значения текстовых данных для названий (ключ title) можно задавать любые.


Файл с переменными окружения (config.ini) содержит:
базовый url-адрес для API-запросов,
базовый url-адрес для веб-интерфейса,
название браузера для проведения UI-автотестов,
timeout для настройки браузера.


Библиотеки:

pip3 install pytest

pip3 install selenium

pip3 install webdriver-manager

pip3 install allure-pytest

pip3 install requests

"# Test" 
