from django.shortcuts import render_to_response
import datetime;

def current_datetime(request):
	current_date = datetime.datetime.now();
	nav = "this is nav";
	return render_to_response('current_datetime.html',locals());