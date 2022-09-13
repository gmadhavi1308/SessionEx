from django.shortcuts import render
from MyApp.forms import *
# Create your views here.
def page_count(request):
    value = request.session.get('value', 0)
    inc_value = value + 1
    request.session['value'] = inc_value
    print("Page expiry age :", request.session.get_expiry_age())
    print("Page expiry date:", request.session.get_expiry_date())
    return render(request,'home.html', {'value': inc_value})

def PersonalInfoView(request):
    form = PersonalInfoForm()
    return render(request,'PersonalInfo.html',{'form':form})

def ContactInfoView(request):
    rollno = request.GET['rollno']
    name = request.GET['name']
    request.session['rollno'] = rollno
    request.session['name'] = name
    form = ContactInfoForm()
    return render(request,'ContactInfo.html', {'form':form})

def MarksInfoView(request):
    email = request.GET['email']
    mobile = request.GET['mobile']

    request.session['email'] = email
    request.session['mobile'] = mobile
    form = MarksInfoForm()
    return render(request,'MarksInfo.html', {'form':form})

def ResultsView(request):
    sub1 = request.GET['sub1']
    sub2 = request.GET['sub2']
    sub3 = request.GET['sub3']
    total = (int(sub1)+int(sub2)+int(sub3))
    avg = (total/3)
    request.session['sub1'] = sub1
    request.session['sub2'] = sub2
    request.session['sub3'] = sub3
    request.session['total']=total
    request.session['avg']=avg
    return render(request,'results.html')
