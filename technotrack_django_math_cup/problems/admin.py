from django.contrib import admin

from models import *

admin.site.register(Problem)
admin.site.register(Answer)
admin.site.register(CorrectAnswerInt)
admin.site.register(CorrectAnswerFloat)
