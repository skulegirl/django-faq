from __future__ import absolute_import

from django.conf.urls import *
from . import views as faq_views

urlpatterns = [
    url(r'^$', faq_views.TopicList.as_view(), name='faq_topic_list'),
    # url(r'^submit/$', faq_views.SubmitFAQ.as_view(), name='faq_submit'),
    # url(r'^submit/thanks/$', faq_views.SubmitFAQThanks.as_view(), name='faq_submit_thanks'),
    url(r'^(?P<slug>[\w-]+)/$', faq_views.TopicDetail.as_view(), name='faq_topic_detail'),
    url(
        r'^(?P<topic_slug>[\w-]+)/(?P<slug>[\w-]+)/$', faq_views.QuestionDetail.as_view(),
        name='faq_question_detail'
    ),
]
