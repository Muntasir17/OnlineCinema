# Generated by Django 4.0.4 on 2022-04-30 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0002_remove_setting_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='logo',
            field=models.ImageField(default=1, upload_to='logo/'),
            preserve_default=False,
        ),
    ]
