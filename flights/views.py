from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters

from flights.models import (
    Airplane,
    AirplaneType,
    Airport,
    Crew,
    Route,
    Flight,
    Order,
    Ticket,
)
from flights.serializers import (
    AirplaneSerializer,
    AirplaneTypeSerializer,
    AirportSerializer,
    CrewSerializer,
    RouteSerializer,
    FlightSerializer,
    OrderSerializer,
    TicketSerializer,
)


class AirplaneViewSet(viewsets.ModelViewSet):
    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer


class AirplaneTypeViewSet(viewsets.ModelViewSet):
    queryset = AirplaneType.objects.all()
    serializer_class = AirplaneTypeSerializer


class AirportViewSet(viewsets.ModelViewSet):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer


class CrewViewSet(viewsets.ModelViewSet):
    queryset = Crew.objects.all()
    serializer_class = CrewSerializer


class RouteViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer


class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.select_related("route", "airplane").prefetch_related(
        "crew"
    )
    serializer_class = FlightSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_fields = ("route", "airplane")
    ordering_fields = ("departure_time", "arrival_time")


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.select_related("flight__airplane", "order__user")
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ["user"]
    ordering_fields = ["created_at"]


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.select_related("user")
    serializer_class = TicketSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ["flight", "order"]
    ordering_fields = ["row", "seat"]

    def perform_create(self, serializer):
        serializer.save(order=Order.objects.create(user=self.request.user))
