from django.http import HttpResponse
from django.shortcuts import render
from .utils import *
from django.template import loader
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm


#class CreatePostView(CreateView):
#    model = Post
#    form_class = PostForm
#    template_name = 'qrcode/post.html'
#    success_url = reverse_lazy('index')

def index(request):
    template = loader.get_template('qrcode/index.html')
    if request.method == "POST":
        screenname = request.POST.get("handle", None)
        #model = Post
        #form_class = PostForm
        a = oi(screenname)
        context = {
            'ola': a,
        }
        return render(request, 'qrcode/index.html', {'result':a})
        return HttpResponse(template.render(context, request))
    return render(request, 'qrcode/index.html', {})