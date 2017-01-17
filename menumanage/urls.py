from django.conf.urls import url
from django.contrib import admin

from menumanage import views

urlpatterns = [
    url(r'^add$', views.add, name='menumanage.add'),
    url(r'^addEntity$', views.addEntity, name='menumanage.addEntity'),
    url(r'^deleteEntity$', views.deleteEntity, name='menumanage.deleteEntity'),
    url(r'^', views.index, name='menumanage.index'),
]
