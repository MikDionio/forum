# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-24 09:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.CharField(max_length=50)),
                ('commnet_pubdate', models.DateTimeField(verbose_name='date commented')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(max_length=50)),
                ('post_text', models.CharField(max_length=1000)),
                ('post_author', models.CharField(max_length=30)),
                ('post_pubdate', models.DateTimeField(verbose_name='date posted')),
            ],
        ),
        migrations.AddField(
            model_name='comments',
            name='comment_post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.Post'),
        ),
    ]
