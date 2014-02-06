from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, request
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib.auth.decorators import login_required

from krsk24au_info.models import Review, User

# Create your views here.

@login_required
def index(request):
    # template_name = 'krsk24au_search/index.html'
    # results = Review.objects.all()
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
            results = Review.objects.filter(pk__in=ids).order_by('-date_time').select_related()

    context = {'reviews': results, 'search': search}
    return render(request, 'krsk24au_search/index.html', context)