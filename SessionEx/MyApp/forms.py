from django import forms

class PersonalInfoForm(forms.Form):
    rollno = forms.IntegerField()
    name = forms.CharField()

class ContactInfoForm(forms.Form):
    email = forms.CharField()
    mobile = forms.CharField()

class MarksInfoForm(forms.Form):
    sub1 = forms.IntegerField()
    sub2 = forms.IntegerField()
    sub3 = forms.IntegerField()
