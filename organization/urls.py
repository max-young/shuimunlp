from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'text-analysis/', views.TextAnalysisView.as_view())
]
