from django.db import models

class Match(models.Model):
    local_team = models.CharField(max_length=200)
    img_local_team = models.CharField(max_length=500)
    result_local_team = models.IntegerField(null=True, blank=True)
    visiting_team = models.CharField(max_length=200)
    img_visiting_team = models.CharField(max_length=500)
    result_visiting_team = models.IntegerField(null=True, blank=True)
    winning_team = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.local_team} vs {self.visiting_team}'

class MatchGuessResult(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    result_local_team = models.IntegerField()
    result_visiting_team = models.IntegerField()
    winning_team = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.winning_team = 'draft'
        if self.result_local_team > self.result_visiting_team:
            self.winning_team = self.match.local_team
        if self.result_local_team < self.result_visiting_team:
            self.winning_team = self.match.visiting_team
        super().save(*args, **kwargs)

class FutbolTable(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    team = models.CharField(max_length=200, blank=True)
    draft = models.IntegerField(default=0, blank=True)
    lose = models.IntegerField(default=0, blank=True)
    win  = models.IntegerField(default=0, blank=True)
    matches_number = models.IntegerField(null=True, blank=True)
    gol_difference =  models.IntegerField(default=0, blank=True)
    total_points = models.IntegerField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.matches_number = self.draft + self.lose + self.win
        self.total_points = (self.win * 3) + self.draft
        super().save(*args, **kwargs)
