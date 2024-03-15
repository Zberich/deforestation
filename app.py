import streamlit as st
import random 
from PIL import Image 

def classify_image  (image) -> bool :
    """ classify if an image has palm trees or not
    
    param : 
    - image(bytes) : image to be classify
    
    Return : 
    - bool : True if image contain palm trees
    
    """
        
    return random.choice(["True","False"])


def analyze_image(image) :

        """
        Analyse parts of image that most contribute to the classification
        Param : 
        - image (butes) : image to analyse
        Returns :
        -bytes : image showing most contributive part of the image

        """
        return Image.open(image).convert("L")





st.write("## Palm Tree Detector")

with st.sidebar :
    image_file = st.file_uploader(" Choose an image",
                              type = ["png", "jpg"],
                              help = "Select image to be classified"
                             )
    

if image_file is not None : 
    bytes_image = image_file.getvalue()
    st.image(byte_image)

    if st.button ("Detect palm trees", disabled = (image_file is None)) : 
            result = classify_image(bytes_images)
            if result :
                 st.write("Palm trees detected")
            else :
                 st.write("Palm trees not detected")
                    
            with st.expander ("Sensitivity Analysis ", expanded = False ) : 
                analysis_image = analyze_image(image_file)
                st.image(analysis_image, width=256)
