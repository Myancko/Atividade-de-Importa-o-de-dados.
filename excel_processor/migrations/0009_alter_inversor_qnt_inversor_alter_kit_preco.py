# Generated by Django 4.2.3 on 2023-07-16 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('excel_processor', '0008_alter_inversor_mod_inversor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inversor',
            name='qnt_inversor',
            field=models.IntegerField(blank=True, null=True, verbose_name='Quantidade de inversores'),
        ),
        migrations.AlterField(
            model_name='kit',
            name='preco',
            field=models.DecimalField(decimal_places=2, max_digits=8000, verbose_name='Preço'),
        ),
    ]