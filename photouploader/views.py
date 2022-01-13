from django.db.models.base import Model
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, FormView

from .models import PostPhoto
from .forms import PostPhotoForm

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['photo_post'] = PostPhoto.objects.all()
        return context

class PhotoPostDetailView(DetailView):
    template_name = 'detail.html'
    model = PostPhoto
    
class PostPhotoView(FormView):
    template_name = 'post.html'
    form_class = PostPhotoForm
    success_url = '/'

    def form_valid(self, form):

        new_object = PostPhoto.objects.create(
            title = form.cleaned_data['title'],
            caption = form.cleaned_data['caption'],
            image = form.cleaned_data['image']
        )

        return super().form_valid(form)