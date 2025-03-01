# Generated by Django 4.1.3 on 2025-01-22 03:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('destinationguidesapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=400)),
                ('commenter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='destinationguidesapi.user')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='destinationguidesapi.post')),
            ],
        ),
    ]
