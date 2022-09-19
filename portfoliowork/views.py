
from django.shortcuts import render
from .models import Mycv,Contact, abousUs,Skill,service_name,Project,Certificate,Hiring,Experience
# mailing liberay 
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def home(request):
    aboutUsRight = abousUs.objects.first()
    SkillRight = Skill.objects.all()
    service_name_Right = service_name.objects.all()
    certificates = Certificate.objects.all()
    experience = Experience.objects.all()
    Projects = Project.objects.all()
    cv = Mycv.objects.last()
    sucess = ""
    error = ""
    your_name =request.POST.get('name')
    your_phone =request.POST.get('phone')
    your_email =request.POST.get('email')
    your_subject =request.POST.get('subject')
    your_message = request.POST.get('message')
    flag =0
    if your_name=="":
        error=error+"Name is required."
        flag =1
    elif your_email=="":
        error=error+"Email is required."
        flag =1
    elif your_subject=="":
        error=error+"Subject is required."
        flag =1
    elif your_message=="":
        error=error+"Message is required."
        flag =1
    subject =your_subject
    message=f' senders name ---->    {str(your_name)}   \n sender"s phone_number is ---->  {str(your_phone)}      \n Sender"s emails is ----->   {str(your_email)}   \n sender"s subject is --->     {str(your_subject  )} \n sender"s message is --->  {str(your_message )}'
    if flag ==0:
        
        if request.method == 'POST':
            try :
                saving_data =Contact(name=your_name, phone_number=your_phone, email=your_email, subject=your_subject,  message=your_message)
                saving_data.save()
                
                send_mail(subject, message, settings.EMAIL_HOST_USER,
                  ['pawan941394@gmail.com'], fail_silently=False)
                sucess = sucess + "Your Hiring message has been sent successfully."
                
                
            except Exception as e :
                print(e)
                error =error+"There was an error while sending the message ! Please try again later."
    return render(request, 'index.html',{'abousUs':aboutUsRight ,'Skills':SkillRight,'service':service_name_Right,'cert':certificates,'proj':Projects,'cv':cv,'error':error,'sucess':sucess,'exper':experience})
def certifications(request):
    aboutUsRight = abousUs.objects.first()
    certificates = Certificate.objects.all()
    cv = Mycv.objects.last()
    sucess = ""
    error = ""
    your_name =request.POST.get('name')
    your_phone =request.POST.get('phone')
    your_email =request.POST.get('email')
    your_subject =request.POST.get('subject')
    your_message = request.POST.get('message')
    subject =your_subject
    message=f' senders name ---->    {str(your_name)}   \n sender"s phone_number is ---->  {str(your_phone)}      \n Sender"s emails is ----->   {str(your_email)}   \n sender"s subject is --->     {str(your_subject  )} \n sender"s message is --->  {str(your_message )}'
    flag =0
    if your_name=="":
        error=error+"Name is required."
        flag =1
    elif your_email=="":
        error=error+"Email is required."
        flag =1
    elif your_subject=="":
        error=error+"Subject is required."
        flag =1
    elif your_message=="":
        error=error+"Message is required."
        flag =1
    if flag ==0:
        
        if request.method == 'POST':
            try :
                saving_data =Contact(name=your_name, phone_number=your_phone, email=your_email, subject=your_subject,  message=your_message)
                saving_data.save()
                send_mail(subject, message, settings.EMAIL_HOST_USER,
                  ['pawan941394@gmail.com'], fail_silently=False)
                sucess = sucess + "Your Hiring message has been sent successfully."
            except Exception as e :
                print(e)
                error =error+"There was an error while sending the message ! Please try again later."
    return render(request, 'certifications/certificationsMore.html',{'abousUs':aboutUsRight ,'certificates':certificates,'cv':cv,'error':error,'sucess':sucess})
def certificationsDescription(request,Certificate_name):
    aboutUsRight = abousUs.objects.first()
    cv = Mycv.objects.last()
    certificates = Certificate.objects.get(Certificate_name=Certificate_name)
    return render(request, 'certifications/certificationdesc.html',{'abousUs':aboutUsRight ,'certificates':certificates,'cv':cv})
def Experiences(request):
    aboutUsRight = abousUs.objects.first()
    experience= Experience.objects.all()
    cv = Mycv.objects.last()
    sucess = ""
    error = ""
    your_name =request.POST.get('name')
    your_phone =request.POST.get('phone')
    your_email =request.POST.get('email')
    your_subject =request.POST.get('subject')
    your_message = request.POST.get('message')
    subject =your_subject
    message=f' senders name ---->    {str(your_name)}   \n sender"s phone_number is ---->  {str(your_phone)}      \n Sender"s emails is ----->   {str(your_email)}   \n sender"s subject is --->     {str(your_subject  )} \n sender"s message is --->  {str(your_message )}'
    flag =0
    if your_name=="":
        error=error+"Name is required."
        flag =1
    elif your_email=="":
        error=error+"Email is required."
        flag =1
    elif your_subject=="":
        error=error+"Subject is required."
        flag =1
    elif your_message=="":
        error=error+"Message is required."
        flag =1
    if flag ==0:
        
        if request.method == 'POST':
            try :
                saving_data =Contact(name=your_name, phone_number=your_phone, email=your_email, subject=your_subject,  message=your_message)
                saving_data.save()
                send_mail(subject, message, settings.EMAIL_HOST_USER,
                  ['pawan941394@gmail.com'], fail_silently=False)
                sucess = sucess + "Your Hiring message has been sent successfully."
            except Exception as e :
                print(e)
                error =error+"There was an error while sending the message ! Please try again later."
    return render(request, 'experiences/experiencesMore.html',{'abousUs':aboutUsRight ,'Experience':experience,'cv':cv,'error':error,'sucess':sucess})
def ExperiencesDescription(request,Experience_name):
    aboutUsRight = abousUs.objects.first()
    cv = Mycv.objects.last()
    experience = Experience.objects.get(Experience_name=Experience_name)
    return render(request, 'experiences/experiencesDescription.html',{'abousUs':aboutUsRight ,'Experience':experience,'cv':cv})




def Projects(request):
    Projects = Project.objects.all()
    cv = Mycv.objects.last()
    aboutUsRight = abousUs.objects.first()
    sucess = ""
    error = ""
    your_name =request.POST.get('name')
    your_phone =request.POST.get('phone')
    your_email =request.POST.get('email')
    your_subject =request.POST.get('subject')
    your_message = request.POST.get('message')
    subject =your_subject
    message=f' senders name ---->    {str(your_name)}   \n sender"s phone_number is ---->  {str(your_phone)}      \n Sender"s emails is ----->   {str(your_email)}   \n sender"s subject is --->     {str(your_subject  )} \n sender"s message is --->  {str(your_message )}'
    flag =0
    if your_name=="":
        error=error+"Name is required."
        flag =1
    elif your_email=="":
        error=error+"Email is required."
        flag =1
    elif your_subject=="":
        error=error+"Subject is required."
        flag =1
    elif your_message=="":
        error=error+"Message is required."
        flag =1
    if flag ==0:
        
        if request.method == 'POST':
            try :
                saving_data =Contact(name=your_name, phone_number=your_phone, email=your_email, subject=your_subject,  message=your_message)
                saving_data.save()
                send_mail(subject, message, settings.EMAIL_HOST_USER,
                  ['pawan941394@gmail.com'], fail_silently=False)
                sucess = sucess + "Your Hiring message has been sent successfully."
            except Exception as e :
                print(e)
                error =error+"There was an error while sending the message ! Please try again later."
    return render(request, 'projects/projectsMore.html',{'abousUs':aboutUsRight ,'proj':Projects,'cv':cv,'error':error,'sucess':sucess})
def ProjectsDescription(request,Project_name):
    Projects = Project.objects.get(Project_name=Project_name)
    aboutUsRight = abousUs.objects.first()
    cv = Mycv.objects.last()
    return render(request, 'projects/projectDescription.html',{'abousUs':aboutUsRight ,'proj':Projects,'cv':cv})
def Hire(request):
    aboutUsRight = abousUs.objects.first()
    cv = Mycv.objects.last()
    sucess = ""
    error = ""
    your_name =request.POST.get('name')
    your_phone =request.POST.get('phone')
    your_email =request.POST.get('email')
    your_subject =request.POST.get('subject')
    your_hiring_for = request.POST.get('hiring')
    your_message = request.POST.get('message')
    subject =your_subject
    message=f' senders name ---->    {str(your_name)}   \n sender"s phone_number is ---->  {str(your_phone)}      \n Sender"s emails is ----->   {str(your_email)}   \n sender"s subject is --->     {str(your_subject  )}   \n Hiring for --->     {str(your_hiring_for  )} \n sender"s message is --->  {str(your_message )}'
    flag =0
    if your_name=="":
        error=error+"Name is required."
        flag =1
    elif your_email=="":
        error=error+"Email is required."
        flag =1
    elif your_subject=="":
        error=error+"Subject is required."
        flag =1
    elif your_hiring_for=="":
        error=error+"Hiring field is required."
        flag =1
    elif your_message=="":
        error=error+"Message is required."
        flag =1
    if flag ==0:
        
        if request.method == 'POST':
            try :
                saving_data =Hiring(name=your_name, phone_number=your_phone, email=your_email, subject=your_subject, hiring_for=your_hiring_for, message=your_message)
                saving_data.save()
                send_mail(subject, message, settings.EMAIL_HOST_USER,
                  ['pawan941394@gmail.com'], fail_silently=False)
                sucess = sucess + "Your Hiring message has been sent successfully."
            except Exception as e :
                error =error+"There was an error while sending the message ! Please try again later."
        
    return render(request, 'hire/hire.html',{'abousUs':aboutUsRight,'error':error,'sucess':sucess,'cv':cv})
def contact(request):
    aboutUsRight = abousUs.objects.first()
    cv = Mycv.objects.last()
    sucess = ""
    error = ""
    your_name =request.POST.get('name')
    your_phone =request.POST.get('phone')
    your_email =request.POST.get('email')
    your_subject =request.POST.get('subject')
    your_message = request.POST.get('message')
    subject =your_subject
    message=f'senders name ---->    {str(your_name)}   "\n" sender"s phone_number is ---->  {str(your_phone)}     + "\n"Sender"s emails is ----->   {str(your_email)}   "\n" sender"s subject is --->     {str(your_subject  )} "\n" sender"s message is --->  {str(your_message )}'
    flag =0
    if your_name=="":
        error=error+"Name is required."
        flag =1
    elif your_email=="":
        error=error+"Email is required."
        flag =1
    elif your_subject=="":
        error=error+"Subject is required."
        flag =1
    elif your_message=="":
        error=error+"Message is required."
        flag =1
    if flag ==0:
        
        if request.method == 'POST':
            try :
                saving_data =Contact(name=your_name, phone_number=your_phone, email=your_email, subject=your_subject,  message=your_message)
                saving_data.save()
                send_mail(subject, message, settings.EMAIL_HOST_USER,
                  ['pawan941394@gmail.com'], fail_silently=False)
                sucess = sucess + "Your Hiring message has been sent successfully."
            except Exception as e :
                print(e)
                error =error+"There was an error while sending the message ! Please try again later."
        
    return render(request, 'contact/contact.html',{'abousUs':aboutUsRight,'error':error,'sucess':sucess,'cv':cv})
def moreSkills(request):
    aboutUsRight = abousUs.objects.first()
    SkillRight = Skill.objects.all()
    return render(request, 'moreskills/moreSkills.html',{'abousUs':aboutUsRight ,'Skills':SkillRight,})
