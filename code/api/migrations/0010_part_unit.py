# Generated by Django 4.0.4 on 2022-05-17 02:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_alter_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='part',
            name='unit',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, related_name='partUnitFk', to='api.unitmeasure'),
        ),
    ]