from django.core.management.base import BaseCommand
from tasks.models import Task
from django.contrib.auth.models import User
from faker import Faker
from datetime import datetime

class Command(BaseCommand):
    help = "Adding 5 fake tasks"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fake = Faker()

    def handle(self, *args, **options):
        # Create a fake user
        user = User.objects.create_user(
            username=self.fake.user_name(),  # create_user نیاز به username دارد
            password="123456@98765"
        )

        # Create 5 fake tasks
        for _ in range(5):
            Task.objects.create(
                user=user,
                title=self.fake.sentence(nb_words=6),
                description=self.fake.paragraph(nb_sentences=5),
                is_completed=True,
                created_at=datetime.now()
            )
        self.stdout.write(self.style.SUCCESS("✅ 5 fake tasks created successfully!"))
