# Generated by Django 2.1.2 on 2018-11-05 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perris', '0007_auto_20181030_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='rescatado',
            name='nombre',
            field=models.CharField(default=' ', max_length=30),
            preserve_default=False,
        ),
    ]