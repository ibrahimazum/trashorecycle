# TrashORecycle

# Background info
prototype of an app that can use machine learning to classify waste as trash or recycle

This prototype was created as part of Assignment task in my studies (Masters of Data Science)

The problem this app try to solve is classifying waste items using images to identify whether image contains recyclable item(s) or trash item(s)

# Tech stack
The machine learning model used for the app was developed and run using python on Google Colab(https://colab.research.google.com/).
The trained model was download and uploaded in this repository(model2.rar)

python appliaton (app.py) can be run on streamlit(https://streamlit.io/) with npx localtunnel(https://github.com/localtunnel/localtunnel) to test the prototype.


# App Features

You can open the App on any device that has access to a web browser. 

The application is optimised to work with mobile phones and tablet computers as well. 

It can use the in built camera to take the photos and upload instantaniously.<br />

The app can run on multiple modes:<br />

1.Single Item Mode: default mode<br />

  This mode can be used to classfiy the items if the iamge contains single item. This is useful for individuals to take a photo of an item  check if the item is trash or   recyclable.<br />
  
2.Multimode: (different number of cropping factor also can be selected(3,5,7 or 9)<br />

  This mode can detect multiple items from an image and classfiy it as trash or reclylable.  
  
  This mode can be adapted in recyle industry centers where large scale waste sorting is practiced.
  
  For example on waste sorting belt , the algorithm can be used to capture image of the items on belt.
  
  It can then quickly scan and notify if the item contains trash or recyclables. 
  
  Depending on this further actions such as belt speed or robotic usage of removing the trash etc can be done.
  
# App Output
  Once you upload the image, you can select the mode and upload the image.
  
  The result will show the classified image with red or green borders representing trash or recyclable respectively.
