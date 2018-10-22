from django.views.generic import TemplateView


class HomeView (TemplateView):
    template_name = 'index.html'


class TestPage(TemplateView):
    template_name = 'test.html'


class ThanksPage(TemplateView):
    template_name = 'thanks.html'