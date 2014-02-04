from django.shortcuts import render
from django.http import HttpResponse
from krsk24au_info.models import Review, User
from django.db.models import Count
from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required
import json
# Create your views here.

@login_required
def index(request):
    # request.session['django_language'] = "en"
    results = Review.objects.extra({'date_time' : "date(date_time)"}).values('date_time').annotate(count=Count('date_time'))
    context = {'reviews': results}
    return render(request, 'krsk24au_reviews/index.html', context)

@login_required
def detailsaboutday(request):
    if request.is_ajax():
        date_str = request.POST.get('date', None)
        date = datetime.strptime(date_str, '%d.%m.%Y')
        results = Review.objects.all().filter(date_time__startswith=datetime.date(date))
        context = {'reviews': results}
        return render(request, 'krsk24au_reviews/ajax/detailsAboutDay.html', context)
    else:
       return render(request, 'layout/ajaxAccessDeny.html')

#FIXME: Error when select period. First element - count error :(
@login_required
def graph_for_period(request):
    if request.is_ajax():
        period = request.GET.get('period', 0)
        period_from = request.GET.get('period_from', 0)
        period_to = request.GET.get('period_to', 0)
        default_period = 7;

        if period != 0:
            if period.isdigit():
                start_date = datetime.now() - timedelta(days=int(period))
            else:
                start_date = datetime.now() - timedelta(days=default_period)

            reviews = Review.objects.filter(date_time__gt=start_date).extra({'date_time' : "date(date_time)"}).values('date_time').annotate(count=Count('date_time'))
        else:
            if period_from != 0 and period_to != 0:
                period_from = datetime.strptime(period_from, '%d.%m.%Y')
                period_to = datetime.strptime(period_to, '%d.%m.%Y')
                reviews = Review.objects.extra({'date_time' : "date(date_time)"}).values('date_time').annotate(count=Count('date_time')).filter(date_time__gte=period_from).filter(date_time__lte=period_to)

        result = []
        for review in reviews:
           result.append({'count': review['count'], 'date': review['date_time'].strftime('%Y/%m/%d')})

        context = {'data': result}

        return HttpResponse(json.dumps(context), content_type="application/json")
    else:
       return render(request, 'layout/ajaxAccessDeny.html')