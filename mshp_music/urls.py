"""
URL configuration for mshp_music project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib.auth import views as a_views
from django.urls import path
from Users import views as Users_views
from Songs import views as Songs_views
from Friends import views as Friends_views
from django.views.generic import RedirectView
from django.http import HttpResponse
from django.contrib.staticfiles.storage import staticfiles_storage

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('',)
    path('login', Users_views.loginPage, name='login'),
    path('register', Users_views.register, name='register'),
    path('logout', Users_views.logoutPage, name='logout'),
    path('profile/<slug:profile_id>/', Users_views.profilePage, name='profile'),
    path('profile/<slug:profile_id>/send',Friends_views.send_request, name='send_friend_request'),
    path('profile/<slug:profile_id>/reject',Friends_views.reject_request, name='reject_friend_request'),
    path('profile/<slug:profile_id>/accept',Friends_views.accept_request, name='accept_friend_request'),
    path('profile/<slug:profile_id>/delete',Friends_views.delete_friend, name='delete_friend'),
    path('profile/change', Users_views.changeProfile),

    path('friend/list', Friends_views.show_list),
    path('friend/requests', Friends_views.show_requests),

    # Password reset links (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)
    path('password_change_done/',
         a_views.PasswordChangeDoneView.as_view(template_name='password_reset/password_change_done.html'),
         name='password_change_done'),

    path('password_change/', a_views.PasswordChangeView.as_view(template_name='password_reset/password_change.html'),
         name='password_change'),

    path('password_reset_done/',
         a_views.PasswordResetDoneView.as_view(template_name='password_reset/password_reset_done.html'),
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/', a_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/', a_views.PasswordResetView.as_view(), name='password_reset'),

    path('password_reset_complete/',
         a_views.PasswordResetCompleteView.as_view(template_name='password_reset/password_reset_complete.html'),
         name='password_reset_complete'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)