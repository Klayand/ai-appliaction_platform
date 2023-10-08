import streamlit as st
from backbones import text_to_image
import os
from utils import show_icon, headers
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())


def generate_image():
    # os.environ['http_proxy'] = "http://127.0.0.1:19180"

    st.set_page_config(page_title='Generate Your Own Image', page_icon=":bridge_at_night:")

    st.markdown("# :unicorn_face: :rainbow[Your Text-to-Image Artistry Studio]")

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
        "## :orange[**Enter prompt: start typing, Brainstorm :writing_hand:**](alt+enter --> run). e.g. An astronaut riding a rainbow unicorn, cinematic, dramatic.")

    if len(prompt):
        image_name = text_to_image(prompt, headers)

        st.image(image_name)

        st.download_button(
            label="Download Image",
            data=open(image_name, 'rb'),
            file_name=image_name,
        )


generate_image()
