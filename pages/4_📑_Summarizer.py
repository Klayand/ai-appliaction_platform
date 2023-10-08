from io import StringIO

import streamlit as st
from backbones import summarize
import os
from utils import show_icon


def generate_summary():
    os.environ['http_proxy'] = os.getenv('HTTPS_PROXY')

    st.set_page_config(page_title='Your Summary Assistant', page_icon=":memo:")

    st.markdown("# :pencil2: :rainbow[Help you make a Summary]")

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
        "## :orange[**Input text:  start typing :black_nib:**]",
        height=50)

    if len(prompt) == 0:
        st.text("Please input your text.")

    else:
        summary = summarize(prompt)
        try:
            words = summary[0]["summary_text"]
            st.write(words)
        except:
            st.text("Please refresh the page.")


generate_summary()