from django.shortcuts import render, redirect
from .models import League, Team, Player
from django.db.models import Count
from . import team_maker

def index(request):
	context = {
		#Display all leagues
		"leagues": League.objects.all(),
		#Display all teams
		"teams": Team.objects.all(),
		#Display all players
		"players": Player.objects.all(),
		#List baseball teams only
		"baseball": League.objects.filter(sport="baseball"),
		#List Womens' teams only
		"womens": League.objects.filter(name__contains="womens"),
		#List any type of Hockey
		"hockey": League.objects.filter(name__contains="hockey"),
		#List anything other than Football
		"no_football": League.objects.exclude(name__contains="football"),
		#List conferences
		"conferences": League.objects.filter(name__contains="conference"),
		#List Atlantic regions
		"atlantic": League.objects.filter(name__contains="Atlantic"),
		#List teams located in Dallas
		"dallas": Team.objects.filter(location__contains="Dallas"),
		#List teams named the Raptors
		"raptors": Team.objects.filter(team_name__contains="Raptors"),
		#Teams whose location includes "City"
		"city": Team.objects.filter(location__contains="City"),
		#Teams whos name begin with "T"
		"teams_T": Team.objects.filter(team_name__startswith="T"),
		#Teams ordered 
		"location_order": Team.objects.order_by("location"),
		#Teams ordered reverse
		"name_order": Team.objects.order_by("-team_name"),
		#every player with last name: "Cooper"
		"coopers": Player.objects.filter(last_name__contains="Cooper"),
		#every player with first name: "Joshua"
		"joshuas": Player.objects.filter(first_name__contains="Joshua"),
		#every player with last name "Cooper" except for "Joshua"
		"coopers2": Player.objects.filter(last_name__contains="Cooper").exclude(first_name__contains="Joshua"), 
		"both_names": Player.objects.filter(first_name__contains="Alexander")| Player.objects.filter(first_name__contains="Wyatt"),
		#Teams in Atlantic Soccer conference
		"atlanticSC": Team.objects.filter(league__name__contains="Atlantic Soccer Conference"),
		#Players in Boston Penguins
		"penguins_players": Player.objects.filter(curr_team__team_name__contains="penguins"),
		#Players in ICBC
		"icbc": Player.objects.filter(curr_team__league__name__contains="International Collegiate Baseball Conference"),
		#Plyers in ACAF with last name "Lopez"
		"acaf_lopez": Player.objects.filter(curr_team__league__name__contains="American Conference of Amateur Football") & Player.objects.filter(last_name__contains="Lopez"),
		#All football players
		"football": Player.objects.filter(curr_team__league__sport__contains="football"),
		#All teams with a (current) player named "Sophia"
		"sophia_team": Team.objects.filter(curr_players__first_name__contains="Sophia"),
		#All leagues with a (current) player named "Sophia"
		"sophia_leagues": League.objects.filter(teams__curr_players__first_name__contains="Sophia"),
		#Everyone with the last name "Anderson" who DOESN'T (currently) play for the Phoenix Rays
		"anderson": Player.objects.filter(last_name__contains="Anderson") & Player.objects.exclude(curr_team__team_name__contains="Rays"),
		#All teams that Samuel Evans has played with
		"sam_evans": Team.objects.filter(all_players__first_name="Samuel").filter(all_players__last_name="Evans"),
		#All players played for Manitoba Tiger-Cats
		"manitoba": Player.objects.filter(all_teams__team_name__contains="Tiger-Cats"),
		#All players formerly played for Vikings (not current)
		"former_viking": Player.objects.filter(all_teams__team_name__contains="Vikings").exclude(curr_team__team_name__contains="Vikings"),
		#All teams Jacob Gray played for
		"jacob": Team.objects.filter(all_players__first_name="Jacob").filter(all_players__last_name="Gray").exclude(team_name__contains='Colts'),
		#All players with first name Joshua played for AFABSP
		"joshua": Player.objects.filter(first_name="Joshua").filter(all_teams__league__name__contains="Atlantic Federation of Amateur Baseball Players"),
		#All teams with 12+ players
		"12players": Team.objects.annotate(num_players=Count("all_players")).filter(num_players__gt=12),
		#All players sorted by number of teams they've played for
		"sort_players_team_number": Player.objects.annotate(num_team=Count("all_teams")).order_by("-num_team")
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")

def show_team(request):

	return render(request, "leagues/index.html")

def show_player(request):

	return render(request, "leagues/index.html")
