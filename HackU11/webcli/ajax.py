import json

from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect

from webcli.models import *
from python_pandora import pandora

from django.conf import settings

def do(req, action):
	actions = {
		'next_song': get_next_song,
		'search': search,
	}
	
	return actions[action](req)

def get_next_song(req):
	api = pandora.Pandora()
	
	if api.authenticate(settings.PANDORA_USERNAME, settings.PANDORA_PASSWORD):
		# output stations (without QuickMix)
		for station in api.getStationList():
			if station['isQuickMix']: 
				quickmix = station
				break
		
		api.switchStation(quickmix)
		
		next_song = api.getNextSong()
		
		x = HttpResponse(json.dumps(next_song))
		x['Cache-Control'] = 'no-cache'
		return x
	else:
		return HttpResponse(json.dumps({
			'error': 'authentication failed'
		}))

def search(req):
	terms = req.GET.get('searchText')
	
	return HttpResponse(json.dumps(terms));