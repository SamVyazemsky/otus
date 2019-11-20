*** Settings ***
Library  Selenium2Library
Library  Selenium2Library

*** Variables ***
${URL}          https://demo23.opencart.pro/admin
# ${BROWSER}      Chrome

*** Test Cases ***
The user can open AdminPanel by Chrome
        The user can open AdminPanel  Chrome
The user can open AdminPanel by Firefox
       The user can open AdminPanel  Firefox

*** Keywords ***
The user can open AdminPanel
    [Arguments]      ${BROWSER1}
    Open browser    ${URL}   ${BROWSER1}
    Input Text      id:input-username     demo
    Input Text      id:input-password     demo
    Click Button    css:button[type='submit']
    Close browser
