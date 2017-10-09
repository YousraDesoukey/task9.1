from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from forms import views

urlpatterns = [

    # /profile/
    url(r'^$', views.FormsList.as_view(), name="get-all"),
    #/profile/id
    url(r'^(?P<id>[0-9]+)/$', views.FormsDetail.as_view(), name="get-certain"),

]

