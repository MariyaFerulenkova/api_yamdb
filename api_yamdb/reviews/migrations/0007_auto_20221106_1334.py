# Generated by Django 2.2.16 on 2022-11-06 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0006_auto_20221106_1327'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='user',
            name='unique_user_username_email',
        ),
        migrations.AddConstraint(
            model_name='user',
            constraint=models.UniqueConstraint(fields=('username', 'email'), name='unique_username_email'),
        ),
    ]
