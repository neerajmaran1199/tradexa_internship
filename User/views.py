from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm
from django.views.generic import CreateView, DetailView, ListView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post
# Create your views here.

class PostCreateView(LoginRequiredMixin,CreateView ):
    model = Post
    template_name = 'user/postcreate.html'
    fields = ['text', 'created_at', 'updated_at']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def get_success_url(self):
        return reverse('home')


class PostListView(ListView):
    model = Post
    template_name = 'User/posts.html'
    context_object_name = 'posts'
    paginate_by = 10

class PostDetailView(DetailView):
    model = Post
    template_name = 'User/posts.html'
    

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = UserRegistrationForm()

    return render(request, 'user/registrationForm.html', {'form':form})