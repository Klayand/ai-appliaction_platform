import os

import streamlit as st

from utils import show_icon
from streamlit_image_select import image_select
from streamlit.runtime.scriptrunner import RerunData, RerunException

load_dotenv(find_dotenv())

def redirect(page_name: str):
    """A hack to make streamlit redirect to a different page"""
    raise RerunException(RerunData(page_name=page_name))


def main():

    # --- UI Configurations --- #
    st.set_page_config(page_title="AI Tools",
                       page_icon=":bridge_at_night:",
                       layout="wide")

    show_icon(":high_brightness:")
    st.markdown("# :rainbow[Your AI Application Platform]")

    # --- Placeholders for Images and Gallery --- #
    gallery_placeholder = st.empty()

    # --- Sidebar Elements --- #
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
    # if page == 'Musician':
    #     redirect('2_🎵_Musician.py')
    # elif page == 'Drawer':
    #     redirect("1_🪅_Drawer.py")
    # elif page == 'Speaker':
    #     redirect('3_📢_Speaker.py')
    # elif page == 'Summarizer':
    #     redirect('4_📑_Summarizer.py')

    # --- Gallery Display for inspiration or just plain admiration --- #

    with gallery_placeholder.container():
        img = image_select(
            label="Like what you see? Right-click and save! It's not stealing if we're sharing! 😉",
            images=[
                "gallery/farmer_sunset.png", "gallery/astro_on_unicorn.png",
                "gallery/friends.png", "gallery/wizard.png", "gallery/puppy.png",
               "gallery/A_smoking_tiger.png", "gallery/sailboatPicasso.jpg",
                "gallery/sailboatPicasso_color_preserve.jpg", "gallery/sailboatSketch.jpg",
            ],
            captions=["A farmer tilling a farm with a tractor during sunset, cinematic, dramatic",
                      "An astronaut riding a rainbow unicorn, cinematic, dramatic",
                      "A group of friends laughing and dancing at a music festival, joyful atmosphere, 35mm film photography",
                      "A wizard casting a spell, intense magical energy glowing from his hands, extremely detailed fantasy illustration",
                      "A cute puppy playing in a field of flowers, shallow depth of field, Canon photography",
                      "A cool tiger is smoking.",
                      "A demo shows sailboat which is the basic image, have been transferred to Picasso self-portrait style.",
                      "A demo shows transferred Picasso self-portrait image preserving its original color.",
                      "A demo shows sailboat which is the basic image, have been transferred to Sketch style.",
                      ],
            use_container_width=True
        )


if __name__ == "__main__":
    main()





