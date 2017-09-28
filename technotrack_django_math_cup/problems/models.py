from __future__ import unicode_literals

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from application import settings


class Problem(models.Model):
    text = models.TextField()
    title = models.CharField(max_length=50)
    key = models.CharField(max_length=4)
    image = models.ImageField(blank=True)
    round = models.ForeignKey('cups.Round')
    correct_answer_type = models.ForeignKey(ContentType)
    correct_answer_id = models.PositiveIntegerField()
    correct_answer = GenericForeignKey('correct_answer_type', 'correct_answer_id')

    users_solved = models.ManyToManyField(settings.AUTH_USER_MODEL)

    def __unicode__(self):
        return u'{}, {}'.format(self.round, self.key)


class Answer(models.Model):
    OK = 'OK'
    WRONG_ANSWER = 'WA'
    WRONG_FORMAT = 'WF'
    ERROR = 'ER'
    IN_PROCESS = 'IP'

    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    problem = models.ForeignKey('problems.Problem')
    value = models.CharField(max_length=255)
    status = models.CharField(choices=(
        (OK, 'OK'),
        (WRONG_ANSWER, 'Wrong answer'),
        (WRONG_FORMAT, 'Wrong format'),
        (ERROR, 'Error'),
        (IN_PROCESS, 'In process'),
    ), max_length=2, default=IN_PROCESS)

    def __unicode__(self):
        return u'date: {}, author: {}, status: {}'.format(self.created_at, self.user.username, self.status)


class CorrectAnswer(models.Model):

    def compare(self, value):
        raise NotImplementedError

    class Meta:
        abstract = True


class CorrectAnswerInt(CorrectAnswer):
    value = models.IntegerField()

    def compare(self, value):
        value = value.replace(',', '.')
        try:
            float_value = float(value)
            if not float_value.is_integer():
                raise ValueError
            int_value = int(float_value)
        except ValueError:
            return Answer.WRONG_FORMAT
        if int_value == self.value:
            return Answer.OK
        else:
            return Answer.WRONG_ANSWER

    def __unicode__(self):
        return str(self.value)


class CorrectAnswerFloat(CorrectAnswer):
    value = models.FloatField()

    def compare(self, value):
        value = value.replace(',', '.')
        try:
            float_value = float(value)
        except ValueError:
            return Answer.WRONG_FORMAT
        if abs(float_value - self.value) <= 1e-4:
            return Answer.OK
        else:
            return Answer.WRONG_ANSWER

    def __unicode__(self):
        return str(self.value)
