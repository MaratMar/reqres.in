import time
import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def base_url():
    print('\nStart...')
    base_url = "https://reqres.in"
    yield base_url
    print("\nThe End..")


@pytest.fixture(scope="function")
def get_api_user():
    url = "/api/users/"
    yield url


@pytest.fixture(scope="function")
def get_api_list_users():
    url = "/api/users?page="
    yield url


@pytest.fixture(scope="function")
def get_api_unknown():
    url = "/api/unknown/"
    yield url


@pytest.fixture(scope="function")
def get_api_delay():
    url = "/api/users?delay="
    yield url


@pytest.fixture(scope="function")
def post_api_create():
    url = "/api/users"
    yield url


@pytest.fixture(scope="function")
def post_api_register():
    url = "/api/register"
    yield url


@pytest.fixture(scope="function")
def post_api_login():
    url = "/api/login"
    yield url


@pytest.fixture(scope="function")
def put_api_users():
    url = "/api/users/"
    yield url


@pytest.fixture(scope="function")
def patch_api_users():
    url = "/api/users/"
    yield url


@pytest.fixture(scope="function")
def delete_api_users():
    url = "/api/users/"
    yield url


@pytest.fixture(scope="function")
def browser():
    print("\nStart chrome browser for test..")
    browser = webdriver.Chrome()

    yield browser
    print("\nquit browser..")
    browser.quit()
