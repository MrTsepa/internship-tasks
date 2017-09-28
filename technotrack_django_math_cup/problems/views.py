from django.http.response import Http404, HttpResponseBadRequest, HttpResponseForbidden, HttpResponseRedirect
from django.urls import reverse
from django.views.generic.detail import DetailView

from cups.models import Round
from problems.models import Problem, Answer


class ProblemDetailView(DetailView):
    model = Problem

    def get_object(self, queryset=None, **kwargs):
        try:
            return Round.objects.get(slug=self.kwargs['slug'])\
                .problem_set.get(key=self.kwargs['key'])
        except Round.DoesNotExist:
            raise Http404
        except Problem.DoesNotExist:
            raise Http404

    def get_context_data(self, **kwargs):
        context = super(ProblemDetailView, self).get_context_data(**kwargs)
        context['user_answers'] = Answer.objects.\
            filter(user=self.request.user, problem=self.get_object(kwargs=kwargs)).\
            order_by('-created_at')
        return context

    def post(self, request, **kwargs):
        if 'answer' in request.POST:
            answer_text = request.POST['answer']
            if not answer_text:
                raise HttpResponseBadRequest
            if not request.user.is_authenticated():
                raise HttpResponseForbidden
            Answer.objects.create(user=request.user, value=answer_text, problem=self.get_object())
            return HttpResponseRedirect(reverse('problem-detail', kwargs=kwargs))
        raise HttpResponseBadRequest
