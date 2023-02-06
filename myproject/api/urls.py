from django.urls import path
from .views import ProfileApiView
from .views import BookApiView
from .views import update,updaterecord,delete,addrecord,details,report,login,signup
from rest_framework import routers
urlpatterns = [
    path('', login , name="login"),
    path('register/' , signup , name="register"),
    path('home/',ProfileApiView.as_view(), name="profile"),
    path('update/<int:id>', update, name='update'),
    path('update/updaterecord/<int:id>', updaterecord, name='updaterecord'),
    path('delete/<int:id>', delete, name='delete'),
    path('home/addrecord/', addrecord, name='addrecord'),
    path('home/details/<int:id>',details,name="details"),
    path('report/',report,name="report"),   
]

rout = routers.SimpleRouter()
rout.register('api',BookApiView,basename="api")
urlpatterns += rout.urls
