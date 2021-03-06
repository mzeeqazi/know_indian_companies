# Generated by Django 3.0.5 on 2020-07-03 08:49

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0004_auto_20200702_1314'),
    ]

    operations = [
        migrations.CreateModel(
            name='CinModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CIN', models.CharField(max_length=100)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AddField(
            model_name='usersearches',
            name='companySearched',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='companies.CinModel'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='companydetail',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='companydetail', to='companies.CinModel'),
        ),
    ]
