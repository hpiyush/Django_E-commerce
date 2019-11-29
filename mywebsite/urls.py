from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from cart.views import cart_view, add_to_cart, buy_now, remove_from_cart, all_orders
from homepage.views import home_view
from posts.views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)
from products.views import products_view, ProductDetailView
from register.views import register_view, profile, preference
from hooks.views import test_hook

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('products/', products_view, name='products'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    # Cart / Order / Buy now
    path('cart/', cart_view, name='cart'),
    path('orders/', all_orders, name='orders'),

    path('cart/<int:item_id>/', add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:id>/', remove_from_cart, name='remove_from_cart'),
    path('products/buy/<int:id>/', buy_now, name='buy_now'),
    # Accounts Related
    path('register/', register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    # Password related
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password/password_reset.html'),
         name='password_reset'),
    path('password_reset_confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='password/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password_reset/done', auth_views.PasswordResetDoneView.as_view(template_name='password/password_reset_done.html'),
         name='password_reset_done'),
    path('password_reset/complete', auth_views.PasswordResetCompleteView.as_view(template_name="password/password_reset_complete.html"),
         name='password_reset_complete'),
    # Profile etc
    path('profile/', profile, name="profile"),
    path('preferences/', preference, name="preference"),
    # Posts related
    path('posts/', PostListView.as_view(), name='posts'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/create/', PostCreateView.as_view(), name='post_create'),
    path('posts/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),

    path('test_hook/', test_hook, name='test_hook')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
