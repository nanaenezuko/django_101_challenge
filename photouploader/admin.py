from django.contrib import admin
from .models import PostPhoto

# Register your models here.
class Posting(admin.ModelAdmin):
    pass

admin.site.register(PostPhoto, Posting)