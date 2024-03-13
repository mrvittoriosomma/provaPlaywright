import pytest
from playwright.sync_api import Page
from function import *

def test_contattami(page: Page):
    richiamami("3330000000", page)
    print("Richiamami OK")

