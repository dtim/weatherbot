# Пример сервиса для погодного бота в Dialogflow

Бот отвечает на вопросы о погоде в том или ином городе.

  * _What is the weather in St. Petersburg?_
  * _How cold is in Helsinki now?_
  * _How strong is the wind in Tokyo?_

Развертывание в Heroku:

```bash
git clone git@github.com:dtim/weatherbot.git
cd weatherbot
heroku login # при первом использовании CLI
heroku create
git push heroku master
```
