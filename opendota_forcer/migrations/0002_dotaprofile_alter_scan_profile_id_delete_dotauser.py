# Generated by Django 4.2.16 on 2024-09-26 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('opendota_forcer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DotaProfile',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='Profile')),
                ('name', models.CharField(max_length=50, verbose_name='Player name')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active status')),
            ],
        ),
        migrations.AlterField(
            model_name='scan',
            name='profile_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opendota_forcer.dotaprofile', verbose_name='Profile'),
        ),
        migrations.DeleteModel(
            name='DotaUser',
        ),
    ]
