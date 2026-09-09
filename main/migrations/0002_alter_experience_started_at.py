import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='started_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
