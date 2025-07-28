import streamlit as st


from PIL import Image
from utils import generate_caption

st.set_page_config(page_title=" PicToWords")

st.title(" See n Say: Image Caption Generator")
st.write("Upload an image to get an auto-generated caption!")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    with st.spinner("Generating caption..."):
        caption = generate_caption(image)
    
    st.success(f"**Caption:** {caption}")


