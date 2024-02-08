# Generated by Django 5.0.1 on 2024-02-07 15:38

from django.db import migrations

def foreignKeyToManyToManyField(apps, schema_migration):
    Blog = apps.get_model("blog", "Blog")
    for blog in Blog.objects.all():
        blog.contributors.add(blog.author, through_defaults={"contribution" : "Auteur principal"})
        blog.save()


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blog_author_blogcontributor_blog_contributors'),
    ]

    operations = [
        migrations.RunPython(foreignKeyToManyToManyField)
    ]