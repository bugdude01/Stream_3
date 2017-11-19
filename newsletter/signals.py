import arrow
from .models import Purchase


def subscription_created(sender, **kwargs):
    ipn_obj = sender
    newsletter_id = ipn_obj.custom.split('-')[0]
    user_id = ipn_obj.custom.split('-')[1]
    Purchase.objects.create(newsletter_id=newsletter_id,
                            user_id=user_id,
                            subscription_end=arrow.now().replace(weeks=+4).datetime)


def subscription_was_cancelled(sender, **kwargs):
    ipn_obj = sender
    newsletter_id = ipn_obj.custom.split('-')[0]
    user_id = ipn_obj.custom.split('-')[1]
    purchase = Purchase.objects.get(user_id=user_id, newsletter_id=newsletter_id)
    purchase.subscription_end = arrow.now().datetime
    purchase.save()