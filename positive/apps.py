from django.apps import AppConfig
from django.db.models.signals import post_migrate

from utils import create_groups


class PositiveConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'positive'

    def ready(self):
        post_migrate.connect(criar_dados_iniciais, sender=self)

def criar_dados_iniciais(sender, **kwargs):
    from django.contrib.auth.models import Group, Permission

    from positive.models import CustomUser

    CustomUser.objects.get_or_create(
            username='Admin',
            email='admin@admin.com',
            password='123456789', 
            is_staff=True, 
            is_superuser=True
        )
    # Exemplo: criar categorias padrão caso não existam
    categorias_iniciais = ['Free', 'Basic', 'Premium', 'Master']

    for group in categorias_iniciais:
        create_groups(group)
