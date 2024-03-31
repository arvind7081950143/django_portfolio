from django.shortcuts import render,redirect
from service.models import service
from projects.models import projects
from formdata.models import formdata
from news.models import News
from skill.models import skill
from django.core.mail import send_mail
def home(request):
    skill_image=skill.objects.all()
    newsservice=News.objects.all()
    data={'newsdata':newsservice,'skillimg':skill_image}
    return render(request,"index.html",data)
def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('meassage')
        en=formdata(name=name,email=email,message=message)
        en.save()
    return render(request,"contact.html")
def project(request):
    projectdata=projects.objects.all()
    data={'projectdata':projectdata}
    return render(request,"project.html",data)
def services(request):
    servicedata=service.objects.all()
    if request.method=='GET':
        st=request.GET.get('servicename')
        if st!=None:
            servicedata=service.objects.filter(service_title__icontains=st)
    data={'service':servicedata}
    return render(request,"service.html",data)
def newsdata(request,slug):
    newsDetail=News.objects.get(news_slug=slug)
    data={'key':newsDetail}
    return render(request,"news.html",data)