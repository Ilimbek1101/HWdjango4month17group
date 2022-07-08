from django.contrib import admin
from .models import Director, Movie, Review


# Register your models here.
class ReviewAdminInline(admin.StackedInline):
    model = Review
    extra = 0

class MovieAdmin(admin.ModelAdmin):
    model = Movie
    list_display = 'image_img title director description'.split()
    search_fields = 'title description'.split()
    list_filter = 'director'.split()
    readonly_fields = 'image_img'.split()
    list_editable = 'director'.split()
    list_per_page = 4
    inlines = [ReviewAdminInline]



admin.site.register(Director)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Review)
