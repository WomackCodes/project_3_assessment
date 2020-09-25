# Generated by Django 3.1.1 on 2020-09-25 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='widget',
            old_name='widget',
            new_name='description',
        ),
        migrations.AddField(
            model_name='widget',
            name='quantity',
            field=models.CharField(default='description', max_length=50),
            preserve_default=False,
        ),
    ]
