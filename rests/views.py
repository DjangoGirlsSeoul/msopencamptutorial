from django.shortcuts import render

def rest_list(request):
    return render(request,'rests/rest_list.html',{})
