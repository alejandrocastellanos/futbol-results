from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import MatchGuessResult, Match

@receiver(pre_save, sender=Match)
def match_winner(sender, instance, **kwargs):
    if instance.result_local_team and instance.result_visiting_team:
        winner = 'draft'
        if instance.result_local_team > instance.result_visiting_team:
            winner = instance.local_team
        if instance.result_local_team < instance.result_visiting_team:
            winner = instance.visiting_team
        instance.winning_team = winner
