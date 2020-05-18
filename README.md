# kittvoicebox-pocketsphinx

kitts voicebox controller for offline use. Speach to txt uses the pocketsphinx library so no internet needed for the translation

You will have to install pocketsphinx on the pi

sudo apt-get update --yes
sudo apt-get install portaudio19-dev swig --yes
sudo apt-get install -y python python-dev python-pip build-essential swig git libpulse-dev --yes
sudo apt-get install libpulse-dev --yes
sudo apt-get install sox --yes
sudo apt-get install pocketsphinx --yes

sudo pip3 install pocketsphinx
sudo pip3 install pydub

once done clone to /home/pi/kitt
python3 kitt.py to run

You will need the html5 voice recorder to upload the instructions .wav file. I installed mine in /var/www/html.
Apache and modssl has to be installed. html5 voice recorder has to work on https://

I use sox to convert the .wav file toa 16000 sample rate.
To test the file you can use pocketsphinx_continuous -infile transcribe_export.wav
manual conver sox transcribe.wav -r 16000 transcribe_new.wav

keyword.list is the keywords you want to search for in the instructional wav file, edit that file to pick out keywords, then open input.txt and match that keyword to an mp3.

So for example if I speak "Kitt where is bonnie" into the html5 recorder. It finds bonnie in keyword.list then matches that in input.txt then plays the bonnie.mp3 file.
