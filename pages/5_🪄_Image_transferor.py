import os
import argparse
from PIL import Image
import torch
from skimage import io, transform
from torchvision import transforms
from torchvision.utils import save_image
from backbones import Model
from utils import ColorTransfer
import streamlit as st
from utils import show_icon


normalize = transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                 std=[0.229, 0.224, 0.225])

trans = transforms.Compose([transforms.ToTensor(),
                            normalize])


def denorm(tensor, device):
    std = torch.Tensor([0.229, 0.224, 0.225]).reshape(-1, 1, 1).to(device)
    mean = torch.Tensor([0.485, 0.456, 0.406]).reshape(-1, 1, 1).to(device)
    res = torch.clamp(tensor * std + mean, 0, 1)

    return res


def resize_image(image_path):
    image = io.imread(image_path)
    if len(image.shape) == 3 and image.shape[-1] == 3:
        H, W, C = image.shape
        if H < W:
            ratio = W / H
            H = 512
            W = int(ratio * H)
        else:
            ratio = H / W
            W = 512
            H = int(ratio * W)

        # 可以放大或者缩小图像
        image = transform.resize(image, (H, W), mode='reflect', anti_aliasing=True)

    return image


def image_transfer():
    model_state_path = 'checkpoint/model_state.pth'

    st.set_page_config(page_title='Image Style Transfer', page_icon=":collision:")

    st.markdown("# :koala: :rainbow[Your Image Transfer Tool]")

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

    content_image_file = st.file_uploader("Upload a base image....", type=["jpg", "png"])

    if content_image_file is not None:
        bytes_data = content_image_file.getvalue()

        with open(content_image_file.name, 'wb') as file:
            file.write(bytes_data)

        st.image(content_image_file, caption="Uploaded Basic Image.",
                 use_column_width=True)

    style_image_file = st.file_uploader("Upload a target image to adopt its style....", type=["jpg", "png"])

    if style_image_file is not None:
        bytes_data = style_image_file.getvalue()

        with open(style_image_file.name, 'wb') as file:
            file.write(bytes_data)

        st.image(style_image_file, caption="Uploaded Target Image.",
                 use_column_width=True)

    if content_image_file is None or style_image_file is None:
        st.write("Make sure you upload both base image and target image.")
    else:
        output_name = st.text_input(
            label="The name of output image",
            value="output"
        )

        color_preserve = st.selectbox(
            label="Preserving the basic image color or not",
            options=(True, False)
        )

        alpha = st.slider(
            "alpha control the fusion degree in Adain",
            value=1.0, min_value=1.0, max_value=10.0, format='%.1f', step=0.5
        )

        content = content_image_file.name
        style = style_image_file.name

        start_generating_button = st.empty()
        if start_generating_button.button("Start Generating"):
            # set device on GPU if available, else CPU
            if torch.cuda.is_available():
                device = torch.device('cuda')
                print(f'# CUDA available: {torch.cuda.get_device_name(0)}')
            else:
                device = 'cpu'

            # set model
            model = Model()
            if model_state_path is not None:
                model.load_state_dict(torch.load(model_state_path, map_location=lambda storage, loc: storage))
            model = model.to(device)

            style_images_tensor = []

            c = Image.open(content)

            if color_preserve:
                s = ColorTransfer(content, style, preserve_paper=False, api=True).transfer_image

            else:
                s = Image.open(style)
            s_tensor = trans(s).unsqueeze(0).to(device)

            c_tensor = trans(c).unsqueeze(0).to(device)

            with torch.no_grad():
                out = model.generate(c_tensor, s_tensor, alpha)

            out = denorm(out, device)
            # c_tensor = denorm(c_tensor, device)
            # s_tensor = denorm(s_tensor, device)
            #
            # out = torch.cat([c_tensor, s_tensor, out], dim=0)
            out.to('cpu')

            if output_name is None:

                c_name = os.path.splitext(os.path.basename(content))[0]

                s_name = os.path.splitext(os.path.basename(style))[0]
                output_name = f'{c_name}_{s_name}'

            if color_preserve:
                save_image(out, f'transfer_images/{output_name}_color_preserve.jpg', nrow=1)
                image_name = f'transfer_images/{output_name}_color_preserve.jpg'
            else:
                save_image(out, f'transfer_images/{output_name}.jpg', nrow=1)
                image_name = f'transfer_images/{output_name}.jpg'

            st.image(image_name, caption="Transferred Image",
                     use_column_width=True)

            st.download_button(
                label="Download Transferred Image",
                data=open(image_name, 'rb'),
                file_name=image_name,
            )


image_transfer()
