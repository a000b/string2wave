"""
https://docs.python.org/3/library/wave.html
https://www.tutorialspoint.com/read-and-write-wav-files-using-python-wave
https://machowski2.wordpress.com/
https://docs.python.org/3/glossary.html#term-bytes-like-object

"""
import wave
import os


def rd_file(file_name):
    """Wczytuje plik, zwraca bajty"""
    with open(file_name, "r") as f:
        strout = f.read()
        bout = bytes(strout, "utf-16")
        return bout


def wr_file(file_name, data):
    """Zapisuje do pliku"""
    with open(file_name, "w") as f:
        f.write(data)


def create_wave(strumien, fwave_out):
    """Tworzy plik wave z zadanego tekstu"""
    sample_rate = 44100  # hertz
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
        fr = frames.decode("utf16")
        return fr

def wave2file(fname):
    """Odczytuje dane z pliku wave"""
    with wave.open(fname, 'r') as obj:
        frames = obj.readframes(obj.getnframes())
        return frames


def raw2wave(strumien, fwave_out):
    """Tworzy plik wave z zadanego tekstu"""
    sample_rate = 8000  # hertz
    with wave.open(fwave_out, 'w') as obj:
        obj.setnchannels(2)  # 1 - mono, 2 - stereo
        obj.setsampwidth(2) # ilość bajtów na sample
        obj.setframerate(sample_rate)
        obj.writeframesraw(strumien)

def wr_bfile(file_name, data):
    """Zapisuje do pliku"""
    with open(file_name, "wb") as f:
        f.write(data)
    return file_name

def rd_bfile(file_name):
    """Zapisuje do pliku"""
    with open(file_name, "rb") as f:
        data = f.read()
    return data

path = os.getcwd() + "/" #cieżka katalogu bieżącego
fin = "in.txt" #plik wejściowy z tekstem
fwave = "out.wav" #plik wyjściowy dźwiękowy
fout = "out.txt" #plik wyjściowy z tekstem

#Utowrzenie wava
create_wave(rd_file(fin), path + fwave)
#zapisanie odzyskanego textu do pliku
wr_file(path + fout, str(read_wave(path + fwave)))

#bonus wczytanie wava z muzyką do pliku binarnego
# fw = "plik.wav"
#raw2wave(rd_bfile(wr_bfile(path + fw + ".out", wave2file(path + fw))), "new.wav")
