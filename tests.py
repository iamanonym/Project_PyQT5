import simpleaudio

a = simpleaudio.WaveObject.from_wave_file('Letters\А.wav')
b = a.play()
b.wait_done()