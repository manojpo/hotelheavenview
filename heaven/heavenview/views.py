from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.models import User
# from .forms import ProfileForm
#
# from .auth import unauthenticated_user


import json
import datetime
from django.contrib import messages
from django.shortcuts import render, redirect

from .auth import admin_only
from .models import Contact, Reserve, Blog
from django.views import generic
from django.urls import reverse_lazy
from .models import Room
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from .forms import *

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'heavenview/signup.html'



def first(request):
    return render(request,'heavenview/first.html')

@login_required()
def index(request):
    return render(request,'heavenview/index.html')

@login_required()
def home(request):
    return render(request,'heavenview/home.html')




@login_required()
def contact(request):
    if request.method == "POST":
        data = request.POST
        name = data['name']
        email = data['email']
        messages = data['messages']

        contact=Contact.objects.create(name=name,
                                         email=email,
                                         messages=messages)
        if contact:
            return redirect('/contact')

        else:
            return HttpResponse("Fail to response")


    return render(request, 'heavenview/contact.html')



def get_Contact(request):
    contact=Contact.objects.all()
    context={
        'contacts':contact,
        'active_contact':'active'

    }
    return render(request,'heavenview/getContact.html',context)

def deleteContact(request,contact_id):
    contact=Contact.objects.get(id=contact_id)
    contact.delete()
    return redirect('/getContact')

def reserve(request):
    if request.method == "POST":
        form = ReserveForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/reserve')
        else:
            return HttpResponse("Fail to response")
    context={
        'form':ReserveForm
    }
    return render(request, 'heavenview/reserve.html', context)



def get_Reserve(request):
    reserves = Reserve.objects.all()
    context = {
        'reserves': reserves,
        'active_reserve': 'active'

    }
    return render(request, 'heavenview/getReserve.html', context)


def deleteReserve(request,reserve_id):
    reserve=Reserve.objects.get(id=reserve_id)
    reserve.delete()
    return redirect('/getReserve')



@login_required()
def about(request):
    return render(request,'heavenview/about.html')

@login_required()
def blog(request):
    return render(request,'heavenview/blog.html')

class AddBookingView(CreateView):
    model = Room
    template_name = 'heavenview/addBooking.html'
    fields = '__all__'
    success_url = reverse_lazy('booking')

@login_required()

def BookingView(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'heavenview/booking.html', context)

class RoomView(DetailView):
    model = Room
    template_name = 'heavenview/view.html'

class RoomUpdate(UpdateView):
    model = Room
    template_name = 'heavenview/update.html'
    fields = '__all__'
    success_url = reverse_lazy('booking')

class RoomDelete(DeleteView):
    model = Room
    template_name = 'heavenview/delete.html'
    success_url = reverse_lazy('booking')


@admin_only
def admin(request):
    return render(request,'heavenview/admin.html')


class CreateBlogView(CreateView):
    model = Blog
    template_name = 'heavenview/createblog.html'
    fields = '__all__'
    success_url = reverse_lazy('blog')

class DetailBlogView(DetailView):
    model = Blog
    template_name = 'heavenview/blogview.html'

def blogView(request):
    blogs = Blog.objects.all()

    context = {
        'blogs': blogs,

    }
    return render(request, 'heavenview/blog.html', context)

class BlogDelete(DeleteView):
    model = Blog
    template_name = 'heavenview/deleteblog.html'
    success_url = reverse_lazy('blog')

class BlogUpdate(UpdateView):
    model = Blog
    fields = '__all__'
    template_name = 'heavenview/updateblog.html'
    success_url = reverse_lazy('blog')


def userView(request):
    users_all = User.objects.all()
    users = users_all.filter(is_staff=0)
    context = {
        'users': users,
    }
    return render(request, 'heavenview/getUsers.html', context)

class UserDelete(DeleteView):
    model = User
    template_name = 'heavenview/userdelete.html'
    success_url = reverse_lazy('get_Users')


@login_required()
@admin_only

def admin_dashboard(request):
    room = Room.objects.all()
    room_count = room.count()
    blog = Blog.objects.all()
    blog_count = blog.count()
    users = User.objects.all()
    user_count = users.filter(is_staff=0).count()
    admin_count = users.filter(is_staff=1).count()
    context = {
        'room': room_count,
        'blog': blog_count,
        'user': user_count,
        'admin': admin_count
    }
    return render(request, 'heavenview/adminDashboard.html', context)

@admin_only
def update_user_to_admin(request,user_id):
    user=User.objects.get(id=user_id)
    user.is_staff=True
    user.save()
    messages.add_message(request,messages.SUCCESS,'User has been updated to Admin')
    return redirect('/admindash')



# def register_user(request):
#     if request.method=="POST":
#         form=UserCreationForm(request.POST)
#         if form.is_valid():
#             user=form.save()
#             # use= added
#             # new profile
#             Profile.objects.create(user=user,username=user.username)
#             messages.add_message(request,messages.SUCCESS,'User registered successfully')
#             return redirect('/')
#         else:
#             messages.add_message(request,messages.ERROR,'unable to regiter')
#             return  render(request,'signup.html',{'form':form})
#     context={
#         'form':UserCreationForm
#
#     }
#     return render(request,'signup.html',context)


# @login_required()
# def user_account(request):
#     profile = request.user.profile
#     form = ProfileForm(instance=profile)
#     if request.method=='POST':
#         form = ProfileForm(request.POST , request.FILES , instance=profile)
#         if form.is_valid():
#             form.save()
#             messages.success(request,'Account Update Successful for'+ str(request.user.profile))
#             return redirect('profile')
#     context = {'form':form}
#     return render(request,'profile.html',context)
#






