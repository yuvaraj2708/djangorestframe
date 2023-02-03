from django.urls import path
from .views import ProfileApiView,BookApiView
from .views import update,updaterecord,delete,addrecord,details

urlpatterns = [
    path('',ProfileApiView.as_view(), name="profile"),
    path('api/',BookApiView.as_view()),
    path('update/<int:id>', update, name='update'),
    path('update/updaterecord/<int:id>', updaterecord, name='updaterecord'),
    path('delete/<int:id>', delete, name='delete'),
    path('addrecord/', addrecord, name='addrecord'),
    path('details/<int:id>',details,name="details")
]