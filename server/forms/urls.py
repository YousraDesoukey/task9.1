from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import FormsList, FormsDetail

urlpatterns = [

    # /profile/
    url(r'^$', FormsList.as_view(), name="get-all"),
    #/profile/id
    url(r'^(?P<id>[0-9]+)/$', FormsDetail.as_view(), name="get-certain"),

]

