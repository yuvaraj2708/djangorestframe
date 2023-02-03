from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.renderers import TemplateHTMLRenderer
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
class ProfileApiView(APIView):
    serializer_class=ProfileSerializer
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'home.html'

    def get(self, request):
        queryset = Profiles.objects.all()
        return Response({'profile': queryset})

def index(request):
  mymembers = Profiles.objects.all().values()
  template = loader.get_template('home.html')
  
  books = Profiles.objects.all()

  book_paginator = Paginator(books, 2)

  page_num = request.GET.get('page',5)

  page = book_paginator.get_page(page_num)

  context = {
    'Profiles': mymembers,
    'count' : book_paginator.count,
    'page' : page
  }

  return HttpResponse,ProfileApiView.as_view()(template.render(context, request))       


  

def addrecord(request):
  title = request.POST['title']
  author = request.POST['author']
  phonenumber = request.POST['phonenumber']
  address = request.POST['address']
  status = request.POST['status']

  member = Profiles(title=title, author=author,phonenumber=phonenumber,address=address,status=status)
  member.save()
  return redirect('profile')

def delete(request, id):
       queryset = Profiles.objects.get(id=id)
       queryset.delete()
       return redirect('profile')
    #    return HttpResponseRedirect(reverse('ProfileApiView'))

def update(request, id):
       profiles = Profiles.objects.get(id=id)
       template = loader.get_template('update.html')
       context = {
       'profiles': profiles,
        }
       return HttpResponse(template.render(context, request))
    
def updaterecord(request, id):
  title = request.POST['title']
  author = request.POST['author']
  phonenumber = request.POST['phonenumber']
  address = request.POST['address']
  status = request.POST['status']
  member = Profiles.objects.get(id=id)
  member.title= title
  member.author= author
  member.phonenumber=phonenumber
  member.address=address
  member.status=status
  member.save()
  return redirect('profile')


def details(request, id):
  profiles = Profiles.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'profiles': profiles,
  }
  return HttpResponse(template.render(context, request))




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
                            author=serializer_obj.data.get("author"),
                            phonenumber=serializer_obj.data.get("phonenumber"),
                            address=serializer_obj.data.get("address"),
                            status=serializer_obj.data.get("status")

                            )

        book=Profiles.objects.all().filter(id=request.data["id"]).values()
        return Response({"Message":"New Book Added!", "Book":book})