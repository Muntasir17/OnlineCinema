# Generated by Django 4.0.4 on 2022-04-30 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_alter_movieimage_options_alter_moviecomment_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='movie_trailer',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
