import speech_recognition as sr

import win32api


def recognize_speech_from_mic(recognizer, microphone):
    """Transcribe speech from recorded from `microphone`.

    Returns a dictionary with three keys:
    "success": a boolean indicating whether or not the API request was
               successful
    "error":   `None` if no error occured, otherwise a string containing
               an error message if the API could not be reached or
               speech was unrecognizable
    "transcription": `None` if speech could not be transcribed,
               otherwise a string containing the transcribed text
    """
    # check that recognizer and microphone arguments are appropriate type
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    # adjust the recognizer sensitivity to ambient noise and record audio
    # from the microphone
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    # set up the response object
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    # try recognizing the speech in the recording
    # if a RequestError or UnknownValueError exception is caught,
    #     update the response object accordingly
    try:
        response["transcription"] = recognizer.recognize_sphinx(audio)
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        # speech was unintelligible
        response["error"] = "Unable to recognize speech"

    return response


def recognizeSpeech(application):
    r = sr.Recognizer()
    mic = sr.Microphone()
    result = recognize_speech_from_mic(r, mic)
    choice = FuzzySearch(result['transcription'])
    if choice:
        if choice == 'music':
            PlayMusic()
            application.ui.gif.stop()
        if choice == 'file':
            OpenFile()
            application.ui.gif.stop()
    else:
        pass


# 模糊搜索
def FuzzySearch(r):
    a = r.split(' ')
    b = ['machine', 'music', 'magic', 'magazine', 'major', 'mommy', 'market', 'supermarket', 'marriage', 'match',
         'maybe']
    c = ['file', 'fire']
    d = list(set(a).intersection(set(b)))
    e = list(set(a).intersection(set(c)))
    print(a, b, c, d, e)
    if len(d):
        return 'music'
    if len(e):
        return 'file'
    else:
        return False


def PlayMusic():
    # 播放音乐
    # ShellExecute 查找与指定文件关联在一起的程序的文件名
    # 第一个参数默认为0,打开，路径名，默认空，默认空，是否显示程序1or0
    win32api.ShellExecute(0, 'open', r'goodnight.mp3', '', '', 1)


def OpenFile():
    # 打开文件
    win32api.ShellExecute(0, 'open', r'file.txt', '', '', 1)

