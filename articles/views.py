from django.http.request import HttpRequest
from django.http.response import HttpResponse

from articles.models import Article


def articles_list(request: HttpRequest) -> HttpResponse:
    count: int = Article.objects.all().count()
    text = "<h1>"
    for i in range(1, count + 1):
        article = Article.objects.filter(id=i).first()
        text += f"{article.title} </h1><br><h1>"
    return HttpResponse(text)


from django.http import HttpResponse

def my_custom_view(request):
    return HttpResponse("Моя кастомная вьюшка.")

from django.views.generic import ListView
from .models import Catalog

class CatalogListView(ListView):
    model = Catalog
    template_name = 'catalog_list.html' 
    context_object_name = 'catalogs'