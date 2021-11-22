from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.decorators import api_view
# Create your views here.
# @api_view()
# def hello(request):
#     return Response({'msg':"Hello World"})

@api_view(['GET','POST'])
def hello(request):
    if request.method == "GET":
        print(request.data)
        return Response({'msg':"This is from GET"})

    if request.method == "POST":
        print(request.data)
        return Response({'msg':"This is from post",'data':request.data})