from django.urls import path
from .views import ProfileApiView,BookApiView


urlpatterns = [
    path('',ProfileApiView.as_view()),
    path('api/',BookApiView.as_view())
]