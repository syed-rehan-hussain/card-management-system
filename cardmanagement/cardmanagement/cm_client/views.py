from django.shortcuts import render
from django.views.generic import View, TemplateView


# Create your views here.
class DepartmentFormView(TemplateView):
    template_name = 'index.html'


class CardView(TemplateView):
    template_name = 'card.html'


class GenerateCardView(TemplateView):
    template_name = 'generated.html'
