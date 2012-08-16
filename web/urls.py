from django.conf.urls.defaults import *
from django.contrib.auth.views import login, logout
from django.conf import settings
import tab.views as views
import tab.judge_views as judge_views
import tab.team_views as team_views
import tab.debater_views as debater_views
import tab.pairing_views as pairing_views
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^tab/', include('tab.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
    (r'^$', views.index),
    (r'^403/', views.render_403),
    #All account related info
    (r'^accounts/login/$',  login),
    (r'^accounts/logout/$', logout),
    #All judge related pages
    (r'^judge/(\d+)/$', judge_views.view_judge),
    (r'^judge/(\d+)/delete/$', judge_views.delete_judge),
    (r'^judge/(\d+)/scratches/add/(\d+)/', judge_views.add_scratches),
    (r'^judge/(\d+)/scratches/view/', judge_views.view_scratches),
    (r'^view_judges/$', judge_views.view_judges),
    (r'^enter_judge/$', judge_views.enter_judge),    
    #All school related pages
    (r'^school/(\d+)/$', views.view_school),
    (r'^school/(\d+)/delete/$', views.delete_school),
    (r'^view_schools/$', views.view_schools),
    (r'^enter_school/$', views.enter_school),
    #All room related pages
    (r'^room/(\d+)/$', views.view_room),
    (r'^room/(\d+)/delete/$', views.delete_room),
    (r'^view_rooms/$', views.view_rooms),
    (r'^enter_room/$', views.enter_room),
    
    #Scratch deletion
    (r'^judge/(\d+)/scratches/delete/(\d+)/', views.delete_scratch),
    (r'^team/(\d+)/scratches/delete/(\d+)/', views.delete_scratch),

    
    #All team related pages
    (r'^team/(\d+)/$', team_views.view_team),
    (r'^team/(\d+)/delete/$', team_views.delete_team),
    (r'^team/(\d+)/scratches/add/(\d+)/', team_views.add_scratches),
    (r'^team/(\d+)/stats/', team_views.team_stats),
    (r'^view_teams/$', team_views.view_teams),
    (r'^enter_team/$', team_views.enter_team),
    (r'^team/card/(\d+)/$', team_views.tab_card),
    (r'^team/ranking/$', team_views.rank_teams),
    
    #All debater related pages
    (r'^debater/(\d+)/$', debater_views.view_debater),
    (r'^debater/(\d+)/delete/$', debater_views.delete_debater),
    (r'^view_debaters/$', debater_views.view_debaters),
    (r'^enter_debater/$', debater_views.enter_debater),
    (r'^debater/ranking/$', debater_views.rank_debaters),
    
    #All pairing related pages
    (r'^pairings/status/$', pairing_views.view_status),
    (r'^pairings/view_rounds/$', pairing_views.view_rounds),
    (r'^pairings/send_texts/$', pairing_views.send_texts),
    (r'^round/(\d+)/$', pairing_views.view_round),
    (r'^round/(\d+)/result/$', pairing_views.enter_result),
    (r'^pairing/pair_round/$', pairing_views.pair_round),
    (r'^pairing/confirm_start_tourny/$', pairing_views.confirm_start_new_tourny),
    (r'^pairing/start_tourny/$', pairing_views.start_new_tourny),
    (r'^pairing/backup/$', pairing_views.manual_backup),
    (r'^pairings/pairinglist/$', pairing_views.pretty_pair),
    (r'^pairings/swap/(\d+)/(\d+)/with/(\d+)/(\d+)/$', pairing_views.swap_judges_in_round),
    (r'^pairings/swap_team/(\d+)/(\d+)/with/(\d+)/(\d+)/$', pairing_views.swap_teams_in_round),
)
