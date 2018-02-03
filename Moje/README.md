#UWSGI

##Uruchamianie
ręcznie 

    uwsgi --http :8080 --home /home/pi/Env/Strona --chdir /home/pi/Strona -w Django.wsgi



##uruchom z konfiguracji 
    sudo uwsgi --ini uwsgi.ini

plik ini do /etc/uwsgi/sites/


## Ustawienie uwsgi.service

    sudo ln -s system.service /etc/systemd/system/uwsgi.service
