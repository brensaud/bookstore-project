from django.urls import path
from django.urls.resolvers import URLPattern

from .views import SignupPageView

urlpatterns = [ 
    path('signup/', SignupPageView.as_view(), name='signup'),
]