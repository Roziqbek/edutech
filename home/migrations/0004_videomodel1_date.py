# Generated by Django 4.2 on 2023-05-20 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_videomodel1_delete_videomodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='videomodel1',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
