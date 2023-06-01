import pytest
from utils.api import Reqres_api
from utils.test_data import test_data_patch


# Проверка PATCH API /api/users/{id}
@pytest.mark.parametrize('id_user, json_request, json_response, status_code_response', test_data_patch)
def test_update_user_patch(base_url, patch_api_users, id_user, json_request, json_response, status_code_response):
    response = Reqres_api.patch_request(base_url + patch_api_users + id_user, json_body=json_request)
    status_code = response.status_code
    assert status_code_response == status_code, f"Код ОР {status_code} не соответствует ФР {status_code_response}"
    assert json_response['name'] == response.json()['name'], f"ОР {json_response['name']} не соответствует ФР {response.json()['name']}"
    assert json_response['job'] == response.json()['job'], f"ОР {json_response['job']} не соответствует ФР {response.json()['job']}"
    assert list(json_response.keys()) == list(response.json().keys()), "Схема ОР, не соответствует ФР"
