# Лабораторная работа 4
## Создание контейнеров
Создавать контейнеры и проводить действия с ними будем на виртуальной машине с установленной Ubuntu.

Для создания и работы с двумя Dockerfile создадим 2 папки, куда и поместим их

![screen](https://github.com/cs-itmo-2023/lab-4-dellup/blob/main/1.png)

В каждом Dockerfile пропишем следующие команды:

![screen1](https://github.com/cs-itmo-2023/lab-4-dellup/blob/main/2.png)

Первая строка объявляет операционную систему и ее версию.

Во второй строке apt-get install -y libaa-bin устанавливаем ПО под названием aafire. apt install iputils-ping -y устанавливает утилиту ping.

Далее в терминале в папке с Dockerfile запустим команду сборки образа с тегом aafire
![screen2](https://github.com/cs-itmo-2023/lab-4-dellup/blob/main/3.png)

С помощью команд docker run -it --name one aafire  и  docker run -it --name two aafire запустим каждый из контейнеров. Внутри каждого запустим команду aafire, чтобы показался огонек.
![screen3](https://github.com/cs-itmo-2023/lab-4-dellup/blob/main/5.png)
## Создание сети
Далее создадим сеть и подключим к ней каждый из контейнеров
![screen4](https://github.com/cs-itmo-2023/lab-4-dellup/blob/main/6.png)

Данные о контейнерах в сети выглядят так
![screen5](https://github.com/cs-itmo-2023/lab-4-dellup/blob/main/7.png)

После поключимся из другого окна терминала к каждому из контейнеров, не прерывая их, с помощью команды docker attach и в каждом из них запустим команду ping для другого
![screen6](https://github.com/cs-itmo-2023/lab-4-dellup/blob/main/8.png)

Как мы видим, пакеты не теряются, а значит подключение установлено
