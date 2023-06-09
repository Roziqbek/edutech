# Generated by Django 4.2 on 2023-05-20 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_chatmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='KursModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='img')),
            ],
        ),
        migrations.RemoveField(
            model_name='videomodel',
            name='img',
        ),
        migrations.AlterField(
            model_name='videomodel',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.kursmodel'),
        ),
    ]
