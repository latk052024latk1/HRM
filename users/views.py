from django.shortcuts import render, redirect, get_object_or_404
from users.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import os
from django.conf import settings
from django.urls import reverse
from driverdocs.models import *
from users.models import *
import datetime
from django.contrib.auth.hashers import make_password
from users.forms import *
from users import forms
from cardocs.models import *
from django.contrib.messages import get_messages
os.environ['DJANGO_SETTINGS_MODULE'] = 'logistics.settings'
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView


class UserList(ListView):
    model = User
    template_name = "users/user_list.html"


def login_user(request):

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user1 = authenticate(request, username=username, password=password)

        if user1 is not None:
            login(request, user1)


            return redirect("driverdocs:dr_list", )
    else:
        return render(request, 'authenticate/login.html', {})


@login_required()
def user_view(request, pk, template_name='users/user_detail.html'):
    users = get_object_or_404(User, pk=pk)

    now1 = datetime.datetime.now().date()
    end_day = now1 + datetime.timedelta(days=30)
    days = Documents.objects.filter(doc_expire__lte=end_day, relevance=True)

    now2 = datetime.datetime.now().date()
    end_day2 = now2 + datetime.timedelta(days=30)
    days2 = CarDocuments.objects.filter(car_doc_expire__lte=end_day, relevance=True)

    actions = UserActions.objects.filter(user1=pk)
    
    user2 = request.user
    user_form = UserChangeForm(request.POST or None, instance=users)
    if request.method == 'POST':
        if user_form.is_valid():
            user_form.save()

            new_password = user_form.cleaned_data.get('password')
            if new_password:
                user2.set_password(new_password)

            user2.username = request.POST["username"]
            user2.email = request.POST["email"]
            user2.first_name = request.POST["first_name"]
            user2.last_name = request.POST["last_name"]
            user2.save()
            
        
            return redirect(reverse('users:u_view', kwargs={"pk": request.user.pk}))

        else:
            messages.add_message(request, settings.MY_EXTRA_ERROR, 
    'გთხოვთ გადაამოწმოთ მონაცემები.')

    return render(request, template_name, {'form':user_form,'object':users, 'doc':days, 'actions':actions, "doccars": days2})

def user_logout(request):
    logout(request)
    return redirect("driverdocs:dr_list")


def user_create(request, template_name="users/client_register.html"):
    formU = forms.formCreateU(request.POST or None, instance=request.user)

    if request.method == "POST":
        if formU.is_valid():

            if request.POST["password1"] == request.POST["password2"]:
                formU.save()

                messages.success(request, "Profile details updated.")
            else:
                messages.add_message(request, settings.MY_EXTRA_ERROR, 
    'პაროლები არ ემთხვევა ერთმანეთს.')
        else:
            messages.add_message(request, settings.MY_EXTRA_ERROR, 
    'გთხოვთ გადაამოწმოთ მონაცემები.')
        
    return render(request, template_name, {'formU':formU})


@login_required()
def user_change(request, template_name="users/client_register.html"):
    user1 = User.objects.get(pk=request.user.id)
    user_form = UserChangeForm(request.POST)

    if request.method == "POST":
        if user_form.is_valid():

            obj = user_form.save(commit=False)
            if request.POST["password"] == "":
                obj.password = request.user.password
                obj.save()
            else:
                obj.password = request.POST["password"]
                user_form.save()
                return redirect(reverse('users:u_view', kwargs={"pk": request.user.pk}))
        else:
            messages.add_message(request, settings.MY_EXTRA_ERROR, 
    'გთხოვთ გადაამოწმოთ მონაცემები.')


    return render(request, template_name, {"form":user_form})

