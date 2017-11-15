from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages


def index(request):
	return render(request, "surveys/index.html")
def result(request):
	return render(request, "surveys/result.html")
def back(request):
	return redirect('/')

def process(request):
	if 'number' in request.session:
		request.session['number'] += 1
	else:
		request.session['number'] =	1
	request.session['name'] = request.POST['name']
	request.session['location'] = request.POST['location']
	request.session['language'] = request.POST['language']
	request.session['comment'] = request.POST['comment']
	return redirect ('/result')
