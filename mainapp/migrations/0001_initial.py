# Generated by Django 3.0.3 on 2020-05-07 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=10)),
                ('quantity', models.IntegerField(default=0)),
                ('pub_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
