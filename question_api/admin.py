# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from question_api.models import (
	Question,
	User,
	Answer,
	Tenant)

class TenantAdmin(admin.ModelAdmin):
    list_display = ('name', 'api_key')

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Tenant, TenantAdmin)
admin.site.register(User)
