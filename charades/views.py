# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext 
import settings
from charades.models import *

import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def start(request):
	app_id = settings.FACEBOOK_APP_ID
	app_uri = 'https://apps.facebook.com/charadeslocal/'
	server_url = "http://ec2-54-234-17-199.compute-1.amazonaws.com/"
	request_ids = request.GET.get('request_ids', None)
	if request_ids:
		app_uri += "?request_ids="+request.GET['request_ids']
		request_ids = request_ids.split(',')[-1]
	return render_to_response("start.html",dict(app_id = app_id, app_uri = app_uri, server_url=server_url))

def home(request):
	print 'In home'
	print request.POST.get('uid')
	user = User.objects.filter(fuid = request.POST.get('uid'))
	if not user:
		print 'no user'
		user = User(fuid = request.POST.get('uid'), name = request.POST.get('name'), coins=0)
		user.save()
		print 'user_save'
	return render_to_response('user_home.html', dict(user=user))
