from django.contrib import admin
from django.urls import path,include
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',user_views.register,name='register'),
    path('', include('blog.urls')),
    path('login/',auth_views.LoginView.as_view(template_name="users/login.html"),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name="users/logout.html"),name='logout'),
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name="users/password_reset.html"),name='password_reset'),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name="users/password_reset_done.html"),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="users/password_reset_confirm.html"),name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name="users/password_reset_complete.html"),name='password_reset_complete'),
    path('profile/',user_views.profile,name='profile'),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)













#as second parameter of path, we'll provide the path which will take us to blog URL so importing Include
#Flow -- if you type admin/ in url, it will take to admin page-->if you type blog/-->it'll take you to blog page-->As you've entered the path as ''(empty) in urls.py of Blog,it'll show the home page of blog
 
#Flow--> If you write "localhost:8000/blog" it'll pop up showing The html text what you had written-->First searchingis done in urls of Main project-->
#then it checks whether it has "blog/" anywhere in path?->if yes, it checks where to go further for the action->
#then "blog/" will be chopped off from our string and it'll send an empty string(after chopping nothing remains)
#now flow will go to blog's url->it will see whether there is path for empty string whoch we definitely have -> then it'll go to views and will call home function and finally show the HTML code.

#Here if you want to do live testing on your website, create a path with different name like path('abc',xyz) and then you can acces through a this url your testing modules