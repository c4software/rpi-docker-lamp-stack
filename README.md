# Docker LAMP Stack for RaspberryPi (32bit)

The purpose of this image is to quicly build a LAMP stack with Docker using a Raspberry Pi 4 **32bit**.

- Web : Apache + PHP (php 7 & adminer)
- Database : `tobi312/rpi-mariadb` (not the official image since armv7 is not supported)
- FTP: custom ftp service to upload your source remotely (see below for password / username pattern)

| Service |        Port |
| ------- | ----------: |
| HTTP    |          80 |
| FTP     |       20121 |
| SQL     | Not Exposed |

**FOR TESTING/EVALUATION ONLY - NOT FOR PRODUCTION**
**I REPEAT DO NOT USE IT IN PRODUCTION**

![Home Example](./home.png)

## Quick usage

```sh
docker-compose up -d
```

- [LAMP Stack Dashboard Access : http://raspberrypi.local/](http://raspberrypi.local/)
- [Adminer Access : http://raspberrypi.local/adminer/](http://raspberrypi.local/adminer/)

Adminer configuration to specify :

```sh
host: mariadb
user: root
password: MARIADB|secret
```

## FTP : How to upload your files

The provided docker stack include an FTP server. This FTP server is not meant _to be open to the public_; Its accepts connections from all user / password pairs as long as they match the correct pattern.

```sh
# Example
username: john
password: RPI|john|LAMP

# Or
username: valentin
password: RPI|valentin|LAMP

# Or
username: sample
password: RPI|sample|LAMP
```

You can change this behavior by changing the `PASSWORD_PREFIX` and `PASSWORD_SUFFIX` settings in the `environnement.yml` file.

## Example

If you do an FTP login with the username `valentin` the password will be `RPI|valentin|LAMP`.

The document root of the user `valentin` will be automaticaly created on the first connexion.

After that your files will be available via a browser at :

[http://raspberrypi.local/~valentin](http://raspberrypi.local/~valentin)

## Live example

[![Démo vidéo](./preview.jpg)](https://www.youtube.com/watch?v=y7HzFidjKjs)
