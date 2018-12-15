from django.shortcuts import render
from .models import Post,Email
from django.http import HttpResponse

#Receive Ajax Data from post comments and subcomments

def index(request):
    return render(request,'blog/index.html')


#return the blog's list of posts
def content_list(request):        
    posts = Post.objects.order_by('-pub_date')  
    context = {'posts':posts}     
    return render(request, 'blog/content_list.html', context)

#return post detail, list of posts and lists of popular posts
def content_detail(request,content_id,slug):
    if request.method == 'POST':
        email = request.POST['email']
        e = Email(email=email)
        e.save()  
    content = Post.objects.get(pk=content_id)
    post_list = Post.objects.order_by('-pub_date')
    popular_posts = Post.objects.order_by('accesses_number')
    context = {'post':content,'post_list':post_list,'popular_posts':popular_posts}
    content.accesses_number +=1
    content.save()
    return render(request, 'blog/content_detail.html',context)

def email_list(request):
    emails = Email.objects.all()    
    context = {'emails':emails} 
    return render(request, 'blog/email_list.html', context) 

