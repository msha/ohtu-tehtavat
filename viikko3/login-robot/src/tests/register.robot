*** Settings ***
Resource  resource.robot

*** Test Cases ***

Register With Valid Username And Password
    Input New Command
    Input Credentials  test  testi123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input New Command
    Input Credentials  test  testi123
    Input New Command
    Input Credentials  test  testi123
    Output Should Contain  User with username test already exists

Register With Too Short Username And Valid Password
    Input New Command
    Input Credentials  te  testi123
    Output Should Contain  Username must be atleast 3 characters long

Register With Valid Username And Too Short Password
    Input New Command
    Input Credentials  testi  kek
    Output Should Contain  Password must be atleast 8 characters long

Register With Valid Username And Long Enough Password Containing Only Letters
    Input New Command
    Input Credentials  testi  kekwkekw
    Output Should Contain  Password must contain both letters and numbers