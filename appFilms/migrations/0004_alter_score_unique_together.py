# Generated by Django 5.1.1 on 2025-06-11 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appFilms', '0003_alter_score_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='score',
            unique_together=set(),
        ),
    ]
