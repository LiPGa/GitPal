# Generated by Django 2.0 on 2019-05-28 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(blank=True, db_column='issue_comment_body', max_length=5000, null=True)),
                ('created_at', models.DateTimeField(db_column='issue_comment_created_at', max_length=50, null=True)),
            ],
            options={
                'db_table': 'github_event_issus_comment',
                'managed': False,
            },
        ),
    ]
