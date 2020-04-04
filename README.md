# django_websocket_restapi_example






<blockquote class="imgur-embed-pub" lang="en" data-id="Y4fZOCy"><a href="https://imgur.com/Y4fZOCy">View post on imgur.com</a></blockquote><script async src="//s.imgur.com/min/embed.js" charset="utf-8"></script>



> Çalışma Mantığı

* Client django sunucuna post isteği gönderir
* Django bu isteği ve json verilerini  veritabanına yazar
* Signals veritabanında yeni bir queryset oluştuğu zaman  kaydedilen veriyi  notifications kanalına gönderir
* websocket dinlediği kanaldan yeni veri geldikçe js yardımıyla bunları grafiğe döker




## Kurulum Server

- git clone https://github.com/erelbi/django_websocket_restapi_example.git
- cd django_websocket_restapi_example
- python3.6 kullanıyorsanız #source venv/bin/active
- yeni bir virtualenv oluşturacaksanız #virtualenv 
- #source venv/bin/active
- server kısmı için gerekli paketler
- pip3 install -r requirements.txt
- son olarak sistem redis-server ihtiyaç duymaktadır.
- sudo apt-get install redis
- sudo yum install redis
-  başlatmak için # redis-server
- django başlatmak için # python3 manage.py runserver 0:8000

## Kurulum Client
- cd django_websocket_restapi_example/client
- virtualenv oluşturacaksanız #virtualenv 
- #source venv/bin/active
- gerekli paketleri yüklemek için requirements.txt dosyasını çalıştırın
- ip adresini kendinize göre değiştirin
- python3 sensors.py




## Lisans

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

- **[MIT license](http://opensource.org/licenses/mit-license.php)**
- Copyright 2020 © <a href="http://deney.site" target="_blank">deney.site</a>.