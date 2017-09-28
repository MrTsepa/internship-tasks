from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from django.contrib.auth import get_user_model

from cups.models import Cup, Round
from problems.models import Answer, Problem


class CupListView(ListView):
    model = Cup


class RoundDetailView(DetailView):
    model = Round


class RoundRatingView(TemplateView):
    template_name = 'cups/round_rating.html'

    def get_context_data(self, **kwargs):
        context = super(RoundRatingView, self).get_context_data(**kwargs)
        context['round'] = Round.objects.get(slug=kwargs['slug'])
        context['problems'] = Problem.objects.filter(round=context['round'])
        context['users'] = get_user_model().objects.filter(
            id__in=Answer.objects.values('user').filter(problem__round=context['round']).distinct())
        return context
