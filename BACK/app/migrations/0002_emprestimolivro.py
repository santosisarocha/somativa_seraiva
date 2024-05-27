# Generated by Django 5.0.6 on 2024-05-26 20:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmprestimoLivro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('emprestimoFK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='EmprestimoFK', to='app.emprestimo')),
                ('livroFK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='EmprestimoLivro', to='app.livro')),
            ],
        ),
    ]