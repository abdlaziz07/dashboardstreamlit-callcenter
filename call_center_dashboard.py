import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("📞 Call Center Dashboard")

df = pd.read_csv("cleaned_call_center.csv", parse_dates=['Call_timestamp'])

st.sidebar.header("Filter")
channel = st.sidebar.multiselect("Pilih Channel:", options=df['Channel'].unique(), default=df['Channel'].unique())
filtered_df = df[df['Channel'].isin(channel)]

st.subheader("Ringkasan Data")
st.write(filtered_df.describe())

st.subheader("Jumlah Panggilan per Bulan")
monthly_calls = filtered_df.resample('M', on='Call_timestamp').size()
st.line_chart(monthly_calls)

st.subheader("Durasi Panggilan vs CSAT Score")
fig, ax = plt.subplots()
sns.scatterplot(data=filtered_df, x='Call duration in minutes', y='Csat_score', hue='Channel', ax=ax)
st.pyplot(fig)

st.subheader("Distribusi Sentimen")
sentiment_count = filtered_df['Sentiment'].value_counts()
st.bar_chart(sentiment_count)

st.markdown("---")
st.markdown("📊 Dibuat dengan Streamlit oleh [Nama Kamu]")
