
from django.contrib import admin
from django.conf.urls import url
from rest_framework.routers import SimpleRouter
from .views import HelloWorldView,SubscriberViewSet,SubscriberView,login

router = SimpleRouter()

router.register('subscribers',SubscriberViewSet)
urlpatterns = router.urls

urlpatterns = [
    url(r'^hello/',HelloWorldView.as_view(),name='hello_world'),
    url(r'^subscriber',SubscriberView.as_view(),name='subscriber'),
    url(r'^login',login),
]