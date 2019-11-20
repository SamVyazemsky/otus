*** Settings ***
Documentation    Suite description
Library      opencart_keywords.py
Library  Selenium2Library

*** Test Cases ***
Test title
    [Tags]    Google    Тест    Отус    PythonQA
    Open Google
    Close Browser
