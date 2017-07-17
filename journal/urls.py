from django.conf.urls import url, include
from journal import views

urlpatterns = [
    url("^$", views.journal_list, name='journal-list'),
    url("^(?P<slug>.*)/$",
        views.journal_detail, name="journal-detail"),
]
