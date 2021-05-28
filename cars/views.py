from django.core import paginator
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from cars.models import Car
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.

def cars(request):
    cars=Car.objects.order_by('created_date')
    paginator= Paginator(cars,2)
    page=request.GET.get('page')
    page_cars=paginator.get_page(page)
    model_search=Car.objects.values_list('model',flat=True).distinct()
    state_search=Car.objects.values_list('state',flat=True).distinct()
    year_search=Car.objects.values_list('year',flat=True).distinct()
    body_style_search=Car.objects.values_list('body_style',flat=True).distinct()
    data={
        'cars':page_cars,
        'model_search':model_search,
        'state_search':state_search,
        'year_search':year_search,
        'body_style_search':body_style_search,
    }
    return render(request,'cars/cars.html', data) 


def car_detail(request, id):
    single_car=get_object_or_404(Car, pk=id)
    data={
        'single_car':single_car
    }
    return render(request,'cars/car_detail.html',data )   

def search(request):
    cars=Car.objects.order_by('created_date')
    model_search=Car.objects.values_list('model',flat=True).distinct()
    state_search=Car.objects.values_list('state',flat=True).distinct()
    year_search=Car.objects.values_list('year',flat=True).distinct()
    body_style_search=Car.objects.values_list('body_style',flat=True).distinct()
    transmission=Car.objects.values_list('transmission',flat=True).distinct()
    
    if 'keyword' in request.GET:
        keyword =request.GET['keyword']
        if keyword:
            cars=cars.filter(description__icontains =keyword)
    if 'model' in request.GET:
        keyword =request.GET['model']
        if keyword:
            cars=cars.filter(model__iexact =keyword)

    if 'state' in request.GET:
        keyword =request.GET['state']
        if keyword:
            cars=cars.filter(state__iexact =keyword)
    if 'year' in request.GET:
        keyword =request.GET['year']
        if keyword:
            cars=cars.filter(year__iexact =keyword)
    if 'body_style' in request.GET:
        keyword =request.GET['body_style']
        if keyword:
            cars=cars.filter(body_style__iexact =keyword)
    if 'transmission' in request.GET:
        keyword =request.GET['transmission']
        if keyword:
            cars=cars.filter(transmission__iexact =keyword)
    if 'min_prize' in request.GET:
        min_prize = request.GET['min_prize']
        max_prize = request.GET['max_prize']

        if 'max_prize':
            cars=cars.filter(price__gte='min_price',price__lte='max_price')
    data={
        'cars':cars,
        'model_search':model_search,
        'state_search':state_search,
        'year_search':year_search,
        'body_style_search':body_style_search,
        'transmission':transmission,
    }
    return render(request,'cars/search.html',data) 