# Generated by Django 3.2.6 on 2021-09-01 13:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myidol', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clusterinfo',
            name='image_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myidol.imageinfo', verbose_name='image_id'),
        ),
    ]
