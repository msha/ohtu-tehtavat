*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go to Register Page

***Test Cases***
Register With Valid Username And Password
    Set Username  testi
    Set Password  testi123
    Set Password_confirmation  testi123
    Submit Credentials
    Welcome Page Should Be Open

Register With Too Short Username And Valid Password
    Set Username  es
    Set Password  testi123
    Set Password_confirmation  testi123
    Submit Credentials
    Register Should Fail With Message  Username must be atleast 3 characters long

Register With Valid Username And Too Short Password
    Set Username  testi
    Set Password  es
    Set Password_confirmation  es
    Submit Credentials
    Register Should Fail With Message  Password must be atleast 8 characters long

Register With Nonmatching Password And Password Confirmation
    Set Username  testi
    Set Password  testi12345
    Set Password_confirmation  testi54321
    Submit Credentials
    Register Should Fail With Message  Password does not match password confirmation

Login After Successful Registration
    Set Username  testaaja
    Set Password  testi123
    Set Password_confirmation  testi123
    Submit Credentials
    Welcome Page Should Be Open
    Go To Login Page
    Login Page Should Be Open
    Set Username  testaaja
    Set Password  testi123
    Submit Login
    Login Should Succeed

Login After Failed Registration
    Set Username  tester
    Set Password  testi12345
    Set Password_confirmation  testi54321
    Submit Credentials
    Register Should Fail With Message  Password does not match password confirmation
    Go To Login Page
    Login Page Should Be Open
    Set Username  tester
    Set Password  testi123
    Submit Login
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Submit Credentials
    Click Button  Register

Submit Login
    Click Button  Login

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password_confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}