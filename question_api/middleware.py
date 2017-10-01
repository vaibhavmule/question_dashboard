import datetime

from django.core.exceptions import ObjectDoesNotExist

from rest_framework.response import Response

from question_api.models import Tenant, APICount


class APIRateThrottleMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        self.process_request(request)
        response = self.get_response(request)
        return response

    def process_request(self, request):
        api_key = request.GET.get('api_key', None)
        if api_key:
            try:
                now = datetime.datetime.now()
                tenant = Tenant.objects.get(api_key=api_key)
                api_count, created = APICount.objects.get_or_create(
                    tenant=tenant)
                if api_count.count > 100 and api_count.next_timestamp + datetime.timedelta(seconds=10) > now:
                    return Response({
                        'message': 'Try after few seconds'
                    }, status=429)
                else:
                    api_count.count += 1
                    api_count.next_timestamp = now
                    api_count.save()
            except ObjectDoesNotExist:
                return Response({'message': 'provide API key'}, status=400)
