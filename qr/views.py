from django.http import HttpResponse
from django.shortcuts import render
from .utils import *
from django.template import loader
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm
from django.utils import timezone


#class CreatePostView(CreateView):
#    model = Post
#    form_class = PostForm
#    template_name = 'qrcode/post.html'
#    success_url = reverse_lazy('index')

def index(request):
    posts = Post.objects.order_by('URL')
    if request.method == "POST":
        val = request.POST.get("btn")
        if val == "G1":
            screenname = request.POST.get("handle", None)
            a = G1(screenname)
            return render(request, 'qrcode/index.html', {'result':a})
        if val == "GE":
            screenname = request.POST.get("handle", None)
            a = GE(screenname)
            return render(request, 'qrcode/index.html', {'result':a})
        
    #if request.method == "POST":
    #    screenname = request.POST.get("handle", None)
        #model = Post
        #form_class = PostForm
    #    a = oi(screenname)
        #context = {
        #    'ola': a,
        #}
     #   return render(request, 'qrcode/index.html', {'result':a})
        #return HttpResponse(template.render(context, request))
    #return render(request, 'qrcode/index.html', {'expense_form': expense_form,})
    return render(request, 'qrcode/index.html', {})