from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from django.views.generic import FormView, DetailView, TemplateView
from .models import *
from .forms import *
from django.utils import timezone 
from django.contrib.auth.forms import AuthenticationForm




def review(request):
    review_object = Review.objects.all()
    return render(request, 'reviews/review.html',
    {'review_object': review_object})




# class ReviewView(FormView):
#     template_name = 'review/review_form.html'
#     form_class = ReviewForm 
#     success_url = '/flowertypes/'

#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)

# class ReviewDetailView(DetailView):
#     queryset = Review.objects.all()
#     template_name = 'review/review.html'







# def review(request):
#     if request.method == "POST":
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.date = timezone.now()
#             # post.author = request.user
#             post.save()
#             return redirect('/review')
#     else:
#         form = ReviewForm()
#     return render(request, 'review/roses.html', {'form': form})
        