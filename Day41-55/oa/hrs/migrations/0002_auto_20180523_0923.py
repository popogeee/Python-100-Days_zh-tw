# Generated by Django 2.0.5 on 2018-05-23 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dept',
            name='excellent',
            field=models.BooleanField(default=0, verbose_name='是否優秀'),
        ),
        migrations.AlterField(
            model_name='dept',
            name='location',
            field=models.CharField(max_length=10, verbose_name='部門所在地'),
        ),
        migrations.AlterField(
            model_name='dept',
            name='name',
            field=models.CharField(max_length=20, verbose_name='部門名稱'),
        ),
        migrations.AlterField(
            model_name='dept',
            name='no',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='部門編號'),
        ),
        migrations.AlterField(
            model_name='emp',
            name='comm',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True),
        ),
        migrations.AlterField(
            model_name='emp',
            name='mgr',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
