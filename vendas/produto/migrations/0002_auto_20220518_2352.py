# Generated by Django 3.1.1 on 2022-05-19 02:52

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='idProduto',
            field=models.UUIDField(default=uuid.uuid1, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='produto',
            name='marca',
            field=models.CharField(max_length=20),
        ),
    ]
