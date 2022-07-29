from django.urls import path,include
from . import views
from . import tasks
urlpatterns = [
    path('',views.test,name='test'),
]
