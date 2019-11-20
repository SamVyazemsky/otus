*** Settings ***
Documentation    Suite description
Resource  oc-keywords.robot
Library  Selenium2Library

*** Test Cases ***
Тест админки
    Открытие админки опенкарт
    Close Browser