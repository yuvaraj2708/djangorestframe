from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.renderers import TemplateHTMLRenderer
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from fpdf import FPDF
from django.http import FileResponse
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
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
    'page' : page,
     'count': book_paginator.count,
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



def report(request):
    sales = [
        {"item": "Keyboard", "amount": "$120,00"},
        {"item": "Mouse", "amount": "$10,00"},
        {"item": "House", "amount": "$1 000 000,00"},
    ]
    pdf = FPDF('P', 'mm', 'A4')
    pdf.add_page()
    pdf.set_font('courier', 'B', 16)
    pdf.cell(40, 10, 'This is what you have sold this month so far:',0,1)
    pdf.cell(40, 10, '',0,1)
    pdf.set_font('courier', '', 12)
    pdf.cell(200, 8, f"{'Item'.ljust(30)} {'Amount'.rjust(20)}", 0, 1)
    pdf.line(10, 30, 150, 30)
    pdf.line(10, 38, 150, 38)
    for line in sales:
        pdf.cell(200, 8, f"{line['item'].ljust(30)} {line['amount'].rjust(20)}", 0, 1)
    pdf.output('report.pdf', 'F')
    return FileResponse(open('report.pdf', 'rb'), as_attachment=True, content_type='application/pdf')


class BookApiView(ModelViewSet):
    queryset = Profiles.objects.all()
    serializer_class=ProfileSerializer
    permission_class = [IsAuthenticated ] 
    

def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            try:
                User.objects.get(username = request.POST['username'])
                return render (request,'register.html', {'error':'Username is already taken!'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                auth.login(request,user)
                return redirect('')
        else:
            return render (request,'register.html', {'error':'Password does not match!'})
    else:
        return render(request,'register.html')

@login_required
def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password = request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('home/')
        else:
            return render (request,'login.html', {'error':'Username or password is incorrect!'})
    else:
        return render(request,'login.html')