import os
import subprocess
from pathlib import Path

def extract_frames(input_file: str, fps: int):
    input_path = Path(input_file)
    output_dir = input_path.stem  # nazwa bez .mp4
    os.makedirs(output_dir, exist_ok=True)

    output_pattern = str(Path(output_dir) / "frame_%04d.jpg")

    command = [
        "ffmpeg",
        "-i", input_file,
        "-vf", f"fps={fps}",
        "-qscale:v", "5",  # kontrola jakości JPEG (1=lepsza, 31=gorsza)
        output_pattern
    ]

    subprocess.run(command, check=True)
    print(f"Klatki zapisane w folderze: {output_dir}")

# Przykład użycia
videos = [f for f in os.listdir('./nowe') if f.endswith('.mp4')]
print(videos)
for video in videos:
    input_file = os.path.join('./nowe', video)
    extract_frames(input_file, fps=2)  # Zmienna fps może być dostosowana