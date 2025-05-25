from django.urls import path
from .views import *

urlpatterns  = [
path('lists',AdListView.as_view()),
path('create',AdCreateView.as_view()),
path('detail/<int:pk>',AdDetailView.as_view()),
path('serach/',AdSearchView.as_view()),
]