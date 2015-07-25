from django import forms
import feedparser
from string import Template 

import xadmin
from xadmin.views.dashboard import BaseWidget, widget_manager


@widget_manager.register
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









