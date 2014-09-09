# -*- coding: utf-8 -*-
import json
from django.core import urlresolvers
from django.http import HttpResponse
from django.shortcuts import render_to_response
from models import PageId, BUnit, UnitRelation, UnitRelationChain, UnitRelationChainItem
from converter.api import v1_api


def index(request):
	return render_to_response('index.html')

def vk_like(request):
	return render_to_response('vk_like.html')

def _get_named_patterns():
	"Returns list of (pattern-name, pattern) tuples"
	resolver = urlresolvers.get_resolver(None)
	patterns = sorted([
		(key, value[0][0][0])
		for key, value in resolver.reverse_dict.items()
		if isinstance(key, basestring)
	])
	return patterns

def chain(request, src_id, trg_id):
	src = BUnit.objects.get(pk=src_id)
	trg = BUnit.objects.get(pk=trg_id)

	UnitRelationChain.objects.filter(sourceUnit=src, targetUnit=trg)

	response_data = {}
	response_data['result'] = 'failed'
	response_data['message'] = 'You лоло up'
	return HttpResponse(json.dumps(response_data), content_type="application/json; charset=utf-8")


