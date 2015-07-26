## Synopsis

This project extends the [django-xadmin](https://github.com/sshwsfc/django-xadmin) demo_app with a simple RSS feed reader widget. 

## Motivation

Tinkering around while I try to learn some python/django...

## Run the demo locally

1. Create a directory and copy/clone the content of this repository into it
	```
	mkdir demo_app
	cd demo_app
	git clone https://github.com/zwollander/django-xadmin-rss.git
	``` 
2. Install django-xadmin
	```
	pip install django-xadmin
	```
3. Sync the database (you will be prompted to create a superuser also)
	```
	./manage.py syncdb
	```
4. Run the web server
	```
	./manage.py runserver
	```
5. Open [http://localhost:8000/xadmin/](http://localhost:8000/xadmin/) in your browser. Log in with the superuser you created. Now you can add the new widget (type **rssfeedreader**) to your admin page.


