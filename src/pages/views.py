# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Candidate
from .forms import CandidateForm
from django.template import Context


import re
from django.db.models import Q



# Create your views here.

def home(request):

	category_list = Candidate.objects.all()
	context_dict = {'candidates': category_list }


	return render(request, 'pages/home.html', context_dict)



def candidate(request, candidate_name_slug):

        # print 'slug name', candidate_slug_nam


        context_dict = {}
	
	# category_list = Candidate.objects.all()
	# context_dict = {'candidates': category_list }

	# print category_list

	try:
		candidate = Candidate.objects.get(slug=candidate_name_slug)
		context_dict['candidate_name'] = candidate.name_candidate
		
	except Candidate.DoesNotExist:
		
		pass

	return render(request, 'pages/candidate.html', context_dict)



def add_candidate(request):
    # A HTTP POST?
    if request.method == 'POST':
        form = CandidateForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return index(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = CandidateForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'pages/add_candidate.html', {'form': form})




def candiate_search(request):
    MIN_SEARCH_CHARS = 2
    search_text = '' 
    if(request.method == "GET"):
        search_text = request.GET.get("search_text", None).strip().lower()
        if (len(search_text) < MIN_SEARCH_CHARS):
            search_text = '' 
        
    # context = dict()
    context_dict = {}

    if (search_text != ""):
        candidateResult = Candidate.objects.filter(content__icontains = search_text).all()
    else:
        candidateResult =[]

    # context = Context({
    #     'candidate': candidateResult
    # })
    context_dict['results'] = candidateResult

    return render(request, 'pages/search_result.html', context_dict)


