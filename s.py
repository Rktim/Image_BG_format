import streamlit as st
from rembg import remove
from PIL import Image, ImageOps
import io

def remove_background(image):
    return remove(image)
def convert_image(image, format):
    buffer = io.BytesIO()
    if format.upper() == 'JPG':
        format = 'JPEG'
    if format.upper() in ['WEBP', 'JPEG', 'PNG']:
        try:
            if image.mode != 'RGB':
                image = image.convert('RGB')
            image.save(buffer, format=format.upper())
        except OSError as e:
            st.error(f"Error saving image: {e}")
            return None
    else:
        st.error(f"Unsupported format: {format}. Please choose WEBP, JPEG, or PNG.")
        return None
    buffer.seek(0)
    return buffer

st.title("📸 Remove Background and Change Format")

uploaded_file = st.file_uploader("Choose your image.", type=["webp", "jpeg", "jpg", "png"])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)
    
    custom_filename = st.text_input("Your Image name :", "processed_image")

    if st.button("Background Remover"):
        image_no_bg = remove_background(image)
        st.image(image_no_bg, caption="Image with Background Removed", use_container_width=True)

        format_no_bg = uploaded_file.name.split('.')[-1].upper()
        if format_no_bg == 'JPG':
            format_no_bg = 'JPEG'
        if format_no_bg in ['WEBP', 'JPEG', 'PNG']:
            st.download_button(
                label="Download Image without Background",
                data=convert_image(image_no_bg, format_no_bg),
                file_name=f"{custom_filename}.{format_no_bg.lower()}",
                mime=f"image/{format_no_bg.lower()}"
            )
        else:
            st.error(f"Unsupported format for download: {format_no_bg}. Please choose WEBP, JPEG, or PNG.")

    new_format = st.selectbox("Convert to format", ["WEBP", "JPEG", "PNG", "JPG"])
    if st.button("Convert Format"):
        converted_image = convert_image(image, new_format)
        if converted_image:
            st.download_button(
                label="Download Converted Image",
                data=converted_image,
                file_name=f"{custom_filename}.{new_format.lower()}",
                mime=f"image/{new_format.lower()}"
            )
st.markdown("Hope you find this tool useful! 🚀 If you like it, consider sharing it with your friends. \n\n💡 Created with ❤️ by [Raktim](https://github.com/Rktim)")
