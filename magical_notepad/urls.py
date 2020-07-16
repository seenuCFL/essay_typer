from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


app_name = 'magical_notepad'
urlpatterns = [
    path('magical_notepad/index/', views.Home.as_view(), name = 'index'),
    path('magical_notepad/notepad/', views.Data.as_view(), name = 'type'),
]

urlpatterns = format_suffix_patterns(urlpatterns)