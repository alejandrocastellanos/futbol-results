# Generated by Django 5.0.6 on 2024-07-04 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('single_match', '0002_alter_match_result_local_team_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='winning_team',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='matchguessresult',
            name='winning_team',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
