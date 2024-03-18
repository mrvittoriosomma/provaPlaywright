import pytest
from playwright.sync_api import Playwright
from function import *

#parametrizzazione di un test
@pytest.mark.parametrize("test_input_user,test_input_pass", get_data("Book1.xlsx", "Sheet1"))
def test_login_wordpress(test_input_user, test_input_pass, playwright: Playwright):
    try:
        loginWordPress(test_input_user, test_input_pass, playwright)
        print("Login OK")
    except:
        pytest.fail("Login FAIL", pytrace=False)
