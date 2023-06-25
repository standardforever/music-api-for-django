# Generated by Django 3.2.17 on 2023-06-25 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_musicgenrequiz_question_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='musicgenrequiz',
            name='question1',
        ),
        migrations.RemoveField(
            model_name='musicgenrequiz',
            name='question2',
        ),
        migrations.RemoveField(
            model_name='musicgenrequiz',
            name='question3',
        ),
        migrations.AddField(
            model_name='musicgenrequiz',
            name='option_1',
            field=models.CharField(default='', max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='musicgenrequiz',
            name='option_2',
            field=models.CharField(default='', max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='musicgenrequiz',
            name='option_3',
            field=models.CharField(default='', max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='musicgenrequiz',
            name='question',
            field=models.CharField(default='', max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='album',
            name='artist',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='album',
            name='name',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='musicgenre',
            name='artist',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='musicgenre',
            name='name',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='musicgenrequiz',
            name='answer',
            field=models.CharField(max_length=250),
        ),
    ]
