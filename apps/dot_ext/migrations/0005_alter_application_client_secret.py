# Generated by Django 3.2.18 on 2023-05-13 07:18

from django.db import migrations, models
import oauth2_provider.generators
import oauth2_provider.models


class Migration(migrations.Migration):

    dependencies = [
        ('dot_ext', '0004_auto_20221117_2012'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='client_secret_plain',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.RunSQL(
            "UPDATE dot_ext_application SET client_secret_plain=client_secret"
        ),
        migrations.AlterField(
            model_name='application',
            name='client_secret',
            field=oauth2_provider.models.ClientSecretField(blank=True, db_index=True, default=oauth2_provider.generators.generate_client_secret, help_text='Hashed on Save. Copy it now if this is a new secret.', max_length=255),
        ),
    ]
