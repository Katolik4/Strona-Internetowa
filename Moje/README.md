#UWSGI
##uruchom z konfiguracji 
sudo uwsgi --ini uwsgi.ini


## Ustawienie uwsgi.service

sudo ln -s system.service /etc/systemd/system/uwsgi.service
