﻿# Запуск pytest -v --tb=line --language=en test_main_page.py

from pages.main_page import MainPage


def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

