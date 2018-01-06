# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


from .models import Candidate

# Create your views here.

def home(request):

	category_list = Candidate.objects.all()
	context_dict = {'candidates': category_list }


	return render(request, 'home.html', context_dict)



def candidate(request, candidate_name_slug):
        # print 'slug name', candidate_slug_nam
        context_dict = {}
	
	category_list = Candidate.objects.all()
	context_dict = {'candidates': category_list }

	print category_list

	# try:
	# 	candidate = Candidate.objects.all()
	# 	print 'candidate', candidate.name_candidate

	# 	context_dict = {'candidates': candidate  }
	# 	# context_dict['candidate_name'] = candidate.name_candidate
		
	# except Candidate.DoesNotExist:
		
	# 	pass

	return render(request, 'pages/candidate.html', context_dict)
