from django.conf.urls import url
#from .views import DescontoCalc
from .views import UsuariosList, UsuariosC, UsuariosRUD
from .views import ProdutosList, ProdutosC, ProdutosRUD, ProdutosDisc

urlpatterns = [
    
    url(r'^products/(?P<pk>[0-9]+)/?$', ProdutosDisc.as_view(), name='produtos-list'),

    url(r'^users/?$', UsuariosList.as_view(), name='usuarios-list'),
    url(r'^users/crud?/?$', UsuariosC.as_view(), name='usuarios-create'),
    url(r'^users/crud?/(?P<pk>[0-9]+)/?$', UsuariosRUD.as_view(), name='usuarios-rud'),

    url(r'^products/?$', ProdutosList.as_view(), name='produtos-list'),
    url(r'^products/crud?/?$', ProdutosC.as_view(), name='produtos-create'),
    url(r'^products/crud?/(?P<pk>[0-9]+)/?$', ProdutosRUD.as_view(), name='produtos-rud'),

    #url(r'^discounts/(?P<pkP>[0-9]+)/(?P<pkU>[0-9]+)/$', DescontoCalc.as_view(), name='desconto'),
    
]