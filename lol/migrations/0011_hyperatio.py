# Generated by Django 2.1.7 on 2019-03-29 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lol', '0010_auto_20190329_1925'),
    ]

    operations = [
        migrations.CreateModel(
            name='HypeRatio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_game', models.IntegerField()),
                ('like_votes', models.IntegerField()),
                ('dislike_votes', models.IntegerField()),
            ],
        ),
    ]