import json

from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect

import os
from multiprocessing import Process, Queue

from webcli.models import *

def do(req, action):
	stdout_handle = os.popen("./wserv_upload 2", "r")
	command = stdout_handle.readline()
	arguments = command.rstrip('\x00').split('\0', 10)
	
	os.system('./wserv_download 1 new-song')
	
	print(arguments)
	
	x = HttpResponse(json.dumps({
		'songUrl': arguments[1],
		'title': arguments[2],
		'artist': arguments[3],
		'album': arguments[4],
		'coverArt': arguments[5],
	}))
	x['Cache-Control'] = 'no-cache'
	return x

def search(req):
	terms = req.GET.get('searchText')
	
	os.system('./wserv_download 1 search-text {0}'.format(terms))
	
	return HttpResponse(json.dumps(terms));

'''
def getWorkerResponse(q):
	while True:
		stdout_handle = os.popen("./wserv_upload 2", "r")
		command = stdout_handle.read()
		arguments = command.rstrip('\x00\n').split('\0', 10)
		q.put(arguments)

if __name__ == '__main__':
	q = Queue()
	p = Process(target=getWorkerResponse, args=(q,))
	p.start()

	while not q.empty():
		args = q.get()
		print args
'''
