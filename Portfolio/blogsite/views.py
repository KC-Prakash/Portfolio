from django.shortcuts import render, get_object_or_404
from .models import Category, Image, About, Profile, blog_post, Contact
from .forms import ContactForm
# Create your views here.
def index(requist):
    return render(requist,'index.html')

def about(requist):
    about=About.objects.latest('update_at')
    profile=Profile.objects.filter(about=about)
    context={
        'about':about,
        'profiles':profile,
    }
    return render(requist,"about.html",context)
    #return render(requist,'about.html')

def service(requist):
    return render(requist,'service.html')

def blog(requist):
    allpost=blog_post.objects.order_by('-post_time')
    context= {
        'allpost':allpost
    }
    return render(requist,'blog.html',context)

def blog_detail(requist,slug):
    detail_post=blog_post.objects.filter(slug=slug)
    context={
        'detail_post':detail_post
    }
    return render(requist,'blog_detail.html',context)



def gallery(requist,category_slug=None):
    images=None
    categories=None
    categories=Category.objects.all()
    if category_slug is not None:
        category=get_object_or_404(Category, category_slug=category_slug)
        images=Image.objects.filter(image_category=category)
    else:
        images=Image.objects.all()
    context={
        'images':images,
        'categories': categories,
    }

    
    return render(requist,'gallery.html',context)

def contact(request):

    form=ContactForm(request.POST)

    if form.is_valid():
        data=Contact()
        data.name=form.cleaned_data['name']
        data.email=form.cleaned_data['email']
        data.subject=form.cleaned_data['subject']
        data.message=form.cleaned_data['message']
        form.save()


    return render(request,'contact.html')


