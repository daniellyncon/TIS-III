from django.contrib import admin
from django.urls import path
from .views import members_list, home, members_new, members_update, members_delete
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', home, name="start"),
    path('list/', members_list, name="member_list"),
    path('new/', members_new, name="member_new"),
    path('update/<int:id>/', members_update, name="member_update"),
    path('delete/<int:id>/', members_delete, name="member_delete"),
]