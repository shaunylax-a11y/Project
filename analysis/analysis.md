# NBA Player Statistics – Exploratory Data Analysis

## Introduction
This project explores an NBA player statistics dataset containing player information across multiple seasons. The goal of the project is to understand the structure of the data, summarize important variables, create visualizations, and add team-level information through a join. I chose this dataset because sports data is familiar, interesting, and useful for practicing exploratory data analysis.

## Dataset Source
The main dataset used in this project is `all_seasons.csv`, which contains NBA player information and seasonal statistics. A second dataset, `team_lookup.csv`, was manually created to add conference and division information using the `team_abbreviation` field.

## What the Dataset Contains
The dataset includes player names, team abbreviations, age, height, weight, college, country, draft information, season, and statistics such as points, rebounds, and assists. Each row represents a player-season record.


```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/all_seasons.csv")
joined_df = pd.read_csv("../clean_data/nba_players_with_team_info.csv")
```

## Join Explanation

The join itself was completed in a separate Python script, where the main NBA dataset (`all_seasons.csv`) was merged with a second dataset (`team_lookup.csv`) using `team_abbreviation` as the key. That process created a new file called `nba_players_with_team_info.csv`, which is loaded in this notebook as `joined_df`.

I used a left merge because the NBA player dataset is the main dataset, and I wanted to keep every player-season record while adding conference and division information where a match existed.

This type of merge can create missing values in the new columns if a team abbreviation does not match between the two datasets.


```python
team_lookup = pd.read_csv("../data/team_lookup.csv")
team_lookup.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>team_abbreviation</th>
      <th>conference</th>
      <th>division</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>ATL</td>
      <td>Eastern</td>
      <td>Southeast</td>
    </tr>
    <tr>
      <th>1</th>
      <td>BOS</td>
      <td>Eastern</td>
      <td>Atlantic</td>
    </tr>
    <tr>
      <th>2</th>
      <td>BKN</td>
      <td>Eastern</td>
      <td>Atlantic</td>
    </tr>
    <tr>
      <th>3</th>
      <td>CHA</td>
      <td>Eastern</td>
      <td>Southeast</td>
    </tr>
    <tr>
      <th>4</th>
      <td>CHI</td>
      <td>Eastern</td>
      <td>Central</td>
    </tr>
  </tbody>
</table>
</div>




```python
joined_check = pd.merge(
    df,
    team_lookup,
    how="left",
    on="team_abbreviation"
)

joined_check[["team_abbreviation", "conference", "division"]].head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>team_abbreviation</th>
      <th>conference</th>
      <th>division</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>HOU</td>
      <td>Western</td>
      <td>Southwest</td>
    </tr>
    <tr>
      <th>1</th>
      <td>WAS</td>
      <td>Eastern</td>
      <td>Southeast</td>
    </tr>
    <tr>
      <th>2</th>
      <td>VAN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>LAL</td>
      <td>Western</td>
      <td>Pacific</td>
    </tr>
    <tr>
      <th>4</th>
      <td>DEN</td>
      <td>Western</td>
      <td>Northwest</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.head()
joined_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0</th>
      <th>player_name</th>
      <th>team_abbreviation</th>
      <th>age</th>
      <th>player_height</th>
      <th>player_weight</th>
      <th>college</th>
      <th>country</th>
      <th>draft_year</th>
      <th>draft_round</th>
      <th>...</th>
      <th>ast</th>
      <th>net_rating</th>
      <th>oreb_pct</th>
      <th>dreb_pct</th>
      <th>usg_pct</th>
      <th>ts_pct</th>
      <th>ast_pct</th>
      <th>season</th>
      <th>conference</th>
      <th>division</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Randy Livingston</td>
      <td>HOU</td>
      <td>22.0</td>
      <td>193.04</td>
      <td>94.800728</td>
      <td>Louisiana State</td>
      <td>USA</td>
      <td>1996</td>
      <td>2</td>
      <td>...</td>
      <td>2.4</td>
      <td>0.3</td>
      <td>0.042</td>
      <td>0.071</td>
      <td>0.169</td>
      <td>0.487</td>
      <td>0.248</td>
      <td>1996-97</td>
      <td>Western</td>
      <td>Southwest</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Gaylon Nickerson</td>
      <td>WAS</td>
      <td>28.0</td>
      <td>190.50</td>
      <td>86.182480</td>
      <td>Northwestern Oklahoma</td>
      <td>USA</td>
      <td>1994</td>
      <td>2</td>
      <td>...</td>
      <td>0.3</td>
      <td>8.9</td>
      <td>0.030</td>
      <td>0.111</td>
      <td>0.174</td>
      <td>0.497</td>
      <td>0.043</td>
      <td>1996-97</td>
      <td>Eastern</td>
      <td>Southeast</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>George Lynch</td>
      <td>VAN</td>
      <td>26.0</td>
      <td>203.20</td>
      <td>103.418976</td>
      <td>North Carolina</td>
      <td>USA</td>
      <td>1993</td>
      <td>1</td>
      <td>...</td>
      <td>1.9</td>
      <td>-8.2</td>
      <td>0.106</td>
      <td>0.185</td>
      <td>0.175</td>
      <td>0.512</td>
      <td>0.125</td>
      <td>1996-97</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>George McCloud</td>
      <td>LAL</td>
      <td>30.0</td>
      <td>203.20</td>
      <td>102.058200</td>
      <td>Florida State</td>
      <td>USA</td>
      <td>1989</td>
      <td>1</td>
      <td>...</td>
      <td>1.7</td>
      <td>-2.7</td>
      <td>0.027</td>
      <td>0.111</td>
      <td>0.206</td>
      <td>0.527</td>
      <td>0.125</td>
      <td>1996-97</td>
      <td>Western</td>
      <td>Pacific</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>George Zidek</td>
      <td>DEN</td>
      <td>23.0</td>
      <td>213.36</td>
      <td>119.748288</td>
      <td>UCLA</td>
      <td>USA</td>
      <td>1995</td>
      <td>1</td>
      <td>...</td>
      <td>0.3</td>
      <td>-14.1</td>
      <td>0.102</td>
      <td>0.169</td>
      <td>0.195</td>
      <td>0.500</td>
      <td>0.064</td>
      <td>1996-97</td>
      <td>Western</td>
      <td>Northwest</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 24 columns</p>
</div>



This confirms how the join works directly in the notebook. The main dataset is merged with the team lookup table using `team_abbreviation`, which adds conference and division columns.


```python
print("Shape:", df.shape)
print("\nColumns:")
print(df.columns.tolist())

print("\nInfo:")
df.info()

print("\nSummary statistics:")
display(df.describe())

print("\nMissing values:")
display(df.isna().sum().sort_values(ascending=False))
```

    Shape: (12844, 22)
    
    Columns:
    ['Unnamed: 0', 'player_name', 'team_abbreviation', 'age', 'player_height', 'player_weight', 'college', 'country', 'draft_year', 'draft_round', 'draft_number', 'gp', 'pts', 'reb', 'ast', 'net_rating', 'oreb_pct', 'dreb_pct', 'usg_pct', 'ts_pct', 'ast_pct', 'season']
    
    Info:
    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 12844 entries, 0 to 12843
    Data columns (total 22 columns):
     #   Column             Non-Null Count  Dtype  
    ---  ------             --------------  -----  
     0   Unnamed: 0         12844 non-null  int64  
     1   player_name        12844 non-null  object 
     2   team_abbreviation  12844 non-null  object 
     3   age                12844 non-null  float64
     4   player_height      12844 non-null  float64
     5   player_weight      12844 non-null  float64
     6   college            10990 non-null  object 
     7   country            12844 non-null  object 
     8   draft_year         12844 non-null  object 
     9   draft_round        12844 non-null  object 
     10  draft_number       12844 non-null  object 
     11  gp                 12844 non-null  int64  
     12  pts                12844 non-null  float64
     13  reb                12844 non-null  float64
     14  ast                12844 non-null  float64
     15  net_rating         12844 non-null  float64
     16  oreb_pct           12844 non-null  float64
     17  dreb_pct           12844 non-null  float64
     18  usg_pct            12844 non-null  float64
     19  ts_pct             12844 non-null  float64
     20  ast_pct            12844 non-null  float64
     21  season             12844 non-null  object 
    dtypes: float64(12), int64(2), object(8)
    memory usage: 2.2+ MB
    
    Summary statistics:



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0</th>
      <th>age</th>
      <th>player_height</th>
      <th>player_weight</th>
      <th>gp</th>
      <th>pts</th>
      <th>reb</th>
      <th>ast</th>
      <th>net_rating</th>
      <th>oreb_pct</th>
      <th>dreb_pct</th>
      <th>usg_pct</th>
      <th>ts_pct</th>
      <th>ast_pct</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>12844.000000</td>
      <td>12844.000000</td>
      <td>12844.000000</td>
      <td>12844.000000</td>
      <td>12844.000000</td>
      <td>12844.000000</td>
      <td>12844.000000</td>
      <td>12844.000000</td>
      <td>12844.000000</td>
      <td>12844.000000</td>
      <td>12844.000000</td>
      <td>12844.000000</td>
      <td>12844.000000</td>
      <td>12844.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>6421.500000</td>
      <td>27.045313</td>
      <td>200.555097</td>
      <td>100.263279</td>
      <td>51.154158</td>
      <td>8.212582</td>
      <td>3.558486</td>
      <td>1.824681</td>
      <td>-2.226339</td>
      <td>0.054073</td>
      <td>0.140646</td>
      <td>0.184641</td>
      <td>0.513138</td>
      <td>0.131595</td>
    </tr>
    <tr>
      <th>std</th>
      <td>3707.887763</td>
      <td>4.339211</td>
      <td>9.111090</td>
      <td>12.426628</td>
      <td>25.084904</td>
      <td>6.016573</td>
      <td>2.477885</td>
      <td>1.800840</td>
      <td>12.665124</td>
      <td>0.043335</td>
      <td>0.062513</td>
      <td>0.053545</td>
      <td>0.101724</td>
      <td>0.094172</td>
    </tr>
    <tr>
      <th>min</th>
      <td>0.000000</td>
      <td>18.000000</td>
      <td>160.020000</td>
      <td>60.327736</td>
      <td>1.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>-250.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>3210.750000</td>
      <td>24.000000</td>
      <td>193.040000</td>
      <td>90.718400</td>
      <td>31.000000</td>
      <td>3.600000</td>
      <td>1.800000</td>
      <td>0.600000</td>
      <td>-6.400000</td>
      <td>0.021000</td>
      <td>0.096000</td>
      <td>0.149000</td>
      <td>0.482000</td>
      <td>0.066000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>6421.500000</td>
      <td>26.000000</td>
      <td>200.660000</td>
      <td>99.790240</td>
      <td>57.000000</td>
      <td>6.700000</td>
      <td>3.000000</td>
      <td>1.200000</td>
      <td>-1.300000</td>
      <td>0.040000</td>
      <td>0.130500</td>
      <td>0.181000</td>
      <td>0.525000</td>
      <td>0.103000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>9632.250000</td>
      <td>30.000000</td>
      <td>208.280000</td>
      <td>108.862080</td>
      <td>73.000000</td>
      <td>11.500000</td>
      <td>4.700000</td>
      <td>2.400000</td>
      <td>3.200000</td>
      <td>0.083000</td>
      <td>0.179000</td>
      <td>0.217000</td>
      <td>0.563000</td>
      <td>0.179000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>12843.000000</td>
      <td>44.000000</td>
      <td>231.140000</td>
      <td>163.293120</td>
      <td>85.000000</td>
      <td>36.100000</td>
      <td>16.300000</td>
      <td>11.700000</td>
      <td>300.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.500000</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>


    
    Missing values:



    college              1854
    Unnamed: 0              0
    pts                     0
    ast_pct                 0
    ts_pct                  0
    usg_pct                 0
    dreb_pct                0
    oreb_pct                0
    net_rating              0
    ast                     0
    reb                     0
    gp                      0
    player_name             0
    draft_number            0
    draft_round             0
    draft_year              0
    country                 0
    player_weight           0
    player_height           0
    age                     0
    team_abbreviation       0
    season                  0
    dtype: int64


## Initial Inspection and Descriptive Analysis

To begin the analysis, I inspected the shape of the dataset, reviewed the columns, checked for missing values, and created summary statistics. This helps establish what kind of data is available and what patterns can be explored further through visualization.


```python
df.isna().sum().sort_values(ascending=False).head(15)
```




    college         1854
    Unnamed: 0         0
    pts                0
    ast_pct            0
    ts_pct             0
    usg_pct            0
    dreb_pct           0
    oreb_pct           0
    net_rating         0
    ast                0
    reb                0
    gp                 0
    player_name        0
    draft_number       0
    draft_round        0
    dtype: int64




```python
df["season"].nunique(), df["season"].min(), df["season"].max()
```




    (27, '1996-97', '2022-23')




```python
df.sort_values("pts", ascending=False)[["player_name","season","team_abbreviation","pts","reb","ast"]].head(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>player_name</th>
      <th>season</th>
      <th>team_abbreviation</th>
      <th>pts</th>
      <th>reb</th>
      <th>ast</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>10227</th>
      <td>James Harden</td>
      <td>2018-19</td>
      <td>HOU</td>
      <td>36.1</td>
      <td>6.6</td>
      <td>7.5</td>
    </tr>
    <tr>
      <th>4163</th>
      <td>Kobe Bryant</td>
      <td>2005-06</td>
      <td>LAL</td>
      <td>35.4</td>
      <td>5.3</td>
      <td>4.5</td>
    </tr>
    <tr>
      <th>10634</th>
      <td>James Harden</td>
      <td>2019-20</td>
      <td>HOU</td>
      <td>34.3</td>
      <td>6.6</td>
      <td>7.5</td>
    </tr>
    <tr>
      <th>12839</th>
      <td>Joel Embiid</td>
      <td>2022-23</td>
      <td>PHI</td>
      <td>33.1</td>
      <td>10.2</td>
      <td>4.2</td>
    </tr>
    <tr>
      <th>4302</th>
      <td>Allen Iverson</td>
      <td>2005-06</td>
      <td>PHI</td>
      <td>33.0</td>
      <td>3.2</td>
      <td>7.4</td>
    </tr>
    <tr>
      <th>12740</th>
      <td>Luka Doncic</td>
      <td>2022-23</td>
      <td>DAL</td>
      <td>32.4</td>
      <td>8.6</td>
      <td>8.0</td>
    </tr>
    <tr>
      <th>12564</th>
      <td>Damian Lillard</td>
      <td>2022-23</td>
      <td>POR</td>
      <td>32.2</td>
      <td>4.8</td>
      <td>7.3</td>
    </tr>
    <tr>
      <th>2847</th>
      <td>Tracy McGrady</td>
      <td>2002-03</td>
      <td>ORL</td>
      <td>32.1</td>
      <td>6.5</td>
      <td>5.5</td>
    </tr>
    <tr>
      <th>11537</th>
      <td>Stephen Curry</td>
      <td>2020-21</td>
      <td>GSW</td>
      <td>32.0</td>
      <td>5.5</td>
      <td>5.8</td>
    </tr>
    <tr>
      <th>8013</th>
      <td>Kevin Durant</td>
      <td>2013-14</td>
      <td>OKC</td>
      <td>32.0</td>
      <td>7.4</td>
      <td>5.5</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.sort_values("pts", ascending=True)[["player_name","season","team_abbreviation","pts","reb","ast"]].head(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>player_name</th>
      <th>season</th>
      <th>team_abbreviation</th>
      <th>pts</th>
      <th>reb</th>
      <th>ast</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>6802</th>
      <td>Hamady Ndiaye</td>
      <td>2011-12</td>
      <td>WAS</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>4235</th>
      <td>Nene</td>
      <td>2005-06</td>
      <td>DEN</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>12048</th>
      <td>Nate Hinton</td>
      <td>2021-22</td>
      <td>IND</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2659</th>
      <td>Pepe Sanchez</td>
      <td>2002-03</td>
      <td>DET</td>
      <td>0.0</td>
      <td>0.7</td>
      <td>0.9</td>
    </tr>
    <tr>
      <th>12095</th>
      <td>M.J. Walker</td>
      <td>2021-22</td>
      <td>PHX</td>
      <td>0.0</td>
      <td>0.5</td>
      <td>0.5</td>
    </tr>
    <tr>
      <th>2675</th>
      <td>Paul Shirley</td>
      <td>2002-03</td>
      <td>ATL</td>
      <td>0.0</td>
      <td>0.5</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>9855</th>
      <td>Chris Boucher</td>
      <td>2017-18</td>
      <td>GSW</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>5624</th>
      <td>Martell Webster</td>
      <td>2008-09</td>
      <td>POR</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>4195</th>
      <td>Randy Livingston</td>
      <td>2005-06</td>
      <td>CHI</td>
      <td>0.0</td>
      <td>0.8</td>
      <td>0.2</td>
    </tr>
    <tr>
      <th>12145</th>
      <td>Matt Mooney</td>
      <td>2021-22</td>
      <td>NYK</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.groupby("season")["pts"].mean()
```




    season
    1996-97    8.026077
    1997-98    7.947608
    1998-99    7.358542
    1999-00    7.985845
    2000-01    7.811338
    2001-02    7.982727
    2002-03    7.849299
    2003-04    7.745475
    2004-05    8.088147
    2005-06    7.982533
    2006-07    8.208734
    2007-08    8.267184
    2008-09    8.503820
    2009-10    8.571719
    2010-11    8.206195
    2011-12    7.928870
    2012-13    7.957996
    2013-14    8.090249
    2014-15    8.122561
    2015-16    8.349370
    2016-17    8.426749
    2017-18    8.160370
    2018-19    8.613585
    2019-20    8.726465
    2020-21    8.942407
    2021-22    8.240000
    2022-23    9.121336
    Name: pts, dtype: float64



## Research Questions

This project is guided by the following questions:

1. What does the distribution of scoring look like across all player-season records?
2. How has average scoring changed across NBA seasons?
3. Is there a relationship between player usage percentage and scoring output?
4. What additional insight can be gained by joining team-level conference and division information?


```python
missing_summary = df.isna().sum().reset_index()
missing_summary.columns = ["column", "missing_values"]
missing_summary = missing_summary.sort_values("missing_values", ascending=False)
missing_summary.head(15)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>column</th>
      <th>missing_values</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>6</th>
      <td>college</td>
      <td>1854</td>
    </tr>
    <tr>
      <th>0</th>
      <td>Unnamed: 0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>12</th>
      <td>pts</td>
      <td>0</td>
    </tr>
    <tr>
      <th>20</th>
      <td>ast_pct</td>
      <td>0</td>
    </tr>
    <tr>
      <th>19</th>
      <td>ts_pct</td>
      <td>0</td>
    </tr>
    <tr>
      <th>18</th>
      <td>usg_pct</td>
      <td>0</td>
    </tr>
    <tr>
      <th>17</th>
      <td>dreb_pct</td>
      <td>0</td>
    </tr>
    <tr>
      <th>16</th>
      <td>oreb_pct</td>
      <td>0</td>
    </tr>
    <tr>
      <th>15</th>
      <td>net_rating</td>
      <td>0</td>
    </tr>
    <tr>
      <th>14</th>
      <td>ast</td>
      <td>0</td>
    </tr>
    <tr>
      <th>13</th>
      <td>reb</td>
      <td>0</td>
    </tr>
    <tr>
      <th>11</th>
      <td>gp</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>player_name</td>
      <td>0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>draft_number</td>
      <td>0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>draft_round</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
import matplotlib.pyplot as plt

df["pts"].hist(bins=30)
plt.title("Distribution of Points Per Game (PTS)")
plt.xlabel("PTS")
plt.ylabel("Count")
plt.show()
```


    
![png](Analysis_files/Analysis_16_0.png)
    


### Interpretation of Points Distribution

This histogram shows the distribution of points per game across all player-season records in the dataset. Most observations are concentrated at the lower end of the scoring range, with fewer players averaging very high point totals. This creates a right-skewed distribution, which makes sense because only a small number of players score at an elite level, while many players have lower scoring averages.


```python
avg_pts_by_season = df.groupby("season")["pts"].mean().sort_index()

avg_pts_by_season.plot()
plt.title("Average Points Per Game by Season")
plt.xlabel("Season")
plt.ylabel("Average PTS")
plt.xticks(rotation=90)
plt.show()
```


    
![png](Analysis_files/Analysis_18_0.png)
    


### Interpretation of Average Points by Season

This graph shows how the average points per game in the dataset changes across NBA seasons. While the values do not rise perfectly every year, the overall pattern suggests that average scoring tends to increase over time. This is useful because it shows that player scoring trends are not static and that season-level analysis can reveal broader changes in the game.


```python
df.plot(kind="scatter", x="usg_pct", y="pts")
plt.title("Usage % vs Points Per Game")
plt.xlabel("Usage %")
plt.ylabel("PTS")
plt.show()
```


    
![png](Analysis_files/Analysis_20_0.png)
    


### Interpretation of Usage % vs Points Per Game

This scatterplot compares player usage percentage with points per game. There is a clear positive relationship, meaning that players with higher usage percentages generally tend to score more points. However, the relationship is not perfect, since some players have moderate or even high usage without scoring at the same level. This graph is important because it shows that offensive role and scoring are related, but other factors also affect production.


```python
joined_df[["team_abbreviation", "conference", "division"]].head(10)
joined_df["conference"].value_counts()
joined_df.groupby("conference")["pts"].mean().round(2)
joined_df.groupby("division")["pts"].mean().round(2).sort_values(ascending=False)
```




    division
    Pacific      8.56
    Northwest    8.25
    Southwest    8.22
    Central      8.16
    Atlantic     8.14
    Southeast    8.09
    Name: pts, dtype: float64




```python
division_avg_points = joined_df.groupby("division")["pts"].mean().round(2).sort_values(ascending=False)
division_avg_points
```




    division
    Pacific      8.56
    Northwest    8.25
    Southwest    8.22
    Central      8.16
    Atlantic     8.14
    Southeast    8.09
    Name: pts, dtype: float64




```python
division_avg_points = (
    joined_df.groupby("division")["pts"]
    .mean()
    .round(2)
    .sort_values(ascending=False)
    .reset_index()
)

division_avg_points.columns = ["division", "average_points"]
division_avg_points
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>division</th>
      <th>average_points</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Pacific</td>
      <td>8.56</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Northwest</td>
      <td>8.25</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Southwest</td>
      <td>8.22</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Central</td>
      <td>8.16</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Atlantic</td>
      <td>8.14</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Southeast</td>
      <td>8.09</td>
    </tr>
  </tbody>
</table>
</div>



This table shows the average points per game across all player-season records in each division. Because it includes every type of player-season entry, including lower-scoring and lower-usage players, the averages are much lower than star-player scoring averages. The Pacific division has the highest overall average in this dataset at 8.56 points per game.


```python
top_10_by_division = (
    joined_df.sort_values(["division", "pts"], ascending=[True, False])
    .groupby("division")
    .head(10)
)

division_top10_avg = (
    top_10_by_division.groupby("division")["pts"]
    .mean()
    .round(2)
    .sort_values(ascending=False)
    .reset_index()
)

division_top10_avg.columns = ["division", "average_points_top_10"]
division_top10_avg
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>division</th>
      <th>average_points_top_10</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Atlantic</td>
      <td>30.75</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Pacific</td>
      <td>30.65</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Southwest</td>
      <td>30.46</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Northwest</td>
      <td>30.14</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Central</td>
      <td>29.81</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Southeast</td>
      <td>29.52</td>
    </tr>
  </tbody>
</table>
</div>



This table shows the average points per game for the top 10 scoring player-season records in each division. This gives a different perspective than averaging all players, because it focuses on the highest-scoring performers in each division. That makes it easier to compare where the strongest offensive player-seasons are concentrated.


```python
highest_scorer_by_division = (
    joined_df.sort_values("pts", ascending=False)
    .groupby("division")
    .head(2)[["division", "player_name", "season", "team_abbreviation", "pts"]]
    .sort_values("pts", ascending=False)
    .reset_index(drop=True)
)

highest_scorer_by_division
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>division</th>
      <th>player_name</th>
      <th>season</th>
      <th>team_abbreviation</th>
      <th>pts</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Southwest</td>
      <td>James Harden</td>
      <td>2018-19</td>
      <td>HOU</td>
      <td>36.1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Pacific</td>
      <td>Kobe Bryant</td>
      <td>2005-06</td>
      <td>LAL</td>
      <td>35.4</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Southwest</td>
      <td>James Harden</td>
      <td>2019-20</td>
      <td>HOU</td>
      <td>34.3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Atlantic</td>
      <td>Joel Embiid</td>
      <td>2022-23</td>
      <td>PHI</td>
      <td>33.1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Atlantic</td>
      <td>Allen Iverson</td>
      <td>2005-06</td>
      <td>PHI</td>
      <td>33.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Northwest</td>
      <td>Damian Lillard</td>
      <td>2022-23</td>
      <td>POR</td>
      <td>32.2</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Southeast</td>
      <td>Tracy McGrady</td>
      <td>2002-03</td>
      <td>ORL</td>
      <td>32.1</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Pacific</td>
      <td>Stephen Curry</td>
      <td>2020-21</td>
      <td>GSW</td>
      <td>32.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Northwest</td>
      <td>Kevin Durant</td>
      <td>2013-14</td>
      <td>OKC</td>
      <td>32.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Central</td>
      <td>LeBron James</td>
      <td>2005-06</td>
      <td>CLE</td>
      <td>31.4</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Southeast</td>
      <td>Bradley Beal</td>
      <td>2020-21</td>
      <td>WAS</td>
      <td>31.3</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Central</td>
      <td>Giannis Antetokounmpo</td>
      <td>2022-23</td>
      <td>MIL</td>
      <td>31.1</td>
    </tr>
  </tbody>
</table>
</div>




```python

```
