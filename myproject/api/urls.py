from django.urls import path
from .views import ProfileApiView,BookApiView
from .views import update,updaterecord,delete,add,addrecord

urlpatterns = [
    path('',ProfileApiView.as_view(), name="profile"),
    path('api/',BookApiView.as_view()),
    path('update/<int:id>', update, name='update'),
    path('update/updaterecord/<int:id>', updaterecord, name='updaterecord'),
    path('delete/<int:id>', delete, name='delete'),
    path('add/', add, name='add'),
    path('add/addrecord/', addrecord, name='addrecord'),
]