# Generated by Django 2.0.4 on 2018-05-13 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Despesas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=255, verbose_name='Descrição')),
                ('valor', models.DecimalField(decimal_places=2, default=0.0, max_digits=8)),
                ('categoria', models.CharField(choices=[('A', 'Mercado'), ('B', 'Farmácia'), ('C', 'Alimentação'), ('D', 'Lazer'), ('E', 'Saúde'), ('F', 'Casa'), ('G', 'Educação'), ('L', 'Outros')], max_length=1, verbose_name='Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Receitas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=255, verbose_name='Descrição')),
                ('valor', models.DecimalField(decimal_places=2, default=0.0, max_digits=8)),
                ('categoria', models.CharField(choices=[('H', 'Salário'), ('I', 'Investimentos'), ('J', 'Reajuste'), ('K', 'Outros')], max_length=1, verbose_name='Categoria')),
            ],
        ),
    ]
