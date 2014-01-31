from django.shortcuts import render
from django.http import HttpResponse
from krsk24au_info.models import Review, User
from django.db.models import Count
from datetime import datetime, timedelta
import json
# Create your views here.

def index(request):
    # request.session['django_language'] = "en"
    results = Review.objects.extra({'date_time' : "date(date_time)"}).values('date_time').annotate(count=Count('date_time'))
    context = {'reviews': results}
    return render(request, 'krsk24au_reviews/index.html', context)


def detailsaboutday(request):
    if request.is_ajax():
        date_str = request.POST.get('date', None)
        date = datetime.strptime(date_str, '%d.%m.%Y')
        results = Review.objects.all().filter(date_time__startswith=datetime.date(date))
        context = {'reviews': results}
        return render(request, 'krsk24au_reviews/ajax/detailsAboutDay.html', context)
    else:
       return render(request, 'layout/ajaxAccessDeny.html')

def graph_for_period(request):
    if request.is_ajax():
        period = request.GET.get('period', None)
        start_date = datetime.now() - timedelta(days=int(period))

        reviews = Review.objects.extra({'date_time' : "date(date_time)"}).values('date_time').annotate(count=Count('date_time')).filter(date_time__gte=start_date)

        #reviews = Review.objects.all().filter(date_time__startswith=datetime.date(start_date))
        result = []
        for review in reviews:
           result.append({'count': review['count'], 'date': review['date_time'].strftime('%Y/%m/%d')})

        context = {'data': result}

        # context = {'start_date': start_date.strftime('%Y-%m-%dT%H:%M:%S')}
        return HttpResponse(json.dumps(context), content_type="application/json")
        #return render(request, 'krsk24au_reviews/ajax/graphForPeriod.html', context)
    else:
       return render(request, 'layout/ajaxAccessDeny.html')