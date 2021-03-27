from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import ContactForm

# Create your views here.
def home(request):
    all_post = Post.objects.all()
    return render(request, "blog/home.html", {'all_post': all_post})

def blog_details(request, id):
    single_post = Post.objects.get(id=id)
    return render(request, "blog/blog-details.html", {'single_post': single_post})

def contact(request):
    form = ContactForm()
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = ContactForm()
    return render(request, "blog/forms.html", {'form': form})
