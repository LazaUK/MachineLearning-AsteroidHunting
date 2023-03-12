import tensorflow as tf
import numpy as np
import cv2 as cv
from classes.object_detection import ObjectDetection
from classes.box import Box

MODEL_FILENAME = 'model/model.pb'
LABELS_FILENAME = 'model/labels.txt'

WIDTH = 512
HEIGHT = 512

# Define the codec and create VideoWriter object
# fourcc = cv.VideoWriter_fourcc(*'DIVX')
# output = cv.VideoWriter('Asteroid_Results.avi',fourcc, 20.0, (640,480))

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

def main(video_file):
    # Load a TensorFlow model
    graph_def = tf.compat.v1.GraphDef()
    with tf.io.gfile.GFile(MODEL_FILENAME, 'rb') as f:
        graph_def.ParseFromString(f.read())

    # Load labels
    with open(LABELS_FILENAME, 'r') as f:
        labels = [label.strip() for label in f.readlines()]

    # Prepare ML model and video dataset
    colors = np.random.uniform(0, 255, size=(len(labels), 3))
    tf_model = TFObjectDetection(graph_def, labels)
    cap = cv.VideoCapture(video_file)

    # Frame-by-frame operations
    while cap.isOpened():
        # Capture frame-by-frame
        ret, frame = cap.read()

        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive video frame. Exiting ...")
            break
        
        # Resize to respect the input_shape
        inp = cv.resize(frame, (WIDTH , HEIGHT))

        # Convert farme image to RGB
        rgb = cv.cvtColor(inp, cv.COLOR_BGR2RGB)

        # Predict object on the frames
        predictions = tf_model.predict_image(rgb)
        for prediction in predictions:
            # Check if probability is higher than 50%
            if prediction["probability"] > 0.5 :
                # Get the probability of detected asteroids
                color = colors[prediction["tagId"]]                
                probability = f'{100 * round(prediction["probability"])}%'
                thickness = 1

                # Draw a rectangle around the detected object
                box = Box(prediction, rgb)
                frame_boxed = cv.rectangle(rgb, box.get_start_point(), box.get_end_point(), color, thickness)

                # Show the label associated with the object
                cv.putText(frame_boxed, str(prediction["tagName"]) + " | Probability:" + probability,
                            (int(prediction["boundingBox"]["left"] * WIDTH),
                            int(prediction["boundingBox"]["top"] * HEIGHT) - 5),
                            cv.FONT_HERSHEY_PLAIN, 1.5, (255, 255, 255), 2)
    
        # Display and export the resulting frame
        cv.imshow('frame', rgb)
        # output.write(rgb)
        if cv.waitKey(1) == ord('q'):
            break

    # When everything is done, release the capture
    cap.release()
    cv.destroyAllWindows()

if __name__ == '__main__':
    main("./ESO_asteroid.mp4")
