from django.apps import AppConfig
from django.http import HttpResponse

class VendorManagementConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "vendor_management"

    # def ready(self):
    #     import vendor_management.signals
    #
    # def index(request):
    #     return HttpResponse("Welcome to the Vendor Management System!")