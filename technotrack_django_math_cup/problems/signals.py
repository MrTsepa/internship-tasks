from django.db.models.signals import post_save, pre_save

from problems.models import Answer

# TODO Move signals to celery


def check_answer(sender, instance, *args, **kwargs):
    assert isinstance(instance, Answer)
    instance.status = instance.problem.correct_answer.compare(instance.value)
    if instance.status == Answer.OK:
        instance.problem.users_solved.add(instance.user)


pre_save.connect(check_answer, Answer)
