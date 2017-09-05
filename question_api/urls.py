from django.conf.urls import url

from rest_framework import routers

from question_api.views import QuestionViewSet, index

router = routers.DefaultRouter()
router.register(r'questions', QuestionViewSet)
urlpatterns = router.urls
