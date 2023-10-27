from django.forms import ModelForm
from app1.models import jobPost, jobSearch
from django import forms


class EmployersForm(ModelForm):
    class Meta:
        model=jobPost
        fields =['job_title','company_name','date_posted','location','shift_and_schedule', 'employment_type',
                 'about_the_job','responsibilities','requirements','technologies','experience',
                  'education_required','salary', 'mode_of_working','no_of_positions']

        widgets = {
            'job_title' : forms.TextInput(attrs={'class':'form-control'}),
            'company_name' : forms.TextInput(attrs={'class':'form-control'}),
            'date_posted' : forms.TextInput(attrs={'class':'form-control'}),
            'location' : forms.TextInput(attrs={'class':'form-control'}),
            'shift_and_schedule' : forms.TextInput(attrs={'class':'form-control'}),
            'employment_type' : forms.TextInput(attrs={'class':'form-control'}),
            'about_the_job': forms.TextInput(attrs={'class':'form-control'}), 
            'responsibilities' : forms.TextInput(attrs={'class':'form-control'}),
            'requirements' : forms.TextInput(attrs={'class':'form-control'}),
            'technologies' : forms.TextInput(attrs={'class':'form-control'}),
            'experience' : forms.TextInput(attrs={'class':'form-control'}),
            'education_required' : forms.TextInput(attrs={'class':'form-control'}),
            'salary' : forms.TextInput(attrs={'class':'form-control'}),
            'mode_of_working' : forms.TextInput(attrs={'class':'form-control'}),
            'no_of_positions' : forms.TextInput(attrs={'class':'form-control'}),

        }

class JobApply(ModelForm):
    class Meta:
        model=jobSearch
        fields =['applicant_name', 'college_name', 'qualification', 'certification','resume']

        widgets = {
            'applicant_name' : forms.TextInput(attrs={'class':'form-control'}),
            'college_name' : forms.TextInput(attrs={'class':'form-control'}),
            'qualification' : forms.TextInput(attrs={'class':'form-control'}),
            'certification' : forms.TextInput(attrs={'class':'form-control'}),
            'resume': forms.ClearableFileInput(attrs={'class': 'form-control'})

        }       