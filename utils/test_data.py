# API DELETE /api/users/{id} (id, код ответа)
test_data_delete = {
    ('2', 204)
}

# API PATCH API /api/users/{id} (id, тело запроса, тело ответа, код ответа)
test_data_patch = [
    ('2', {"name": "morpheus", "job": "zion resident"}, {"name": "morpheus", "job": "zion resident","updatedAt": "2023-05-31T15:05:20.010Z"}, 200)
]

# API POST API /api/users (тело запроса, тело ответа, код ответа)
test_data_create_user_post = [
    ({"name": "morpheus", "job": "leader"}, ['name', 'job', 'id', 'createdAt'], 201)
]

# API POST API /api/register (тело запроса, тело ответа, код ответа)
test_data_register_post = [
    ({"email": "eve.holt@reqres.in", "password": "pistol"}, {"id": 4, "token": "QpwL5tke4Pnpja7X4"}, 200),
    ({"email": "sydney@fife"}, {"error": "Missing password"}, 400)]

# API POST API /api/login (тело запроса, тело ответа, код ответа)
test_data_login_post = [
    ({"email": "eve.holt@reqres.in", "password": "cityslicka"}, {"token": "QpwL5tke4Pnpja7X4"}, 200),
    ({"email": "peter@klaven"}, {"error": "Missing password"}, 400)]

# API PUT /api/users/{id} (id, тело запроса, тело ответа, код ответа)
test_data_put = [
    ('2', {"name": "morpheus", "job": "zion resident"}, {"name": "morpheus", "job": "zion resident","updatedAt": "2023-05-31T15:05:20.010Z"}, 200)
]

# API GET /api/users/{id} (id, тело ответа, код ответа)
test_data_user_get = [
    ('2', {"data": {"id": 2, "email": "janet.weaver@reqres.in", "first_name": "Janet", "last_name": "Weaver",
                    "avatar": "https://reqres.in/img/faces/2-image.jpg"},
           "support": {"url": "https://reqres.in/#support-heading",
                       "text": "To keep ReqRes free, contributions towards server costs are appreciated!"}}, 200),
    ('200', {}, 404)
]

# API GET  /api/unknown/{id} (id, код ответа)
test_data_unknown_get = [
    ('', 200),
    ('2', 200),
    ('23', 404)
]

# API GET /api/users?delay={id} (id, код ответа)
test_data_delay_get = {
    ('3', 200)
}

# API GET /api/users?page={id} (id, код ответа)
test_list_users_get = {
    ('2', 200)
}
