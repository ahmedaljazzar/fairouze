# Fairuze
The largest database for Arabic lyrics on the web!

## Installation
### Create DB
```shell
$ mysql -uroot 
mysql> CREATE DATABASE fairuze DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci;
```

### Getting Project (Ubuntu/osX)
```shell
$ git clone git@github.com:ahmedaljazzar/fairuze.git 
$ cd fairuze
$ mkvirtualenv fairuze -p python3 -r requirements.txt
$ python manage.py migrate
```

## Running server
```shell
$ python manage.py runserver 
```




# فيروزيّ
الموقع العربي الأكبر لكلمات الأغاني!‏

## التنزيل
### تحضير قاعدة البيانات
```shell
$ mysql -uroot 
mysql> CREATE DATABASE fairuze DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci;
```

### تحضري المشروع (على أوبنتو وعلى نظام تشغيل الماك)‏
```shell
$ git clone git@github.com:ahmedaljazzar/fairuze.git 
$ cd fairuze
$ mkvirtualenv fairuze -p python3 -r requirements.txt
$ python manage.py migrate
```

## تشغيل الخادم
```shell
$ python manage.py runserver 
```
