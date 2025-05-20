#  VerboLumiere  
*Your AI-powered Audio/Video Translation & Transcription Dashboard*

VerboLumiere is a Django-based web application designed to empower users to upload videos, transcribe their audio using Whisper, translate the transcript into other languages using MarianMT, and generate both translated audio and video content — all through a sleek, neon-themed dashboard.
![Title](ReadmeMedia/Verbolumiére_20250520_092601_0000.png)
---

##  Features

###  Upload Videos
Upload your `.mp4` files to the platform and have them automatically queued for processing.

###  Transcription (Whisper by OpenAI)
Once uploaded, the app extracts and transcribes audio using Whisper models.

###  Translation (MarianMT)
The transcribed text is then translated from the source language to English (or other languages if extended), using the MarianMT transformer models.

###  Translated Audio Generation
The translated transcript is converted to speech using TTS models (optionally).

###  Translated Video Overlay
The generated translated audio can be embedded into the original video, creating a dubbed version of the original content.

###  Download Options
- Download transcriptions (plain text)
- Download translated audio (MP3)
- Download translated video (MP4)

###  Video Management
- View uploaded videos with upload timestamps.
- Delete videos and their associated assets easily.
- Secure login/logout with Django's authentication system.

###  Neon-Themed UI
A stunning black background interface with glowing neon pink accents for a visually captivating experience. Mobile-friendly with media queries included.

---

## 📸 Screenshots

###  Login Page  
![Login Page](ReadmeMedia/image.png)

###  Registeration Page  
![Login Page](ReadmeMedia/registeration.png)

###  Dashboard  
![Dashboard Screenshot](ReadmeMedia/dashboard.png)

### 📤 Upload Page  
![Upload Screenshot](ReadmeMedia/upload.png)

### 📝 Transcript and Translated Media  
![Results Screenshot](ReadmeMedia/translated.png)

---

##  Tech Stack

- **Backend**: Django 4.x
- **Frontend**: Bootstrap 5, Orbitron Fonts, Neon CSS
- **ML Models**:
  - Whisper (for transcription)
  - MarianMT (for translation)
  - TTS (Text-to-Speech for audio generation)
- **Storage**: FileSystem (media/uploads)
- **Authentication**: Django Auth

---

##  Installation

```bash
git clone https://github.com/yourusername/verbolumiere.git
cd verbolumiere
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
