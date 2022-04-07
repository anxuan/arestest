from django.contrib import admin
from django.urls import path
from ares_t1.views import do_test, index,write_cookie

urlpatterns = [
    path('a', do_test),
    path("", index),
    path("write_cookie", write_cookie)
]
