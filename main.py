import pytest
from playwright.sync_api import Page
from function import *

def test_api_login(playwright: Playwright):
    api_login(playwright)

