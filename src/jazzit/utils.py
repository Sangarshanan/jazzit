def track_length(track_path):
    from mutagen.mp3 import MP3

    audio = MP3(track_path)
    return audio.info.length
