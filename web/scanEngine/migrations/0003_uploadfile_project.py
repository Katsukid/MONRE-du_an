# Generated by Django 3.2.23 on 2024-08-31 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
        ('scanEngine', '0002_uploadfile'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadfile',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.project'),
        ),
    ]
