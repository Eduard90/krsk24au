from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.db.models import Count
from django.views import generic
import logging

from krsk24au_last.models import NewReview

# Create your views here.

class AllNewUsersView(generic.ListView):
    template_name = 'krsk24au_last/index.html'
    context_object_name = '24au_new_users'

    def get_queryset(self):
        search = ""

        kwargs = {
            'count__gt': 2,
        }

        if self.request.method == 'GET':
            search = self.request.GET.get('search', None)

        if search:
            resultsSphinx = NewReview.search.query(search)
            resultsSphinx = resultsSphinx[0:resultsSphinx.count()]
            ids = []
            for result in resultsSphinx:
               ids.append(result.id)

            kwargs['pk__in'] = ids

        sellers = NewReview.objects.values('seller_user_name').annotate(count=Count('seller_user_name')).filter(**kwargs).all()
        buyers = NewReview.objects.values('buyer_user_name').annotate(count=Count('buyer_user_name')).filter(**kwargs).all()

        users = {}
        for seller in sellers:
            users[seller['seller_user_name']] = {'sells': seller['count']}

        for buyer in buyers:
            if users.get(buyer['buyer_user_name']):
                users[buyer['buyer_user_name']]['buyes'] = buyer['count']
            else:
                users[buyer['buyer_user_name']] = {'buyes': buyer['count']}

        return users
