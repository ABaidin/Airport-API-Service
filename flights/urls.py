from rest_framework.routers import DefaultRouter
from flights.views import (
    AirportViewSet,
    AirplaneViewSet,
    AirplaneTypeViewSet,
    CrewViewSet,
    RouteViewSet,
    FlightViewSet,
    OrderViewSet,
    TicketViewSet,
)


app_name = "flights"

router = DefaultRouter()
router.register(r"airports", AirportViewSet)
router.register(r"airplanes", AirplaneViewSet)
router.register(r"airplane-types", AirplaneTypeViewSet)
router.register(r"crews", CrewViewSet)
router.register(r"routes", RouteViewSet)
router.register(r"flights", FlightViewSet)
router.register(r"orders", OrderViewSet)
router.register(r"tickets", TicketViewSet)

urlpatterns = router.urls
