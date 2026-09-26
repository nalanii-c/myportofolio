from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_experience_started_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='experience',
            options={'ordering': ['-started_at']},
        ),
    ]
