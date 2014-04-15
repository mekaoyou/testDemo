from django.shortcuts import render_to_response
from django.http import HttpResponse
import datetime;

def current_datetime(request):
	current_date = datetime.datetime.now();
	nav = "this is nav";
	return render_to_response('current_datetime.html',locals());

def test_request(request):
	metaValues = request.META.items()
	metaValues.sort()
	# html = []
	# for k,v in values:
	# 	html.append('<tr><td>%s</td><td>%s</td></tr>' %(k,v))
	return render_to_response('request_meta.html',locals());