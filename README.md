# Docker LAMP Stack for RaspberryPi (32bit)

The purpose of this image is to quicly build a LAMP stack with Docker using a Raspberry Pi 4 **32bit**.

**WIP Project**

- Web : Apache + PHP (php 7 & adminer)
- Database : tobi312/rpi-mariadb (not the official image since armv7 is not supported)
- FTP: ftp service to upload your source remotely (password & username should be the same, ex. `user: sample` & `pass: sample`)

**FOR TESTING/EVALUATION ONLY - NOT FOR PRODUCTION**
**I REPEAT DO NOT USE IT IN PRODUCTION**

## Quick usage

```sh
docker-compose up -d
```

- [Access to your server (should serve the server phpinfo())](http://raspberrypi.local/)
- [Access to adminer](http://raspberrypi.local/adminer/)

For adminer :

```
host: mariadb
user: root
password: secret
```

## Upload your files

The docker stack include an FTP server. The FTP server is not meant to be open to the public; Its accepts connections from all user / password pairs as long as they are identical.

## Example :

If you login with the username `valentin` the password will be `valentin`. The document root of `sample` will be automaticaly created on the first connexion. Your file will be available at :

[http://raspberrypi.local/~valentin](http://raspberrypi.local/~valentin)

## Live example

[![Démo vidéo](https://img.youtube.com/vi/yYruyRbhyPU/0.jpg)](https://www.youtube.com/watch?v=yYruyRbhyPU)
