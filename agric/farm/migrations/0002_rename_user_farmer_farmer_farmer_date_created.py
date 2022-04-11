# Generated by Django 4.0.3 on 2022-04-04 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farm', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='farmer',
            old_name='user',
            new_name='farmer',
        ),
        migrations.AddField(
            model_name='farmer',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]