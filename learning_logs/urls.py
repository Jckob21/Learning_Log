"""Defines URL patterns for learning_logs."""

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Topics page
    path('topics/', views.topics, name='topics'),
    # Single topic page
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # Page to add a topic
    path('new_topic/', views.new_topic, name='new_topic'),
    # Page to add an entry
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
]
