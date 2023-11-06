from django.core import management
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help="Load all Geography fixtures"
    def __init__(self):
        super().__init__()
        self.app_name = "app_platform"
        self.cities = "cities.json"
        self.states = "states.json"
    def call_command(self, file_name):
        management.call_command("loaddata", file_name, app=self.app_name)

    def handle(self, *args, **kwargs):
        self.call_command(self.states)
        self.call_command(self.cities)