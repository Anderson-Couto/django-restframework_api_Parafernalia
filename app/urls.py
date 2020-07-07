from django.conf.urls import url
from .views import ProdutosList, UsuariosList, DescontoCalc
#from .views import ProdutosObj, UsuariosObj

urlpatterns = [
    url(r'^products/?$', ProdutosList.as_view(), name='produtos-list'),
    url(r'^usuarios/?$', UsuariosList.as_view(), name='usuarios-list'),
    url(r'^discounts/(?P<pkP>[0-9]+)/(?P<pkU>[0-9]+)/$', DescontoCalc.as_view(), name='desconto'),
    #url(r'^products/(?P<pk>[0-9]+)/?$', ProdutosObj.as_view(), name='produtos'),
    #url(r'^usuarios/(?P<pk>[0-9]+)/?$', UsuariosObj.as_view(), name='usuarios'),
]