

from django.urls import path


from yoga_website.views import (AtelierListView,
                                CreateAteliersView,
                                )

from. import views
urlpatterns = [
    path('', views.home, name="home"),
    path('upload', views.upload_file, name="upload"),
    path('yoga', views.yoga, name="yoga"),
    path('video', views.video, name="video"),
    path('connexion', views.connexion, name="connexion"),
    path('deconnexion', views.deconnexion, name="deconnexion"),
    path('inscription', views.register, name="inscription"),
    path('ateliers', views.ateliers, name="ateliers"),
    path('detailAteliers/<int:idatelier>/<int:idclient>',
         views.detail_atelier, name="detailAteliers"),
    path('contact', views.contact_email, name="contact"),
    path('register', views.register, name="register"),
    path('espace', views.my_espace, name="espace"),
    path('clients', views.clients, name="clients"),
    path('nidra', views.nidra, name="nidra"),
    path('participants/<int:id_atelier>', views.participants, name="participants"),
    path('test', AtelierListView.as_view(), name="test"),
    path('inscribe/<int:id_atelier>/<int:id_client>',
         views.inscribe, name="inscribe"),
    path('unsubscribe/<int:id_atelier>/<int:id_client>',
         views.unsubscribe, name="unsubscribe"),
    path('new-atelier/', CreateAteliersView.as_view(), name="create-atelier"),
    path('registrationValid/<str:username>/<str:email>',
         views.registration_valid, name="registrationValid"),
    path('deleteAtelier/<int:id_atelier>', views.delete_atelier, name="deleteAtelier"),
    path('delete_compte', views.delete_compte, name="delete_compte"),
    path('resetPassword', views.reset_password, name="reset_password"),
    path('resetPasswordStep/<str:username>/<str:adresse_mail>',
         views.reset_password_step_2, name="resset_password_step"),
]
