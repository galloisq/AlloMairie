from django.shortcuts 		import render, get_object_or_404
from django.core 			import serializers
from django.http 			import HttpResponse
from django.contrib.auth 	import authenticate, login
from django.conf 			import settings

from django.views.decorators.csrf 	import csrf_exempt
from django.contrib.auth.decorators import login_required

import json

"""Login , Inscription, Profil """
@csrf_exempt
def connection(request):
	response_data = {}
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				response_data['StatutCode'] = 200
    		else:
				response_data['StatutCode'] = 400
	else:
		response_data['StatutCode'] = 500
	return HttpResponse(json.dumps(response_data), content_type="application/json")