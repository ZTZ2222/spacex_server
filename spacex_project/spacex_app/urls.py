from django.urls import path

from . import views


urlpatterns = [
    path('menu-content/', views.get_menu_content, name='menu_content'),
    path('stats-content/', views.get_stats_content, name='stats_content'),
]
