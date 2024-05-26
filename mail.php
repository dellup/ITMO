<?php
$name = $_GET['name'];
$phone = $_GET['phone'];

$to_email = 'zenindanil2000@gmail.com';
$subject = 'Даня, пиши код сам';
$message = 'Даня, данные пришли, смотри: ' + $name + 'Это - его имя, а это - ' + $phone + 'Его номер теелфонра. Вызвывай на него психушку';
$headers = 'From: progulkinakatere@gmail.com';
mail($to_email,$subject,$message,$headers);

?>