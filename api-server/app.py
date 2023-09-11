from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse
import uvicorn

from PIL import Image
import numpy as np
from io import BytesIO
import cv2

from keras.models import load_model
from helper_functions import highlight_classes
import warnings

app = FastAPI()
warnings.filterwarnings('ignore')

model = load_model('cardiac_mri_segmenter.h5')

@app.post("/annotate")
async def annotate(file: UploadFile = File(...)):
    img_bytes = await file.read()
    pil_img = Image.open(BytesIO(img_bytes))
    img = np.array(pil_img)

    # Resize Image
    resized_img = cv2.resize(img, (256, 256))
    # Convert to grayscale
    gray_img = cv2.cvtColor(resized_img, cv2.COLOR_RGB2GRAY)
    # Normalize
    normalized_img = gray_img / 255
    # Match Input Shape
    input = np.expand_dims(normalized_img, axis=0)

    # Get Segmentation Mask
    output = model.predict(input)
    mask = np.argmax(output[0], axis=2)

    # Return Annotation
    anot_array = highlight_classes(gray_img, mask)
    annotation = Image.fromarray(anot_array.astype(np.uint8))

    # Save the processed image to a BytesIO object
    image_bytes = BytesIO()
    annotation.save(image_bytes, format="JPEG")
    
    # Return image bytes as a response
    return StreamingResponse(BytesIO(image_bytes.getvalue()), media_type="image/jpeg")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
