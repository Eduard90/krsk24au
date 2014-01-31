from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, request
from django.core.urlresolvers import reverse
from django.views import generic

from krsk24au_info.models import Review, User

# Create your views here.

def index(request):
    # template_name = 'krsk24au_search/index.html'
    # results = Review.objects.all()
    #results = Review.objects.all().filter(title__contains='playstation')
    results = 0
    search = ""
    if request.method == 'POST':
        search = request.POST.get('search', None)
        if search:
            resultsSphinx = Review.search.query(search)
            resultsSphinx = resultsSphinx[0:resultsSphinx.count()]
            ids = []
            for result in resultsSphinx:
               ids.append(result.id)

            # results = Review.objects.filter(title__icontains='playstation').order_by('-date_time')
            results = Review.objects.filter(pk__in=ids).order_by('-date_time')

    context = {'reviews': results, 'search': search}
    return render(request, 'krsk24au_search/index.html', context)