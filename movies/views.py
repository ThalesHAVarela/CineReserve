from django.shortcuts import render

from rest_framework import viewsets
from .models import Movie, Session, Seat, Reservation, Ticket
from .serializers import MovieSerializer, SessionSerializer, SeatSerializer, ReservationSerializer, TicketSerializer, UserSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from rest_framework.decorators import action
from rest_framework.response import Response


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class SessionViewSet(viewsets.ModelViewSet):
    serializer_class = SessionSerializer
    def get_queryset(self):
        movie = self.request.query_params.get('movie')
        if movie:
            return Session.objects.filter(movie=movie)
        return Session.objects.all()

class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer
    def get_queryset(self):
        session = self.request.query_params.get('session')
        if session:
            return Seat.objects.filter(session=session)
        return Seat.objects.all()


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    def perform_create(self, serializer):
        seat = serializer.validated_data['seat']
        if seat.seat_status != 'available':
            raise ValidationError('Este assento já está reservado.')
        serializer.save(user=self.request.user)
        seat.seat_status = 'reserved'
        seat.save()

    @action(detail=True, methods=['post'])
    def checkout(self,request, pk=None):
        reservation = self.get_object()
        if reservation.status != 'pending':
            raise ValidationError('esta reserva não está pendente.')
        reservation.status = 'confirmed'
        reservation.save()
        seat = reservation.seat
        seat.seat_status = 'purchased'
        seat.save()
        ticket = Ticket.objects.create(user=reservation.user, seat=reservation.seat)
        return Response({'message': 'Reserva confirmada e ticket gerado.', 'ticket_id': ticket.id})


class TicketViewSet(viewsets.ModelViewSet):
    serializer_class = TicketSerializer
    def get_queryset(self):
        return Ticket.objects.filter(user=self.request.user)

class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]