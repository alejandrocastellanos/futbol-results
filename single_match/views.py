from django.shortcuts import render, get_object_or_404, redirect

from single_match.forms import MatchResultForm, NewMatchForm
from single_match.models import Match, FutbolTable


def new_match(request):
    if request.method == 'POST':
        form = NewMatchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('single_match_view')
    return render(request, 'single_match/new_match.html', {'form': NewMatchForm()})


def single_match_view(request):
    matches = Match.objects.all()
    return render(request, 'single_match/single_matches.html', {'matches': matches})


def update_match_result(request, match_id):
    match = get_object_or_404(Match, pk=match_id)
    if request.method == 'POST':
        form = MatchResultForm(request.POST, instance=match)
        if form.is_valid():
            form.save()
            return redirect('single_match_view')
    else:
        form = MatchResultForm(instance=match)

    context = {
        'match': match,
        'form': form
    }

    return render(request, 'single_match/update_match_result.html', context)


def delete_match(request, match_id):
    match = get_object_or_404(Match, pk=match_id)
    if request.method == 'POST':
        match.delete()
    return redirect('single_match_view')

def teams_position(request):
    teams = FutbolTable.objects.all().order_by('-total_points')
    return render(request, 'teams_position/teams_position.html', {'teams': teams})
