from django.urls import path
from App import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',views.inicio, name='Inicio'),

    path('locales',views.locales, name='Locales'),
    path('locales_formulario', views.locales_formulario, name="Locales_Formulario"),  
    path('buscar_local/',views.buscar_local, name="Buscar_Local"),  

    path('vendedores',views.vendedores, name='Vendedores'),
    path('vendedores_formulario',views.vendedores_formulario, name="Vendedores_Formulario"),  
    path('leer_vendedor/',views.leer_vendedor, name="Leer_Vendedor"),
    path('eliminar_vendedor/<vendedor_nombre>',views.eliminar_vendedor, name="Eliminar_Vendedor"),
    path('editar_vendedor/<vendedor_nombre>',views.editar_vendedor, name="Editar_Vendedor"),

    path('productos',views.productos, name='Productos'),
    path('productos_formulario',views.productos_formulario, name="Productos_Formulario"),
    path('buscar_producto/',views.buscar_producto, name="Buscar_Producto"),
    path('descripcion/',views.descripcion, name="Descripcion"),

    path('login', views.login_request, name='Log_In'),
    path('register', views.register, name='Register'),  
    path('logout', LogoutView.as_view(template_name='App/logout.html'), name='Log_Out'),
    path('editar_perfil', views.editar_perfil, name='Editar_Perfil'),

    path('nuevos_productos', views.nuevos_productos, name='Nuevos_Productos'), 
    path('nuevos_productos_formulario', views.nuevos_productos_formulario, name='Nuevos_Productos_Formulario'), 
    path('nuevos_productos_detalle', views.info_nuevos_productos, name='Nuevos_Productos_Detalle'),
    path('editar_nuevo_producto/<nuevo_producto_nombre>', views.editar_nuevo_producto, name='Nuevos_Productos_Editar'),
    path('eliminar_nuevo_producto/<nuevo_producto_nombre>', views.eliminar_nuevo_producto, name='Nuevos_Productos_Eliminar'),

    path('about_us/',views.about_us, name="About_Us"),
] 