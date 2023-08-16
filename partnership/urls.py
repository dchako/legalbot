from django.urls import path
from .views import PartnershipView, CreatePartnerView, CreateManagerView
from .views import sociedad_by_rut

urlpatterns = [
    path(
        'partnership',
        PartnershipView.as_view(),
        name="post_partnership_create"
    ),
    path(
        'partnership/<int:pk>',
        PartnershipView.as_view(),
        name="get_put_delete_partnership"
    ),
    path(
        'partnership/<int:pk>/partner',
        CreatePartnerView.as_view(),
        name="post_partner_create_by_partnership"
    ),
    path(
        'partnership/<int:pk>/manager',
        CreateManagerView.as_view(),
        name="post_manager_create_by_partnership"
    ),
    path('sociedad-by-rut/', sociedad_by_rut, name='sociedad-by-rut')
]
