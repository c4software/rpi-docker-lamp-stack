<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Docker LAMP Stack for RaspberryPi</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
    <style>
        body {
            padding-top: 5rem;
        }
    </style>
</head>
<body>
    <nav class="navbar navbar-expand-md navbar-dark bg-primary fixed-top">
        <div class="container-fluid">
            <a class="navbar-brand" href="#">Docker LAMP Stack for RaspberryPi</a>
            <div class="d-flex">
                <a href="/adminer" class="btn btn-outline-light">Adminer</a>
            </div>
        </div>
    </nav>

    <main class="container">
        <h4 class="text-center mt-2 mb-4">Please upload your files using your favorite FTP Software.</h4>

        <?php 
            $dirs = array_diff(glob('users/*', GLOB_ONLYDIR),  array('..', '.'));

            if(sizeof($dirs) > 0){
        ?>
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
        <?php
            }
        ?>

        <hr />
        <h2>This Docker Stack include</h2>
        <ul>
            <li>PHP 7</li>
            <li>MariaDB</li>
            <li><a href="/adminer">Adminer</a></li>
            <li>Apache mod_userdir to allow multi user document root</li>
            <li>Basic <a href="ftp://raspberrypi.local">FTP Server</a></li>
        </ul>
    </main>
</body>
</html>
