## Synopsis

This project extends the [django-xadmin](https://github.com/sshwsfc/django-xadmin) demo_app with a simple RSS feed reader widget. 

```python
class RssFeedReaderWidget(BaseWidget):
    widget_type = 'rssfeedreader'
    widget_icon = 'fa fa-rss'
    description =  u'An (extremely simple) RSS feed reader.'

    title = forms.CharField(label='Title', required=True)
    link = forms.URLField(label='Link', required=True)
    limit = forms.IntegerField(min_value=1, max_value=20, required=True)

    def has_perm(self):
        return True

    def context(self, context):
        feeds = feedparser.parse(self.cleaned_data['link'])
        feed_template = Template('<a href="$link"> $title </a><hr>')

        content = ''
        for feed in feeds.entries[:self.cleaned_data['limit']]:
            content += feed_template.substitute(link=feed.link, title=feed.title)
        content = content[:-4]

        context['content'] = content
```

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


