# 4-20-FIlms
**4:20 Films** is a web-server for film streaming. Films can be either watch online or download via web-page. Developed with ***Django***. For production use, I used ***Nginx-Gunicorn-Django*** combination.

*this repository only include the ***Django*** proyect. ***Nginx*** and ***Gunicorn*** configuration files and sockets are **not included**. Film files are also not included ;)

![](docs/420_index.jpg)
![](docs/420_film.jpg)
![](docs/420_director.jpg)

## Structure
* **appMediaCenter**: ***Django*** web-server application.
  * **migrations**: migratios dir.
  * **static**: static dir.
    * **admin**: I included here the admin application's static files. 
    * **css**: css style files.
    * **fonts**: font files.
    * **js**: js scripts that are used in the server.
    * **media**: the media corresponding to the films and directors.
  * **templates**: different templates used in the server.
    * **base.html**: main layout where other html files are inserted on runtime. The other html files extend from this one.
    * **director.html**: html file corresponding to the director view.
    * **film.html**: html file corresponding to the film view.
    * **index.html**: html file corresponding to the index view.
  * **admin.py**: all the admin configuration for managing the django application.
  * **apps.py**: here is the appMediaCenter declared
  * **models.py**: here the different data structures (models) used in the application are declared. 
  * **urls.py**: here the different routes used in the application are declared.
  * **views.py**: different views used in the application
* **MediaCenter**: Default django proyect folder
  * **settings.py**: server settings are configured here
  * **urls.py**: routes of the proyect. link between application urls.
  * **wsgi.py**: wsgi config for the proyect. Wsgi is used to connect ***Django*** with ***Gunicorn*** 
* **db.sqlite3**: db for the proyect. Is preferible to use other SGBD as ***mysql*** or ***postgresql***; ***sqlite*** is for little development projects.
* **manage.py**: ***Django's*** command-line utility for administrative tasks. Run administrative tasks.

## Command
* python manage.py runserver
