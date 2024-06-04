<?php
$name = $_POST['name'];
$phone = $_POST['phone'];

$name = htmlspecialchars($name);
$phone = htmlspecialchars($phone);

$name = urldecode($name);
$phone = urldecode($phone);

$name = trim($name);
$phone = trim($phone);


if (mail("zenindanil2000@gmail.com",
        "Новая заявка",
        "Имя: ".$name."\n".
        "Телефон: ".$phone,
        "From: zenindanil2004@gmail.com \r\n")
) {
    echo("Письмо отправлено!");
}
else {
    echo("Есть ошибки! Проверьте данные...");
}

?>