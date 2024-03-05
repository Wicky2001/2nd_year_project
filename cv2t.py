import cv2

# Open the default camera (Camera index 0)
cap = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

while True:
    # Read a frame from the camera
    license_plate_text = "ABC123"
    ret, frame = cap.read()
    cv2.putText(frame, "Waiting for Gate to Close", (120, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1,
                cv2.LINE_AA)
    cv2.putText(frame, f"License Plate: {license_plate_text}", (150, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 1,
                cv2.LINE_AA)
    # Check if the frame was successfully captured
    if not ret:
        print("Error: Failed to capture frame.")
        break

    # Display the frame
    cv2.imshow('Webcam Video', frame)

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the window
cap.release()
cv2.destroyAllWindows()
# import torch
#
# # Check if CUDA is available
# cuda_available = torch.cuda.is_available()
#
# if cuda_available:
#     # Print information about the available GPUs
#     print(f"CUDA is available. Number of GPUs: {torch.cuda.device_count()}")
#     for i in range(torch.cuda.device_count()):
#         print(f"GPU {i}: {torch.cuda.get_device_name(i)}")
# else:
#     print("CUDA is not available. You may not have a compatible GPU or CUDA is not properly installed.")
# import cv2
#
# print("OpenCV version:", cv2.__version__)
