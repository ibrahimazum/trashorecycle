import streamlit as st
import tensorflow as tf
import streamlit as st


@st.cache(allow_output_mutation=True)
def load_model():
  model=tf.keras.models.load_model('/content/model2.hdf5') 
  return model
with st.spinner('Model is being loaded..'):
  model=load_model()

st.write("""
         Deakin University
         T2-2022 SIT744-Assignment2 Task
         Ibrahim Azum
         """
         )  

st.write("""
         ## App Prototype: Recyle or Trash
         """
         )
#select the tiles
mode_option = st.selectbox(
    'Select Mode',
    ('Single Item','Mulitple Item 3 x 3','Mulitple Item 5 x 5','Mulitple Item 7 x 7', 'Mulitple Item 9 x 9'))


file = st.file_uploader("Please upload an image (jpg) you want to classify", type=["jpg", "png","jpeg"])
import cv2
from PIL import Image, ImageOps
from google.colab.patches import cv2_imshow
import numpy as np




st.set_option('deprecation.showfileUploaderEncoding', False)



def import_and_predict(image_data, model):
    
        size = (150,150)    
        image = ImageOps.fit(image_data, size, Image.ANTIALIAS)
        image = np.asarray(image)
       
        
        img_reshape = image[np.newaxis,...]
    
        prediction = model.predict(img_reshape)

        return prediction



        


if file is None:
    st.text("Please upload an image file")
else:
    image = Image.open(file)
    width, height = image.size

    slice_numbers=1
    mode_x=mode_option

    if(mode_option=='Single Item'):
      slice_numbers=1
    if(mode_option=='Mulitple Item 3 x 3'):
      slice_numbers=3
    if(mode_option=='Mulitple Item 5 x 5'):
      slice_numbers=5
    if(mode_option=='Mulitple Item 7 x 7'):
      slice_numbers=7
    if(mode_option=='Mulitple Item 9 x 9'):
      slice_numbers=9


    

    x=int(width/slice_numbers)
    y=int(height/slice_numbers)

    rt=x
    bt=y
    lt=0
    tp=0

    for i in range(slice_numbers):
      cols = st.columns(slice_numbers)

      for j in range(slice_numbers):

        left = lt
        
        top = tp
        
        right = rt
        
        bottom = bt

        im1 = image.crop((left, top, right, bottom))
        # making border around image using copyMakeBorder
        borderoutput = cv2.copyMakeBorder(np.asarray(im1), 5, 5, 5, 5, cv2.BORDER_CONSTANT, value=[0, 255, 0])
        
        prediction=import_and_predict(im1, model)

        score = int(np.round(prediction))

        klass="Recyle Material"
        if score is 1:
          klass="Trash"
          borderoutput = cv2.copyMakeBorder(np.asarray(im1), 5, 5, 5, 5, cv2.BORDER_CONSTANT, value=[255, 0, 0])
          
        #st.text(score)
        #st.text(klass)

        #cols[j].image(borderoutput, caption=klass)
        cols[j].image(borderoutput)
        
        lt=lt+x
        rt=rt+x
        

      
      bt=bt+y
      tp=tp+y

      lt=0
      rt=x

recycle_txt = '<span> recyle </span> <span style="font-family:sans-serif; color:#00ff00; font-size: 24px;">---    </span> <span> trash</span> <span style="font-family:sans-serif; color:#ff0000; font-size: 24px;">---</span> '
trash_txt = '<p> </p>'
st.markdown(trash_txt, unsafe_allow_html=True)
st.markdown(recycle_txt, unsafe_allow_html=True)
#st.markdown(trash_txt, unsafe_allow_html=True)



