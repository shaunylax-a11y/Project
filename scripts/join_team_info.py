import pandas as pd
from pathlib import Path

project_root = Path(__file__).resolve().parents[1]

nba_path = project_root / "data" / "all_seasons.csv"
team_path = project_root / "data" / "team_lookup.csv"
output_path = project_root / "clean_data" / "nba_players_with_team_info.csv"

nba_df = pd.read_csv(nba_path)
team_df = pd.read_csv(team_path)

merged_df = pd.merge(
    nba_df,
    team_df,
    how="left",
    on="team_abbreviation"
)

merged_df.to_csv(output_path, index=False)

print("Merge complete.")
print(merged_df.head())
print("\nMissing values in joined columns:")
print(merged_df[["conference", "division"]].isna().sum())