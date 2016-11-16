from django.conf.urls import url
from . import views

urlpatterns = [
	url(r"^$", views.index, name="index"),
	url(r"^make_data/", views.make_data, name="make_data"),
	# url(r"^team/(?P<team_id>\d+)/", views.show_team, name="show_team"),
	# url(r"^player/(?P<player_id>\d+)/", views.show_player, name="show_player"),
]
