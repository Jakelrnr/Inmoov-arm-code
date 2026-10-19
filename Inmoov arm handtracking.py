import cv2
import serial
import time
import mediapipe as mp
import math

# comunicates with the arduino on port 6 , you can change this
arduino = serial.Serial(port='COM6', baudrate=9600, timeout=0.1)
time.sleep(2)  # Give time for Arduino to initialize


mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

#send the finger position angle
def send_finger_command(finger_angles):
    command = f'{finger_angles[0]},{finger_angles[1]},{finger_angles[2]},{finger_angles[3]},{finger_angles[4]}\n'
    arduino.write(command.encode())
    time.sleep(0.05)

# Function to calculate angle between three points
def calculate_angle(a, b, c):
    ang = math.degrees(math.atan2(c[1]-b[1], c[0]-b[0]) - math.atan2(a[1]-b[1], a[0]-b[0]))
    return abs(ang)

# to see if a fist is being made
def is_fist(hand_landmarks):
    thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
    index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    middle_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
    ring_tip = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]
    pinky_tip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]
    
    
    return (index_tip.y > hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP].y and
            middle_tip.y > hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].y and
            ring_tip.y > hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_MCP].y and
            pinky_tip.y > hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP].y)

# capturde the webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, image = cap.read()
    if not success:
        break

    # Flip video
    image = cv2.flip(image, 1)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image_rgb)

    finger_angles = [90, 90, 90, 90, 90]  # Default Servo position

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            height, width, _ = image.shape

            #check for a fist
            if is_fist(hand_landmarks):
                finger_angles = [0, 0, 0, 0, 0]  # Close all fingers for a fist
            else:
                # landmarks for each finger's base and tip
                thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
                thumb_ip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP]
                thumb_mcp = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP]

                index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                index_pip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP]
                index_mcp = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP]

                middle_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
                middle_pip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP]
                middle_mcp = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP]

                ring_tip = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]
                ring_pip = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP]
                ring_mcp = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_MCP]

                pinky_tip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]
                pinky_pip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP]
                pinky_mcp = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP]

                # Calculate angles for each finger
                finger_angles[0] = calculate_angle((thumb_mcp.x, thumb_mcp.y), (thumb_ip.x, thumb_ip.y), (thumb_tip.x, thumb_tip.y))
                finger_angles[1] = calculate_angle((index_mcp.x, index_mcp.y), (index_pip.x, index_pip.y), (index_tip.x, index_tip.y))
                finger_angles[2] = calculate_angle((middle_mcp.x, middle_mcp.y), (middle_pip.x, middle_pip.y), (middle_tip.x, middle_tip.y))
                finger_angles[3] = calculate_angle((ring_mcp.x, ring_mcp.y), (ring_pip.x, ring_pip.y), (ring_tip.x, ring_tip.y))
                finger_angles[4] = calculate_angle((pinky_mcp.x, pinky_mcp.y), (pinky_pip.x, pinky_pip.y), (pinky_tip.x, pinky_tip.y))

            # Map angles to servo positions (0-180 degrees)
            mapped_angles = [int(angle / 180 * 90) for angle in finger_angles]
            send_finger_command(mapped_angles)  # Send to Arduino

            # Draw finger and hand landmarks on image
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Display Camera 
    cv2.imshow("Hand Tracking", image)
    if cv2.waitKey(5) & 0xFF == 27:  # Press 'Esc' to exit
        break


cap.release()
cv2.destroyAllWindows()
arduino.close()
