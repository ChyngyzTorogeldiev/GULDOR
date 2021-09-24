from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.views import View
from django.views import generic 
from .models import *
from .forms import CommentForm
from django.contrib.auth.forms import AuthenticationForm
from core.models import Product
from core.views import *




# def product_detail(request, slug):
#     template_name = 'review.html'
#     product = get_object_or_404(Flower(), slug=slug)
#     comments = product.comments.filter(active=True)
#     new_comment = None
 
#     if request.method == 'POST':
#         comment_form = CommentForm(data=request.POST)
#         if comment_form.is_valid():

           
#             new_comment = comment_form.save(commit=False)
          
#             new_comment.product = product
       
#             new_comment.save()
#     else:
#         comment_form = CommentForm()

#     return render(request, template_name, {'product': product,
#                                            'comments': comments,
#                                            'new_comment': new_comment,
#                                            'comment_form': comment_form})




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
        