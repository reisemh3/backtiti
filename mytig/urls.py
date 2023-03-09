from django.urls import path
from mytig import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('products/', views.RedirectionListeDeProduits.as_view()),
    path('product/<int:pk>/', views.RedirectionDetailProduit.as_view()),
###################
#...TME2 starts...#
    path('product/<int:pk>/image/', views.ProduitImageRandom.as_view()),
    path('product/<int:pk>/image/<int:image_id>/', views.ProduitImage.as_view()),
#...end of TME2...#
###################

###################
#...TME1 starts...#
    # EXO 2
    path('shipPoints/', views.RedirectionListeDeShipPoints.as_view()),
    path('shipPoint/<int:pk>/', views.RedirectionDetailShipPoint.as_view()),
    #
    # EXO 5
    path('poissons/', views.ListeDePoissons.as_view()),
    # path('poisson/<int:pk>/', views.RedirectionListeDePoisson.as_view()),
    path('coquillages/', views.ListeDeCoquillages.as_view()),
    # path('coquillage/<int:pk>/', views.RedirectionListeDeCoquillage.as_view()),
    path('crustaces/', views.ListeDeCrustaces.as_view()),
    # path('crustacre/<int:pk>/', views.RedirectionListeDeCrustace.as_view()),

    path('availableproducts/', views.AvailableList.as_view()),
    path('availableproduct/<int:pk>/', views.AvailableDetail.as_view()),
#...end of TME1...#
###################

    path('onsaleproducts/', views.PromoList.as_view()),
    path('onsaleproduct/<int:pk>/', views.PromoDetail.as_view())
]
