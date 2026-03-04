import pandas as pd
from pathlib import Path

project_root = Path(__file__).resolve().parents[1]

df = pd.read_csv(project_root / "data" / "all_seasons.csv")
joined_df = pd.read_csv(project_root / "clean_data" / "nba_players_with_team_info.csv")

results_dir = project_root / "results"
results_dir.mkdir(exist_ok=True)

missing_summary = df.isna().sum().reset_index()
missing_summary.columns = ["column", "missing_values"]
missing_summary = missing_summary.sort_values("missing_values", ascending=False)

top_scorers = df[df["pts"] > 20][
    ["player_name", "season", "team_abbreviation", "pts", "reb", "ast"]
].sort_values("pts", ascending=False)

conference_summary = joined_df.groupby("conference").agg(
    player_season_records=("player_name", "count"),
    avg_points=("pts", "mean"),
    avg_rebounds=("reb", "mean"),
    avg_assists=("ast", "mean")
).round(2)

division_summary = joined_df.groupby("division").agg(
    player_season_records=("player_name", "count"),
    avg_points=("pts", "mean")
).round(2).sort_values("avg_points", ascending=False)

season_scoring_summary = df.groupby("season").agg(
    avg_points=("pts", "mean"),
    avg_rebounds=("reb", "mean"),
    avg_assists=("ast", "mean")
).round(2)

missing_summary.to_csv(results_dir / "missing_values_summary.csv", index=False)
top_scorers.to_csv(results_dir / "top_scorers.csv", index=False)
conference_summary.to_csv(results_dir / "conference_summary.csv")
division_summary.to_csv(results_dir / "division_summary.csv")
season_scoring_summary.to_csv(results_dir / "season_scoring_summary.csv")

print("Summary tables created in results/")