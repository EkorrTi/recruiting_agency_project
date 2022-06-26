# Generated by Django 3.2.8 on 2022-06-26 11:14

from django.db import migrations, models
import managing.models


class Migration(migrations.Migration):

    dependencies = [
        ('managing', '0003_auto_20220626_1648'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancyemployee',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to=managing.models.user_directory_path),
        ),
        migrations.AddField(
            model_name='vacancyemployee',
            name='smoking',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='vacancyemployee',
            name='work_model',
            field=models.CharField(choices=[('Full time employment', 'Full employment with monthly salary'), ('Single project', 'Single project and single payment on finishing'), ('Internship', 'Internship')], default='Full time employment', max_length=100),
        ),
        migrations.AddField(
            model_name='vacancyemployer',
            name='smoking',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='vacancyemployer',
            name='work_model',
            field=models.CharField(choices=[('Full time employment', 'Full employment with monthly salary'), ('Single project', 'Single project and single payment on finishing'), ('Internship', 'Internship')], default='Full time employment', max_length=100),
        ),
        migrations.AlterField(
            model_name='vacancyemployee',
            name='city',
            field=models.CharField(choices=[('Almaty', 'Almaty, Kazakhstan'), ('Astana', 'Astana, Kazakhstan'), ('Karagandy', 'Karagandy, Kazakhstan'), ('Moscow', 'Moscow, Russia')], max_length=100),
        ),
        migrations.AlterField(
            model_name='vacancyemployer',
            name='city',
            field=models.CharField(choices=[('Almaty', 'Almaty, Kazakhstan'), ('Astana', 'Astana, Kazakhstan'), ('Karagandy', 'Karagandy, Kazakhstan'), ('Moscow', 'Moscow, Russia')], max_length=100),
        ),
    ]
