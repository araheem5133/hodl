# HODL
## An automated tool by which the average retail investor can design and implement their own algorithmic trading strategy. Functions with a built-in back tester to test any created strategies before they ever hit the market.
### Written and designed in Python while utilizing the Django REST framework.

## Pre-requirements
Python3 and pip installed

## Database Setup
#### Use local database:
In HODL/settings.py, DATABASE section, uncomment sqlight3 database details. Comment out postgresql database detail.  

#### Use AWS postgresql database:
In HODL/settings.py, DATABASE section, comment out sqlight3 database details. Uncomment out postgresql database detail. Create an .env file in the same directory as setting.py, store database variables there.  

## To run the project
run command below to install dependencies\
pip install -r requirements.txt 

run command below to migrate database \
python3 manage.py makemigrations \
python3 manage.py migrate

run command below to run the project\
python3 manage.py runserver 

## Off-site Requirements
Creating a HODL account requires an Alpaca security key and an email. You can acquire one for free by signing up at https://alpaca.markets/

## Features
### HODL comes with a fully responsive dashboard that tracks the overall value of your account as well as any positions you currently have.
Tracks your Alpaca account in real time, along with showing the user any percent change for the day as well as any currently open positions that the user may have.

![Dashboard](https://github.com/araheem5133/hodl/assets/140485628/200d52aa-444a-4e7e-8258-0c100349a0b1)

#### Algorithms and full trading history can also be viewed through the application, along with a watch list that follows a stock price.
Trading history takes into note every single buy or sell trigger that was implement by the algorithm so the user can have a strict knowledge on how many sells or buys their algorithm does in a week. Watch list stocks can follow anything currently supported by the Alpaca stock API

![Dashboard 2](https://github.com/araheem5133/hodl/assets/140485628/d1bab064-526c-4e74-9d32-fde8407b7b3a)

### Preset strategies can also be enabled through the application for those newer to trading or just experimenting.
Strategies currently provided for preset are the following:
* Moving Average
* RSI (Relative Strength Indicator)
* Average True Range
* Bollinger Bands
* MACD with Fib. Levels

![Algorithms](https://github.com/araheem5133/hodl/assets/140485628/be431201-ffd5-4875-93b2-5485a1cccd09)

### Built-in backtesting module that allows a user to test a custom strategy over up to seven years of data before implementing it.
Parameters are changed dynamically depending on the algorithm chosen, explanations of all of the provided algorithms are given on the HODL help page for any new users. The engine is strict with provided parameters and will check them prior to use in order to prevent error.

![Backtesting 1](https://github.com/araheem5133/hodl/assets/140485628/9ebccab4-ab6d-41e7-be2c-5f8565174903)
![Backtesting 2](https://github.com/araheem5133/hodl/assets/140485628/67eedb8d-966b-4fde-8e5a-dcc531474934)


### Indicator analysis is also provided for a more in-depth look on buy and sell triggers.
![Indicator Analysis 1](https://github.com/araheem5133/hodl/assets/140485628/c8764df3-e257-4666-ac7e-1f217aa0d481)
![Indicator Analysis 2](https://github.com/araheem5133/hodl/assets/140485628/84e6348b-5e48-460b-8304-5a0b19971075)
![Indicator Analysis 3](https://github.com/araheem5133/hodl/assets/140485628/1d811383-59f3-4357-8dd2-63bdd96a6ea7)


More to come in the future!
