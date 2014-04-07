from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Query.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^exact/','my_app.views.my_exact'),
    url(r'^iexact/','my_app.views.my_iexact'),    
    url(r'^contains/','my_app.views.my_contains'),
    url(r'^icontains/','my_app.views.my_icontains'),
    url(r'^in/','my_app.views.my_in'),
    url(r'^gt/','my_app.views.my_gt'), 
    url(r'^gte/','my_app.views.my_gte'), 
    url(r'^lt/','my_app.views.my_lt'), 
    url(r'^lte/','my_app.views.my_lte'),
    url(r'^startswith/','my_app.views.my_startswith'),
    url(r'^istartswith/','my_app.views.my_istartswith'),
    url(r'^endswith/','my_app.views.my_endswith'),
    url(r'^iendswith/','my_app.views.my_iendswith'),
    url(r'^range/','my_app.views.my_range'),
    url(r'^year/','my_app.views.my_year'),
    url(r'^month/','my_app.views.my_month'),
    url(r'^day/','my_app.views.my_day'),
    url(r'^isnull/','my_app.views.my_isnull'),
)
