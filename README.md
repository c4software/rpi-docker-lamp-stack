# Raspberry Pi 4 32bit Docker based LAMP stack

The purpose of this image is to quicly build a LAMP stack with Docker using a Raspberry Pi 4 **32bit**.

**WIP Project**

- PHP (7)
- tobi312/rpi-mariadb (not the official image since armv7 is not supported)
- adminer

TODO:
- Multi-users hosting.
- Add FTP to quickly upload user file in the stack.
- Customize the PHP Docker to enable «per user folder ~/username »

**FOR TEST ONLY - DO NOT USE IT FOR PRODUCTION**

## Quick use

```sh
docker-compose up -d
```

[Access to your server (should serve the server phpinfo())](http://localhost:9000/)
[Access to adminer](http://localhost:9000/adminer/)

For adminer :

```
host: mariadb
user: root
password: secret
```
