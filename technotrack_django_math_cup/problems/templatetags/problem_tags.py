from django import template
from django.db.models import Max

from problems.models import Answer
register = template.Library()


@register.simple_tag
def get_status(problem, user):
    if problem.answer_set.filter(user=user, status=Answer.OK).count() > 0:
        return 'solved'
    if problem.answer_set.filter(user=user).count() > 0:
        return 'failed'
    return 'empty'


@register.simple_tag
def last_updated(problem, user):
    return problem.answer_set\
        .filter(user=user).all()\
        .aggregate(Max('created_at'))['created_at__max']
