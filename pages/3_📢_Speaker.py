import streamlit as st
from backbones import image_to_text, text_to_speech, text_to_text
import os
from utils import show_icon, proxies, headers
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())


def generate_speech():
    os.environ['http_proxy'] = "http://127.0.0.1:19180"

    st.set_page_config(page_title='Story from Image', page_icon=":rainbow:")

    with st.sidebar:
        show_icon(":hugging_face:")
        st.info("**Yo fam! Start here ☝ **", icon="👋")
        with st.form("my_form"):
            st.write(":rainbow[**If you think it's good, give it a**] :thumbsup:")
            submit = st.form_submit_button(label="Good", type="primary", use_container_width=True)
            if submit:
                st.write(":rainbow[*Thanks for your*] :thumbsup:")

        # Credits and resources
        st.divider()

        st.markdown(
            """
            ---
            Follow me on:

            Github → [@Klayand](https://Klayand.github.io) :dragon_face:

            Google Scholar → [@Zikai Zhou](https://scholar.google.com/citations?user=u6TjscAAAAAJ) :eyes:

            """
        )

    st.header(":sunrise: Turn Image into Audio Story")

    uploaded_file = st.file_uploader("Choose an image....", type=["jpg", "png"])

    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()

        with open(uploaded_file.name, 'wb') as file:
            file.write(bytes_data)

        st.image(uploaded_file, caption="Uploaded Image.",
                 use_column_width=True)

        scenario = image_to_text(uploaded_file.name, proxies, headers)

        with st.expander("caption"):
            st.write(scenario[0]['generated_text'])

        story = text_to_text(scenario)
        with st.expander("story"):
            st.write(story)

        speech_name = text_to_speech(story, proxies, headers)
        st.audio(speech_name)

        st.download_button(
            label="Download Speech",
            data=open(speech_name, 'rb'),
            file_name=speech_name,
        )


generate_speech()

