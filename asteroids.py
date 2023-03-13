import tensorflow as tf
import numpy as np
import cv2 as cv
from classes.object_detection import ObjectDetection

MODEL_FILENAME = 'model/model.pb'
LABELS_FILENAME = 'model/labels.txt'

WIDTH_IN = 512
HEIGHT_IN = 512

class TFObjectDetection(ObjectDetection):
    """Object Detection class for TensorFlow"""

    def __init__(self, graph_def, labels):
        super(TFObjectDetection, self).__init__(labels)
        self.graph = tf.compat.v1.Graph()
        with self.graph.as_default():
            input_data = tf.compat.v1.placeholder(tf.float32, [1, None, None, 3], name='Placeholder')
            tf.import_graph_def(graph_def, input_map={"Placeholder:0": input_data}, name="")

    def predict(self, preprocessed_image):
        inputs = np.array(preprocessed_image, dtype=np.float)[:, :, (2, 1, 0)]  # RGB -> BGR

        with tf.compat.v1.Session(graph=self.graph) as sess:
            output_tensor = sess.graph.get_tensor_by_name('model_outputs:0')
            outputs = sess.run(output_tensor, {'Placeholder:0': inputs[np.newaxis, ...]})
            return outputs[0]

def main(video_stream):
    # Load a TensorFlow model
    graph_def = tf.compat.v1.GraphDef()
    with tf.io.gfile.GFile(MODEL_FILENAME, 'rb') as f:
        graph_def.ParseFromString(f.read())

    # Load labels
    with open(LABELS_FILENAME, 'r') as f:
        labels = [label.strip() for label in f.readlines()]

    # Prepare ML model and video dataset
    tf_model = TFObjectDetection(graph_def, labels)
    cap = cv.VideoCapture(0)

    # Frame-by-frame operations
    while cap.isOpened():
        # Capture frame-by-frame
        ret, frame = cap.read()

        # If frame is read correctly, ret is True
        if not ret:
            print("Can't receive video frame. Exiting ...")
            break
        
        # Resize frame and convert to RGB
        inp = cv.resize(frame, (WIDTH_IN, HEIGHT_IN))        
        rgb = cv.cvtColor(inp, cv.COLOR_BGR2RGB)

        # Predict object on the frames
        predictions = tf_model.predict_image(rgb)
        for prediction in predictions:
            # Check if probability is higher than 25%
            if prediction["probability"] > 0.25 :
                # Get the probability of detected asteroids                
                probability = f'{100 * round(prediction["probability"])}%'

                # Draw a rectangle around the detected object
                point1 = (
                    int(prediction["boundingBox"]["left"] * WIDTH_IN),
                    int(prediction["boundingBox"]["top"] * HEIGHT_IN)
                )
                point2 = (
                    int(prediction["boundingBox"]["left"] * WIDTH_IN) + int(prediction["boundingBox"]["width"] * WIDTH_IN),
                    int(prediction["boundingBox"]["top"] * HEIGHT_IN) + int(prediction["boundingBox"]["height"] * HEIGHT_IN)
                )
                colour_red = (0, 0, 255)
                frame_boxed = cv.rectangle(
                    rgb, point1, point2,
                    colour_red
                )

                # Show label associated with detected object
                font = cv.FONT_HERSHEY_PLAIN
                point3 = (
                    int(prediction["boundingBox"]["left"] * WIDTH_IN),
                    int(prediction["boundingBox"]["top"] * HEIGHT_IN) - 5
                )
                cv.putText(
                    frame_boxed,
                    str(prediction["tagName"]), # + " " + probability,
                    point3, font, 0.7, colour_red
                )
    
        # Display and export the resulting frame
        cv.imshow('frame', rgb)
        if cv.waitKey(1) == ord('q'):
            break

    # When everything is done, release the capture
    cap.release()
    cv.destroyAllWindows()

if __name__ == '__main__':
    main("XX")