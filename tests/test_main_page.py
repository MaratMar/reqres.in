import pytest
import ast
import time
from utils.api import Reqres_api
from pages.base_page import BasePage
from pages.locators import Response, Request, GetRequest, PostRequest, PatchRequest, PutRequest, DeleteRequest

link = "https://reqres.in"


@pytest.mark.skip
@pytest.mark.parametrize('selector', {GetRequest.SINGLE_USER,
                                      GetRequest.LIST_USERS,
                                      GetRequest.SINGLE_USER_NOT_FOUND,
                                      GetRequest.DELAY,
                                      GetRequest.LIST_UNKNOWN,
                                      GetRequest.SINGLE_UNKNOWN,
                                      GetRequest.SINGLE_UNKNOWN_NOT_FOUND
                                      })
def test_main_page_method_get(browser, base_url, selector):
    page = BasePage(browser, link)
    page.open()
    print(selector)
    page.go_to_choice(*selector)
    page.waiting_element(*Response.Response_BODY)  # Ждем когда прогрузится эелемент
    text_response = page.get_text(*Response.Response_BODY)
    status_code_response = page.get_text(*Response.Response_STATUS_CODE)
    response_web_body = ast.literal_eval(text_response)
    response_api = Reqres_api.get_request(base_url + page.get_text(*Request.URL))
    print(response_web_body)
    print(response_api.json())
    assert response_web_body == response_api.json(), 'Структура ответа api, не соответсвует указанному web'
    assert status_code_response == str(response_api.status_code), 'Статус код ответа api, не соответсвует коду web'


@pytest.mark.skip
@pytest.mark.parametrize('selector', {PostRequest.CREATE_USERS,
                                      PostRequest.LOGIN_SUCCESSFUL,
                                      PostRequest.LOGIN_UNSUCCESSFUL,
                                      PostRequest.REGISTER_SUCCESSFUL,
                                      PostRequest.REGISTER_UNSUCCESSFUL
                                      })
def test_main_page_method_post(browser, base_url, selector):
    page = BasePage(browser, link)
    page.open()
    print(selector)
    page.go_to_choice(*selector)
    page.waiting_element(*Response.Response_BODY)  # Ждем когда прогрузится эелемент
    text_response = page.get_text(*Response.Response_BODY)
    status_code_response = page.get_text(*Response.Response_STATUS_CODE)
    request_web_body = ast.literal_eval(page.get_text(*Request.OUTPUT))
    response_web_body = ast.literal_eval(text_response)
    response_api = Reqres_api.post_request(base_url + page.get_text(*Request.URL), request_web_body)
    print(response_web_body)
    print(response_api.json())
    assert status_code_response == str(response_api.status_code), 'Статус код ответа api, не соответсвует коду web'
    assert response_web_body == response_api.json(), 'Структура ответа api, не соответсвует указанному web'

@pytest.mark.skip
@pytest.mark.parametrize('selector', {PatchRequest.patch_USER, PutRequest.PUT_USER})
def test_main_page_update(browser, base_url, selector):
    page = BasePage(browser, link)
    page.open()
    print(selector)
    page.go_to_choice(*selector)
    page.waiting_element(*Response.Response_BODY)  # Ждем когда прогрузится эелемент
    text_response = page.get_text(*Response.Response_BODY)
    status_code_response = page.get_text(*Response.Response_STATUS_CODE)
    request_web_body = ast.literal_eval(page.get_text(*Request.OUTPUT))
    response_web_body = ast.literal_eval(text_response)
    response_api = Reqres_api.put_request(base_url + page.get_text(*Request.URL), request_web_body)
    if 'patch' in selector:
        response_api = Reqres_api.patch_request(base_url + page.get_text(*Request.URL), request_web_body)

    print(response_web_body)
    print(response_api.json())
    assert status_code_response == str(response_api.status_code), 'Статус код ответа api, не соответсвует коду web'
    assert response_web_body['name'] == response_api.json()['name'], 'Name ответа api, не соответсвует Name в web'
    assert response_web_body['job'] == response_api.json()['job'], 'Job ответа api, не соответсвует job в web'


@pytest.mark.parametrize('selector', {DeleteRequest.DELETE_USER})
def test_main_page_delete(browser, base_url, selector):
    page = BasePage(browser, link)
    page.open()
    print(selector)
    page.go_to_choice(*selector)
    page.waiting_element(*Response.Response_BODY)  # Ждем когда прогрузится эелемент
    text_response = page.get_text(*Response.Response_BODY)
    status_code_response = page.get_text(*Response.Response_STATUS_CODE)
    response_api = Reqres_api.delete_request(base_url + page.get_text(*Request.URL))
    assert status_code_response == str(response_api.status_code), 'Статус код ответа api, не соответсвует коду web'