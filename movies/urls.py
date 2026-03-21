from rest_framework import routers
from .views import MovieViewSet, SessionViewSet, SeatViewSet, ReservationViewSet, TicketViewSet, RegisterView
from django.urls import path

router = routers.DefaultRouter()
router.register('movies', MovieViewSet)
router.register('sessions', SessionViewSet, basename='session')
router.register('seats', SeatViewSet)
router.register('reservations', ReservationViewSet)
router.register('tickets', TicketViewSet, basename= 'ticket')

urlpatterns = router.urls