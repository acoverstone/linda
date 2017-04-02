# Entry point to the program
# Run with 'python linda.py'

import snowboydecoder
import sys
import signal
import main
import speech

interrupted = False


def signal_handler(signal, frame):
    global interrupted
    interrupted = True


def interrupt_callback():
    global interrupted
    return interrupted

# uncomment for different models, for Linda we hardcode the pmdl
# if len(sys.argv) == 1:
#     print("Error: need to specify model name")
#     print("Usage: python demo.py your.model")
#     sys.exit(-1)
# model = sys.argv[1]
model = "resources/linda.pmdl"

# capture SIGINT signal, e.g., Ctrl+C
signal.signal(signal.SIGINT, signal_handler)


while True:
    detector = snowboydecoder.HotwordDetector(model, sensitivity=0.5)
    print('Listening... Press Ctrl+C to exit')
    # main loop, change callback to change functionality
    detector.start(detected_callback= main.controlLoop,#snowboydecoder.play_audio_file,
               interrupt_check=interrupt_callback,
               sleep_time=0.03)


