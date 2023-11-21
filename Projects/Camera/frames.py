
# pip install scrcpy-client

import scrcpy
import numpy as np
import cv2

# Create a scrcpy client
client = scrcpy.Client()
# print(help(client))

# Start the frame loop
for frame in client.iterate_frames():

    # Convert the frame to a NumPy array
    frame_array = np.frombuffer(frame, dtype=np.uint8)

    # Convert the frame to a BGR image
    frame_image = cv2.imdecode(frame_array, cv2.IMREAD_COLOR)

    # Display the frame
    cv2.imshow("scrcpy", frame_image)

    # Wait for a key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Close the client
client.close()
