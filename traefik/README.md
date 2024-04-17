* Сгенерируйте самоподписной ключ в data/certs/cert.crt, cert.key например для *.kag2.fake
```bash
mkdir data/certs/; cd data/certs/; openssl req -x509 -out cert.crt -keyout cert.key -newkey rsa:2048 -nodes -sha256 -subj '/CN=*.dev.fake'
```
* добавьте один раз сеть для связи траефика с образами jira и confluence
```bash
docker network create carbon
```
* пропишите домен для которого сгенерировали сертификат в .env
* запустите
```bash
docker-compose up -d
```
<br>Если виртуалка будет смотреть наружу, то можно подключить Lets encrypt

> **Внимание:** для Windows надо отключить taffic-shaper в docker-compose.yml
