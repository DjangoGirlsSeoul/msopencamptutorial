from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Restaurant

def rest_list(request):
    rests = Restaurant.objects.filter(createdAt__lte=timezone.now()).order_by('createdAt')
    return render(request,'rests/rest_list.html',{'rests':rests})

def rest_detail(request,pk):
    rest = get_object_or_404(Restaurant,pk=pk)
    return render(request,'rests/rest_detail.html',{'rest':rest})
