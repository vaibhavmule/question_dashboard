from rest_framework import serializers

from question_api.models import Question, Answer


class AnswerSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Answer
		fields = ('body', 'user')
		depth = 1 


class QuestionSeriliazer(serializers.ModelSerializer):
	answers = AnswerSerializer(many=True, read_only=True)

	class Meta:
		model = Question
		fields = ('title','user', 'answers',)
		depth = 1
