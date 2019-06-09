import wave
import pyaudio

def play(file_path):
	CHUNK = 1024
	sound_file = file_path
	f = wave.open(sound_file, 'rb')
	data = f.readframes(CHUNK)

	p = pyaudio.PyAudio()

	FORMAT = p.get_format_from_width(f.getsampwidth())
	CHANNELS = f.getnchannels()
	RATE = f.getframerate()

	stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, frames_per_buffer=CHUNK, output=True)

	while len(data) > 0:
		stream.write(data)
		data = f.readframes(CHUNK)
	

if __name__ == '__main__':
	play(file_path)