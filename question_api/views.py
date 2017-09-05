# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render_to_response
from django.db.models import Sum

from rest_framework import viewsets
from rest_framework.response import Response

from question_api.models import (
    Question,
    Tenant,
    User,
    Answer,
    APICount)
from question_api.serilaizer import QuestionSeriliazer


class QuestionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Question.objects.filter(private=False)
    serializer_class = QuestionSeriliazer

    def list(self, request):
        api_key = request.query_params.get('api_key', None)
        if not api_key:
            return Response({'message': 'provide API key'}, status=400)
        try:
            tenant = Tenant.objects.get(api_key=api_key)
            queryset = self.queryset
            q = request.query_params.get('q', None)
            if q:
                queryset = queryset.filter(title__icontains=q)
                if queryset.count() == 0:
                    return Response({"No results found"}, status=404)
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data)
        except (ObjectDoesNotExist):
            return Response({'message': 'API key is not valid'}, status=401)

    def retrieve(self, request, pk):
        api_key = request.query_params.get('api_key', None)
        if not api_key:
            return Response({'message': 'provide API key'}, status=400)
        try:
            tenant = Tenant.objects.get(api_key=api_key)
            instance = self.get_object()
            serializer = self.serializer_class(instance)
            return Response(serializer.data)
        except (ObjectDoesNotExist):
            return Response({'message': 'API key is not valid'}, status=401)


def index(request):
    context = {
        "questions": Question.objects.count(),
        "answers": Answer.objects.count(),
        "users": User.objects.count(),
        "tenants": [{
            "name": tenant.name,
            "api_key": tenant.api_key,
            "count": APICount.objects.filter(
                tenant=tenant).aggregate(Sum('count'))['count__sum'] or 0,
        } for tenant in Tenant.objects.all()]
    }
    return render_to_response('index.html', context=context)
