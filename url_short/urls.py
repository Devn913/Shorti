from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('result', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('<str:my_short_url>', views.redirect_me, name='redirect_me')
]
