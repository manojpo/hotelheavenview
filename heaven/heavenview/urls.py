from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from .views import first, home, contact, get_Contact, about, blog, SignUpView, index, AddBookingView, BookingView, \
    RoomView, RoomUpdate, RoomDelete, reserve, get_Reserve, admin, CreateBlogView, DetailBlogView, blogView, BlogUpdate, \
    BlogDelete, userView, UserDelete

urlpatterns = [
    path('', first, name='first'),
    path('home', home, name='home'),
    path('contact', contact,name='contact'),
    path('getContact',get_Contact,name='get_Contact'),
    # path('getContact',views.get_Contact),
    path('deleteContact/<int:contact_id>',views.deleteContact),
    path('reserve', reserve,name='reserve'),
    path('getReserve',get_Reserve,name='get_Reserve'),
    path('deleteReserve/<int:reserve_id>',views.deleteReserve),
    path('about',about,name='about'),
    path('blog',blogView,name='blog'),
    path('blog/<int:pk>/update',BlogUpdate.as_view(),name="updateblog"),
    path('blog/<int:pk>/delete', BlogDelete.as_view(),name="deleteblog"),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('index',index,name='index'),
    path('addbooking', AddBookingView.as_view(), name='AddBookingView'),
    path('booking/', BookingView, name='booking' ),
    path('room/view/<int:pk>/', RoomView.as_view(), name='roomview'),
    path('room/<int:pk>/update', RoomUpdate.as_view(), name="update"),
    path('room/<int:pk>/delete', RoomDelete.as_view(), name="delete"),
    path('adminpannel',admin,name='admin'),
    path('addblog',CreateBlogView.as_view(), name='CreateBlogView'),
    path('blogview/<int:pk>/', DetailBlogView.as_view(),name='DetailBlogView'),
    path('getUsers', userView,name='get_Users'),
    path('userdelete/<int:pk>/', UserDelete.as_view(), name='user_delete'),
    path('admindash',views.admin_dashboard),



    path('update-user-to-admin/<int:user_id>',views.update_user_to_admin),

    path('password_change', auth_views.PasswordChangeView.as_view(
                      template_name='heavenview/passwordChange.html')),
    path('password_change_done', auth_views.PasswordChangeView.as_view(
                      template_name='heavenview/passwordChangeDone.html'), name='password_change_done'),

    # path('profile', views.user_account)


]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)