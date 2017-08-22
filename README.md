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

## License
The code in this repository is licensed under version 3 of the AGPL unless otherwise noted. Please see the [LICENSE](https://github.com/ahmedaljazzar/fairuze/blob/master/LICENSE) file for details.

Copyright (c) 2017 Ahmed Jazzar <me@ahmedjazzar.com>




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
## الرخصة

إن هذا النص المصدري محمي بموجب ترخيص رخصة أفيرو العمومية بإصدارها الثالث مالم يتم النص على غير ذلك بصراحة. رجاء زُر صفحة [الرخصة](https://github.com/ahmedaljazzar/fairuze/blob/master/LICENSE) للمزيد من المعلومات.‏

٢٠١٧ أحمد جزار. جميع الحقوق محفوظة.‏ (c) 
