from django.db import models
from django.contrib.auth.models import User


class Party(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Candidate(models.Model):
    name = models.CharField(max_length=100)
    party = models.ForeignKey(Party, on_delete=models.CASCADE)
    vote_count = models.PositiveIntegerField(default=0)
    voters = models.ManyToManyField(User, related_name='voted_candidates')

    def __str__(self) -> str:
        return self.name
