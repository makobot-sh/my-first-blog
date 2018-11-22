from django.shortcuts import render
from django.utils import timezone
from .models import Post  # El . indica directorio actual xq models y views estan en el mismo dir.

def post_list(request):
	#Pasamos el QuerySet "posts" a la plantilla:
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
