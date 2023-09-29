from ..models import Bookings
from django.contrib.auth.models import User
import json

def get_bookings(request):
    if request.method == "POST":
        req_body = json.loads(request.body.decode("utf-8"))
        user = User.objects.get(username=req_body["username"])
        bookings = Bookings.objects.filter(account=user)
