# Generated by Django 4.0.2 on 2022-02-02 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stdprofile', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='id',
        ),
        migrations.AlterField(
            model_name='profile',
            name='reg_no',
            field=models.CharField(max_length=16, primary_key=True, serialize=False),
        ),
    ]
