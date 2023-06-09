# Generated by Django 4.2 on 2023-04-16 12:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('students', '0004_alter_course_students'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='user',
        ),
        migrations.AddField(
            model_name='student',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='course',
            name='number',
            field=models.CharField(max_length=6),
        ),
    ]
