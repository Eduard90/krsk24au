from django.contrib import admin

from krsk24au_info.models import Review, User
# Register your models here.

class SphinxModelAdmin(admin.ModelAdmin):
    def get_search_results(self, request, queryset, search_term):
        if search_term:
            sphinx_queryset = self.model.search.query(search_term)
            doc_ids = [doc.pk for doc in sphinx_queryset]
            queryset = queryset.filter(pk__in=doc_ids)
            return queryset, True
        else:
            return super(SphinxModelAdmin, self).get_search_results(
                request, queryset, search_term
            )

class ReviewInline(admin.TabularInline):
    model = Review
    extra = 3

class ReviewAdmin(SphinxModelAdmin):
    list_display = ('title', 'date_time')
    search_fields = ['title']

# class UserAdmin(admin.ModelAdmin):
    # inlines = [ReviewInline]

admin.site.register(User)
admin.site.register(Review, ReviewAdmin)
