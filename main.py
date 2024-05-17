import cv2
import numpy as np
import mediapipe as mp 


camera = cv2.VideoCapture(0)
mp_solution = mp.solutions.selfie_segmentation
selfie_segmentation = mp_solution.SelfieSegmentation()
office_background = cv2.imread('office.jpg')

while True:
    _, frame = camera.read()

    input_img = frame
    result = selfie_segmentation.process(frame)    
    mask = result.segmentation_mask
    mask = (mask * 255).astype(np.uint8)
    mask_bgr = cv2.cvtColor(mask, cv2.COLOR_GRAY2RGB)
    inverted_mask = cv2.bitwise_not(mask_bgr)

    office_background = cv2.resize(office_background, (frame.shape[1], frame.shape[0]))
    background_img = cv2.bitwise_and(office_background, inverted_mask)
    background_blurred_img = cv2.blur(background_img, (80, 80), 0)

    cropped_img = cv2.bitwise_and(input_img, mask_bgr)

    combined_img = cv2.add(background_blurred_img, cropped_img)

    cv2.imshow('Filter: ', combined_img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
