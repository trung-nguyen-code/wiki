from django.urls import path

from . import views

urlpatterns = [
    path("wiki/", views.index, name="index"),
    path("wiki/<str:title>", views.entry_content, name="entry_content"),
    path("search/",views.search,name="search"),
    path("search/<str:title>",views.entry_content,name="recommend"),
    path("newpage/",views.create_newpage,name="newpage"),
    # path("edit/",views.edit,name="edit"),

]
