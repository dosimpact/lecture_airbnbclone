from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "This commnad tells you that I love you"

    def add_arguments(self, parser):
        parser.add_argument(
            "--times",
            type=int,
            help="How many times do you want me to tell you that I love you?",
        )

    def handle(self, *args, **options):
        times = options.get("times")
        for t in range(0, times):
            self.stdout.write(self.style.SUCCESS("I love you"))
