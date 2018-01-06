# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Candidate(models.Model): 
	id_candidate = models.CharField(max_length=32, unique=True)
	name_candidate = models.CharField(max_length=60, unique=False)
	summary = models.TextField(max_length=500)
	descriptions = models.TextField(max_length=2000)
	slug = models.SlugField(unique=True)
	# candidate_pic = models.ImageField(upload_to=None, default=None)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name_candidate)
		super(Candidate, self).save(*args, **kwargs)

	def __str__(self):
		return self.name_candidate


class CandidateAchivement(models.Model):
	id_candidate_achivement = models.ForeignKey(Candidate, related_name = 'achivement')
	achivement1 = models.TextField(max_length=500)
	achivement2 = models.TextField(max_length=500)
	achivement3 = models.TextField(max_length=500)
	achivement4 = models.TextField(max_length=500)
	achivement5 = models.TextField(max_length=500)

class CandidateScore(models.Model):
    id_candidate_score = models.ForeignKey(Candidate, related_name = 'score')
    score = models.IntegerField()
    userId = models.ForeignKey(User, related_name = 'score')


class Reviews(models.Model):
	userId = models.ForeignKey(User, related_name = 'reviewer')
	id_candidate_reivew = models.ForeignKey(Candidate, related_name = 'reviews')
	header = models.CharField(max_length=500, unique=True)
	review = models.CharField(max_length=500, unique=True)
	date_of_review = models.DateTimeField(auto_now_add = True)



