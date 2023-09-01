import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
from statsmodels.graphics.tsaplots import plot_acf


st.set_page_config(
    page_title="Beat81 Dashboard",
    page_icon="💪🏻",
    layout="wide"
)

################################################################################################################
# Import data
data = pd.read_excel('B81.xlsx')
# Note: If your excel sheet with the results is not in the same folder as this code file, then replace 'B81.xlsx' with the path to the excel file!

# Some data cleanup
data['Date'] = pd.to_datetime(data['Date'])  # Convert 'Date' column to datetime format
data['Date'] = data['Date'].dt.strftime('%Y-%m-%d')
data['Recovery points'] = pd.to_numeric(data['Recovery points'], errors='coerce')
data['Recovery points'] = data['Recovery points'].apply(lambda x: int(x) if not np.isnan(x) else x)
data = data.sort_values(by = 'Date', ascending=False)

# Calculate some metrics
recent_sweatPoints= data.sort_values(by = 'Date', ascending=False)['Sweat points'].iloc[0]
recent_recoveryPoints= data.sort_values(by = 'Date', ascending=False)['Recovery points'].iloc[0]
delta_sweatPoints = recent_sweatPoints - data.sort_values(by = 'Date', ascending=False)['Sweat points'].iloc[1]
delta_recoveryPoints = recent_recoveryPoints - data.sort_values(by = 'Date', ascending=False)['Recovery points'].iloc[1]

################################################################################################################
st.title("Beat81 Dashboard")

col1, col2,col3 = st.columns([2,1,1])

with col1:
    st.line_chart(data=data.set_index('Date')[['Sweat points', 'Recovery points']])

col2.subheader("Sweat points 💦")
col2.metric("Recent", recent_sweatPoints, str(delta_sweatPoints))
col2.metric("Average", data['Sweat points'].mean().round(2))
col2.write("🏅 Best day: " + data.loc[data['Sweat points'].idxmax()]['Date']+ " with " + str(data['Sweat points'].max()) + " Sweat points")
col2.write("Total number  of workouts: " + str(len(data)))

col3.subheader("Recovery points 🧘🏻‍♀️")
if np.isnan(delta_recoveryPoints):
    col3.metric("Recent",recent_recoveryPoints,  'not available')
else:
    col3.metric("Recent",recent_recoveryPoints,  str(delta_recoveryPoints))
col3.metric("Average", data['Recovery points'].mean().round(2))
col3.write("🏅 Best day: " + data.loc[data['Recovery points'].idxmax()]['Date']+ " with " + str(data['Recovery points'].max()) + " Recovery points")

st.write("---")
################################################################################################################

col1, col2 = st.columns([1.5, 1.5])

col1.subheader("Overview")
with col1:
    asc = st.radio( "Sort by: ", ["newest", "oldest"], horizontal = True)

if asc == 'newest':
    col1.dataframe(data.sort_values(by = 'Date', ascending=False))
else:
    col1.dataframe(data.sort_values(by = 'Date', ascending=True))


col2.subheader("Stats")
mean_df = data.groupby('Workout Type').mean()
count_df = data.groupby('Workout Type').count()['Date']
stats_table= pd.concat([mean_df, count_df], axis=1)
stats_table.rename(columns={'Date': 'Count'}, inplace=True)  # Rename the count column

with col2:
    radio_stats = st.radio( "Sort by: ", ["Sweat points", "Recovery points", "Count"], horizontal = True)

if radio_stats == 'Sweat points':
    col2.dataframe(stats_table.sort_values(by = 'Sweat points', ascending=False))
elif radio_stats == 'Recovery points':
    col2.dataframe(stats_table.sort_values(by = 'Recovery points', ascending=False))
elif radio_stats == 'Count':
    col2.dataframe(stats_table.sort_values(by = 'Count', ascending=False))


st.write("---")
################################################################################################################
# Autocorrelation plots

# Create subplots
st.header("For time series enthusiasts: Autocorrelations 📈")
fig, axes = plt.subplots(1, 2, figsize=(8, 4))  # 1 row, 2 columns

# Plot autocorrelation for 'Sweat points'
plot_acf(data['Sweat points'].dropna(), lags=50, ax=axes[0])
axes[0].set_title("Sweat Points")
axes[0].set_xlabel("Lags")
axes[0].set_ylabel("Autocorrelation")

# Plot autocorrelation for 'Recovery points'
plot_acf(data['Recovery points'].dropna(), lags=50, ax=axes[1])
axes[1].set_title("Recovery Points")
axes[1].set_xlabel("Lags")
axes[1].set_ylabel("Autocorrelation")

col1, col2 = st.columns([1,2])

with col1:
    st.write("Calculates the autocorrelation of sweat and recovery points for different lags. "
         + "It shows whether there are seasonal or cyclical patterns in the data. "
         + "For example, it can show whether the menstrual cycle periodically affects your recovery points 💁🏻‍♀️.  "
         + "Or whether the winter blues have an effect on your sweat points ❄️. ")

    st.write("Data points contained in  blue area are not significant. "
           +"Read more about autocorrelations [here](https://en.wikipedia.org/wiki/Autocorrelation).")
    
col2.pyplot(fig)

