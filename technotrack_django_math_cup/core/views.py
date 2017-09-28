from django.views.generic.base import TemplateView


class Profile(TemplateView):
    template_name = 'core/profile.html'
