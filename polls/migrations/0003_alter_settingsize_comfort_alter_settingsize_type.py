# Generated by Django 4.1 on 2023-01-05 03:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_settingsize'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settingsize',
            name='comfort',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='polls.comfort'),
        ),
        migrations.AlterField(
            model_name='settingsize',
            name='type',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='polls.type'),
        ),
    ]