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
    st.title('World Bank\'s Work Program Group Analysis')

    # Pie Charts
    st.subheader('Budget Breakdown by Major Work Program Group')
    col1, col2 = st.columns(2)

    # Function to group categories
    def group_categories(fiscal_year):
        df_year = df[df['Fiscal Year'] == fiscal_year]
        df_grouped = df_year.groupby('Work Program Group')['All Funds (US$, Millions)'].sum().reset_index()
        return df_grouped

    # Define custom color sequence
    color_sequence = px.colors.qualitative.Plotly

    with col1:
        st.markdown('**FY2015**')
        df_2015 = group_categories('2015')
        fig3 = go.Figure(data=[go.Pie(labels=df_2015['Work Program Group'], values=df_2015['All Funds (US$, Millions)'],
                                      textinfo='label+percent', insidetextorientation='radial',
                                      marker=dict(colors=color_sequence))])
        st.plotly_chart(fig3, use_container_width=True)

    with col2:
        st.markdown('**FY2024**')
        df_2024 = group_categories('2024')
        fig4 = go.Figure(data=[go.Pie(labels=df_2024['Work Program Group'], values=df_2024['All Funds (US$, Millions)'],
                                      textinfo='label+percent', insidetextorientation='radial',
                                      marker=dict(colors=color_sequence))])
        st.plotly_chart(fig4, use_container_width=True)

    # Bar Chart for Percent Change
    st.subheader('Percent Change in Budget by Major Work Program Group (FY2015 to FY2024)')

    # Calculate percent change
    df_pct_change = pd.merge(df_2015, df_2024, on='Work Program Group', suffixes=('_2015', '_2024'))
    df_pct_change['Percent Change'] = (df_pct_change['All Funds (US$, Millions)_2024'] - df_pct_change[
        'All Funds (US$, Millions)_2015']) / df_pct_change['All Funds (US$, Millions)_2015'] * 100

    # Create bar chart
    fig5 = go.Figure(data=[go.Bar(x=df_pct_change['Work Program Group'], y=df_pct_change['Percent Change'],
                                  marker=dict(color=color_sequence))])
    fig5.update_layout(xaxis_title='Work Program Group', yaxis_title='Percent Change', height=500)
    st.plotly_chart(fig5, use_container_width=True)

    col3, col4 = st.columns(2)
    with col3:
        # Stacked Bar Chart
        st.subheader('Bank Budget vs All Funds by Major Work Program Group (FY2024)')
        df_fy2024 = df[df['Fiscal Year'] == '2024']
        fig5 = go.Figure(data=[
            go.Bar(name='Bank Budget', x=df_fy2024['Work Program Group'],
                   y=df_fy2024['Bank Budget (BB) (US$, Millions)']),
            go.Bar(name='All Funds', x=df_fy2024['Work Program Group'], y=df_fy2024['All Funds (US$, Millions)'])
        ])
        fig5.update_layout(barmode='stack', height=500, yaxis_title='Bank Funds (US$, Millions)',
                           xaxis_title='Work Program Group')
        st.plotly_chart(fig5, use_container_width=True)

    with col4:
        # Net Bank Budget Contribution Chart
        st.subheader("Net Bank Budget Contribution by Major Work Program Group (FY2024)")

        df_net_budget = df[df['Fiscal Year'] == '2024'].groupby('Work Program Group').sum().reset_index()
        df_net_budget['Net Bank Budget Contribution'] = df_net_budget['Bank Budget (BB) (US$, Millions)'] - \
                                                        df_net_budget[
                                                            'All Funds (US$, Millions)']

        fig7 = go.Figure(data=[
            go.Bar(x=df_net_budget['Work Program Group'], y=df_net_budget['Net Bank Budget Contribution'],
                   marker_color=color_sequence)])
        fig7.update_layout(xaxis_title='Work Program Group', yaxis_title='Net Bank Budget Contribution (US$, Millions)',
                           height=500)
        st.plotly_chart(fig7, use_container_width=True)

    st.markdown("""
    The chart above to the right shows the net contribution from the World Bank's own budget to each major work program group in FY2024, after accounting for external funds. This is calculated by subtracting the "All Funds" amount from the "Bank Budget" amount for each group (The information shown at the chart above to the left).

    A positive value indicates that the World Bank is contributing more from its own budget than it receives in external funds for that work program group. Conversely, a negative value suggests that the work program group is relying more on external funds than on the World Bank's own budget.

    This visualization provides insights into the World Bank's financial commitment to each area of work, and highlights the relative importance of external funds in supporting the Bank's activities.
    """)


if __name__ == '__main__':
    app()
