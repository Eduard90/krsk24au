from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from krsk24au_info.models import Review, User


# Create your views here.
class IndexView(generic.TemplateView):
    template_name = 'krsk24au_info/index.html'

class UsersView(generic.ListView):
    template_name = 'krsk24au_info/users.html'
    context_object_name = '24au_users'

    def get_queryset(self):
        return User.objects.order_by('name').all();

class UserView(generic.DetailView):
    template_name = 'krsk24au_info/user.html'
    context_object_name = '24au_user'
    model = User



    # def get_object(self):
    #     return get_object_or_404(User)
    # def get_queryset(self):
    #     return User.objects.get()

# class IndexView(generic.ListView):
#     template_name = 'krsk24au_info/index.html'
#     context_object_name = 'latest_reviews'
#
#     def get_queryset(self):
#         return Review.objects.order_by('-date_time')[:100]

    # latest_reviews = Review.objects.order_by('-date_time')[:1000]
    # context = {'latest_reviews': latest_reviews}
    # return render(request, 'krsk24au_info/index.html', context)

