from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ReservationSerializer
from .models import Reservation

# CRUD
# Create your views here.
@api_view(['GET'])
def get_reservations(request):
    reservations = Reservation.objects.all()
    serializer = ReservationSerializer(reservations, many=True)
    return Response(serializer.data)