# Generated by Django 5.0.3 on 2024-03-13 08:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('website', models.CharField(blank=True, max_length=100, null=True)),
                ('msg', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='postapp.post')),
                ('reply', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='postapp.comment')),
            ],
        ),
    ]
