from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm
# Create your views here.
def index(request):
    reviews = Review.objects.all().order_by('-pk')
    cnt = 1
    reviews_list = []
    for i in reviews:
        reviews_list.append({'num': cnt, 'title': i.title, 'pk':i.id, 'created_at': i.created_at, 'updated_at':i.updated_at})
        cnt += 1
    context = {
        'reviews': reviews_list,
    }
    return render(request, 'reviews/index.html', context)

def create(request):
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review_form.save()
            return redirect('reviews:index')
    else: 
        review_form = ReviewForm()
    context = {
        'review_form' : review_form,
    }        
    return render(request, 'reviews/new.html', context)

def detail(request,pk):
    review = Review.objects.get(pk=pk)
    context={
        'review': review,
    }
    return render(request,'reviews/detail.html',context)

def update (request,pk):
    review = Review.objects.get(pk=pk)
    if request.method == 'POST':
        review_form = ReviewForm(request.POST,instance=review)
        if review_form.is_valid():
            review_form.save()
            return redirect('reviews:detail',review.pk)
    else: 
        review_form = ReviewForm(instance=review)
    context = {
        'review_form' : review_form,
    }        
    return render(request, 'reviews/update.html', context)

def delete (request,pk):
    review = Review.objects.get(pk=pk)
    review.delete()
    return redirect('reviews:index')    