# Docker LAMP Stack for RaspberryPi (32bit)

The purpose of this image is to quicly build a LAMP stack with Docker using a Raspberry Pi 4 **32bit**.

- Web : Apache + PHP (php 7 & adminer)
- Database : `tobi312/rpi-mariadb` (not the official image since armv7 is not supported)
- FTP: custom ftp service to upload your source remotely (password & username should be the same, ex. `user: sample` & `pass: sample`)

**FOR TESTING/EVALUATION ONLY - NOT FOR PRODUCTION**
**I REPEAT DO NOT USE IT IN PRODUCTION**

## Quick usage

```sh
docker-compose up -d
```

- [Access to your server (should serve the server phpinfo())](http://raspberrypi.local/)
- [Access to adminer](http://raspberrypi.local/adminer/)

Adminer configuration to specify :

```sh
host: mariadb
user: root
password: secret
```

## How to upload your files

The provided docker stack include an FTP server. This FTP server is not meant _to be open to the public_; Its accepts connections from all user / password pairs as long as they are identical.

## Example

If you login with the username `valentin` the password will be `valentin`. The document root of the user `valentin` will be automaticaly created on the first connexion.

After that your files will be available via a browser at :

[http://raspberrypi.local/~valentin](http://raspberrypi.local/~valentin)

## Live example

[![Démo vidéo](./preview.jpg)](https://www.youtube.com/watch?v=yYruyRbhyPU)
