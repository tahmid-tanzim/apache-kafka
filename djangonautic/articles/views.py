from django.shortcuts import render
from .models import Article

# Create your views here.
def list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, "articles/list.html", {"articles": articles})