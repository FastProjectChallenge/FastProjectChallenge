# -*- coding: utf-8 -*-
import json
from django.core import urlresolvers
from django.http import HttpResponse
from models import BUnit, UnitRelation, UnitRelationChain, UnitRelationChainItem, Comment
from converter.api import v1_api

intro_text = ""

def index(request):
	patterns = _get_named_patterns()
	r = HttpResponse(intro_text, content_type = 'text/plain')
	longest = max([len(pair[0]) for pair in patterns])
	for key, value in patterns:
		r.write('%s %s\n' % (key.ljust(longest + 1), value))
	return r

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


