# -*- coding: utf-8 -*-
from django.urls import path
from django.views.generic import TemplateView

app_name = "contragents"
urlpatterns = [
    path("", TemplateView.as_view(template_name="base.html")),
]
