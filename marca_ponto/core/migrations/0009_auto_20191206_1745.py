# Generated by Django 3.0 on 2019-12-06 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20191206_1744'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registroponto',
            name='dia',
        ),
        migrations.AlterField(
            model_name='registroponto',
            name='colaborador',
            field=models.ForeignKey(db_column='nome_completo', default=0, on_delete=django.db.models.deletion.CASCADE, to='core.Colaboradores'),
        ),
    ]
