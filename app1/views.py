from django.shortcuts import render, HttpResponse,redirect, get_object_or_404
from django.contrib.auth.models import User #import User model from django.
from django.contrib.auth import authenticate, login as auth_login
from app1.models import jobPost,jobSearch,Contact
from app1.forms import EmployersForm,JobApply
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):

    return render(request,'index.html')

def signup(request):
    if request.method == 'POST':
        uname = request.POST.get('username') # uname is variable to store info about username from my signup page.
        email = request.POST.get('email') # similarly email,pwd1, pwd2 are creates for storing info.
        pwd1 = request.POST.get('password1')
        pwd2 = request.POST.get('pasword2')
        users = User.objects.create_user(uname,email,pwd1) #Creates my_user varible to create a user which holds the all info about the user like uname pwd and email.
        users.save()
        return redirect('login')
    return render(request,'signup.html')

def login(request):
    if request.method == 'POST':
        uname1 = request.POST.get('username')#Store data from HTML form into this variable.
        pass1 = request.POST.get('pass')
        user = authenticate(request, username = uname1, password = pass1)

        if user is not None:
            auth_login(request, user)
            user_role = request.POST.get('user_role')  # Get the selected user role from the form

            if user_role == 'employer':
                return redirect('employer')
            elif user_role == 'job_seeker':
                return redirect('job_seeker')
            else:
                # Handle other cases if needed, e.g., show an error message
                return HttpResponse('Invalid User Role')

        else:
            return HttpResponse('Incorrect Username Or Password!')

    return render(request, 'login.html')
   


@login_required  # Restrict access to authenticated users only
# only users who are logged in can access this view.
def employer(request):
    msg = ""        # used to display a message to the user in the template.
    form = EmployersForm()  # used to handle job post submissions.

    if request.method == 'POST':
        form = EmployersForm(request.POST)  # binds the form to the POST data that was submitted.
        if form.is_valid():
            # Save the job post with the logged-in user as the owner
            job_post = form.save()
            job_post.user = request.user #set the user field of the job post to the currently logged-in user. This associates the job post with the user who created it.
            job_post.save()
            msg = '1'       # used to display a success message in the template.
            form = EmployersForm()  # Clear the form for a fresh entry

    # Filter job posts to display only those created by the logged-in user
    data = jobPost.objects.filter(user=request.user) #only display job posts created by the user.

    context = {
        'form': form,
        'data': data,
        'msg': msg
    }

    return render(request, 'employer.html', context)

def delete_jobPost(request,id):  
      # Retrieve the job post to be deleted using its ID
    delete_job = jobPost.objects.get(pk = id)
    delete_job.delete()     # Delete the job post
    messages.success(request, 'Data Deleted successfully') 
    return redirect("employer")

def edit_jobPost(request , id):  
    if request.method == 'POST':
        edit_job = jobPost.objects.get(pk=id)# Retrieve the job post to be edited using its ID
        form = EmployersForm(request.POST,instance = edit_job)     # Bind the form to the POST data for processing, with the instance of the job post to be edited
        if form.is_valid:
            form.save()
            messages.success(request, 'Data Update successfully')
            form = EmployersForm() # Clear the form after submission
        else:
            form = EmployersForm()         
    else:
         edit_job = jobPost.objects.get(pk=id)  # If the request method is not POST, retrieve the job post to be edited and create a form with its data
         form = EmployersForm(instance = edit_job)
    context = {
        'form':form,
    } 
    return render(request,'edit_job.html',context)

def job_seeker(request):
    job_list = jobPost.objects.all() # Get All Data from employers posted job job,Retrieve all job applications from the jobSearch model.
    job_apply = jobSearch.objects.all()# Get All Data from job seekers model, # Retrieve all job applications from the jobSearch model
    context = {
        'job_list': job_list,
        'job_apply': job_apply,
    }# Create a context dictionary with the job list and job applications

    return render(request, 'job_search.html', context)

def apply_job(request, id):
    job_post = jobPost.objects.get(pk=id)  # Retrieve the job post with the given 'id'
    
    user_has_applied = request.user in job_post.applied_by_users.all()
    
    if request.method == 'POST':
        form = JobApply(request.POST, request.FILES)
        
        if form.is_valid() and not user_has_applied:
            job_application = form.save(commit=False)
            job_application.user = request.user
            job_application.job_post = job_post
            job_application.save()
            job_post.applied_by_users.add(request.user)
            form = JobApply()  # Clear the form after submission
            return render(request, 'applied.html')
    else:
        form = JobApply()

    context = {
        'job_post': job_post,
        'form': form,
        'user_has_applied': user_has_applied,
    }

    return render(request, 'apply.html', context)

def logout(request):
    
    return redirect('login')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        msg = request.POST.get('msg')
        print(f'name: {name}, email: {email}, phone: {phone}, msg: {msg}')
        print(f'phone: {phone}')
        contact = Contact(name=name , email=email,phone=phone, msg=msg )   
        contact.save()
        messages.success(request, "Your Message has been sent Successfully!")

    return render(request, 'contact.html')
def about(request):
    return render(request,'about.html')

