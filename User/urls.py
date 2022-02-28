from django.urls import path
from .views import register
from django.contrib.auth.views import LoginView, LogoutView


from .views import PostCreateView, PostDetailView, PostListView
urlpatterns = [
    path('postcreate/', PostCreateView.as_view(), name="postcreate"),
    path('post/<int:pk>/detail', PostDetailView.as_view(), name="post-detail"),
    path('', PostListView.as_view(), name="home"),
    path('login/', LoginView.as_view(template_name='User/login.html'), name="login"),
    path('logout/', LogoutView.as_view(template_name='User/logout.html'), name="logout"),

    path('register/', register, name="register"),
    
]






    