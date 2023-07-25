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

![Dashboard](https://github.com/araheem5133/hodl/assets/140485628/f942310c-80f0-402b-9586-a9855f7752b6)

#### Algorithms and full trading history can also be viewed through the application, along with a watch list that follows a stock price.
Trading history takes into note every single buy or sell trigger that was implement by the algorithm so the user can have a strict knowledge on how many sells or buys their algorithm does in a week. Watch list stocks can follow anything currently supported by the Alpaca stock API

![Dashboard 2](https://github.com/araheem5133/hodl/assets/140485628/2db74dcb-8611-4b5a-9a4b-88be3f6cb962)

### Preset strategies can also be enabled through the application for those newer to trading or just experimenting.
Strategies currently provided for preset are the following:
* Moving Average
* RSI (Relative Strength Indicator)
* Average True Range
* Bollinger Bands
* MACD with Fib. Levels

![Algorithms](https://github.com/araheem5133/hodl/assets/140485628/9fd5a76e-3c84-4084-8b6c-5b2e3c7d8ee5)

### Built-in backtesting module that allows a user to test a custom strategy over up to seven years of data before implementing it.
Parameters are changed dynamically depending on the algorithm chosen, explanations of all of the provided algorithms are given on the HODL help page for any new users. The engine is strict with provided parameters and will check them prior to use in order to prevent error.

![Backtesting 1](https://github.com/araheem5133/hodl/assets/140485628/20273112-8e65-43f0-b98e-fd95ec7c4059)
![Backtesting 2](https://github.com/araheem5133/hodl/assets/140485628/5f28ef3d-dda0-44bd-bed4-1823046ab43e)

### Indicator analysis is also provided for a more in-depth look on buy and sell triggers.
![Indicator 1](https://github.com/araheem5133/hodl/assets/140485628/3998f55c-f2bf-4822-b0c9-dda7c1e29add)
![Indicator 2](https://github.com/araheem5133/hodl/assets/140485628/259c422d-f916-41f1-b615-e027548f0397)
![Indicator 3](https://github.com/araheem5133/hodl/assets/140485628/012e3be6-a82f-41a8-b690-667a0e90e0e3)

More to come in the future!
