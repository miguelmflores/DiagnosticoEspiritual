"""
Comprehensive KPI and Quality Auditor for BL400K.html
"""
import re
import os
import json

HTML_PATH = r"c:\Users\migue\OneDrive - Universidad Catolica del Maule\BL400K\BL400K.html"

def audit():
    print("=== AUDIT REPORT: BL400K.html ===")
    assert os.path.exists(HTML_PATH), "HTML file does not exist!"
    size_bytes = os.path.getsize(HTML_PATH)
    size_mb = size_bytes / (1024 * 1024)
    print(f"1. Single-File Size: {size_bytes:,} bytes ({size_mb:.2f} MB)")
    assert size_mb < 20, "File too large for easy WhatsApp transfer!"

    with open(HTML_PATH, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check external URLs
    raw_urls = re.findall(r'https?://[^\s"\'<>]+', content)
    allowed_prefixes = ["https://api.whatsapp.com"]
    disallowed = [u for u in raw_urls if not any(u.startswith(p) for p in allowed_prefixes)]
    print(f"2. External Network Calls (should be 0): {len(disallowed)} -> {disallowed}")
    assert len(disallowed) == 0, f"Found external dependencies: {disallowed}"

    # Check CDNs or external fonts
    external_cdns = [cdn for cdn in ["fonts.googleapis.com", "cdnjs", "unpkg", "jsdelivr"] if cdn in content]
    print(f"3. External CDNs (should be 0): {external_cdns}")
    assert len(external_cdns) == 0, "Found external CDNs!"

    # Parse characters
    m = re.search(r'const CHARACTERS = (\[.*?\]);\s*\n\s*const state', content, re.DOTALL)
    assert m, "Characters array not found in script!"
    characters = json.loads(m.group(1))
    print(f"4. Biblical Characters Count: {len(characters)} (Requirement: >= 15)")
    assert len(characters) >= 15, "Fewer than 15 characters!"

    for idx, c in enumerate(characters, 1):
        assert c["name"], f"Char {idx} missing name"
        assert c["citation"], f"Char {idx} missing citation"
        assert c["image"].startswith("data:image/jpeg;base64,"), f"Char {idx} missing base64 image"
        assert len(c["scene"]) <= 3, f"Char {idx} scene exceeds 3 phrases!"
        assert len(c["qDiagnostic"]["options"]) >= 3, f"Char {idx} diagnostic options missing"
        assert "easy" in c["immersion"], f"Char {idx} missing easy immersion"
        assert "hard" in c["immersion"], f"Char {idx} missing hard immersion"
        assert "realityCheck" in c["immersion"], f"Char {idx} missing reality check"
        print(f"   [{idx:02d}] {c['name']:<25} | Cita: {c['citation']:<20} | Era: {c['era']}")

    # Check memes
    memes = [
        "farmear aura", "red flag", "main character", "POV:",
        "la neta", "cringe", "NPC espiritual", "basado",
        "0 de IQ espiritual", "postureo"
    ]
    found_memes = [m for m in memes if m.lower() in content.lower()]
    print(f"5. Youth Memes in Spanish: {len(found_memes)}/{len(memes)} detected: {found_memes}")
    assert len(found_memes) >= 8, "Not enough youth meme references!"

    # Check theological core message (Juan 16:8 + Romanos 8:1)
    has_j16 = "Juan 16:8" in content
    has_r8 = "Romanos 8:1" in content
    print(f"6. Hopeful Theological Message: Juan 16:8 ({has_j16}), Romanos 8:1 ({has_r8})")
    assert has_j16 and has_r8, "Missing required scriptures for theological hope!"

    # Check Sound synthesizer
    has_sound = "class SoundEngine" in content and "AudioContext" in content
    print(f"7. Procedural Sound Synthesizer (Web Audio API): {has_sound}")
    assert has_sound, "Missing SoundEngine!"

    # Check LocalStorage
    has_ls = "localStorage.getItem('bl400k_score')" in content and "localStorage.setItem" in content
    print(f"8. LocalStorage Persistence: {has_ls}")
    assert has_ls, "Missing LocalStorage persistence!"

    # Check Presenter Mode
    has_presenter = "presenterBar" in content and "togglePresenter" in content
    print(f"9. Presenter Synchronized Mode: {has_presenter}")
    assert has_presenter, "Missing Presenter Mode!"

    # Check Help Manual
    has_manual = "helpModal" in content and "Manual de Juego y Reglas" in content
    print(f"10. In-Game Manual Modal: {has_manual}")
    assert has_manual, "Missing Game Manual Modal!"

    print("\n>>> ALL KPIS VERIFIED: 100% COMPLETE & PASSING <<<")

if __name__ == "__main__":
    audit()
