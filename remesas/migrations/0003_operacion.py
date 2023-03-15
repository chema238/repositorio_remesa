# Generated by Django 4.1.7 on 2023-03-15 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('remesas', '0002_rename_ususario_member_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Operacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Phone', models.IntegerField(verbose_name=9)),
                ('Firstname', models.CharField(max_length=100)),
                ('Lastname', models.CharField(max_length=50)),
                ('Cantidad', models.FloatField(max_length=100)),
                ('IBAN', models.CharField(max_length=24)),
                ('Beneficiario', models.CharField(max_length=100)),
                ('Concepto', models.CharField(max_length=100)),
                ('Bank', models.CharField(max_length=100)),
            ],
        ),
    ]