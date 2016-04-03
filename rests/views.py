from django.shortcuts import render

def rest_list(request):
    render(request,'rests/rest_list.html',{})
