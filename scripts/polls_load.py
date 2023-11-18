import csv  # https://docs.python.org/3/library/csv.html
from django.utils import timezone

from polls.models import Question, Choice


def run():
    print("=== Polls Loader")

    Choice.objects.all().delete()
    Question.objects.all().delete()
    print("=== Objects deleted")

    fhand = open('scripts/dj4e_batch.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    for row in reader:
        print("Row type", type(row))
        q = Question(question_text=row[0], pub_date=timezone.now())
        for element in row[1:]:
            q.choice_set.create(choice_text=element, votes=0)
            print("This is element", q)
        q.save()

        print(q.id, q.question_text)

        # Make a new Question and save it

        # Loop through the choice strings in row[1:] and add each choice,
        # connect it to the question and save it

    print("=== Load Complete")
