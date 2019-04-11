# Пример сервиса для погодного бота в Dialogflow

Бот отвечает на вопросы о погоде в том или ином городе.

  * _What is the weather in St. Petersburg?_
  * _How cold is in Helsinki now?_
  * _How strong is the wind in Tokyo?_

Развертывание в Heroku:

``
shell> git clone git@github.com:dtim/weatherbot.git

shell> cd weatherbot

shell> heroku login # при первом использовании CLI

shell> heroku create

shell> git push heroku master
``
