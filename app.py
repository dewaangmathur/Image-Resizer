import streamlit as st
from image_processor import resize_image
from twitter_api import authenticate_twitter, post_images

st.title("📸 Image Resizer & X Publisher")

# Upload image
uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

    # Resize image
    resized_images = resize_image(uploaded_file)
    st.subheader("Resized Images")
    for size, img in resized_images.items():
        st.image(img, caption=f"{size}", use_column_width=True)

    # Post to X
    if st.button("Post to X"):
        api = authenticate_twitter()
        message = post_images(api, resized_images)
        st.success(message)
