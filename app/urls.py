from django.urls import path, include
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', include('allauth.urls'), name="accounts_login"),
    path('', login_required(views.PostView.as_view()), name='index'),
    path('post/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('profile/add', views.CreateView.as_view(), name='add-post'),
    path('post/<int:pk>/add/comment/', views.AddCommentView.as_view(), name='add-comment'),
    path('edit/<int:pk>/', views.UpdateView.as_view(), name='edit-post'),
    path('delete/<int:pk>/', views.DeleteView.as_view(), name='delete-post'),
    # path('comment')
        # path('<slug:slug>/', views.DetailView, name='detail'),

]