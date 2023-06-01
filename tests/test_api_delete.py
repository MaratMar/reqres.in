import pytest
from utils.api import Reqres_api
from utils.test_data import test_data_delete


# Проверка API DELELE /api/users/{id}
@pytest.mark.parametrize('id_user, status_code_response', test_data_delete)
def test_delete_user(base_url, delete_api_users, id_user, status_code_response):
    response = Reqres_api.delete_request(base_url + delete_api_users + id_user)
    status_code = response.status_code
    assert status_code_response == status_code, f"Код ОР {status_code} не соответствует ФР {status_code_response}"
