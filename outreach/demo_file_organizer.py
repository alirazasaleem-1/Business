"""
ARS Digital - File Organizer Demo Script
========================================
A visually impressive Python automation that organizes
a messy Downloads folder in seconds.

PERFECT FOR: Screen recording a short demo video for social media.

HOW TO RECORD:
1. Create a test folder with 15-20 random files (.jpg, .pdf, .docx, .py, .mp3, etc.)
2. Start screen recording (OBS, Loom, or Windows Game Bar: Win+G)
3. Run this script
4. Show the beautiful organized result
5. Post with the caption from outreach/social_media_captions.md

Usage: python demo_file_organizer.py [folder_path]
If no path given, it creates a demo folder with sample files.
"""

import os
import shutil
import sys
import time
from pathlib import Path
from datetime import datetime

# File type categories with emojis for terminal output
CATEGORIES = {
    "📸 Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp", ".ico"],
    "📄 Documents": [".pdf", ".doc", ".docx", ".txt", ".xlsx", ".xls", ".pptx", ".csv"],
    "🎵 Music": [".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a"],
    "🎬 Videos": [".mp4", ".avi", ".mkv", ".mov", ".wmv", ".webm"],
    "💻 Code": [".py", ".js", ".html", ".css", ".java", ".cpp", ".c", ".ts", ".json"],
    "📦 Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "🎨 Design": [".psd", ".ai", ".fig", ".sketch", ".xd"],
}

# Terminal colors for Windows
class Colors:
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    MAGENTA = "\033[95m"
    BOLD = "\033[1m"
    END = "\033[0m"


def get_category(extension):
    """Find which category a file extension belongs to."""
    ext = extension.lower()
    for category, extensions in CATEGORIES.items():
        if ext in extensions:
            return category
    return "📁 Other"


def create_demo_files(demo_path):
    """Create a messy demo folder with sample files for the recording."""
    demo_path.mkdir(parents=True, exist_ok=True)
    
    sample_files = [
        "holiday_photo.jpg", "budget_2024.xlsx", "meeting_notes.pdf",
        "favourite_song.mp3", "website_mockup.psd", "backup.zip",
        "profile_pic.png", "invoice_march.pdf", "presentation.pptx",
        "app.py", "styles.css", "index.html", "data.json",
        "wedding_video.mp4", "podcast_ep3.wav", "logo.svg",
        "report_final.docx", "screenshot.png", "receipt.pdf",
        "background_music.mp3", "old_project.rar", "notes.txt",
    ]
    
    print(f"\n{Colors.YELLOW}📂 Creating messy demo folder with {len(sample_files)} files...{Colors.END}\n")
    time.sleep(1)
    
    for filename in sample_files:
        filepath = demo_path / filename
        filepath.write_text(f"Demo file: {filename}\nCreated by ARS Digital File Organizer")
        print(f"   💾 {filename}")
        time.sleep(0.05)  # Small delay for visual effect in recording
    
    print(f"\n{Colors.CYAN}{'='*50}{Colors.END}")
    print(f"{Colors.BOLD}   ✅ {len(sample_files)} messy files created!{Colors.END}")
    print(f"{Colors.CYAN}{'='*50}{Colors.END}\n")
    return demo_path


def organize_folder(folder_path):
    """Organize files in the given folder into categorized subfolders."""
    folder = Path(folder_path)
    
    if not folder.exists():
        print(f"❌ Folder not found: {folder}")
        return
    
    # Get all files (not directories)
    files = [f for f in folder.iterdir() if f.is_file() and f.name != os.path.basename(__file__)]
    
    if not files:
        print("📭 No files to organize!")
        return
    
    print(f"\n{Colors.MAGENTA}{'='*50}{Colors.END}")
    print(f"{Colors.BOLD}   🤖 ARS Digital - File Organizer{Colors.END}")
    print(f"   Powered by Python Automation")
    print(f"{Colors.MAGENTA}{'='*50}{Colors.END}\n")
    
    print(f"   📂 Scanning: {folder}")
    print(f"   📊 Found: {len(files)} files to organize\n")
    time.sleep(1.5)  # Dramatic pause for recording
    
    print(f"{Colors.CYAN}   ⚡ Organizing...{Colors.END}\n")
    time.sleep(0.5)
    
    moved_count = 0
    category_counts = {}
    
    for file in files:
        category = get_category(file.suffix)
        # Clean category name for folder (remove emoji)
        folder_name = category.split(" ", 1)[1] if " " in category else category
        target_dir = folder / folder_name
        target_dir.mkdir(exist_ok=True)
        
        target_path = target_dir / file.name
        shutil.move(str(file), str(target_path))
        
        moved_count += 1
        category_counts[category] = category_counts.get(category, 0) + 1
        
        print(f"   {category.split(' ')[0]} {file.name} → {folder_name}/")
        time.sleep(0.08)  # Slight delay for visual effect
    
    # Summary
    print(f"\n{Colors.GREEN}{'='*50}{Colors.END}")
    print(f"{Colors.BOLD}   ✅ DONE! Organized {moved_count} files{Colors.END}")
    print(f"{Colors.GREEN}{'='*50}{Colors.END}\n")
    
    print("   📊 Summary:")
    for category, count in sorted(category_counts.items(), key=lambda x: x[1], reverse=True):
        bar = "█" * count
        print(f"   {category}: {bar} ({count})")
    
    print(f"\n   ⏱️  Time: {datetime.now().strftime('%H:%M:%S')}")
    print(f"   🏢 Built by ARS Digital | wa.me/923467282874\n")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        target = sys.argv[1]
    else:
        # Create demo folder for recording
        demo_dir = Path(__file__).parent / "demo_messy_folder"
        print(f"\n{Colors.BOLD}🎬 DEMO MODE{Colors.END}")
        print(f"   No folder specified. Creating a demo folder...\n")
        time.sleep(1)
        create_demo_files(demo_dir)
        
        input(f"{Colors.YELLOW}   Press ENTER to organize this mess... ⚡{Colors.END}")
        target = str(demo_dir)
    
    organize_folder(target)
