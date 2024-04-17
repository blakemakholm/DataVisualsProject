import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st

# Read the data from CSV
df = pd.read_csv("World_Bank_Program_Budget_and_All_Funds_20240406.csv")

# Data preprocessing
df['Fiscal Year'] = df['Fiscal Year'].astype(str)
df['Bank Budget (BB) (US$, Millions)'] = df['Bank Budget (BB) (US$, Millions)'].fillna(0)
df['All Funds (US$, Millions)'] = df['All Funds (US$, Millions)'].fillna(0)

def app():
    st.title('World Bank\'s Total Budget Overview')

    # Stacked Bar Chart
    st.subheader('Total Budget by Major Work Program Group Over Time')
    df_stacked = df[df['Work Program Group'] != 'Funded by External Funds - All Funds'].groupby(
        ['Fiscal Year', 'Work Program Group'])['All Funds (US$, Millions)'].sum().reset_index()
    fig1 = px.bar(df_stacked, x='Fiscal Year', y='All Funds (US$, Millions)', color='Work Program Group', height=500)
    st.plotly_chart(fig1, use_container_width=True)

    # Explanation for excluding "Funded by External Funds"
    st.markdown("""
        **Note:** The "Funded by External Funds - All Funds" category has been excluded from the stacked bar chart above. This category represents reimbursables, which are negative amounts.
        As stated in the data notes:

        > For Bank Budget columns, this line only shows reimbursables.

        Excluding this category allows for a clearer visualization of the total budget across different work program groups over time.
        """)

    # Line Chart
    st.subheader('Total Budget by Major Work Program Group Over Time')
    df_line = df.groupby(['Fiscal Year', 'Work Program Group'])['All Funds (US$, Millions)'].sum().reset_index()
    df_total = df.groupby('Fiscal Year')['All Funds (US$, Millions)'].sum().reset_index()

    fig2 = px.line(df_line, x='Fiscal Year', y='All Funds (US$, Millions)', color='Work Program Group', height=500)

    # Total budget trace
    fig2.add_trace(go.Scatter(x=df_total['Fiscal Year'], y=df_total['All Funds (US$, Millions)'],
                              mode='lines',
                              name='Total Budget',
                              line=dict(color='#1cc959', width=3, dash='dash')))

    fig2.update_layout(yaxis_title='Budget (US$, Millions)')
    st.plotly_chart(fig2, use_container_width=True)

    # ggplot embedding
    st.image("WorldBankplot.png")















if __name__ == '__main__':
    app()