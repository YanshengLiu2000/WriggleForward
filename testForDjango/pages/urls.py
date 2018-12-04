from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns=[
    # path('', views.index, name='index'),
    path('testpage', TemplateView.as_view(template_name='pages/page.html')),
    path('', views.index, {'pagename':''},name='home'),
    path('contact', views.contact, name='contact'),
    path('<str:pagename>', views.index, name='index'),
]
# handler404 = path('', views.error_404,name='error_404')