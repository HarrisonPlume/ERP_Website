from django_q.models import Schedule
Schedule.objects.filter(name='Update Payment Status').delete()

Schedule.objects.create(
    func='ERP.tasks.update_payment_status',
    name='Update Payment Status',
    schedule_type=Schedule.MINUTES,
    minutes=1,
    repeats=-1
)