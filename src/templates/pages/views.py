# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.shortcuts import render
from django.forms.utils import ErrorList
# to force the user to loggin - https://docs.djangoproject.com/en/2.0/topics/auth/default/
from django.contrib.auth.mixins import LoginRequiredMixin  

# from .forms import CandidateForm
from django.template import Context

from django.views.generic import (
    DetailView, 
    ListView, 
    CreateView, 
    FormView,
    UpdateView
)

from .forms import CandidateModelForm
from .mixins import FormUserNeededMixin
from .models import (
    Candidate,
    CandidateAchivement,
    CandidateScore, 
    Reviews
    )

# -------------------------------------------------------------
# this is the Create View
# -------------------------------------------------------------

# Login required is used to make sure that before the form is submitted user is loggied. 

# -------------------------------------------------------------
# Adding an entry to the Candidate model - index 
# -------------------------------------------------------------
class CandidateCreateView(LoginRequiredMixin, FormUserNeededMixin, CreateView):
    # queryset = Candidate.objects.all()
    form_class = CandidateModelForm
    template_name = 'pages/add_candidate.html'
    success_url = '/pages/'
    login_url = '/admin/'
    # redirect_field_name = 'redirect_to'


# -------------------------------------------------------------
# this is the home page - index 
# -------------------------------------------------------------
class CandidateListView(ListView):
    template_name = 'pages/home.html'
    queryset = Candidate.objects.all()



# -------------------------------------------------------------
# this is the  Detail view - Page for Candidate
# -------------------------------------------------------------
class CandidateDetailView(DetailView):
    queryset = Candidate.objects.all()

    def get_objects(self):
        return Candidate.objects.get(id =1)



# -------------------------------------------------------------
# this is the Update view - Page for Candidate
# -------------------------------------------------------------
class CandidateUpdateView(UpdateView):
    queryset = Candidate.objects.all()
    form_class = CandidateModelForm
    success_url = '/pages/'
    template_name = 'pages/update_candidate.html'



# -------------------------------------------------------------
# this is the home page - index 
# -------------------------------------------------------------

# class PageListView(ListView):
#     template_name = 'pages/home.html'
#     queryset = Candidate.objects.all()


# def home(request):
#     category_list = Candidate.objects.all()
#     context_dict = {'candidates': category_list }
#     return render(request, 'pages/home.html', context_dict)



# -------------------------------------------------------------
# Individual profile page of the candidates
# -------------------------------------------------------------
# def candidate(request, candidate_name_slug):

#         # print 'slug name', candidate_slug_nam


#         context_dict = {}
	
# 	# category_list = Candidate.objects.all()
# 	# context_dict = {'candidates': category_list }

# 	# print category_list

# 	try:
# 		candidate = Candidate.objects.get(slug=candidate_name_slug)
# 		context_dict['candidate_name'] = candidate.name_candidate
		
# 	except Candidate.DoesNotExist:
		
# 		pass

# 	return render(request, 'pages/candidate.html', context_dict)

# -------------------------------------------------------------
# Adding the caandidate 
# -------------------------------------------------------------

# def add_candidate(request):
#     # A HTTP POST?
#     if request.method == 'POST':
#         form = CandidateForm(request.POST)

#         # Have we been provided with a valid form?
#         if form.is_valid():
#             # Save the new category to the database.
#             form.save(commit=True)

#             # Now call the index() view.
#             # The user will be shown the homepage.
#             return index(request)
#         else:
#             # The supplied form contained errors - just print them to the terminal.
#             print form.errors
#     else:
#         # If the request was not a POST, display the form to enter details.
#         form = CandidateForm()

#     # Bad form (or form details), no form supplied...
#     # Render the form with error messages (if any).
#     return render(request, 'pages/add_candidate.html', {'form': form})


# -------------------------------------------------------------
# Search query for the book 
# -------------------------------------------------------------

# def candiate_search(request, id =1):
#     MIN_SEARCH_CHARS = 2
#     search_text = '' 

#     # if(request.method == "GET"):
#     #     search_text = request.GET.get("search_text", None).strip().lower()
#     #     if (len(search_text) < MIN_SEARCH_CHARS):
#     #         search_text = '' 
        
#     # # context = dict()
#     # context_dict = {}

#     # if (search_text != ""):
#     #     candidateResult = Candidate.objects.filter(content__icontains = search_text).all()
#     # else:
#     #     candidateResult =[]

#     # # context = Context({
#     # #     'candidate': candidateResult
#     # # })
#     # context_dict['results'] = candidateResult


#     if(request.method == "GET"):
#         search_text = request.GET.get("search_text", None).strip().lower()
#         if len(search_text)<MIN_SEARCH_CHARS:
#             search_text = None 
#     if (search_text != ""):
#        queryset = Candidate.objects.filter(name_candidate__icontains = search_text).all()
#     #    queryset2 = Candidate.objects.filter(name_candidate__icontains = search_text).all()
#     else:
#        queryset = []

#     context = {
#             "object_list":queryset
#     } 


#     # print 'test', context["object_list"]

#     # for i in context["object_list"]:
#     #     print "testx", i

#     # for i in queryset:
#     #     print i.name_candidate
    
#     # for i in context["object_list"]:
#     #     print "context", i

#     return render(request, 'pages/search_result.html', context)









# Create your views here.- this is the the infomation from the 

# class CandidateProfile(DetailView,candidate_name_slug):
#     queryset = Candidate.objects.all()
    
#     def get_object(self):
#         candidate = Candidate.objects.get(slug=candidate_name_slug)
#         context_dict['candidate_name'] = candidate.name_candidate


# class CandidateList(ListView):
#      template_name = 'pages/test.html'
#      queryset = Candidate.objects.all()

# class CandidateDetails(DetailView):

#         def candidate_det(self, candidate_name_slug):
#             template_name = 'pages/candidate.html'
#             candidate = Candidate.objects.get(slug=candidate_name_slug)
#             context_dict['candidate_name'] = candidate.name_candidate
#             QuerySet = context_dict
#             # return context_dict


# def test(request):

#     # obj = Candidate.objects.get(id = 1)
#     # # returns one item
#     # context1 = {
#     #         "object":obj
#     # }

#     # returns a list 
#     queryset = Candidate.objects.all()
#     context = {
#             "object_list":queryset
#     }
#     for i in queryset:
#         print i.name_candidate
#     return render(request, 'pages/test.html', context)
