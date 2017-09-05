from django.core.management.base import BaseCommand, CommandError

from question_api.models import (
    Question, Answer, Tenant, User)

class Command(BaseCommand):
    help = 'populate data'
    def handle(self, *args, **options):
        # create users and tenants
        User.objects.all().delete()
        Tenant.objects.all().delete()
        names = ['Hugo', 'Shannon', 'Taylor', 'Julius', 'Reginald', 'Agnes', 'Corey']
        for name in names:
            User.objects.create(name=name)
            Tenant.objects.create(name=name)

        # create questions and answer
        Question.objects.all().delete()
        Answer.objects.all().delete()
        questions_and_answers = [
            {
                "question": "What is data structure?",
                "answer": "A data structure is a way of organizing data that considers not only the items stored, but also their relationship to each other. Advance knowledge about the relationship between data items allows designing of efficient algorithms for the manipulation of data.",
                "user": User.objects.get(name='Hugo'),
            },
            {
                "question": "List out the areas in which data structures are applied extensively?",
                "answer": "Compiler Design,Operating System,Database Management System,Statistical analysis package,Numerical Analysis,Graphics,Artificial Intelligence,Simulation",
                "user": User.objects.get(name='Hugo'),
            },
            {
                "question": "What is the data structures used to perform recursion?",
                "answer": "Stack. Because of its LIFO (Last In First Out) property it remembers its 'caller' so knows whom to return when the function has to return. Recursion makes use of system stack for storing the return addresses of the function calls.Every recursive function has its equivalent iterative (non-recursive) function. Even when such equivalent iterative procedures are written, explicit stack is to be used.",
                "user": User.objects.get(name='Julius'),
            },
            {
                "question": "Minimum number of queues needed to implement the priority queue?",
                "answer": "Two. One queue is used for actual storing of data and another for storing priorities.",
                "user": User.objects.get(name='Hugo'),
            },
            {
                "question": "What is database?",
                "answer": "A database is a logically coherent collection of data.",
                "user": User.objects.get(name='Agnes'),
            },
            {
                "question": "What is DBMS?",
                "answer": "It is a collection of programs that enables user to create and maintain a database. In other words it is general-purpose software that provides the users with the processes of defining, constructing and manipulating the database for various applications.",
                "user": User.objects.get(name='Corey'),
            }
        ]


        for qa in questions_and_answers:
            user = qa['user']
            question = Question.objects.create(title=qa['question'], user=user)
            Answer.objects.create(body=qa['answer'], user=user, question=question)
