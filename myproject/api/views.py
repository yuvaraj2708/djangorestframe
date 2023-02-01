from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.renderers import TemplateHTMLRenderer
from django.shortcuts import get_object_or_404
# Create your views here.
class ProfileApiView(APIView):
    serializer_class=ProfileSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'home.html'

    def get(self, request):
        queryset = Profiles.objects.all()
        return Response({'profile': queryset})
       
class BookApiView(APIView):
    serializer_class=ProfileSerializer
    def get(self,request):
        allBooks=Profiles.objects.all().values()
        return Response({"Message":"List of Books", "Book List":allBooks})

    def post(self,request):
        print('Request data is : ',request.data)
        serializer_obj=ProfileSerializer(data=request.data)
        if(serializer_obj.is_valid()):

            Profiles.objects.create(id=serializer_obj.data.get("id"),
                            title=serializer_obj.data.get("title"),
                            author=serializer_obj.data.get("author")
                            )

        book=Profiles.objects.all().filter(id=request.data["id"]).values()
        return Response({"Message":"New Book Added!", "Book":book})