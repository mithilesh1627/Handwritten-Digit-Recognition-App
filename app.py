import streamlit as st
import numpy as np
import tensorflow as tf
from PIL import Image, ImageOps
from streamlit_drawable_canvas import st_canvas


model = tf.keras.models.load_model("model/cnn_digit_model.h5")

st.set_page_config(page_title="Digit Recognition",  layout="centered")

st.title(" Handwritten Digit Recognition App")
st.markdown("Draw a digit (0–9) below and let the AI predict it!")


canvas_result = st_canvas(
    fill_color="white",
    stroke_width=10,
    stroke_color="black",
    background_color="white",
    width=280,
    height=280,
    drawing_mode="freedraw",
    key="canvas"
)

if st.button("Predict"):
    if canvas_result.image_data is not None:
        
        img = Image.fromarray((255 - canvas_result.image_data[:, :, 0]).astype('uint8'))
        img = img.resize((28, 28))
        img = ImageOps.grayscale(img)
        img = np.array(img).reshape(1, 28, 28, 1) / 255.0

        # Make prediction
        pred = model.predict(img)
        st.subheader(f"Prediction: {np.argmax(pred)}")
    else:
        st.warning("Please draw a digit first!")
