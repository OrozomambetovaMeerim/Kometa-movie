# Generated by Django 3.1.3 on 2022-03-17 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='videofile',
            field=models.FileField(null=True, upload_to='videos/', verbose_name='видео'),
        ),
    ]
