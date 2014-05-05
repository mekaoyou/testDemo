from django.shortcuts import render_to_response
from django.http import HttpResponse
from mysite.books.models import Book
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.template import RequestContext
# Create your views here.

# def search_form(request):
#   return render_to_response('search_form.html')


def search(request):
  '''
  this is function docs
  '''
  error = False;
  if 'q' in request.GET:
  	q = request.GET['q']
  	if not q:
  	  error = True
  	else:
	  books = Book.objects.filter(title__icontains=q)
	  return render_to_response('search_results.html',{'books':books,'query':q})
  return render_to_response('search_form.html',{'error':error})

def contact(request):
  errors = [];
  if request.method == "POST":
  	if not request.POST.get('subject',''):
  		errors.append('Enter a subject.');
  	if not request.POST.get('message',''):
  		errors.append('Enter a message.');
  	if request.POST.get('email') and '@' not in request.POST['email']:
  		errors.append('Enter a valid e-mail address.');
  	if not errors:
  		# send_mail(
  		# 		request.POST['subject'],
  		# 		request.POST['message'],
  		# 		request.POST.get('email','noreply@example.com'),
  		# 		['mekaoyou4@163.com'],
  		# 	)
  		return HttpResponseRedirect('/contact/thanks')
  return render_to_response('contact_form.html',{'errors':errors},context_instance=RequestContext(request))

def thanks(request):
  return HttpResponse("thanks")