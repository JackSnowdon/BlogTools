# Generated by Django 3.0.3 on 2020-03-28 19:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('tools', '0002_accountitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtraItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=255)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('amount', models.IntegerField()),
                ('done_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='extra_items', to='accounts.Profile')),
            ],
        ),
    ]
