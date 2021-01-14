from django.shortcuts import render,HttpResponse
from .models import Post

def post_list(request):
    #return HttpResponse('글 리스트')
    posts = Post.objects.all() #models.py에서 만든 post 클래스를 모두 가져와서 posts에 넣는다.
    ctx = {'posts' : posts}

    return render(request, template_name = 'posts/list.html', context = ctx)
