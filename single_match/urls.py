from django.urls import path

from .views import single_match_view, update_match_result, delete_match, new_match, teams_position

urlpatterns = [
    path("", single_match_view, name="single_match_view"),
    path("new-match/", new_match, name="new_match"),
    path("<int:match_id>/update/", update_match_result, name="update_match_result"),
    path("<int:match_id>/delete-match/", delete_match, name="delete_match"),
    path("teams_position/", teams_position, name="teams_position")
]
