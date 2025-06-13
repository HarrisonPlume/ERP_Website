from django.utils import timezone
from .models import UserProfile


def update_payment_status():
    now = timezone.now()
    UserProfile.objects.filter(next_payment__lte = now, is_paid =True).update(is_paid=False)
    print("Payment_status_Checked")