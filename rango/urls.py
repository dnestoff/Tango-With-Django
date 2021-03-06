from django.conf.urls import url
from rango import views

# urlpatterns = [url(matching_criteria, location_of_view, optional_arg)]

urlpatterns = [
  url(r'^$', views.index, name = 'index'),
  url(r'^about/$', views.about, name = 'about'), 
  url(r'^contact/$', views.contact, name = 'contact'),
  url(r'^register/$', views.register, name = 'register'),
  url(r'^login/$', views.user_login, name = 'login'),
  url(r'^logout/$', views.user_logout, name = 'logout'),
  url(r'^add_category/$', views.add_category, name = 'add_category'),
  # <category_name_url> names the parameter
  url(r'^category/(?P<category_name_url>[\w\-]+)/add_page/$', views.add_page, name = 'add_page'),
  url(r'^category/(?P<category_name_url>[\w\-]+)/$', views.category, name = 'category'),
  url(r'^page/(?P<page_name_url>[\w\-]+)/$', views.page, name = 'page'),
  url(r'^restricted/', views.restricted, name = 'restricted')
]