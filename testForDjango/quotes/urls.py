from django.urls import path

from . import views

from django.views.generic.base import TemplateView

from quotes.views import QuoteList, QuoteView

urlpatterns = [
    path('', views.quote_req, name='quote-request'),
    path('show/<int:pk>', QuoteView.as_view(), name='show-quotes'),
    path('show', QuoteList.as_view(), name='show-quotes'),
]
