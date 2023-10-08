import streamlit as st
from backbones import text_to_audio
import os
from utils import show_icon, proxies, headers
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())


def generate_audio():
    os.environ['http_proxy'] = "http://127.0.0.1:19180"

    st.set_page_config(page_title='Your Own Music Assistant', page_icon=":musical_keyboard:")

    st.markdown("# :guitar: :rainbow[Your Text-to-Audio Artistry Assistant]")

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

    prompt = st.text_area(
        "## :orange[**Enter prompt(str or list[str]):  start typing, Brainstorm :writing_hand:**](alt+enter --> run), e.g. lo-fi music with a soothing melody",
        value="")

    if len(prompt):
        audio_name = text_to_audio(prompt, proxies, headers)

        st.audio(audio_name)

        st.download_button(
            label="Download Audio",
            data=open(audio_name, 'rb'),
            file_name=audio_name,
        )


generate_audio()
