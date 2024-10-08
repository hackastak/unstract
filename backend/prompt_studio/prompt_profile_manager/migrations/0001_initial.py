# Generated by Django 4.2.1 on 2024-01-20 08:04

import uuid

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="ProfileManager",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "profile_id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("profile_name", models.TextField(unique=True)),
                (
                    "vector_store",
                    models.TextField(
                        db_comment="Field to store the chosen vector store."
                    ),
                ),
                ("embedding_model", models.TextField()),
                (
                    "llm",
                    models.TextField(
                        db_comment="Field to store the LLM chosen by the user"
                    ),
                ),
                ("chunk_size", models.IntegerField(blank=True, null=True)),
                ("chunk_overlap", models.IntegerField(blank=True, null=True)),
                ("reindex", models.BooleanField(default=False)),
                ("vector_size", models.IntegerField()),
                (
                    "pdf_to_text_converters",
                    models.TextField(blank=True, null=True),
                ),
                (
                    "retrival_strategy",
                    models.TextField(
                        blank=True,
                        choices=[
                            ("simple", "Simple retrieval"),
                            ("subquestion", "Subquestion from prompt"),
                            ("vector+keyword", "Uses vector for retrieval"),
                        ],
                        db_comment="Field to store the retrieval strategy for prompts",
                    ),
                ),
                (
                    "similarity_top_k",
                    models.IntegerField(
                        blank=True,
                        db_comment="Field to store matching count",
                        null=True,
                    ),
                ),
                (
                    "section",
                    models.TextField(
                        blank=True,
                        db_comment="Field to store limit to section",
                        null=True,
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        blank=True,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="profile_created_by",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "modified_by",
                    models.ForeignKey(
                        blank=True,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="profile_modified_by",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
