from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from user import views as user_views


urlpatterns = [
    path('accounts/', include('allauth.urls'), name="accounts_login"),
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('register/', include('user.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    path('profile/', user_views.profile, name='profile'),
    # path('profile/send-email/', user_views.send_email, name='send_email'),
    path('profile/<int:pk>/', user_views.ProfileDetailView.as_view(), name='other-profile'),
    path('profile/download/', user_views.profiles_in_xlxs, name='user-data'),
    path('profile/<int:pk>/followers/add', user_views.AddFollower.as_view(), name='add-follower'),
    path('profile/<int:pk>/followers/remove', user_views.RemoveFollower.as_view(), name='remove-follower'),
    path('profile/<int:pk>/followers/add/email-recevier/', user_views.Add_Email_Receiver.as_view(), name='add-email-receiver'),
    path('profile/<int:pk>/followers/remove/email-recevier/', user_views.Remove_Email_Receiver.as_view(), name='remove-email-receiver'),
    path('following/', user_views.follwing, name='following'),
    path('following/<int:pk>/', user_views.relevantpost, name="relevant-post"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
