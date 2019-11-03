"""
https://docs.python.org/3/library/wave.html
https://www.tutorialspoint.com/read-and-write-wav-files-using-python-wave

"""
import wave
import os

def rd_file(file_name):
    """Wczytuje plik, zwraca bajty"""
    with open(file_name, "r") as f:
        data = f.readlines()
        stext = ""
        for line in data:
            stext += str(line)
        strout = str(stext).replace(chr(10) + chr(32), chr(10))
        if strout[0] == chr(32):
            strout = strout[1:]
        bout = bytes(strout, "utf-16")
        return bout


def wr_file(file_name, data):
    """Zapisuje do pliku"""
    with open(file_name, "w") as f:
        f.write(data)


def create_wave(strumien, fwave_out):
    """Tworzy plik wave z zadanego tekstu"""
    sample_rate = 8000  # hertz
    with wave.open(fwave_out, 'w') as obj:
        obj.setnchannels(2)  # 1 - mono, 2 - stereo
        obj.setsampwidth(2) # ilość bajtów na sample
        obj.setframerate(sample_rate)
        #Pętla w przypadku krótkiego tekstu
        for counter in range(1000):
            for i in range(0, len(strumien), 2):
                tbytes = strumien[i:i +2]
                obj.writeframesraw(tbytes)


def read_wave(fname):
    """Odczytuje dane z pliku wave, zwraca zdekodowany tekst"""
    with wave.open(fname, 'r') as obj:
        print("Nazwa pliku: ", fname)
        print("Number of channels", obj.getnchannels())
        print("Sample width", obj.getsampwidth())
        print("Frame rate.", obj.getframerate())
        print("Number of frames", obj.getnframes())
        print("parameters:", obj.getparams())
        frames = obj.readframes(obj.getnframes())
        fr = frames.decode('utf16')
        return fr

path = os.getcwd() + "/" #cieżka katalogu bieżącego
fin = "in.txt" #plik wejściowy z tekstem
fwave = "out.wav" #plik wyjściowy dźwiękowy
fout = "out.txt" #plik wyjściowy z tekstem

#Utowrzenie wava
create_wave(rd_file(fin), path + fwave)
#zapisanie odzyskanego textu do pliku
wr_file(path + fout, str(read_wave(path + fwave)))

