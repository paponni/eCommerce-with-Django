# Generated by Django 2.2.12 on 2021-06-09 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20210609_1425'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='transactional_id',
        ),
        migrations.AddField(
            model_name='order',
            name='transaction_id',
            field=models.CharField(max_length=200, null=True),
        ),
    ]