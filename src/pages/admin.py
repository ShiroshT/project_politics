# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .forms import CandidateModelForm
from .models import Candidate

# Register your models here.


# admin.site.register(Candidate)




class CandiateModelAdmin(admin.ModelAdmin):
         form = CandidateModelForm
    # class Meta:
    #     model = Candidate
   



admin.site.register(Candidate, CandiateModelAdmin)

