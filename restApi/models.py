from django.db import models


class user(models.Model):
    username = models.TextField(null=False, unique=True)
    balance = models.DecimalField(null=False, max_digits=12, decimal_places=2)


class lobby(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.TextField(null=False, unique=True)
    capacity = models.IntegerField(null=False)
    entryFee = models.DecimalField(null=False, max_digits=12, decimal_places=2)
    finished = models.BooleanField(default=False)


class lottery(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    lobby = models.ForeignKey(lobby,  null=False, on_delete=models.RESTRICT)
    houseChargeAmount = models.DecimalField(
        default=0.0, null=False, max_digits=12, decimal_places=2)
    participants = models.ManyToManyField(
        user, blank=True, related_name="lottery_participants")
    winner = models.ForeignKey(
        user, related_name="lottery_winner_user", null=True, on_delete=models.RESTRICT)
