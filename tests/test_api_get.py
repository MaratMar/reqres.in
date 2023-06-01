import pytest
from utils.api import Reqres_api
from utils.test_data import test_data_user_get, test_data_unknown_get, test_data_delay_get, test_list_users_get


# Проверка GET API /api/users/{id}
@pytest.mark.parametrize('id_user, json_response, status_code', test_data_user_get)
def test_get_single_user(base_url, get_api_user, id_user, status_code, json_response):
    print("Method Get single user Request", get_api_user + id_user)
    response = Reqres_api.get_request(base_url + get_api_user + id_user)
    actual_status_code = response.status_code
    actual_schema = response.json()
    assert json_response == actual_schema, "Схема ОР, не соответствует ФР"
    assert status_code == actual_status_code, f"Код ОР {status_code} не соответствует ФР {actual_status_code}"


# Проверка GET API /api/unknown/{id}
@pytest.mark.parametrize('id_user, status_code', test_data_unknown_get)
def test_get_unknown(base_url, get_api_unknown, id_user, status_code):
    print("Method Get unknown", get_api_unknown + id_user)
    actual_status_code = Reqres_api.get_request(base_url + get_api_unknown + id_user).status_code
    assert status_code == actual_status_code, f"Код ОР {status_code} не соответствует ФР {actual_status_code}"


# Проверка GET API /api/users?delay={id}
@pytest.mark.parametrize('id_user, status_code', test_data_delay_get)
def test_get_delay(base_url, get_api_delay, id_user, status_code):
    print("Method Get delay", get_api_delay + id_user)
    actual_status_code = Reqres_api.get_request(base_url + get_api_delay + id_user).status_code
    assert status_code == actual_status_code, f"Код ОР {status_code} не соответствует ФР {actual_status_code}"


# Проверка GET API /api/users?page={id}
@pytest.mark.parametrize('id_page, status_code', test_list_users_get)
def test_get_list_users(base_url, get_api_list_users, id_page, status_code):
    print("Method Get delay", base_url + get_api_list_users + id_page)
    response = Reqres_api.get_request(base_url + get_api_list_users + id_page)
    assert status_code == response.status_code, f"Код ОР {status_code} не соответствует ФР {response.status_code}"
