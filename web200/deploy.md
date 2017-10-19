Если деплой на хероку, то:
1 - логинимся в хероку
2 - создаем приложение хероку "heroku apps:create not-yours"
3 - заливаем репозиторий "git push heroku master"
4 - накатываем миграции "heroku run rake db:migrate"
5 - заталкиваем флаг в бд "heroku run rake db:seed"
