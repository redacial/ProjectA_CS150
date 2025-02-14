import pandas as pd
import plotly.express as px

from dash import Dash, dcc, html, Input, Output

# Preparing your data for usage *******************************************
# Load air quality data (PM 2.5)
df = pd.read_csv("ad_viz_plotval_data.csv")
df["Date"] = pd.to_datetime(df["Date"])

# Load Wildfire Data *******************************************
wildfire_df = pd.read_csv("Washington_Large_Fires_1973-2022.csv")

# Filter for 2015 data
wildfire_df["STARTDATE"] = pd.to_datetime(wildfire_df["STARTDATE"], errors="coerce")
wildfire_df = wildfire_df[wildfire_df["STARTDATE"].dt.year == 2015]

# Aggregate wildfire data by data
wildfire_agg = wildfire_df.groupby("STARTDATE")["ACRES"].sum().reset_index()

# Inintialize Dash App **************************
app = Dash(__name__)

app.layout = html.Div([
    html.H1("Impact of 2015 wildfires on Air Quality in Washington", style = {'textAlign': 'center'}),

    dcc.Graph(id="pm25-line-chart"),

    html.Label("Select a County"),
    dcc.Dropdown(
        id="region-dropdown",
        options=[{"label": region, "value": region} for region in df["County"].dropna().unique()],
        multi=True,
        placeholder = "Filter by County"),

    dcc.Graph(id="wildfire-bar-chart")

])
# Call Back ***********************
@app.callback(
    [Output("pm25-line-chart", "figure"),
     Output("wildfire-bar-chart", "figure")],
    [Input("region-dropdown", "value")]
)
def update_graph(selected_regions):
    filtered_pm25 = df
    filtered_wildfire = wildfire_agg

    if selected_regions:
        filtered_pm25 = df[df["County"].isin(selected_regions)]

    pm25_fig = px.line(
        filtered_pm25, x="Date", y="Daily Mean PM2.5 Concentration", color="County",
        title = "PM2.5 Levels overtime in Washington (2015)",
        labels={"Date": "Date", "Daily Mean PM2.5 Concentration": "PM2.5 (µg/m³)"})
    wildfire_fig = px.bar (
        filtered_wildfire, x="STARTDATE", y="ACRES",
        title="Acres Burned by Wildfires in Washington (2015)",
        labels={"STARTDATE": "Date", "ACRES": "Acres"})

    return pm25_fig, wildfire_fig

if __name__ == "__main__":
    app.run_server(debug=True)
