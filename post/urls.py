from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.liste_posts, name='liste_posts'),
    path('post/creer/', views.post_create, name='post_create'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/modifier/', views.post_update, name='modifier_post'),
    path('post/<int:pk>/supprimer/', views.post_delete, name='supprimer_post'),
    path('signup/', views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
]