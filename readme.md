# ✨ AI Application App ✨
[_AI application platform: where art meets algorithms and dreams meet pixels!_ 🚀]((https://klayand-ai-appliaction.streamlit.app/))

### Author: Zikai Zhou

![Smoking Tiger](./gallery/A_smoking_tiger.png)

## Overview

Powered by cutting-edge AI models and wrapped in a Streamlit interface, this app lets you transform plain text prompts into mesmerizing visual masterpieces.

## Technical Features

- **Neural Model**: Leverages the power of the LLM model for image generation, image transfer, audio generation, speech generation and summary generation, providing detailed and accurate depictions.
- **Streamlit Framework**: Built atop the versatile Streamlit library, ensuring a smooth and responsive UI/UX.
- **Dynamic Customization**: You can peek "under the hood", tune hyperparameters like guidance_scale, prompt_strength, and more for fine-grained control.
- **Gallery**: A curated gallery for inspiration, showcasing the prowess of the underlying model.

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/Klayand/ai-appliaction_platform.git
   ```

2. Navigate to the project directory:

   ```bash
   cd AI_applications
   ```

3. Install the dependencies:

   ```python
   pip install -r requirements.txt
   ```

4. Rename the `.streamlit/example_secrets.toml` file to `.streamlit/secrets.toml`.

5. Paste your Replicate API token in the secrets.toml file:

   ```bash
   HUGGINGFACE_API_TOKEN = "paste-your-replicate-api-token-here"
   OPENAI_API_TOKEN = "paste-your-replicate-api-token-here"
   ```

## Usage

1. Run the Streamlit app:

   ```python
   streamlit run 🏠_Home.py
   or
   python main.py 
   ```

2. Navigate to the provided local URL, and voila! Start crafting your visual narratives.

## Contributions

Your insights can make this tool even better! Feel free to fork, make enhancements, and raise a PR.

## Attribution

- **Developed by**: The wizards over at [Stability AI](https://stability.ai/) 🧙‍♂️

- **Model type**: Diffusion-based text-to-image generative model

- **License**: [CreativeML Open RAIL++-M License](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/blob/main/LICENSE.md)

- **Model Description**: This is a model that can be used to generate and modify images based on text prompts. It is a [Latent Diffusion Model](https://arxiv.org/abs/2112.10752) that uses two fixed, pretrained text encoders ([OpenCLIP-ViT/G](https://github.com/mlfoundations/open_clip) and [CLIP-ViT/L](https://github.com/openai/CLIP/tree/main)).

- **Resources for more information**: Check out our [GitHub Repository](https://github.com/Stability-AI/generative-models) and the [SDXL report on arXiv](https://arxiv.org/abs/2307.01952).
