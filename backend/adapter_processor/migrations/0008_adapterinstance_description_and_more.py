# Generated by Django 4.2.1 on 2024-04-29 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "adapter_processor",
            "0007_remove_adapterinstance_is_default_userdefaultadapter",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="adapterinstance",
            name="description",
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name="adapterinstance",
            name="is_friction_less",
            field=models.BooleanField(
                db_comment="Was the adapter created through frictionless onboarding",
                default=False,
            ),
        ),
        migrations.AddField(
            model_name="adapterinstance",
            name="is_usable",
            field=models.BooleanField(db_comment="Is the Adpater Usable", default=True),
        ),
        migrations.AddField(
            model_name="adapterinstance",
            name="shared_to_org",
            field=models.BooleanField(
                db_comment="Is the adapter shared to entire org", default=False
            ),
        ),
    ]
