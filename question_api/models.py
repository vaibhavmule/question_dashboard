# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid
import datetime

from django.db import models


class Question(models.Model):
	title = models.CharField(max_length=50) 
	private = models.BooleanField(default=False)
	user = models.ForeignKey('question_api.User')


class Answer(models.Model):
	question = models.ForeignKey(Question, related_name='answers') 
	body = models.TextField(max_length=50)
	user = models.ForeignKey('question_api.User')


class Tenant(models.Model):
	name = models.CharField(max_length=30)
	api_key = models.CharField(default=uuid.uuid4, max_length=100, editable=False)

	def __unicode__(self):
		return self.name

class User(models.Model):
	name = models.CharField(max_length=30)

	def __unicode__(self):
		return self.name


class APICount(models.Model):
    tenant = models.ForeignKey(Tenant)
    count = models.IntegerField(default=0)
    next_timestamp = models.DateTimeField(default=datetime.datetime.now())

    def __unicode__(self):
        return "Tenant: {} | Api Count: {}".format(
        	self.tenant.name, self.count)