# Generated by Django 3.1 on 2020-08-13 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genzone', '0003_customer_regdate'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminLogin',
            fields=[
                ('adminid', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
