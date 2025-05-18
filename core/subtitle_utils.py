import subprocess

def save_subtitles(translated_text, output_srt="Temp/output.srt"):
    with open(output_srt, "w") as f:
        f.write("1\n")
        f.write("00:00:00,000 --> 00:01:00,000\n")  
        f.write(translated_text.strip() + "\n")

# Burn subtitles on video
def burn_subtitles_on_video(video_path, srt_path, output_path):
    command = [
        "ffmpeg", "-y",
        "-i", video_path,
        "-vf", f"subtitles={srt_path}",
        "-c:a", "copy",
        output_path
    ]
    subprocess.run(command, check=True)