# signals.py
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.contrib import messages
from django.utils.translation import gettext as _
from .models import Gym_class  # Import your model

# Signal Receiver Function
@receiver(pre_delete, sender=Gym_class)
def check_protected(sender, instance, **kwargs):
    print("#########################################")
    if instance.is_protected:
        messages.warning(instance.user, _("This object is currently in use and cannot be deleted."))
        # Optionally, raise an exception to prevent deletion (optional)
        # raise Exception("This object is protected and cannot be deleted.")