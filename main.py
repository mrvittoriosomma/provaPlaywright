import pytest
from playwright.async_api import expect
from playwright.sync_api import Playwright, sync_playwright, expect
from function import *

def test_api_login(playwright: Playwright):
    api_login(playwright)

