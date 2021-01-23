<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Docker LAMP Stack for RaspberryPi</title>
</head>
<body>
    <h1>Welcome home</h1>
    <p>Please upload your files using your favorite FTP Software.</p>

    <h2>Current user(s) base directory</h2>
    <ul>
        <?php
            $dirs = scandir("./users/");

            foreach ($dirs as $dirs) {
                echo "<li><a href='/~$dir'>~$dir</a></li>";
            }
        ?>
    </ul>

    <h2>This Docker Stack include</h2>
    <ul>
        <li>PHP 7</li>
        <li>Adminer</li>
        <li>Apache mod_userdir to allow multi user document root</li>
        <li>Basic FTP Server</li>
    </ul>
</body>
</html>