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
        return User.objects.order_by('name').all()

    def get_context_data(self, **kwargs):
        context = super(UsersView, self).get_context_data(**kwargs)
        return context

class UserView(generic.DetailView):
    template_name = 'krsk24au_info/user.html'
    context_object_name = '24au_user'
    model = User

    def get_context_data(self, **kwargs):
        context = super(UserView, self).get_context_data(**kwargs)
        au_user_id = kwargs['object'].id
        key = 'period_user_%s' % au_user_id

        if key in self.request.session:
            context['period_user'] = self.request.session[key]

        return context

# class IndexView(generic.ListView):
#     template_name = 'krsk24au_info/index.html'
#     context_object_name = 'latest_reviews'
#
#     def get_queryset(self):
#         return Review.objects.order_by('-date_time')[:100]

    # latest_reviews = Review.objects.order_by('-date_time')[:1000]
    # context = {'latest_reviews': latest_reviews}
    # return render(request, 'krsk24au_info/index.html', context)

