from django.conf.urls import url
from .views import DescontoCalc
from .views import UsuariosList, UsuariosCreate, UsuariosRead, UsuariosUpdate, UsuariosDelete
from .views import ProdutosList, ProdutosCreate, ProdutosRead, ProdutosUpdate, ProdutosDelete

urlpatterns = [
    
    url(r'^discounts/(?P<pkP>[0-9]+)/(?P<pkU>[0-9]+)/$', DescontoCalc.as_view(), name='desconto'),


    url(r'^users/?$', UsuariosList.as_view(), name='usuarios-list'),
    url(r'^users/create?/?$', UsuariosCreate.as_view(), name='usuarios'),
    url(r'^users/read?/(?P<pk>[0-9]+)/?$', UsuariosRead.as_view(), name='usuarios'),
    url(r'^users/update?/(?P<pk>[0-9]+)/?$', UsuariosUpdate.as_view(), name='usuarios'),
    url(r'^users/delete?/(?P<pk>[0-9]+)/?$', UsuariosDelete.as_view(), name='usuarios'),


    url(r'^products/?$', ProdutosList.as_view(), name='usuarios-list'),
    url(r'^products/create?/?$', ProdutosCreate.as_view(), name='usuarios'),
    url(r'^products/read?/(?P<pk>[0-9]+)/?$', ProdutosRead.as_view(), name='usuarios'),
    url(r'^products/update?/(?P<pk>[0-9]+)/?$', ProdutosUpdate.as_view(), name='usuarios'),
    url(r'^products/delete?/(?P<pk>[0-9]+)/?$', ProdutosDelete.as_view(), name='usuarios'),

]