import streamlit as st

def app():
    st.set_page_config(page_title="World Bank Budget Dashboard", layout="wide")
    st.markdown("""
                <h1 style='text-align: center; font-weight: bold;'>🌐 What is the World Bank?</h1>
                """, unsafe_allow_html=True)
    st.markdown("""
                <style>
                .big-font {
                    font-size:20px !important;
                    font-weight:bold;
                }
                .small-font {
                    font-size:16px !important;
                }
                </style>
                
                <div class="small-font">The World Bank is an 
                international financial institution aimed at reducing poverty and supporting development in poorer 
                countries. The World Bank's goals are to end extreme poverty and promote 
                shared prosperity through financial products, policy advice, and support for a wide array of 
                investments in areas like education, health, infrastructure, and environmental sustainability.</div><br>
            """, unsafe_allow_html=True)

    st.markdown("""
                <h1 style='text-align: center; font-weight: bold;'>World Bank's Work Program Groups Overview</h1>
                """, unsafe_allow_html=True)
    st.markdown("""
                <style>
                .big-font {
                    font-size:20px !important;
                    font-weight:bold;
                }
                .small-font {
                    font-size:16px !important;
                }
                </style>
    
                <div class="big-font">🌍 Centrally Managed Accounts & Miscellaneous Programs</div>
                <div class="small-font">Encompasses centrally administered programs, including a variety of specialized initiatives across different themes.</div><br>

                <div class="big-font">🤝 Client Engagement</div>
                <div class="small-font">Focused on engaging with countries or regions to support development projects, policy advice, and technical assistance tailored to their specific needs.</div><br>

                <div class="big-font">💸 Funded by External Funds - All Funds</div>
                <div class="small-font">Includes programs primarily financed through external sources, reflecting partnerships and alignment with the priorities of external donors.</div><br>

                <div class="big-font">🏛️ Institutional, Governance, and Administrative Services</div>
                <div class="small-font">Focuses on strengthening institutional capacities, governance, and administrative services to improve public sector management and efficiency.</div><br>

                <div class="big-font">🎁 Operational Grant Making Facilities</div>
                <div class="small-font">Refers to funds and mechanisms providing grants for specific projects, crucial for financing development especially in low-income countries or for global public goods.</div><br>

                <div class="big-font">⚙️ Program and Practice Management</div>
                <div class="small-font">Concentrates on internal management and operational efficiency of the World Bank's development initiatives, ensuring resources are used effectively.</div><br>
            """, unsafe_allow_html=True)


if __name__ == '__main__':
    app()