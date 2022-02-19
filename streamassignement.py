import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import streamlit.components.v1 as components
st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSydmQLXYG892eM3wbpkv1Yu_-DYceLmh7aQe9EyVjaSMXeZrZDK0rT5th6OlGoJFCCeg&usqp=CAU')
st.title('Top Tiktok Tracks')

components.html("""<hr style="height:2px;border:none;color:#333;background-color:#333;" /> """)
df = pd.read_csv('tiktok.csv')

df2 = df.rename(columns={'track_id': 'TrackID', 'track_name': 'TrackName', 'artist_name':'Artist','danceability': 'Danceability', 'loudness': 'Loudness', 'liveness': 'Liveness', 'valence': 'Valence', 'duration_mins':'Duration', 'acousticness': 'Acousticness', 'speechiness':'Speechiness', 'popularity': 'Popularity'})
if st.checkbox('Show Dataset for Top Tiktok Tracks'):
    chart_data = df2
    chart_data
#st.dataframe(df2.head(10))


topsongs = df2.sort_values('Popularity')
top20songs = topsongs.head(20)
topsong= topsongs.head(1)

#data = [go.Bar(x=top20songs.TrackName,
           # y=top20songs.Danceability)]

#fig = py.iplot(data, filename='Danceability/Song')
#st.plotly_chart(fig)

st.subheader('Bar Chart of Top Genres')
fig = px.bar(df['genre'].value_counts().nlargest(20), color_discrete_sequence=px.colors.sequential.Sunset)
st.plotly_chart(fig)


st.subheader('Bar Chart of Top 20 Artists ')
fig=px.histogram(data_frame=top20songs, x='Artist',color_discrete_sequence=px.colors.sequential.Sunset)
st.plotly_chart(fig)

st.subheader('Bar Chart of Top 20 Songs: Duration vs. Danceability per Track')
fig = px.bar(top20songs, x='Duration', y='TrackName', color='Danceability')
st.plotly_chart(fig)

st.subheader('Correlation Plot of Song Elements')
corr=top20songs.drop(columns=['TrackID', 'TrackName', 'artist_id','Artist','album_id','duration','release_date', 'playlist_id', 'playlist_name', 'genre']).corr()

fig = px.imshow(corr, color_continuous_scale='piyg', color_continuous_midpoint=0)
st.plotly_chart(fig)


st.subheader('Scatterplot of Top 20 Songs:Duration vs. Energy vs. Danceability')
fig = px.scatter(top20songs, x='TrackName', y='Duration', color='Danceability', size='energy', size_max=14, hover_name='TrackName', color_discrete_sequence=px.colors.sequential.Sunset)
st.plotly_chart(fig)

components.html("""<hr style="height:2px;border:none;color:#333;background-color:#333;" /> """)

@st.cache
def convert_df(df2):
     # IMPORTANT: Cache the conversion to prevent computation on every rerun
     return df2.to_csv().encode('utf-8')

csv = convert_df(df2)

if st.checkbox('Top Song on Tiktok Music Video'):
    st.video('https://www.youtube.com/watch?v=XMZ8zknb6BA')

st.download_button(
     label="Download tiktok data as CSV",
     data=csv,
     file_name='tiktok.csv',
     mime='text/csv',
 )