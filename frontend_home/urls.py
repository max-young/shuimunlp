from django.conf.urls import url

from . import views

# 与React Router匹配
urlpatterns = [
    url(r'^$', views.home_page),
    url(r'^(?:(?!api|flow|admin|api-doc|api-auth|docs).*)/?$', views.home_page),
]
