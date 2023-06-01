from selenium.webdriver.common.by import By


class GetRequest():
    LIST_USERS = (By.XPATH, '//li[@data-id="users"]')
    SINGLE_USER = (By.XPATH, '//li[@data-id="users-single"]')
    SINGLE_USER_NOT_FOUND = (By.XPATH, '//li[@data-id="users-single-not-found"]')
    LIST_UNKNOWN = (By.XPATH, '//li[@data-id="unknown"]')
    SINGLE_UNKNOWN = (By.XPATH, '//li[@data-id="unknown-single"]')
    SINGLE_UNKNOWN_NOT_FOUND = (By.XPATH, '//li[@data-id="unknown-single-not-found"]')
    DELAY = (By.XPATH, '//li[@data-id="delay"]')


class PostRequest():
    CREATE_USERS = (By.XPATH, '//li[@data-id="post"]')
    REGISTER_SUCCESSFUL = (By.XPATH, '//li[@data-id="register-successful"]')
    REGISTER_UNSUCCESSFUL = (By.XPATH, '//li[@data-id="register-unsuccessful"]')
    LOGIN_SUCCESSFUL = (By.XPATH, '//li[@data-id="login-successful"]')
    LOGIN_UNSUCCESSFUL = (By.XPATH, '//li[@data-id="login-unsuccessful"]')


class DeleteRequest():
    DELETE_USER = (By.XPATH, '//li[@data-id="delete"]')


class PutRequest():
    PUT_USER = (By.XPATH, '//li[@data-id="put"]')


class PatchRequest():
    patch_USER = (By.XPATH, '//li[@data-id="patch"]')


class Request():
    URL = (By.CLASS_NAME, "url")
    OUTPUT = (By.XPATH, '//pre[@data-key="output-request"]')


class Response():
    Response_STATUS_CODE = (By.XPATH, '//span[@data-key="response-code"]')
    Response_BODY = (By.XPATH, '//pre[@data-key="output-response"]')
