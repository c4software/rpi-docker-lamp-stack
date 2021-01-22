# RaspberryPi 32bit Docker based LAMP stack

The purpose of this image is to quicly build a LAMP stack with Docker using a Raspberry Pi 4 **32bit**.

**WIP Project**

- PHP (7)
- tobi312/rpi-mariadb (not the official image since armv7 is not supported)
- adminer

TODO:
- Multi-users hosting :
  - [ ] Add FTP in the compose-stack for multi-users file upload
  - [ ] Customize the PHP Docker to enable «per userpublic directory aka ~/username »

**FOR TESTING/EVALUATION ONLY - NOT FOR PRODUCTION**
**I REPEAT DO NOT USE IT IN PRODUCTION**

## Quick use

```sh
docker-compose up -d
```

- [Access to your server (should serve the server phpinfo())](http://localhost:9000/)
- [Access to adminer](http://localhost:9000/adminer/)

For adminer :

```
host: mariadb
user: root
password: secret
```
