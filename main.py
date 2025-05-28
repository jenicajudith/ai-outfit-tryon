import cv2
import mediapipe as mp
import numpy as np

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1)
mp_draw = mp.solutions.drawing_utils

# List of glasses images
glasses_files = ["glasses1.png", "glasses2.png", "glasses3.png"]
current_glasses = 0
glasses = cv2.imread(glasses_files[current_glasses], cv2.IMREAD_UNCHANGED)

def overlay_transparent(background, overlay, x, y, overlay_size=None):
    if overlay_size:
        overlay = cv2.resize(overlay, overlay_size)

    b, g, r, a = cv2.split(overlay)
    overlay_color = cv2.merge((b, g, r))
    mask = cv2.merge((a, a, a))

    h, w, _ = overlay.shape
    if y + h > background.shape[0] or x + w > background.shape[1] or x < 0 or y < 0:
        return background # Prevent overlaying outside frame

    roi = background[y:y+h, x:x+w]
    img1_bg = cv2.bitwise_and(roi, cv2.bitwise_not(mask))
    img2_fg = cv2.bitwise_and(overlay_color, mask)
    dst = cv2.add(img1_bg, img2_fg)
    background[y:y+h, x:x+w] = dst
    return background

cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = face_mesh.process(rgb_frame)

    if result.multi_face_landmarks:
        for face_landmarks in result.multi_face_landmarks:
            left_eye = face_landmarks.landmark[33]
            right_eye = face_landmarks.landmark[263]

            # Convert to pixel coordinates
            x1, y1 = int(left_eye.x * w), int(left_eye.y * h)
            x2, y2 = int(right_eye.x * w), int(right_eye.y * h)

            # Midpoint between eyes
            cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

            # Calculate distance between eyes
            eye_width = int(2.5 * abs(x2 - x1))
            glasses_height = int(eye_width * glasses.shape[0] / glasses.shape[1])

            # Top-left corner for placement
            x = cx - eye_width // 2
            y = cy - glasses_height // 2

            try:
                frame = overlay_transparent(frame, glasses, x, y, (eye_width, glasses_height))
            except:
                pass

    cv2.imshow("Virtual Try-On", frame)

    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        break
    elif key & 0xFF == ord('1'):
        current_glasses = 0
        glasses = cv2.imread(glasses_files[current_glasses], cv2.IMREAD_UNCHANGED)
    elif key & 0xFF == ord('2'):
        current_glasses = 1
        glasses = cv2.imread(glasses_files[current_glasses], cv2.IMREAD_UNCHANGED)
    elif key & 0xFF == ord('3'):
        current_glasses = 2
        glasses = cv2.imread(glasses_files[current_glasses], cv2.IMREAD_UNCHANGED)

cap.release()
cv2.destroyAllWindows()