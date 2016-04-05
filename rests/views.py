from django.shortcuts import render, get_object_or_404,redirect
from django.utils import timezone
from .models import Restaurant
from .forms import RestaurantForm

def rest_list(request):
    rests = Restaurant.objects.filter(createdAt__lte=timezone.now()).order_by('createdAt')
    return render(request,'rests/rest_list.html',{'rests':rests})

def rest_detail(request,pk):
    rest = get_object_or_404(Restaurant,pk=pk)
    return render(request,'rests/rest_detail.html',{'rest':rest})

def rest_new(request):
    if request.method == "POST":
        form = RestaurantForm(request.POST)
        if form.is_valid():
            rest = form.save(commit=False)
            rest.createdAt = timezone.now()
            rest.save()
            return redirect('rest_detail',pk=rest.pk)
    else:
        form = RestaurantForm()
    return render(request,'rests/rest_new.html',{'form':form})
