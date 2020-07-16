from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


app_name = 'magical_notepad'
urlpatterns = [
    path('magical_notepad/home/', views.Home.as_view(), name = 'home'),
    path('magical_notepad/notepad/', views.Data.as_view(), name = 'type'),
]

urlpatterns = format_suffix_patterns(urlpatterns)