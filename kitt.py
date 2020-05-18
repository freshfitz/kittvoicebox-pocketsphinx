#!/usr/bin/env python
import re
import os, sys, subprocess
from os import path
import time
import RPi.GPIO as GPIO
from pocketsphinx import *
from sphinxbase import *
from pydub import AudioSegment as am

modeldir = "/usr/local/share/pocketsphinx/model/"
datadir = "/home/pi/kitt/"
filename = "transcribe.wav"
new_filename = "transcribe_export.wav"

config = Decoder.default_config()
config.set_string('-hmm', os.path.join(modeldir, 'en-us/en-us'))
config.set_string('-dict', os.path.join(modeldir, 'en-us/cmudict-en-us.dict'))
config.set_string('-kws', os.path.join(datadir, 'keyword.list'))
#config.set_string('-keyphrase', 'morning')
#config.set_float('-kws_threshold', 1e-30)

def start():

 print ("Starting")
 #time_to_wait = 9999
 time_counter = 0
 while not os.path.exists(filename):
    time.sleep(1)
    time_counter += 1
    #if time_counter > time_to_wait:break

 # Convert transcibe.wav to text
 subprocess.run(["sox", filename, "-r 16000", new_filename])

 stream = open(os.path.join(datadir, new_filename), "rb")

 decoder = Decoder(config)
 decoder.start_utt()
 while True:
    buf = stream.read(1024)
    if buf:
        decoder.process_raw(buf, False, False)
    else:
        omxprocess = subprocess.Popen(['omxplayer', '--no-keys', '-olocal', 'understand.mp3'],  stdin=subprocess.PIPE, stdout=None, stderr=None, bufsize=0)
        os.remove(filename)
        start()
        break
    if decoder.hyp() is not None:
        #print([(seg.word, seg.prob, seg.start_frame, seg.end_frame) for seg in decoder.seg()])
        #print([(seg.word) for seg in decoder.seg()])
        keyword = ([(seg.word) for seg in decoder.seg()])
        decoder.end_utt()
        # PERFORM COOL TASK   
        
        #Match keyword to flat file input.txt and get audio MP3
        keyword = ([(seg.word) for seg in decoder.seg()])

        found = (keyword)
        name = re.sub('\W+','', str(found))
        print (name)
  
        with open('input.txt') as fd:
         print (name)
      
         #Do stuff based on the audio match
         for line in fd:
          match = re.search(rf'.*{name}.* : (\S+)', line)
          print (match)
    
          if (name == "cereal"):
            omxprocess = subprocess.Popen(['omxplayer', '--no-keys', '-olocal', 'fx-scanner.mp3'],  stdin=subprocess.PIPE, stdout=None, stderr=None, bufsize=0)
            os.remove(filename)
            time.sleep(1)
            print ("GOing to chaser")
            chaser()
          
          elif (name == "skinny"):
            omxprocess = subprocess.Popen(['omxplayer', '--no-keys', '-olocal', 'fx-scanner.mp3'],  stdin=subprocess.PIPE, stdout=None, stderr=None, bufsize=0)
            os.remove(filename)
            time.sleep(1)
            print ("GOing to chaser")
            chaser()

          elif (name == "scan"):
            omxprocess = subprocess.Popen(['omxplayer', '--no-keys', '-olocal', 'fx-scanner.mp3'],  stdin=subprocess.PIPE, stdout=None, stderr=None, bufsize=0)
            os.remove(filename)
            time.sleep(1)
            print ("GOing to chaser")
            chaser()


          elif match:
            music = match.group(1)
            print('{}'.format(music))
            omxprocess = subprocess.Popen(['omxplayer', '--no-keys', '-olocal', music],  stdin=subprocess.PIPE, stdout=None, stderr=None, bufsize=0)
            os.remove(filename)
            start()       
      
def chaser():
 # Use BCM GPIO references
 # instead of physical pin numbers
 GPIO.setmode(GPIO.BCM)
  
 # Define GPIO signals to use
 # that are connected to 10 LEDs
 # Pins 7,11,15,21,23,16,18,22,24,26
 # GPIO4,GPIO17,GPIO22,GPIO9,GPIO11
 # GPIO23,GPIO24,GPIO25,GPIO8,GPIO7
 RpiGPIO = [4,17,22,9,11,23,24,25,8,7]
  
 # Set all pins as output
 for pinref in RpiGPIO:
 # print("Setup pins")
  GPIO.setup(pinref,GPIO.OUT)
  
 # Define some settings
 StepCounter = 0
 StepDir = 1
 WaitTime = 0.2
  
 # Define some sequences
  
 # One LED
 StepCount1 = 10
 Seq1 = []
 Seq1 = list(range(0,StepCount1))
 Seq1[0] =[1,0,0,0,0,0,0,0,0,0]
 Seq1[1] =[0,1,0,0,0,0,0,0,0,0]
 Seq1[2] =[0,0,1,0,0,0,0,0,0,0]
 Seq1[3] =[0,0,0,1,0,0,0,0,0,0]
 Seq1[4] =[0,0,0,0,1,0,0,0,0,0]
 Seq1[5] =[0,0,0,0,0,1,0,0,0,0]
 Seq1[6] =[0,0,0,0,0,0,1,0,0,0]
 Seq1[7] =[0,0,0,0,0,0,0,1,0,0]
 Seq1[8] =[0,0,0,0,0,0,0,0,1,0]
 Seq1[9] =[0,0,0,0,0,0,0,0,0,1]
  
 # Double LEDs
 StepCount2 = 11
 Seq2 = []
 Seq2 = list(range(0,StepCount2))
 Seq2[0] =[1,0,0,0,0,0,0,0,0,0]
 Seq2[1] =[1,1,0,0,0,0,0,0,0,0]
 Seq2[2] =[0,1,1,0,0,0,0,0,0,0]
 Seq2[3] =[0,0,1,1,0,0,0,0,0,0]
 Seq2[4] =[0,0,0,1,1,0,0,0,0,0]
 Seq2[5] =[0,0,0,0,1,1,0,0,0,0]
 Seq2[6] =[0,0,0,0,0,1,1,0,0,0]
 Seq2[7] =[0,0,0,0,0,0,1,1,0,0]
 Seq2[8] =[0,0,0,0,0,0,0,1,1,0]
 Seq2[9] =[0,0,0,0,0,0,0,0,1,1]
 Seq2[10]=[0,0,0,0,0,0,0,0,0,1]
  
 # Two LEDs from opposite ends
 StepCount3 = 9
 Seq3 = []
 Seq3 = list(range(0,StepCount3))
 Seq3[0] =[1,0,0,0,0,0,0,0,0,1]
 Seq3[1] =[0,1,0,0,0,0,0,0,1,0]
 Seq3[2] =[0,0,1,0,0,0,0,1,0,0]
 Seq3[3] =[0,0,0,1,0,0,1,0,0,0]
 Seq3[4] =[0,0,0,0,1,1,0,0,0,0]
 Seq3[5] =[0,0,0,1,0,0,1,0,0,0]
 Seq3[6] =[0,0,1,0,0,0,0,1,0,0]
 Seq3[7] =[0,1,0,0,0,0,0,0,1,0]
 Seq3[8] =[1,0,0,0,0,0,0,0,0,1]
 count = 1
 
  
 # Choose a sequence to use
 Seq = Seq3
 StepCount = StepCount3
 i=0
 
 # Start main loop
 while True:
 # print("-- Step : "+ str(StepCounter) +" --")
  for pinref in range(0, 10):
    xpin=RpiGPIO[pinref]#
    # Check if LED should be on or off
    if Seq[StepCounter][pinref]!=0:
    #  print(" Enable " + str(xpin))
      GPIO.output(xpin, True)
      i += 1
    else:
    #  print(" Disable " + str(xpin))
      GPIO.output(xpin, False)
  
  StepCounter += StepDir
  
  # If we reach the end of the sequence reverse
  # the direction and step the other way
  if (StepCounter==StepCount) or (StepCounter<0):
    
    StepDir = StepDir * -1
    StepCounter = StepCounter + StepDir + StepDir
    print(i)
  
  if (i > 51):
         print ("i = 8")
         GPIO.cleanup() 
         start()

    
  # Wait before moving on
  time.sleep(0.2)
  
start()
