from django.urls import path
from .views import ProfileApiView,BookApiView
from .views import update,updaterecord,delete,addrecord,details,report,login,signup

urlpatterns = [
    path('', login , name="login"),
    path('register/' , signup , name="register"),
    path('home/',ProfileApiView.as_view(), name="profile"),
    path('api/',BookApiView.as_view()),
    path('update/<int:id>', update, name='update'),
    path('update/updaterecord/<int:id>', updaterecord, name='updaterecord'),
    path('delete/<int:id>', delete, name='delete'),
    path('home/addrecord/', addrecord, name='addrecord'),
    path('home/details/<int:id>',details,name="details"),
    path('details/report/<int:id>',report,name="report"),   
]