* ДЛЯ WINDOWS ПОЛЬЗОВАТЕЛЕЙ НАДО ВСЕ ФАЙЛЫ СКРИПТОВ И КОНФИГОВ ПРЕОБРАЗОВАТЬ В LINUX СПОМОЩЬЮ NOTEPAD++
* 
* Добавьте ssh ключ в root/.ssh/authorized_keys
* Добавьте id_rsa в root/.ssh, чтобы сразу иметь доступ к гиту
``` 
ssh-keygen -f /home/devel/containers-test/eva_app/root/.ssh/id_rsa
```
Чтобы узнать последнюю доступную версию
``` 
python3 get_version.py devel
``` 
* Укажите версию, домен, почту, traefik имя сервиса и ssh порт в .env
* Для запуска
``` 
docker-compose up -d --build
```
* Для подключения к консоли
``` 
docker-compose exec app bash
``` 

* В консоли виртуалки инициализировать git-репозитории с обновлением на последние коммиты
* Указать ветку вместо $BRANCH
``` 
/root/bin/init_git $BRANCH
``` 
* Сделать дамп bcrm и накатить
```
/root/bin/get_bcrm
```
* Подпуллить crm и обновить бэк (для разработки фронта в команде на одной ветке)
```
/root/bin/pull_crm
```
* Подпулить и обновить все
```
/root/bin/update_all
```
* Зарегистрировать пользователя
``` 
/opt/bin/register.sh
```
