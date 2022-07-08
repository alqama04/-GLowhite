# Generated by Django 4.0.4 on 2022-07-07 15:00

import accounts.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_user_is_active_alter_user_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=accounts.models.LowerEmailField(max_length=100, unique=True),
        ),
    ]