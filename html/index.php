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

    <hr />
    <h2>Current user(s) base directory</h2>
    <ul>
        <?php
            $dirs = array_diff(glob('users/*', GLOB_ONLYDIR),  array('..', '.'));

	    foreach ($dirs as $dir) {
		    $dir = basename($dir);
                echo "<li><a href='/~$dir'>/~$dir/</a></li>";
            }
        ?>
    </ul>

    <hr />
    <h2>This Docker Stack include</h2>
    <ul>
        <li>PHP 7</li>
        <li>Adminer</li>
        <li>Apache mod_userdir to allow multi user document root</li>
        <li>Basic FTP Server</li>
    </ul>
</body>
</html>
