import os
from moviepy.editor import VideoFileClip
from .whisper_utils import transcribe_audio
from .translation_utils import translate_text
from .subtitle_utils import save_subtitles, burn_subtitles_on_video
from .audio_utils import text_to_speech

def process_input_basic(input_path, input_type="video", target_lang="en"):
    temp_audio_path = "Temp/temp_extracted_audio.wav"
    final_audio_path = "Temp/final_translated_audio.mp3"
    srt_path = "Temp/output.srt"
    subtitle_video_path = "Temp/video_with_subtitles.mp4"

    if not os.path.exists("Temp"):
        os.makedirs("Temp")

    # Extract audio
    if input_type == "video":
        video = VideoFileClip(input_path)
        video.audio.write_audiofile(temp_audio_path, codec='pcm_s16le')
        video.reader.close()
        video.audio.reader.close_proc()
    elif input_type == "audio":
        temp_audio_path = input_path
    else:
        raise ValueError("Unsupported input type. Use 'video' or 'audio'.")

    # Process
    transcript = transcribe_audio(temp_audio_path)
    translated = translate_text(transcript, target_lang)
    save_subtitles(translated, srt_path)
    text_to_speech(translated, final_audio_path)

    if input_type == "video":
        burn_subtitles_on_video(input_path, srt_path, subtitle_video_path)

    # Cleanup
    if input_type == "video" and os.path.exists(temp_audio_path):
        os.remove(temp_audio_path)

    return {
        "transcript": transcript,
        "translated_text": translated,
        "translated_audio_path": final_audio_path,
        "subtitle_video_path": subtitle_video_path if input_type == "video" else None
    }
