# Raspberry Pi 4 32bits Docker based LAMP stack

WIP Project

- PHP (7)
- mariadb (not the official image since armv7 is not supported)
- adminer

FOR TEST ONLY - DO NOT USE IT FOR PRODUCTION

## Quick use

```sh
docker-compose up -d
```

[Access to your server](http://localhost:9000/)
[Access to adminer](http://localhost:9000/adminer/)

For adminer :

```
host: mariadb
user: root
password: secret
```
