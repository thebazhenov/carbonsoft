ARG VERSION
FROM docker-registry.evateam.ru/evateam:${VERSION}
LABEL maintainer='klinskih@gmail.com'
ARG ADMIN_EMAIL
ARG DOMAIN
ARG BRANCH
# Ключи для ssh
COPY root /root
RUN chown -R root: /root && chmod 600 /root/.ssh/*
RUN chmod +x /root/bin/*
EXPOSE 22

# Настройки
COPY CONFIG /mnt/shared/config/CONFIG
COPY environment.ts /mnt/shared/config/eva-app

RUN echo ADMIN_EMAIL=$ADMIN_EMAIL >> ./mnt/shared/config/CONFIG
RUN echo DOMAIN=$DOMAIN >> ./mnt/shared/config/CONFIG
RUN echo "test_settings = {\
        'login': '$ADMIN_EMAIL',\
        'password': 'servicemode',\
        'phone': '+71234567890',\
        'crm': 'https://$DOMAIN',\
        'account': 'https://${DOMAIN}',\
        'signup_salt': 'd4e80877fa8d72263916090ae6a5c765',\
        'signup_hash': '970e6b6e305838846508992d6580560df6a1ceeb8b481b8d859cd72c21a4a97d'\
}" >> ./mnt/shared/config/eva-app/config.py
RUN echo "RAISE_LAZYLOAD = True" >> ./mnt/shared/config/eva-app/config.py
RUN echo "UPLOAD_DIR = '/mnt/shared/files/'" >> ./mnt/shared/config/eva-app/config.py
RUN apt-get update && apt-get install -y build-essential g++ libnet1 libnl-3-200 libprotobuf-c1 python3-protobuf npm
RUN ssh-keyscan -t rsa gitrd.carbonsoft.ru >> /root/.ssh/known_hosts
RUN /bin/python3 -m pip install -U bandit

ENTRYPOINT service ssh start && /wrapper 2>&1 | tee /var/log/init.log
