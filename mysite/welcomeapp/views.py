from django.shortcuts import render
from django.http import HttpResponse
def welcome(request):
    return HttpResponse ("""<html><body bgcolor=cyan><center><h1>Welcome To JathinSolutions</h1></center></body><html>""")


