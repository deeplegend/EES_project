import streamlit as st
from PIL import Image
import base64
st.set_page_config(page_title="About Us",layout="wide")

#calling all images
image_14=Image.open("Images/Ankit Baidsen.png")
image_29=Image.open("Images/Deep Patel.png")
image_30=Image.open("Images/Devu Gupta.png")
image_42=Image.open("Images/Khoshang Kashyap.png")
image_46=Image.open("Images/Kunal Agrawal.png")

with st.container():
    st.header("About the project")
    st.write("The \"Carbon Footprint Calculator\" project is a web-based application designed to empower individuals to track and manage their carbon footprint in their daily lives. With growing concerns about climate change and environmental sustainability, there is an increasing need for tools that enable individuals to understand the impact of their actions on the planet. This project aims to address this need by providing a user-friendly platform for calculating and visualizing personal carbon emissions.")
    st.write("The core functionality of the \"Carbon Footprint Calculator\" revolves around its ability to calculate carbon emissions based on user inputs. Through a simple and intuitive user interface, users can input data such as their daily commute distance, monthly electricity consumption, meals per day, and waste generation. These inputs are then processed using predefined emission factors for different activities and regions to calculate the user's total carbon footprint.")
    st.write("One of the key features of the website is its integration with Google Sheets for data storage and management. By allowing users to submit their personal details through a form embedded in the application, the project facilitates the collection of data for analysis and reporting.")
    st.write("---")
#with st.container():
#    st.header("About Us")
#    st.write("")
#    st.write("---")
with st.container():
    st.header("**The Team**")
    Ankit_column,Deep_column,Devu_column,Khoshang_column,Kunal_column=st.columns((1,1,1,1,1))
    with Ankit_column:
        st.image(image_14,caption="Ankit Baidsen\n (IMT-014)")
        col1,col2,col3,col4,col5=st.columns(5)
        with col1:
            st.write('')
        with col2:
            st.markdown(
                """<a href="https://www.linkedin.com/in/ankit-baidsen-202106290/">
                <img src="data:image/png;base64,{}" width="20">
                </a>""".format(
                base64.b64encode(open("Images/LinkedIn_icon.png", "rb").read()).decode()),unsafe_allow_html=True)
        with col3:
            st.markdown(
                """<a href="https://github.com/neetance">
                <img src="data:image/png;base64,{}" width="20">
                </a>""".format(
                base64.b64encode(open("Images/Github_icon.png", "rb").read()).decode()),unsafe_allow_html=True)
        with col4:
            st.write('')
    with Deep_column:
        st.image(image_29,caption="Deep Patel\n (IMT-029)")
        col1,col2,col3,col4=st.columns(4)
        with col1:
            st.write('')
        with col2:
            st.markdown(
                """<a href="https://www.linkedin.com/in/deep-patel-5b3912207/">
                <img src="data:image/png;base64,{}" width="20">
                </a>""".format(
                base64.b64encode(open("Images/LinkedIn_icon.png", "rb").read()).decode()),unsafe_allow_html=True,)
        with col3:
            st.markdown(
                """<a href="https://github.com/deeplegend">
                <img src="data:image/png;base64,{}" width="20">
                </a>""".format(
                base64.b64encode(open("Images/Github_icon.png", "rb").read()).decode()),unsafe_allow_html=True,)
        with col4:
            st.write('')
    with Devu_column:
        st.image(image_30,caption="Devu Gupta\n (IMT-030)")
        col1,col2,col3,col4=st.columns(4)
        with col1:
            st.write('')
        with col2:
            st.markdown(
                """<a href="https://www.linkedin.com/in/devu-gupta007/">
                <img src="data:image/png;base64,{}" width="20">
                </a>""".format(
                base64.b64encode(open("Images/LinkedIn_icon.png", "rb").read()).decode()),unsafe_allow_html=True,)
        with col3:
            st.markdown(
                """<a href="https://github.com/codealpha07">
                <img src="data:image/png;base64,{}" width="20">
                </a>""".format(
                base64.b64encode(open("Images/Github_icon.png", "rb").read()).decode()),unsafe_allow_html=True,)
        with col4:
            st.write('')
    with Khoshang_column:
        st.image(image_42,caption="Khoshang Kashyap\n (IMT-042)")
        col1,col2,col3,col4=st.columns(4)
        with col1:
            st.write('')
        with col2:
            st.markdown(
                """<a href="https://www.linkedin.com/in/khoshang/">
                <img src="data:image/png;base64,{}" width="20">
                </a>""".format(
                base64.b64encode(open("Images/LinkedIn_icon.png", "rb").read()).decode()),unsafe_allow_html=True,)
        with col3:
            st.markdown(
                """<a href="https://github.com/khoshang-k">
                <img src="data:image/png;base64,{}" width="20">
                </a>""".format(
                base64.b64encode(open("Images/Github_icon.png", "rb").read()).decode()),unsafe_allow_html=True,)
        with col4:
            st.write('')
    with Kunal_column:
        st.image(image_46,caption="Kunal Agrawal\n (IMT-046)")
        col1,col2,col3,col4=st.columns(4)
        with col1:
            st.write('')
        with col2:
            st.markdown(
                """<a href="https://www.linkedin.com/in/kunal-agrawal-886b08285/">
                <img src="data:image/png;base64,{}" width="20">
                </a>""".format(
                base64.b64encode(open("Images/LinkedIn_icon.png", "rb").read()).decode()),unsafe_allow_html=True,)
        with col3:
            st.markdown(
                """<a href="https://github.com/Kunal-8799">
                <img src="data:image/png;base64,{}" width="20">
                </a>""".format(
                base64.b64encode(open("Images/Github_icon.png", "rb").read()).decode()),unsafe_allow_html=True,)
        with col4:
            st.write('')
    st.write("---")
    
