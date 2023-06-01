import pytest
from utils.api import Reqres_api
from utils.test_data import test_data_create_user_post, test_data_register_post, test_data_login_post


# Проверка POST API /api/users
@pytest.mark.parametrize('json_body, json_response, status_code', test_data_create_user_post)
def test_create_user_post(base_url, post_api_create, json_body, json_response, status_code):
    print("Method POST create user API", base_url + post_api_create)
    response = Reqres_api.post_request(base_url + post_api_create, json_body=json_body)
    status_code_response = response.status_code
    assert status_code == status_code_response, f"Код ОР {status_code_response} не соответствует ФР {status_code}"
    assert json_response == list(response.json().keys()), "Схема ОР, не соответствует ФР"


# Проверка POST API /api/register
@pytest.mark.parametrize('json_request, json_response, status_code_response', test_data_register_post)
def test_register_user_post(base_url, post_api_register, json_request, json_response, status_code_response):
    response = Reqres_api.post_request(base_url + post_api_register, json_body=json_request)
    status_code = response.status_code
    schema = json_response
    assert status_code_response == status_code, f"Код ОР {status_code} не соответствует ФР {status_code_response}"
    assert schema == dict(response.json()), "Схема ОР, не соответствует ФР"


# Проверка POST API /api/login
@pytest.mark.parametrize('json_request, json_response, status_code_response', test_data_login_post)
def test_login_user_post(base_url, post_api_login, json_request, json_response, status_code_response):
    response = Reqres_api.post_request(base_url + post_api_login, json_body=json_request)
    status_code = response.status_code
    schema = json_response
    assert status_code_response == status_code, f"Код ОР {status_code} не соответствует ФР {status_code_response}"
    assert schema == dict(response.json()), "Схема ОР, не соответствует ФР"
