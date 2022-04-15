# Generated by Django 4.0.4 on 2022-04-15 17:11

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('candidate', '0003_candidate_voters'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='voters',
            field=models.ManyToManyField(related_name='voted_candidates', to=settings.AUTH_USER_MODEL),
        ),
    ]