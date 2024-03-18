from playwright.async_api import expect
from playwright.sync_api import expect

def api_login(playwright):
    context = playwright.request.new_context()
    data = {
        'login': 'test@test.ru',
        'password': 'test',
        'rememberMe': 1}
    response = context.post("https://freedom24.com/api/check-login-password", data=data)
    assert response.status is 200
    assert response.ok
    print(response.status)
    print(response.body)

