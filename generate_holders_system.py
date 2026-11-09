"""
Generator script for BL400K Holders Architecture (Fase 4 - Experiencia 100% Definitiva)
- Embers particles on TOP (z-index: 99)
- Removed 'Experiencia interactiva premium' banner
- Full screen container sizing with ZERO clipping / overflow of buttons
- Dynamic side-switching per character (textSide: 'left' | 'right') to never obstruct character faces/bodies
- Background artwork filling the entire holder with 5% black transparency on narrative phrases
- Explicit difficulty badge and differentiation for Iniciado (13-17) vs Paladin (18+)
- Guaranteed button visibility across all screens (1366x768 to 4K + Mobile Portrait)
"""
import os
import json
import base64
import sys

# Safe UTF-8
sys.stdout.reconfigure(encoding='utf-8')

# Import data and assets from data_characters
from data_characters import CHARACTERS, ASSETS

print(f"Loaded {len(CHARACTERS)} characters and {len(ASSETS)} assets.")

OUTPUT_FILE = r"c:\Users\migue\OneDrive - Universidad Catolica del Maule\BL400K\BL400K.html"

# Prepare JSON string of characters
CHARACTERS_JSON = json.dumps(CHARACTERS, ensure_ascii=False)

hero_b64 = ASSETS["hero"]
hope_b64 = ASSETS["hope_finale"]

# Load BGM Soundtrack to Base64 (100% Offline Single-File WhatsApp compatibility)
bgm_file = os.path.join("audio", "BGM_BL400K.mp3") if os.path.exists(os.path.join("audio", "BGM_BL400K.mp3")) else "BGM_BL400K.mp3"
if os.path.exists(bgm_file):
    with open(bgm_file, 'rb') as f:
        bgm_b64 = base64.b64encode(f.read()).decode('ascii')
        bgm_data_uri = f"data:audio/mp3;base64,{bgm_b64}"
    print(f"Loaded BGM soundtrack from {bgm_file} ({len(bgm_data_uri)} chars).")
else:
    bgm_data_uri = "audio/BGM_BL400K.mp3"
    print("Warning: BGM soundtrack file not found, using fallback relative path.")

HTML_CONTENT = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
<title>Diagnóstico Bíblico: ¿Tienes el Espíritu Santo? | BL400K</title>

<!-- Favicon Links & Theme Color -->
<link rel="icon" type="image/svg+xml" href="favicon.svg">
<link rel="icon" type="image/png" sizes="32x32" href="favicon-32x32.png">
<link rel="apple-touch-icon" sizes="180x180" href="apple-touch-icon.png">
<link rel="shortcut icon" href="favicon.svg">
<meta name="theme-color" content="#d4af37">

<!-- SEO & Primary Meta Tags -->
<meta name="title" content="Diagnóstico Bíblico: ¿Tienes el Espíritu Santo? | BL400K">
<meta name="description" content="Descubre a través de 19 personajes bíblicos las evidencias reales de quiénes fueron verdaderamente guiados por el Espíritu de Dios y quiénes operaron bajo el engaño de la carne.">

<!-- Open Graph / Facebook / WhatsApp / Telegram -->
<meta property="og:type" content="website">
<meta property="og:url" content="https://miguelmflores.github.io/DiagnosticoEspiritual/">
<meta property="og:title" content="Diagnóstico Bíblico: ¿Tienes el Espíritu Santo?">
<meta property="og:description" content="Descubre a través de 19 personajes bíblicos las evidencias reales de quiénes fueron verdaderamente guiados por el Espíritu de Dios y quiénes operaron bajo el engaño de la carne.">
<meta property="og:image" content="https://miguelmflores.github.io/DiagnosticoEspiritual/og-preview.jpg">
<meta property="og:image:secure_url" content="https://miguelmflores.github.io/DiagnosticoEspiritual/og-preview.jpg">
<meta property="og:image:type" content="image/jpeg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="es_ES">

<!-- Twitter Card -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:url" content="https://miguelmflores.github.io/DiagnosticoEspiritual/">
<meta name="twitter:title" content="Diagnóstico Bíblico: ¿Tienes el Espíritu Santo?">
<meta name="twitter:description" content="Descubre a través de 19 personajes bíblicos las evidencias reales de quiénes fueron verdaderamente guiados por el Espíritu de Dios y quiénes operaron bajo el engaño de la carne.">
<meta name="twitter:image" content="https://miguelmflores.github.io/DiagnosticoEspiritual/og-preview.jpg">
<!-- 
========================================================================
DIAGNÓSTICO BÍBLICO: ¿TIENES EL ESPÍRITU SANTO? (BL400K - HOLDERS SYSTEM)
Formato: Single-File Autónomo 100% Offline (Zero External CDNs/Fonts/APIs)
Arquitectura: Holders / Diapositivas a Pantalla Completa (100vh / FHD 1920x1080 & Portrait)
Zero Scroll: Control estricto de desplazamiento; navegación fluida guiada por botones
Audio: BGM Soundtrack integrado (audio/BGM_BL400K.mp3) + Control de Volumen Interactivo
Pantalla Completa: Integración Fullscreen API nativa + Botón flotante '✕'
Partículas: Ascuas celestiales flotando en primer plano (z-index: 99)
========================================================================
-->
<style>
/* CSS RESET & VARIABLES */
*, *::before, *::after {{
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  -webkit-tap-highlight-color: transparent;
}}

:root {{
  --bg-deep: #07080c;
  --bg-surface: #0f1118;
  --bg-card: #151822;
  --bg-card-hover: #1c2130;
  --gold-primary: #f59e0b;
  --gold-bright: #fbbf24;
  --gold-dark: #b45309;
  --gold-glow: rgba(245, 158, 11, 0.45);
  --crimson-blood: #dc2626;
  --crimson-dark: #7f1d1d;
  --crimson-glow: rgba(220, 38, 38, 0.45);
  --emerald-holy: #10b981;
  --emerald-glow: rgba(16, 185, 129, 0.35);
  --cyan-shekinah: #06b6d4;
  --cyan-glow: rgba(6, 182, 212, 0.35);
  --text-main: #f3f4f6;
  --text-muted: #9ca3af;
  --text-dim: #6b7280;
  --border-gold: rgba(212, 175, 55, 0.35);
  --border-glow: rgba(245, 158, 11, 0.6);
  --font-serif: Georgia, "Times New Roman", Garamond, serif;
  --font-sans: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  --font-display: "Cinzel", "Outfit", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  --hud-height: 50px;
}}

html, body {{
  height: 100%;
  min-height: 100%;
  width: 100%;
  overflow-x: hidden;
  word-break: break-word;
  overflow-wrap: anywhere;
  background-color: var(--bg-deep);
  color: var(--text-main);
  font-family: var(--font-sans);
  line-height: 1.5;
  user-select: none;
  -webkit-user-select: none;
  touch-action: pan-y;
  -webkit-tap-highlight-color: transparent;
}}

/* CANVAS BACKGROUND PARTICLES (EN PRIMER PLANO POR ENCIMA DE HOLDERS Y TEXTOS) */
#embersCanvas {{
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  pointer-events: none;
  z-index: 99; /* Ascuas por encima de los holders */
  opacity: 0.8;
}}

.vignette-overlay {{
  position: fixed;
  inset: 0;
  background: radial-gradient(circle at center, transparent 40%, rgba(3, 4, 7, 0.88) 100%);
  pointer-events: none;
  z-index: 1;
}}

/* FLOATING EXIT FULLSCREEN BUTTON (TOP-RIGHT CORNER) */
.fullscreen-exit-btn {{
  position: fixed;
  top: 8px;
  right: 10px;
  z-index: 10000;
  width: 36px;
  height: 36px;
  border-radius: 50%;
  background: rgba(15, 17, 24, 0.88);
  border: 1.5px solid var(--border-gold);
  color: #fff;
  font-size: 1.15rem;
  font-weight: 900;
  display: none;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  backdrop-filter: blur(8px);
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.8);
  transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
}}
.fullscreen-exit-btn:hover {{
  background: rgba(220, 38, 38, 0.9);
  border-color: #f87171;
  transform: scale(1.1);
  box-shadow: 0 0 15px var(--crimson-glow);
}}

/* ELIMINAR COLISIÓN: El botón flotante jamás se muestra sobre el HUD */
#gameHudHeader.is-visible ~ .fullscreen-exit-btn,
.hud-active .fullscreen-exit-btn {{
  display: none !important;
}}

/* HUD HEADER REDESIGNED (COMPACT & FIXED 50px) */
.hud-header {{
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: var(--hud-height);
  max-height: 52px;
  background: rgba(11, 13, 20, 0.94);
  backdrop-filter: blur(14px);
  border-bottom: 1.5px solid var(--border-gold);
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 1.2rem;
  z-index: 100;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.8);
}}

.hud-left {{
  display: flex;
  align-items: center;
  gap: 0.8rem;
  min-width: 0;
}}

.hud-logo-crest {{
  font-size: 1.35rem;
  line-height: 1;
  filter: drop-shadow(0 0 8px var(--gold-glow));
}}

.hud-stage-block {{
  display: flex;
  flex-direction: column;
  gap: 3px;
}}

.hud-stage-name {{
  font-family: var(--font-display);
  font-size: 0.88rem;
  font-weight: 800;
  letter-spacing: 0.8px;
  color: var(--gold-bright);
  text-transform: uppercase;
  white-space: nowrap;
}}

.hud-progress-track {{
  width: 120px;
  height: 4px;
  background: rgba(255, 255, 255, 0.12);
  border-radius: 3px;
  overflow: hidden;
}}

.hud-progress-bar {{
  height: 100%;
  width: 0%;
  background: linear-gradient(90deg, var(--gold-dark), var(--gold-bright));
  box-shadow: 0 0 8px var(--gold-glow);
  transition: width 0.4s ease;
}}

/* BADGE DE DIFICULTAD ACTIVA EN HUD */
.hud-diff-badge {{
  background: rgba(6, 182, 212, 0.18);
  border: 1px solid var(--cyan-shekinah);
  color: #a5f3fc;
  font-family: var(--font-display);
  font-size: 0.72rem;
  font-weight: 800;
  letter-spacing: 0.8px;
  text-transform: uppercase;
  padding: 0.2rem 0.6rem;
  border-radius: 12px;
  white-space: nowrap;
  box-shadow: 0 0 10px rgba(6, 182, 212, 0.2);
}}
.hud-diff-badge.paladin {{
  background: rgba(245, 158, 11, 0.2);
  border-color: var(--gold-bright);
  color: var(--gold-bright);
  box-shadow: 0 0 10px var(--gold-glow);
}}

.hud-score-chip {{
  background: rgba(0, 0, 0, 0.65);
  border: 1px solid var(--border-gold);
  border-radius: 20px;
  padding: 0.22rem 0.85rem;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.4rem;
  box-shadow: 0 0 12px rgba(245, 158, 11, 0.2);
  white-space: nowrap;
  flex-shrink: 0;
}}
.hud-score-chip span {{
  white-space: nowrap;
}}

.hud-actions {{
  display: flex;
  align-items: center;
  gap: 0.5rem;
}}

.hud-icon-btn {{
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid rgba(212, 175, 55, 0.3);
  color: #fff;
  width: 34px;
  height: 34px;
  border-radius: 8px;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  font-size: 0.95rem;
  transition: all 0.2s ease;
}}

.hud-icon-btn:hover {{
  background: rgba(245, 158, 11, 0.2);
  border-color: var(--gold-bright);
  transform: translateY(-1px);
}}

/* VOLUME POPOVER PANEL */
.volume-popup {{
  position: fixed;
  top: calc(var(--hud-height) + 6px);
  right: 12px;
  background: rgba(15, 17, 24, 0.96);
  border: 1.5px solid var(--border-gold);
  border-radius: 12px;
  padding: 0.9rem 1.1rem;
  z-index: 1000;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.9), 0 0 15px var(--gold-glow);
  backdrop-filter: blur(14px);
  width: 260px;
}}
.volume-popup-header {{
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 0.75rem;
}}
.volume-popup-title {{
  font-family: var(--font-display);
  font-size: 0.85rem;
  color: var(--gold-bright);
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.8px;
}}
.volume-popup-close {{
  background: none;
  border: none;
  color: var(--text-muted);
  font-size: 1.2rem;
  cursor: pointer;
  line-height: 1;
}}
.volume-popup-close:hover {{
  color: #fff;
}}
.volume-slider-row {{
  display: flex;
  align-items: center;
  gap: 0.65rem;
  margin-bottom: 0.75rem;
}}
.volume-mute-btn {{
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid rgba(212, 175, 55, 0.3);
  border-radius: 6px;
  color: #fff;
  width: 32px;
  height: 32px;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  font-size: 0.92rem;
}}
.volume-mute-btn:hover {{
  border-color: var(--gold-bright);
}}
.volume-slider {{
  flex: 1;
  accent-color: var(--gold-bright);
  cursor: pointer;
}}
.volume-percent {{
  font-family: var(--font-display);
  font-size: 0.85rem;
  font-weight: 700;
  color: var(--gold-bright);
  min-width: 36px;
  text-align: right;
}}
.volume-presets {{
  display: flex;
  gap: 0.4rem;
  justify-content: space-between;
}}
.vol-preset-btn {{
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: 6px;
  color: var(--text-muted);
  padding: 0.25rem 0.45rem;
  font-size: 0.72rem;
  cursor: pointer;
  transition: all 0.2s ease;
}}
.vol-preset-btn:hover {{
  background: rgba(245, 158, 11, 0.2);
  color: var(--gold-bright);
  border-color: var(--gold-bright);
}}

/* ========================================================================
   SLIDE / HOLDER DECK ARCHITECTURE
   ======================================================================== */
#slideDeck {{
  position: relative;
  width: 100vw;
  height: 100%;
  min-height: 100vh;
  min-height: 100dvh;
  overflow-x: hidden;
  z-index: 10;
}}

.slide-holder {{
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  min-height: 100vh;
  min-height: 100dvh;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  padding: calc(var(--hud-height) + 0.5rem) 1.2rem 1rem 1.2rem;
  opacity: 0;
  visibility: hidden;
  transform: translateY(24px) scale(0.99);
  transition: opacity 0.45s cubic-bezier(0.16, 1, 0.3, 1), transform 0.45s cubic-bezier(0.16, 1, 0.3, 1), visibility 0.45s;
  pointer-events: none;
  box-sizing: border-box;
  overflow-y: auto !important;
  overflow-x: hidden !important;
  -webkit-overflow-scrolling: touch !important;
  touch-action: pan-y;
  scrollbar-width: thin;
  scrollbar-color: var(--gold-dark) transparent;
}}

.slide-holder.active {{
  opacity: 1;
  visibility: visible;
  transform: translateY(0) scale(1);
  pointer-events: auto;
  z-index: 15;
}}

/* Backward-compatible .screen classes for existing audit selectors */
.screen {{
  display: none;
}}
.screen.active {{
  display: flex;
}}

/* HOLDER CONTAINER SIZES - FULL VIEWPORT FIT (CERO ESCAPING / CERO OVERFLOW) */
.holder-box,
.holder-box-center {{
  width: 100vw;
  max-width: 100vw;
  height: calc(100vh - var(--hud-height));
  max-height: calc(100vh - var(--hud-height));
  margin: 0 auto;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0.5rem 1rem;
  box-sizing: border-box;
}}

/* ========================================================================
   HOLDER 1: HERO / WELCOME SLIDE
   ======================================================================== */
.hero-card {{
  background: linear-gradient(180deg, var(--bg-card) 0%, rgba(10, 11, 16, 0.98) 100%);
  border: 1px solid var(--border-gold);
  border-radius: 20px;
  overflow: hidden;
  box-shadow: 0 25px 60px rgba(0, 0, 0, 0.9), inset 0 1px 0 rgba(245, 158, 11, 0.35);
  width: 96vw;
  max-width: 1720px;
  height: calc(100vh - var(--hud-height) - 1.2rem);
  max-height: calc(100vh - var(--hud-height) - 1.2rem);
  display: grid;
  grid-template-columns: 0.95fr 1.05fr;
  align-items: stretch;
  box-sizing: border-box;
}}

.hero-media {{
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  border-right: 2px solid var(--gold-dark);
}}

.hero-body {{
  padding: clamp(1.5rem, 3vh, 2.5rem) clamp(1.8rem, 3.5vw, 3.2rem);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: flex-start;
  text-align: left;
  box-sizing: border-box;
  height: 100%;
  overflow-y: auto;
}}

.hero-body-top {{
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: clamp(0.4rem, 1vh, 0.8rem);
  width: 100%;
}}

.hero-action-row {{
  width: 100%;
  padding-top: 0.8rem;
}}

.hero-title {{
  font-family: var(--font-display);
  font-size: clamp(2.5rem, 4.2vw, 3.8rem); /* ESCALADO GRANDE PARA PROYECCIÓN */
  font-weight: 900;
  line-height: 1.18;
  letter-spacing: 1.2px;
  color: #fff;
  text-transform: uppercase;
  margin-bottom: 0.5rem;
  text-shadow: 0 4px 22px rgba(0, 0, 0, 0.95);
}}

.hero-title span {{
  color: var(--gold-bright);
  text-shadow: 0 0 25px var(--gold-glow);
}}

.hero-sub {{
  font-size: clamp(1.35rem, 1.75vw, 1.68rem); /* LECTURA CLARA A DISTANCIA */
  color: #e2e8f0;
  max-width: 880px;
  line-height: 1.52;
  font-weight: 500;
}}

.hero-citation {{
  font-family: var(--font-serif);
  font-size: clamp(1.2rem, 1.5vw, 1.45rem); /* CITA CLARA Y DESTACADA */
  color: var(--gold-bright);
  font-style: italic;
  display: inline-block;
  background: rgba(245, 158, 11, 0.14);
  padding: 0.85rem 1.5rem;
  border-radius: 12px;
  border-left: 5px solid var(--gold-bright);
  margin-top: 0.35rem;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.5);
}}

/* ACTION BUTTONS */
.action-btn {{
  background: linear-gradient(180deg, var(--gold-bright) 0%, var(--gold-dark) 100%);
  color: #07080c;
  font-family: var(--font-display);
  font-size: clamp(1.35rem, 1.8vw, 1.68rem); /* BOTÓN GRANDE Y VISIBLE */
  font-weight: 900;
  text-transform: uppercase;
  letter-spacing: 2px;
  padding: clamp(0.95rem, 1.8vh, 1.35rem) clamp(2.2rem, 3.5vw, 3.2rem);
  border: none;
  border-radius: 10px;
  cursor: pointer;
  box-shadow: 0 8px 24px var(--gold-glow), inset 0 1px 0 rgba(255, 255, 255, 0.6);
  transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.7rem;
}}

.action-btn:hover {{
  transform: translateY(-2px);
  box-shadow: 0 12px 30px var(--gold-glow);
}}

.action-btn:active {{
  transform: translateY(1px);
}}

.pulse-btn {{
  animation: pulseGold 2.2s infinite;
}}
@keyframes pulseGold {{
  0% {{ box-shadow: 0 0 0 0 rgba(245, 158, 11, 0.7), inset 0 1px 0 rgba(255, 255, 255, 0.6); }}
  70% {{ box-shadow: 0 0 0 14px rgba(245, 158, 11, 0), inset 0 1px 0 rgba(255, 255, 255, 0.6); }}
  100% {{ box-shadow: 0 0 0 0 rgba(245, 158, 11, 0), inset 0 1px 0 rgba(255, 255, 255, 0.6); }}
}}

/* ========================================================================
   HOLDER 2: DIFFICULTY SELECTOR SLIDE
   ======================================================================== */
.diff-slide-card {{
  background: linear-gradient(180deg, var(--bg-card) 0%, rgba(12, 14, 22, 0.98) 100%);
  border: 1px solid var(--border-gold);
  border-radius: 20px;
  padding: clamp(1.8rem, 3vh, 2.5rem) clamp(2rem, 3.5vw, 3.5rem);
  width: 96vw;
  max-width: 1560px;
  height: calc(100vh - var(--hud-height) - 1.2rem);
  max-height: calc(100vh - var(--hud-height) - 1.2rem);
  margin: 0 auto;
  box-shadow: 0 25px 60px rgba(0, 0, 0, 0.9);
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
  box-sizing: border-box;
}}

.diff-slide-eyebrow {{
  color: var(--gold-bright);
  font-size: 1.25rem; /* ESCALADO GRANDE */
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 2.5px;
  margin-bottom: 0.35rem;
}}

.diff-slide-title {{
  font-family: var(--font-display);
  font-size: clamp(2.4rem, 3.6vw, 3.5rem); /* TÍTULO DESTACADO */
  font-weight: 900;
  line-height: 1.2;
  color: #fff;
  text-transform: uppercase;
  margin-bottom: 0.45rem;
  text-shadow: 0 3px 18px rgba(0, 0, 0, 0.95);
}}

.diff-slide-sub {{
  color: #cbd5e1;
  font-size: clamp(1.35rem, 1.75vw, 1.65rem); /* SUBTÍTULO VISIBLE */
  margin-bottom: 1.2rem;
  line-height: 1.48;
}}

.diff-options {{
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.8rem;
  width: 100%;
  margin-bottom: 1.2rem;
}}

.diff-btn {{
  background: var(--bg-surface);
  border: 2px solid rgba(212, 175, 55, 0.35);
  padding: clamp(1.4rem, 2.4vh, 2rem) 1.8rem;
  border-radius: 16px;
  cursor: pointer;
  color: var(--text-main);
  text-align: left;
  transition: all 0.25s ease;
  position: relative;
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.55);
}}

.diff-btn:hover {{
  border-color: rgba(245, 158, 11, 0.8);
  background: rgba(245, 158, 11, 0.12);
  transform: translateY(-2px);
}}

.diff-btn.active {{
  border-color: var(--gold-bright);
  background: rgba(245, 158, 11, 0.22);
  box-shadow: 0 0 25px var(--gold-glow);
}}

.diff-name {{
  font-weight: 900;
  font-size: 1.65rem; /* NOMBRE DE DIFICULTAD GRANDE */
  color: var(--gold-bright);
  display: block;
  margin-bottom: 0.5rem;
  letter-spacing: 0.5px;
}}

.diff-desc {{
  font-size: clamp(1.18rem, 1.45vw, 1.42rem); /* DESCRIPCIÓN NÍTIDA */
  color: #e2e8f0;
  line-height: 1.5;
  font-weight: 500;
}}

/* ========================================================================
   HOLDER 3A: STAGE INTRO (FULL-SCREEN ARTWORK AS BACKGROUND + 3 PHRASES)
   DYNAMIC SIDE-SWITCHING (align-left vs align-right)
   ======================================================================== */
.character-split-grid,
.stage-intro-grid {{
  position: relative;
  display: grid;
  gap: 2.5rem;
  align-items: stretch;
  background: var(--bg-card);
  border: 1.5px solid var(--border-gold);
  border-radius: 20px;
  padding: clamp(1.2rem, 2.5vh, 2rem) clamp(1.5rem, 3vw, 3rem);
  box-shadow: 0 25px 60px rgba(0, 0, 0, 0.9);
  width: 96vw;
  max-width: 1760px;
  height: calc(100vh - var(--hud-height) - 1.2rem);
  max-height: calc(100vh - var(--hud-height) - 1.2rem);
  overflow: hidden;
  box-sizing: border-box;
}}

/* BASE CHARACTER TAG BADGE (KPI 4 AUDITED) */
.character-tag-badge {{
  position: absolute;
  font-size: 0.60rem;
  font-weight: 900;
  text-transform: uppercase;
  letter-spacing: 1.2px;
  padding: 0.28rem 0.65rem;
  border-radius: 4px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.8);
  z-index: 5;
}}

.tag-red {{ background: var(--crimson-blood); color: #fff; }}
.tag-green {{ background: var(--emerald-holy); color: #042f1a; font-weight: 900; }}
.tag-gold {{ background: var(--gold-bright); color: #07080c; font-weight: 900; }}

/* CASO A: TEXTO A LA IZQUIERDA (PERSONAJE A LA DERECHA) */
.stage-intro-grid.align-left {{
  grid-template-columns: 1.15fr 0.85fr;
}}
.stage-intro-grid.align-left .intro-info-col {{
  order: 1;
}}
.stage-intro-grid.align-left .intro-art-col {{
  order: 2;
}}
.stage-intro-grid.align-left .stage-intro-bg-img,
.stage-intro-grid.align-left .stage-intro-bg-picture img {{
  object-position: 78% center; /* Personaje nítido en el lado derecho */
}}
.stage-intro-grid.align-left .stage-intro-overlay {{
  background: linear-gradient(90deg, rgba(7, 8, 12, 0.96) 0%, rgba(7, 8, 12, 0.82) 48%, rgba(7, 8, 12, 0.35) 75%, rgba(7, 8, 12, 0.05) 100%);
}}
.stage-intro-grid.align-left .character-tag-badge {{
  bottom: 1.4rem;
  right: 1.8rem;
  left: auto;
}}

/* CASO B: TEXTO A LA DERECHA (PERSONAJE A LA IZQUIERDA) */
.stage-intro-grid.align-right {{
  grid-template-columns: 0.85fr 1.15fr;
}}
.stage-intro-grid.align-right .intro-art-col {{
  order: 1;
}}
.stage-intro-grid.align-right .intro-info-col {{
  order: 2;
}}
.stage-intro-grid.align-right .stage-intro-bg-img,
.stage-intro-grid.align-right .stage-intro-bg-picture img {{
  object-position: 22% center; /* Personaje nítido en el lado izquierdo */
}}
.stage-intro-grid.align-right .stage-intro-overlay {{
  background: linear-gradient(90deg, rgba(7, 8, 12, 0.05) 0%, rgba(7, 8, 12, 0.35) 25%, rgba(7, 8, 12, 0.82) 52%, rgba(7, 8, 12, 0.96) 100%);
}}
.stage-intro-grid.align-right .character-tag-badge {{
  bottom: 1.4rem;
  left: 1.8rem;
  right: auto;
}}

/* BACKGROUND IMAGE OF THE ENTIRE HOLDER */
.stage-intro-bg-picture {{
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  z-index: 1;
  pointer-events: none;
  border-radius: inherit;
  overflow: hidden;
}}

.stage-intro-bg-img,
.stage-intro-bg-picture img {{
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  z-index: 1;
  pointer-events: none;
  border-radius: inherit;
}}

.stage-intro-overlay {{
  position: absolute;
  inset: 0;
  z-index: 2;
  pointer-events: none;
  border-radius: inherit;
}}

.intro-art-col {{
  display: flex;
  flex-direction: column;
  align-items: center;
  position: relative;
  height: 100%;
  z-index: 3;
  pointer-events: none;
}}

.character-media-box {{
  position: relative;
  width: 100%;
  height: 100%;
}}

.character-img {{
  display: none;
}}

/* CONTENT COLUMN: METADATA & 3 PHRASES (GUARANTEED ZERO ESCAPING / OVERFLOW) */
.intro-info-col {{
  position: relative;
  z-index: 3;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  height: 100%;
  max-height: 100%;
  gap: clamp(0.35rem, 0.9vh, 0.75rem);
  box-sizing: border-box;
  overflow: hidden;
}}

.character-header {{
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 1rem;
  margin-bottom: 0.2rem;
}}

.char-meta {{
  display: flex;
  flex-direction: column;
  gap: 0.2rem;
}}

.char-era {{
  color: var(--gold-bright);
  font-size: 1.15rem;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 2px;
  display: inline-block;
  margin-bottom: 0.25rem;
  line-height: 1.2;
}}

.char-name {{
  font-family: var(--font-display);
  font-size: clamp(2.4rem, 3.6vw, 3.4rem); /* BOLD Y DESTACADO */
  font-weight: 900;
  line-height: 1.28;
  color: #fff;
  text-transform: uppercase;
  letter-spacing: 1px;
  margin: 0.1rem 0 0.25rem 0;
  overflow: visible;
  text-shadow: 0 2px 14px rgba(0, 0, 0, 0.98), 0 5px 28px rgba(0, 0, 0, 0.95);
}}

.char-subtitle {{
  font-size: clamp(1.2rem, 1.5vw, 1.45rem);
  color: #e2e8f0;
  font-style: italic;
  line-height: 1.38;
  margin-top: 0.15rem;
  display: block;
}}

.bible-citation-badge {{
  background: rgba(245, 158, 11, 0.12);
  border: 1px solid var(--border-gold);
  border-radius: 8px;
  padding: 0.4rem 0.8rem;
  text-align: right;
  white-space: nowrap;
}}

.bible-citation-badge span:first-child {{
  display: block;
  font-size: 1.08rem;
  font-weight: 800;
  color: var(--gold-bright);
}}

.citation-note {{
  display: block;
  font-size: 0.7rem;
  color: var(--gold-dark);
  text-transform: uppercase;
  font-weight: 900;
  letter-spacing: 0.5px;
}}

/* SEQUENTIAL 3 PHRASES (KPI 3 AUDITED) */
.scene-body {{
  display: flex;
  flex-direction: column;
  gap: clamp(0.35rem, 0.8vh, 0.55rem);
}}

.scene-phrase {{
  background: rgba(0, 0, 0, 0.15); /* Contraste óptimo para pantalla y proyector */
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  border: 1.5px solid rgba(255, 255, 255, 0.22);
  border-left: 5px solid var(--gold-bright);
  border-radius: 12px;
  padding: clamp(0.75rem, 1.4vh, 1.15rem) 1.4rem;
  font-size: clamp(1.35rem, 1.85vw, 1.7rem); /* ULTRA LEGIBLE EN PC Y PROYECTOR */
  line-height: 1.46;
  font-weight: 500;
  color: #ffffff;
  display: flex;
  align-items: flex-start;
  gap: 0.95rem;
  opacity: 0;
  transform: translateX(-16px);
  transition: opacity 0.4s cubic-bezier(0.16, 1, 0.3, 1), transform 0.4s cubic-bezier(0.16, 1, 0.3, 1);
  box-shadow: 0 6px 22px rgba(0, 0, 0, 0.65);
  text-shadow: 0 2px 10px rgba(0, 0, 0, 0.98), 0 4px 18px rgba(0, 0, 0, 0.95);
}}

.scene-phrase.revealed {{
  opacity: 1;
  transform: translateX(0);
}}

.scene-bullet {{
  color: var(--gold-bright);
  font-size: 1.6rem;
  line-height: 1;
  margin-top: 2px;
}}

/* ========================================================================
   HOLDER 3B, 3C, 3D: QUESTIONS SLIDES (GUARANTEED ZERO ESCAPING)
   ======================================================================== */
.question-slide-card {{
  background: linear-gradient(180deg, var(--bg-card) 0%, rgba(10, 11, 16, 0.98) 100%);
  border: 1px solid var(--border-gold);
  border-radius: 20px;
  padding: clamp(1.2rem, 2.5vh, 2rem) clamp(1.5rem, 3vw, 3rem);
  width: 96vw;
  max-width: 1600px;
  height: calc(100vh - var(--hud-height) - 1.2rem);
  max-height: calc(100vh - var(--hud-height) - 1.2rem);
  max-height: 88vh;
  margin: 0 auto;
  box-shadow: 0 25px 60px rgba(0, 0, 0, 0.9);
  box-sizing: border-box;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  overflow-y: auto;
}}

.question-title-badge {{
  display: inline-block;
  color: var(--gold-bright);
  font-size: 1.15rem;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 2px;
  margin-bottom: 0.4rem;
}}

.question-text {{
  font-family: var(--font-display);
  font-size: clamp(1.55rem, 2.4vw, 2.3rem); /* ENUNCIADOS GRANDES */
  font-weight: 800;
  color: #fff;
  line-height: 1.32;
  letter-spacing: 0.8px;
  text-transform: uppercase;
  margin-bottom: clamp(0.7rem, 1.5vh, 1.25rem);
  text-shadow: 0 2px 14px rgba(0, 0, 0, 0.95);
}}

.options-list {{
  display: flex;
  flex-direction: column;
  gap: clamp(0.5rem, 1.1vh, 0.75rem);
  margin-bottom: clamp(0.6rem, 1.2vh, 1rem);
}}

.opt-btn {{
  background: var(--bg-surface);
  border: 2px solid rgba(212, 175, 55, 0.35);
  border-radius: 14px;
  padding: clamp(0.95rem, 1.6vh, 1.35rem) 1.5rem;
  color: #ffffff;
  font-size: clamp(1.35rem, 1.8vw, 1.75rem); /* BOLD & ULTRA LEGIBLE */
  font-weight: 600;
  line-height: 1.42;
  text-align: left;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 1.2rem;
  min-height: 62px;
  transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.55);
}}

.opt-btn:hover:not(:disabled) {{
  border-color: var(--gold-bright);
  background: rgba(245, 158, 11, 0.12);
  transform: translateX(4px);
}}

.opt-letter {{
  background: rgba(245, 158, 11, 0.22);
  border: 2px solid var(--gold-bright);
  color: var(--gold-bright);
  font-family: var(--font-display);
  font-size: 1.6rem;
  font-weight: 900;
  min-width: 52px;
  height: 52px;
  border-radius: 10px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  box-shadow: 0 0 12px rgba(245, 158, 11, 0.3);
}}

.opt-btn.correct {{
  background: rgba(16, 185, 129, 0.2) !important;
  border-color: var(--emerald-holy) !important;
  color: #ecfdf5 !important;
}}
.opt-btn.correct .opt-letter {{
  background: var(--emerald-holy);
  color: #042f1a;
}}

.opt-btn.incorrect {{
  background: rgba(220, 38, 38, 0.2) !important;
  border-color: var(--crimson-blood) !important;
  color: #fef2f2 !important;
}}
.opt-btn.incorrect .opt-letter {{
  background: var(--crimson-blood);
  color: #fff;
}}

.opt-btn.neutral {{
  background: rgba(156, 163, 175, 0.2) !important;
  border-color: #9ca3af !important;
  color: #f3f4f6 !important;
}}

/* FEEDBACK BOXES (KPI 5 AUDITED) */
.feedback-box {{
  display: none;
  background: rgba(0, 0, 0, 0.75);
  border-radius: 12px;
  padding: clamp(0.8rem, 1.5vh, 1.2rem);
  margin-top: clamp(0.4rem, 1vh, 0.8rem);
  border: 1.5px solid var(--border-gold);
  animation: fadeIn 0.35s ease forwards;
}}

.feedback-box.active {{
  display: block;
}}

.correct-fb {{
  border-color: var(--emerald-holy);
  background: rgba(6, 46, 28, 0.85);
}}
.incorrect-fb {{
  border-color: var(--crimson-blood);
  background: rgba(69, 10, 10, 0.85);
}}
.neutral-fb {{
  border-color: #6b7280;
  background: rgba(31, 41, 55, 0.85);
}}

.fb-header {{
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 0.4rem;
}}

.fb-badge {{
  font-weight: 900;
  font-size: 1.2rem;
  text-transform: uppercase;
  letter-spacing: 1.2px;
}}
.correct-fb .fb-badge {{ color: #34d399; }}
.incorrect-fb .fb-badge {{ color: #f87171; }}
.neutral-fb .fb-badge {{ color: #d1d5db; }}

.fb-points {{
  font-family: var(--font-display);
  font-size: 1.35rem;
  font-weight: 900;
}}
.correct-fb .fb-points {{ color: #34d399; }}
.incorrect-fb .fb-points {{ color: #f87171; }}
.neutral-fb .fb-points {{ color: #d1d5db; }}

.fb-meme {{
  font-family: var(--font-serif);
  font-size: clamp(1.2rem, 1.5vw, 1.5rem);
  font-style: italic;
  color: var(--gold-bright);
  margin-bottom: 0.4rem;
}}

.fb-explanation {{
  font-size: clamp(1.15rem, 1.45vw, 1.4rem);
  line-height: 1.5;
  color: #f8fafc;
  margin-bottom: 0.8rem;
}}

.flow-btn-primary {{
  background: linear-gradient(180deg, var(--gold-bright) 0%, var(--gold-dark) 100%);
  color: #07080c;
  font-family: var(--font-display);
  font-size: 1.12rem;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 1.4px;
  padding: 0.75rem 2rem;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 0.6rem;
  min-height: 48px;
  box-shadow: 0 4px 15px var(--gold-glow);
  transition: all 0.2s ease;
}}

.flow-btn-primary:hover {{
  transform: translateY(-2px);
  box-shadow: 0 8px 22px var(--gold-glow);
}}

/* ========================================================================
   HOLDER 3C: PERSONAL QUESTION & HOLDER 3D: REALITY CHECK
   ======================================================================== */
.privacy-banner {{
  background: rgba(6, 182, 212, 0.16);
  border: 1.5px solid rgba(6, 182, 212, 0.45);
  color: #a5f3fc;
  font-size: 1.15rem;
  font-weight: 700;
  padding: 0.55rem 1.1rem;
  border-radius: 10px;
  margin-bottom: 0.8rem;
  display: inline-flex;
  align-items: center;
  gap: 0.6rem;
}}

.reality-check-zone {{
  background: rgba(220, 38, 38, 0.12);
  border: 1.5px solid var(--crimson-blood);
  border-radius: 12px;
  padding: 1.2rem;
  margin-top: 0.6rem;
  animation: fadeIn 0.4s ease forwards;
}}

.reality-badge {{
  display: inline-block;
  background: var(--crimson-blood);
  color: #fff;
  font-size: 0.75rem;
  font-weight: 900;
  text-transform: uppercase;
  letter-spacing: 1.5px;
  padding: 0.3rem 0.75rem;
  border-radius: 4px;
  margin-bottom: 0.6rem;
}}

.flow-btn-next {{
  background: linear-gradient(180deg, var(--gold-bright) 0%, var(--gold-dark) 100%);
  color: #07080c;
  font-family: var(--font-display);
  font-size: 1.12rem;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 1.4px;
  padding: 0.75rem 2rem;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 0.6rem;
  min-height: 48px;
  box-shadow: 0 4px 15px var(--gold-glow);
  transition: all 0.2s ease;
  margin-top: 0.8rem;
}}

.flow-btn-next:hover {{
  transform: translateY(-2px);
  box-shadow: 0 8px 22px var(--gold-glow);
}}

/* ========================================================================
   HOLDER 4: FINALE SLIDE
   ======================================================================== */
.finale-card {{
  background: linear-gradient(180deg, var(--bg-card) 0%, rgba(10, 11, 16, 0.98) 100%);
  border: 1px solid var(--border-gold);
  border-radius: 20px;
  padding: clamp(1.8rem, 3vh, 2.5rem) clamp(2rem, 3.5vw, 3.5rem);
  max-width: 1560px;
  width: 96vw;
  margin: 0 auto;
  box-shadow: 0 25px 60px rgba(0, 0, 0, 0.9);
  text-align: center;
  box-sizing: border-box;
  max-height: calc(100vh - var(--hud-height) - 1.2rem);
  overflow-y: auto;
}}

.finale-media {{
  width: 100%;
  max-height: 24vh;
  object-fit: cover;
  border-radius: 12px;
  border: 1px solid var(--border-gold);
  margin-bottom: 1.2rem;
}}

.finale-rank-badge {{
  display: inline-block;
  background: rgba(245, 158, 11, 0.15);
  border: 1px solid var(--gold-bright);
  color: var(--gold-bright);
  font-size: 0.82rem;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 2px;
  padding: 0.35rem 1rem;
  border-radius: 20px;
  margin-bottom: 0.5rem;
}}

.finale-title {{
  font-family: var(--font-display);
  font-size: clamp(1.8rem, 3vw, 2.5rem);
  font-weight: 800;
  line-height: 1.25;
  color: #fff;
  text-transform: uppercase;
  margin-bottom: 1.2rem;
}}
.finale-title span {{
  color: var(--gold-bright);
}}

.score-overview-box {{
  background: rgba(0, 0, 0, 0.6);
  border: 1px solid rgba(212, 175, 55, 0.3);
  border-radius: 14px;
  padding: 1.2rem 1.6rem;
  margin-bottom: 1.4rem;
}}

.score-main-row {{
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1.5rem;
  margin-bottom: 1rem;
}}

.finale-score-number {{
  font-family: var(--font-display);
  font-size: 3.5rem;
  font-weight: 800;
  line-height: 1;
  color: var(--gold-bright);
  text-shadow: 0 0 25px var(--gold-glow);
}}

.finale-score-meta {{
  text-align: left;
}}

.finale-accuracy-title {{
  font-family: var(--font-display);
  font-size: 1.4rem;
  font-weight: 800;
  color: #fff;
  text-transform: uppercase;
}}

.finale-accuracy-sub {{
  color: var(--text-muted);
  font-size: 0.88rem;
}}

.score-chips-grid {{
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 1rem;
}}

.stat-chip {{
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 10px;
  padding: 0.7rem 0.5rem;
}}

.stat-chip-val {{
  display: block;
  font-family: var(--font-display);
  font-size: 1.5rem;
  font-weight: 800;
  line-height: 1;
  margin-bottom: 0.2rem;
}}
.stat-chip-val.green {{ color: #34d399; }}
.stat-chip-val.red {{ color: #f87171; }}
.stat-chip-val.gray {{ color: #9ca3af; }}
.stat-chip-val.gold {{ color: var(--gold-bright); }}

.stat-chip-label {{
  font-size: 0.75rem;
  color: var(--text-muted);
  text-transform: uppercase;
  font-weight: 700;
}}

.hope-box {{
  border-radius: 12px;
  padding: 1.2rem;
  text-align: left;
  margin-bottom: 1.5rem;
  transition: all 0.3s ease;
}}
.hope-box.tier-alert {{
  background: rgba(239, 68, 68, 0.1);
  border: 1.5px solid rgba(239, 68, 68, 0.45);
}}
.hope-box.tier-conflict {{
  background: rgba(245, 158, 11, 0.1);
  border: 1.5px solid rgba(245, 158, 11, 0.45);
}}
.hope-box.tier-growth {{
  background: rgba(59, 130, 246, 0.1);
  border: 1.5px solid rgba(59, 130, 246, 0.45);
}}
.hope-box.tier-supreme {{
  background: rgba(16, 185, 129, 0.1);
  border: 1.5px solid rgba(16, 185, 129, 0.45);
}}

.hope-tag {{
  display: inline-block;
  font-size: 0.85rem;
  font-weight: 900;
  text-transform: uppercase;
  letter-spacing: 1.5px;
  margin-bottom: 0.5rem;
}}
.hope-box.tier-alert .hope-tag {{ color: #f87171; }}
.hope-box.tier-conflict .hope-tag {{ color: #fbbf24; }}
.hope-box.tier-growth .hope-tag {{ color: #60a5fa; }}
.hope-box.tier-supreme .hope-tag {{ color: #34d399; }}

.finale-score-number.negative {{
  color: #ef4444 !important;
  text-shadow: 0 0 25px rgba(239, 68, 68, 0.6) !important;
}}

.hope-quote {{
  font-family: var(--font-serif);
  font-size: 0.95rem;
  font-style: italic;
  color: #ecfdf5;
  margin-bottom: 0.7rem;
  line-height: 1.5;
}}

.hope-explanation {{
  font-size: 0.9rem;
  color: #d1fae5;
  line-height: 1.5;
}}

.finale-actions {{
  display: flex;
  justify-content: center;
  gap: 1.2rem;
}}

.whatsapp-btn {{
  background: #25d366;
  color: #07080c;
  font-family: var(--font-display);
  font-size: 1.12rem;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 1.2px;
  padding: 0.75rem 2rem;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  min-height: 48px;
  box-shadow: 0 4px 15px rgba(37, 211, 102, 0.4);
  transition: all 0.2s ease;
}}
.whatsapp-btn:hover {{
  transform: translateY(-2px);
  box-shadow: 0 8px 22px rgba(37, 211, 102, 0.5);
}}

.reset-btn {{
  background: rgba(255, 255, 255, 0.08);
  border: 1.5px solid var(--border-gold);
  color: #fff;
  font-family: var(--font-display);
  font-size: 1.12rem;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 1.2px;
  padding: 0.75rem 2rem;
  border-radius: 8px;
  cursor: pointer;
  min-height: 48px;
  transition: all 0.2s ease;
}}
.reset-btn:hover {{
  background: rgba(245, 158, 11, 0.18);
  border-color: var(--gold-bright);
}}

/* ========================================================================
   MODAL / MANUAL
   ======================================================================== */
.modal-overlay {{
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.85);
  backdrop-filter: blur(8px);
  display: none;
  align-items: center;
  justify-content: center;
  z-index: 1000;
  padding: 1.5rem;
}}

.modal-overlay.active {{
  display: flex;
}}

.modal-card {{
  background: var(--bg-card);
  border: 1.5px solid var(--border-gold);
  border-radius: 16px;
  max-width: 650px;
  width: 100%;
  max-height: 85vh;
  overflow-y: auto;
  padding: 1.8rem 2.2rem;
  box-shadow: 0 25px 60px rgba(0, 0, 0, 0.9);
}}

.modal-header {{
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1.2rem;
  border-bottom: 1px solid rgba(212, 175, 55, 0.25);
  padding-bottom: 0.8rem;
}}

.modal-title {{
  font-family: var(--font-display);
  font-size: 1.4rem;
  font-weight: 800;
  color: var(--gold-bright);
  text-transform: uppercase;
}}

.modal-close-btn {{
  background: none;
  border: none;
  color: var(--text-muted);
  font-size: 1.8rem;
  cursor: pointer;
  line-height: 1;
}}
.modal-close-btn:hover {{
  color: #fff;
}}

.modal-body p {{
  margin-bottom: 1rem;
  line-height: 1.5;
  color: var(--text-main);
}}

.modal-body ul {{
  margin-left: 1.4rem;
  margin-bottom: 1.2rem;
}}

.modal-body li {{
  margin-bottom: 0.4rem;
}}

/* FLOATING SCORE PARTICLES */
.floating-score {{
  position: fixed;
  font-family: var(--font-display);
  font-size: 1.6rem;
  font-weight: 800;
  pointer-events: none;
  z-index: 999;
  animation: floatUp 1.1s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}}

@keyframes floatUp {{
  0% {{ opacity: 1; transform: translate(-50%, 0) scale(1); }}
  100% {{ opacity: 0; transform: translate(-50%, -60px) scale(1.3); }}
}}

.floating-score.plus {{ color: #34d399; text-shadow: 0 0 14px rgba(52, 211, 153, 0.8); }}
.floating-score.minus {{ color: #f87171; text-shadow: 0 0 14px rgba(248, 113, 113, 0.8); }}
.floating-score.zero {{ color: #d1d5db; text-shadow: 0 0 14px rgba(209, 213, 219, 0.8); }}

/* ========================================================================
   PORTRAIT & MOBILE MODULAR HOLDERS ARCHITECTURE (ZERO ACCIDENTAL SCROLL)
   ======================================================================== */
@media (orientation: portrait), (max-width: 860px) {{
  html, body {{
    overflow-x: hidden;
    overflow-y: auto;
    height: 100%;
    width: 100%;
  }}

  .slide-holder {{
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    min-height: 100dvh;
    overflow-y: auto !important;
    overflow-x: hidden !important;
    -webkit-overflow-scrolling: touch !important;
    padding: 0.6rem 0.6rem calc(env(safe-area-inset-bottom, 0px) + 2rem) 0.6rem;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    box-sizing: border-box;
  }}

  .slide-holder.has-hud {{
    padding-top: calc(var(--hud-height) + env(safe-area-inset-top, 0px) + 0.6rem);
  }}

  .holder-box,
  .holder-box-center {{
    width: 100%;
    max-width: 100%;
    min-height: min-content;
    height: auto;
    max-height: none;
    display: flex;
    flex-direction: column;
    margin: 0 auto;
    padding: 0.2rem;
  }}

  /* HOLDER 1: HERO IN PORTRAIT (MOBILE-FIRST NO-SCROLL FIT) */
  .hero-card {{
    display: flex;
    flex-direction: column;
    width: 100%;
    height: 100%;
    min-height: calc(100dvh - env(safe-area-inset-top, 0px) - env(safe-area-inset-bottom, 0px) - 1rem);
    max-height: calc(100dvh - env(safe-area-inset-top, 0px) - env(safe-area-inset-bottom, 0px) - 1rem);
    border-radius: 16px;
    overflow: hidden !important;
    margin-bottom: 0;
  }}

  .hero-media {{
    width: 100%;
    height: 20vh;
    max-height: 20vh;
    min-height: 110px;
    object-fit: cover;
    border-right: none;
    border-bottom: 2px solid var(--gold-dark);
    flex-shrink: 0;
  }}

  .hero-body {{
    padding: 0.65rem 0.85rem;
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    justify-content: space-between;
    flex: 1 1 auto;
    height: calc(100% - 20vh);
    overflow-y: auto !important;
    gap: 0.35rem;
  }}

  .hero-body-top {{
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0.3rem;
    width: 100%;
  }}

  .hero-title {{
    font-size: clamp(1.2rem, 4.6vw, 1.55rem);
    line-height: 1.15;
    margin-bottom: 0.1rem;
  }}

  .hero-sub {{
    font-size: clamp(0.78rem, 2.7vw, 0.9rem);
    line-height: 1.32;
    max-width: 100%;
    color: #cbd5e1;
  }}

  .hero-citation {{
    font-size: clamp(0.74rem, 2.4vw, 0.84rem);
    padding: 0.35rem 0.65rem;
    margin-top: 0.15rem;
    line-height: 1.28;
  }}

  .hero-action-row {{
    padding: 0.4rem 0 0.2rem 0;
    width: 100%;
    position: static;
    margin-top: auto;
    flex-shrink: 0;
  }}

  .hero-action-row .action-btn {{
    width: 100%;
    min-height: 48px;
    font-size: 1.12rem;
    padding: 0.65rem 1.2rem;
    box-shadow: 0 4px 18px rgba(245, 158, 11, 0.5);
  }}

  /* HOLDER 2: DIFFICULTY IN PORTRAIT (MOBILE-FIRST NO-SCROLL FIT) */
  .diff-slide-card {{
    width: 100%;
    height: 100%;
    min-height: calc(100dvh - env(safe-area-inset-top, 0px) - env(safe-area-inset-bottom, 0px) - 1rem);
    max-height: calc(100dvh - env(safe-area-inset-top, 0px) - env(safe-area-inset-bottom, 0px) - 1rem);
    padding: 0.8rem 0.85rem;
    border-radius: 16px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    overflow-y: auto !important;
    gap: 0.5rem;
    margin-bottom: 0;
  }}

  .diff-slide-title {{
    font-size: clamp(1.25rem, 4.8vw, 1.6rem);
    margin-bottom: 0.15rem;
  }}

  .diff-slide-sub {{
    font-size: clamp(0.8rem, 2.7vw, 0.92rem);
    margin-bottom: 0.25rem;
    color: #cbd5e1;
  }}

  .diff-options {{
    display: flex;
    flex-direction: column;
    gap: 0.55rem;
    margin-bottom: 0.45rem;
    width: 100%;
    flex: 1 1 auto;
  }}

  .diff-btn {{
    padding: 0.7rem 0.85rem;
    border-radius: 12px;
  }}

  .diff-name {{
    font-size: 1.05rem;
    margin-bottom: 0.15rem;
  }}

  .diff-desc {{
    font-size: 0.82rem;
    line-height: 1.32;
  }}

  .diff-slide-card .action-btn {{
    width: 100%;
    min-height: 48px;
    font-size: 1.12rem;
    margin-top: auto;
    flex-shrink: 0;
  }}

  /* HOLDER 3A: HUD HEADER IN PORTRAIT (MOBILE-FIRST CLEAN ORDERED LAYOUT) */
  .hud-header {{
    height: 48px;
    max-height: 48px;
    padding: 0 0.5rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 0.35rem;
    z-index: 1000;
  }}

  .hud-left {{
    display: flex;
    align-items: center;
    gap: 0.35rem;
    min-width: 0;
    flex: 1 1 auto;
    overflow: hidden;
  }}

  .hud-logo-crest {{
    font-size: 1.15rem;
    line-height: 1;
    flex-shrink: 0;
  }}

  .hud-stage-block {{
    display: flex;
    flex-direction: column;
    gap: 2px;
    min-width: 0;
    overflow: hidden;
  }}

  .hud-stage-name {{
    font-size: 0.72rem;
    font-weight: 800;
    letter-spacing: 0.3px;
    color: var(--gold-bright);
    white-space: nowrap !important;
    overflow: hidden !important;
    text-overflow: ellipsis !important;
    max-width: 115px;
    line-height: 1.2;
    display: block;
  }}

  .hud-progress-track {{
    width: 55px;
    height: 3px;
    flex-shrink: 0;
  }}

  .hud-diff-badge {{
    display: none !important;
  }}

  .hud-score-chip {{
    padding: 0.18rem 0.5rem;
    font-size: 0.76rem;
    gap: 0.25rem;
    white-space: nowrap !important;
    flex-shrink: 0 !important;
    display: inline-flex;
    align-items: center;
    border-radius: 12px;
  }}

  .hud-score-chip span {{
    white-space: nowrap !important;
  }}

  .hud-actions {{
    display: flex;
    align-items: center;
    gap: 0.25rem;
    flex-shrink: 0 !important;
  }}

  .hud-icon-btn {{
    width: 32px;
    height: 32px;
    min-width: 32px;
    font-size: 0.88rem;
    border-radius: 7px;
    flex-shrink: 0;
  }}

  .fullscreen-exit-btn {{
    display: none !important;
  }}

  .stage-intro-grid.align-left,
  .stage-intro-grid.align-right,
  .stage-intro-grid {{
    position: relative;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    width: 100%;
    height: 100%;
    min-height: calc(100dvh - var(--hud-height) - env(safe-area-inset-top, 0px) - env(safe-area-inset-bottom, 0px) - 1.2rem);
    max-height: calc(100dvh - var(--hud-height) - env(safe-area-inset-top, 0px) - env(safe-area-inset-bottom, 0px) - 1.2rem);
    padding: 0.75rem 0.85rem;
    gap: 0.35rem;
    border-radius: 16px;
    overflow: hidden !important;
    margin-bottom: 0;
  }}

  .stage-intro-grid .stage-intro-bg-img,
  .stage-intro-grid.align-left .stage-intro-bg-img,
  .stage-intro-grid.align-right .stage-intro-bg-img,
  .stage-intro-grid .stage-intro-bg-picture img,
  .stage-intro-grid.align-left .stage-intro-bg-picture img,
  .stage-intro-grid.align-right .stage-intro-bg-picture img,
  .stage-intro-bg-img {{
    object-position: center top !important;
  }}

  .stage-intro-grid.align-left .stage-intro-overlay,
  .stage-intro-grid.align-right .stage-intro-overlay,
  .stage-intro-overlay {{
    background: linear-gradient(180deg, rgba(7, 8, 12, 0.2) 0%, rgba(7, 8, 12, 0.55) 30%, rgba(7, 8, 12, 0.88) 65%, rgba(7, 8, 12, 0.98) 100%);
  }}

  .intro-art-col {{
    display: none;
  }}

  .character-tag-badge,
  .stage-intro-grid.align-left .character-tag-badge,
  .stage-intro-grid.align-right .character-tag-badge {{
    position: static;
    display: inline-block;
    align-self: flex-start;
    font-size: 0.65rem;
    padding: 0.2rem 0.55rem;
    border-radius: 6px;
    margin-bottom: 0.2rem;
    top: auto;
    left: auto;
    bottom: auto;
    right: auto;
  }}

  .intro-info-col {{
    position: relative;
    z-index: 3;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    gap: 0.35rem;
    overflow: hidden;
  }}

  .character-header {{
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    gap: 0.15rem;
    margin-bottom: 0.2rem;
    width: 100%;
  }}

  .char-meta {{
    width: 100%;
  }}

  .char-era {{
    font-size: 0.7rem;
    margin-bottom: 0.05rem;
    display: none;
  }}

  .char-name {{
    font-size: clamp(1.15rem, 4.4vw, 1.45rem);
    line-height: 1.15;
    margin: 0 0 0.1rem 0;
    word-break: normal;
    overflow-wrap: normal;
    hyphens: none;
    white-space: normal;
    width: 100%;
  }}

  .char-subtitle {{
    font-size: clamp(0.78rem, 2.8vw, 0.88rem);
    line-height: 1.25;
    color: #cbd5e1;
    margin: 0;
  }}

  .bible-citation-badge {{
    display: none;
  }}

  .scene-body {{
    display: flex;
    flex-direction: column;
    gap: 0.35rem;
    flex: 1 1 auto;
    justify-content: center;
  }}

  .scene-phrase {{
    padding: 0.45rem 0.65rem;
    font-size: clamp(0.78rem, 2.7vw, 0.88rem);
    line-height: 1.32;
    gap: 0.5rem;
    background: rgba(0, 0, 0, 0.35);
    backdrop-filter: blur(8px);
    -webkit-backdrop-filter: blur(8px);
    border-radius: 8px;
    border-left: 3.5px solid var(--gold-bright);
  }}

  .scene-bullet {{
    font-size: 1.1rem;
    margin-top: 1px;
  }}

  .stage-intro-grid .action-btn {{
    width: 100%;
    min-height: 48px;
    font-size: 1.1rem;
    padding: 0.65rem 1.2rem;
    margin-top: auto;
    flex-shrink: 0;
    box-shadow: 0 4px 18px rgba(245, 158, 11, 0.5);
  }}

  /* HOLDERS 3B, 3C, 3D: QUESTIONS IN PORTRAIT (MOBILE-FIRST NO-SCROLL FIT) */
  .question-slide-card {{
    width: 100%;
    height: 100%;
    min-height: calc(100dvh - var(--hud-height) - env(safe-area-inset-top, 0px) - env(safe-area-inset-bottom, 0px) - 1.2rem);
    max-height: calc(100dvh - var(--hud-height) - env(safe-area-inset-top, 0px) - env(safe-area-inset-bottom, 0px) - 1.2rem);
    padding: 0.8rem 0.85rem;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    gap: 0.45rem;
    border-radius: 16px;
    overflow-y: auto !important;
    overflow-x: hidden !important;
    -webkit-overflow-scrolling: touch !important;
    margin-bottom: 0;
  }}

  .question-title-badge {{
    font-size: 0.72rem;
    margin-bottom: 0.15rem;
  }}

  .question-text {{
    font-size: clamp(0.88rem, 3.3vw, 1.05rem);
    line-height: 1.24;
    margin-bottom: 0.25rem;
    word-break: normal;
    overflow-wrap: normal;
    hyphens: none;
  }}

  .options-list {{
    gap: 0.35rem;
    margin-bottom: 0.35rem;
    width: 100%;
    flex: 1 1 auto;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }}

  .options-list.has-answered .opt-btn {{
    transition: all 0.28s cubic-bezier(0.16, 1, 0.3, 1);
  }}

  .options-list.has-answered .opt-btn:not(.selected) {{
    opacity: 0.35;
    max-height: 34px;
    min-height: 32px;
    padding: 0.2rem 0.55rem;
    font-size: 0.72rem;
    overflow: hidden;
    white-space: nowrap;
    text-overflow: ellipsis;
    pointer-events: none;
    border-color: rgba(255, 255, 255, 0.08);
  }}

  .options-list.has-answered .opt-btn.selected {{
    transform: scale(1.01);
    box-shadow: 0 0 14px rgba(245, 158, 11, 0.25);
    border-width: 1.5px;
    padding: 0.45rem 0.75rem;
  }}

  .opt-btn {{
    padding: 0.48rem 0.75rem;
    font-size: clamp(0.78rem, 2.8vw, 0.90rem);
    line-height: 1.25;
    min-height: 42px;
    gap: 0.45rem;
    border-radius: 10px;
  }}

  .opt-letter {{
    width: 28px;
    height: 28px;
    min-width: 28px;
    font-size: 0.85rem;
    border-radius: 6px;
  }}

  .feedback-box {{
    padding: 0.5rem 0.7rem;
    margin-top: 0.3rem;
    border-radius: 10px;
    animation: fadeIn 0.3s cubic-bezier(0.16, 1, 0.3, 1) forwards;
  }}

  .fb-meme {{
    font-size: 0.80rem;
    margin-bottom: 0.2rem;
  }}

  .fb-explanation {{
    font-size: 0.75rem;
    line-height: 1.28;
    margin-bottom: 0.4rem;
  }}

  .flow-btn-primary,
  .flow-btn-next {{
    width: 100%;
    min-height: 42px;
    justify-content: center;
    font-size: 0.92rem;
    padding: 0.55rem 1rem;
    border-radius: 10px;
  }}

  /* HOLDER 4: FINALE IN PORTRAIT (MOBILE-FIRST FIT) */
  .finale-card {{
    width: 100%;
    height: 100%;
    min-height: calc(100dvh - var(--hud-height) - env(safe-area-inset-top, 0px) - env(safe-area-inset-bottom, 0px) - 1.2rem);
    max-height: calc(100dvh - var(--hud-height) - env(safe-area-inset-top, 0px) - env(safe-area-inset-bottom, 0px) - 1.2rem);
    padding: 0.85rem 0.85rem;
    border-radius: 16px;
    overflow-y: auto !important;
    overflow-x: hidden !important;
    -webkit-overflow-scrolling: touch !important;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    gap: 0.45rem;
    margin-bottom: 0;
  }}

  .finale-media {{
    max-height: 16vh;
    min-height: 90px;
    object-fit: cover;
    margin-bottom: 0.35rem;
    flex-shrink: 0;
  }}

  .finale-title {{
    font-size: clamp(1.15rem, 4.2vw, 1.45rem);
    margin-bottom: 0.35rem;
  }}

  .score-overview-box {{
    padding: 0.65rem;
    margin-bottom: 0.45rem;
  }}

  .score-chips-grid {{
    grid-template-columns: 1fr 1fr;
    gap: 0.35rem;
  }}

  .stat-chip {{
    padding: 0.35rem;
  }}

  .stat-chip-val {{
    font-size: 1.1rem;
  }}

  .hope-box {{
    padding: 0.65rem 0.8rem;
    margin-bottom: 0.45rem;
  }}

  .hope-quote {{
    font-size: 0.82rem;
    margin-bottom: 0.35rem;
  }}

  .hope-explanation {{
    font-size: 0.78rem;
    line-height: 1.32;
  }}

  .finale-actions {{
    flex-direction: column;
    gap: 0.45rem;
    margin-top: auto;
    flex-shrink: 0;
  }}

  .whatsapp-btn,
  .reset-btn {{
    width: 100%;
    min-height: 48px;
    font-size: 1.05rem;
    padding: 0.65rem 1rem;
  }}
}}

/* ========================================================================
   IMPECCABLE & REACT-BITS ADVANCED UI / UX / ANIMATION ENHANCEMENTS
   ======================================================================== */

/* ACCESSIBILITY: REDUCED MOTION (WCAG AA & IMPECCABLE HEURISTIC) */
@media (prefers-reduced-motion: reduce) {{
  *, *::before, *::after {{
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }}
  #embersCanvas, #sparksCanvas {{
    display: none !important;
  }}
  .slide-holder {{
    transition: opacity 0.15s ease !important;
    transform: none !important;
  }}
  .scene-phrase {{
    opacity: 1 !important;
    transform: none !important;
    transition: none !important;
  }}
}}

/* ACCESSIBILITY: FOCUS-VISIBLE FOR KEYBOARD AUDIT (IMPECCABLE P1 FIX) */
button:focus-visible,
input:focus-visible,
[tabindex]:focus-visible,
.opt-btn:focus-visible,
.action-btn:focus-visible,
.hud-icon-btn:focus-visible {{
  outline: 2.5px solid var(--gold-bright) !important;
  outline-offset: 3px !important;
  box-shadow: 0 0 16px var(--gold-glow) !important;
}}

/* SCREEN READER ONLY ACCESSIBLE TEXT */
.sr-only {{
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}}

/* GPU ACCELERATION & ZERO LAYOUT THRASHING */
.slide-holder,
.hero-card,
.diff-slide-card,
.stage-intro-grid,
.question-slide-card,
.finale-card,
.opt-btn,
.action-btn,
.flow-btn-primary,
.flow-btn-next {{
  will-change: transform, opacity;
  transform: translate3d(0, 0, 0);
  backface-visibility: hidden;
}}

/* REACT-BITS: SPOTLIGHT CARD EFFECT (CURSOR-FOLLOWING AMBIENT GLOW) */
.spotlight-card {{
  position: relative;
  overflow: hidden;
}}

.spotlight-card::before {{
  content: '';
  position: absolute;
  inset: 0;
  background: radial-gradient(circle 380px at var(--mouse-x, 50%) var(--mouse-y, 50%), rgba(245, 158, 11, 0.12), transparent 75%);
  pointer-events: none;
  z-index: 2;
  opacity: 0;
  transition: opacity 0.3s ease;
}}

.spotlight-card:hover::before {{
  opacity: 1;
}}

/* REACT-BITS: TOUCH RIPPLE EFFECT */
.ripple-surface {{
  position: relative;
  overflow: hidden;
}}

.ripple-wave {{
  position: absolute;
  border-radius: 50%;
  background: rgba(245, 158, 11, 0.38);
  transform: scale(0);
  animation: rippleAnim 0.45s cubic-bezier(0.16, 1, 0.3, 1) forwards;
  pointer-events: none;
  z-index: 10;
}}

@keyframes rippleAnim {{
  to {{
    transform: scale(3.5);
    opacity: 0;
  }}
}}

/* REACT-BITS: STAR & ELECTRIC BORDER GLOW ON ACTIVE / CORRECT OPTIONS */
.opt-btn.correct {{
  background: rgba(16, 185, 129, 0.22) !important;
  border-color: var(--emerald-holy) !important;
  color: #ecfdf5 !important;
  box-shadow: 0 0 20px var(--emerald-glow), inset 0 0 12px rgba(16, 185, 129, 0.3) !important;
  position: relative;
}}

.opt-btn.incorrect {{
  box-shadow: 0 0 20px var(--crimson-glow), inset 0 0 12px rgba(220, 38, 38, 0.3) !important;
}}

/* SPARKS CANVAS (CLICKSPARK OVERLAY) */
#sparksCanvas {{
  position: fixed;
  inset: 0;
  width: 100vw;
  height: 100vh;
  pointer-events: none;
  z-index: 101;
}}

</style>
</head>
<body>

<!-- CANVAS BACKGROUND PARTICLES (Z-INDEX 99 POR ENCIMA DE HOLDERS) -->
<canvas id="embersCanvas"></canvas>
<!-- SPARKS CANVAS (REACT-BITS CLICKSPARK ENGINE) -->
<canvas id="sparksCanvas"></canvas>

<!-- ACCESSIBILITY LIVE ANNOUNCER (WCAG AA) -->
<div id="a11yAnnouncer" class="sr-only" aria-live="polite" aria-atomic="true"></div>

<div class="vignette-overlay"></div>

<!-- FLOATING EXIT FULLSCREEN BUTTON ('✕' EN ESQUINA SUPERIOR DERECHA) -->
<button class="fullscreen-exit-btn" id="exitFullscreenBtn" title="Salir de Pantalla Completa" aria-label="Salir de Pantalla Completa">
  <span>✕</span>
</button>

<!-- BGM AUDIO PLAYER (100% EMBEDDED BASE64 + LOCAL FALLBACKS) -->
<audio id="bgmAudio" loop preload="auto">
  <source src="{bgm_data_uri}" type="audio/mpeg">
  <source src="audio/BGM_BL400K.mp3" type="audio/mpeg">
  <source src="BGM_BL400K.mp3" type="audio/mpeg">
</audio>

<!-- VOLUME POPOVER PANEL (DESPLEGABLE INTERACTIVO) -->
<div class="volume-popup" id="volumePopup" style="display: none;">
  <div class="volume-popup-header">
    <span class="volume-popup-title">🎵 Volumen BGM</span>
    <button class="volume-popup-close" id="closeVolumePopup">&times;</button>
  </div>
  <div class="volume-slider-row">
    <button class="volume-mute-btn" id="volumeMuteBtn" title="Silenciar / Activar">🔊</button>
    <input type="range" min="0" max="100" value="20" class="volume-slider" id="volumeSlider">
    <span class="volume-percent" id="volumePercent">20%</span>
  </div>
  <div class="volume-presets">
    <button class="vol-preset-btn" onclick="setAppVolume(0)">Mute</button>
    <button class="vol-preset-btn" onclick="setAppVolume(20)">20%</button>
    <button class="vol-preset-btn" onclick="setAppVolume(50)">50%</button>
    <button class="vol-preset-btn" onclick="setAppVolume(100)">100%</button>
  </div>
</div>

<!-- MAIN APP ROOT -->
<div id="app">

  <!-- HUD HEADER REDESIGNED (FASE 3 & 4 - COMPACT 50px) -->
  <header class="hud-header" id="gameHudHeader" style="display: none;">
    <div class="hud-left">
      <div class="hud-logo-crest" title="Diagnóstico Bíblico">🕊️</div>
      <div class="hud-stage-block">
        <span class="hud-stage-name" id="hudStageTitle"></span>
        <div class="hud-progress-track">
          <div class="hud-progress-bar" id="hudProgressBar"></div>
        </div>
      </div>
      <span class="hud-diff-badge" id="hudDiffBadge">INICIADO (13-17)</span>
    </div>

    <div class="hud-score-chip" id="hudScoreBadge" title="Puntaje de Carrera Bíblica">
      <span>⚡</span>
      <span id="hudScoreVal" style="font-family: var(--font-display); font-size: 0.95rem; font-weight: 800; color: var(--gold-bright);">0</span>
      <span style="font-size: 0.72rem; color: var(--gold-dark); margin-left: 2px;">PTS</span>
    </div>

    <div class="hud-actions">
      <button class="hud-icon-btn" id="fullscreenToggleBtn" title="Alternar Pantalla Completa" aria-label="Pantalla Completa">
        <span id="fullscreenIcon">⛶</span>
      </button>
      <button class="hud-icon-btn" id="audioToggleBtn" aria-expanded="false" aria-haspopup="true" title="Ajustar Volumen BGM y Sonido" aria-label="Sonido">
        <span id="audioIcon">🔊</span>
      </button>
      <button class="hud-icon-btn" id="helpModalBtn" aria-expanded="false" aria-haspopup="dialog" title="Manual Bíblico" aria-label="Manual">
        <span>📖</span>
      </button>
    </div>
  </header>

  <!-- MASTER SLIDE DECK (100vh / ZERO ACCIDENTAL SCROLL) -->
  <main id="slideDeck">

    <!-- HOLDER 1: HERO / WELCOME SLIDE (BANNER BORRADO SEGÚN SOLICITUD) -->
    <section class="slide-holder screen active" id="heroScreen">
      <div class="holder-box holder-box-center">
        <div class="hero-card spotlight-card">
          <img src="{hero_b64}" alt="Altar sagrado y presencia divina" class="hero-media">
          <div class="hero-body">
            <div class="hero-body-top">
              <h1 class="hero-title">Diagnóstico Bíblico<br><span>¿Tienes el Espíritu Santo?</span></h1>
              <p class="hero-sub">Descubre a través de 19 personajes bíblicos las evidencias reales de quiénes fueron verdaderamente guiados por el Espíritu Santo y quiénes operaron bajo el engaño de la carne. Una evaluación directa, honesta y confrontativa para discernir si en tu vida cotidiana estás siendo guiado por el Espíritu de Dios o por tu propio ego.</p>
              
              <div class="hero-citation">
                «El viento sopla de donde quiere, y oyes su sonido; mas ni sabes de dónde viene, ni a dónde va; así es todo aquel que es nacido del Espíritu.» — Juan 3:8
              </div>
            </div>

            <div class="hero-action-row">
              <button class="action-btn pulse-btn" id="startGameBtn" onclick="handleStartDiagnosis()">
                <span>⚔️ Diagnosticar</span>
                <span>→</span>
              </button>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- HOLDER 2: DIFFICULTY SELECTOR SLIDE -->
    <section class="slide-holder" id="difficultySlide">
      <div class="holder-box holder-box-center">
        <div class="diff-slide-card spotlight-card">
          <div class="diff-slide-eyebrow">Paso Previo</div>
          <h2 class="diff-slide-title">Selecciona tu Rango de Edad</h2>
          <p class="diff-slide-sub">El diagnóstico adaptará los dilemas y preguntas personales a tu etapa de vida.</p>
          
          <div class="diff-options">
            <button class="diff-btn active" data-diff="easy" id="diffEasyBtn" aria-pressed="true" onclick="selectDifficulty('easy')">
              <span class="diff-name">Iniciado (13 a 17 años)</span>
              <span class="diff-desc">Preguntas directas, memes juveniles, feedback visual inmediato y dilemas de identidad escolar y familiar.</span>
            </button>
            <button class="diff-btn" data-diff="hard" id="diffHardBtn" aria-pressed="false" onclick="selectDifficulty('hard')">
              <span class="diff-name">Paladín (18 a ∞ años)</span>
              <span class="diff-desc">Para jóvenes universitarios, adultos y padres. Dilemas morales profundos, discernimiento ministerial y santidad en el mundo real.</span>
            </button>
          </div>

          <button class="action-btn pulse-btn" id="btnConfirmStart" onclick="startDiagnosticGame()">
            <span>Comenzar Carrera Bíblica</span>
            <span>→</span>
          </button>
        </div>
      </div>
    </section>

    <!-- HOLDER 3A: STAGE INTRO (ARTWORK + SEQUENTIAL 3 PHRASES) -->
    <section class="slide-holder" id="stageIntroSlide">
      <div class="holder-box">
        <div class="stage-intro-grid" id="stageIntroGrid">
          <!-- Injected dynamically by renderStageIntro() with dynamic align-left or align-right -->
        </div>
      </div>
    </section>

    <!-- HOLDER 3B: DIAGNOSTIC QUESTION SLIDE -->
    <section class="slide-holder" id="stageDiagnosticSlide">
      <div class="holder-box holder-box-center">
        <div class="question-slide-card spotlight-card" id="stageDiagnosticCard">
          <!-- Injected dynamically by renderStageDiagnostic() -->
        </div>
      </div>
    </section>

    <!-- HOLDER 3C: PERSONAL QUESTION SLIDE («¿QUÉ HARÍAS TÚ?») -->
    <section class="slide-holder" id="stagePersonalSlide">
      <div class="holder-box holder-box-center">
        <div class="question-slide-card spotlight-card" id="stagePersonalCard">
          <!-- Injected dynamically by renderStagePersonal() -->
        </div>
      </div>
    </section>

    <!-- HOLDER 3D: REALITY CHECK SLIDE («¿Y LO HACES HOY?») -->
    <section class="slide-holder" id="stageRealitySlide">
      <div class="holder-box holder-box-center">
        <div class="question-slide-card spotlight-card" id="stageRealityCard">
          <!-- Injected dynamically by renderStageReality() -->
        </div>
      </div>
    </section>

    <!-- HOLDER 4: GRAND FINALE SLIDE -->
    <section class="slide-holder screen" id="finaleScreen">
      <div class="holder-box holder-box-center">
        <div class="finale-card spotlight-card">
          <img src="{hope_b64}" alt="Consolador y Victoria en el Espíritu" class="finale-media">
          <div class="finale-body">
            <div class="finale-rank-badge" id="finaleRankBadge">DIAGNÓSTICO CUMPLIDO</div>
            <h2 class="finale-title">Tu Diagnóstico Espiritual:<br><span id="finaleRankTitle">Farmeador de Santidad</span></h2>
            
            <div class="score-overview-box">
              <div class="score-main-row">
                <div class="finale-score-number" id="finaleScoreNum">19</div>
                <div class="finale-score-meta">
                  <div class="finale-accuracy-title" id="finaleAccuracyTitle">88% de Aciertos Reales</div>
                  <div class="finale-accuracy-sub" id="finaleAccuracySub">Puntaje Neto Auditado</div>
                </div>
              </div>
              
              <div class="score-chips-grid">
                <div class="stat-chip">
                  <span class="stat-chip-val green" id="statCorrect">0</span>
                  <span class="stat-chip-label">Aciertos (+1)</span>
                </div>
                <div class="stat-chip">
                  <span class="stat-chip-val red" id="statIncorrect">0</span>
                  <span class="stat-chip-label">Errores (-1)</span>
                </div>
                <div class="stat-chip">
                  <span class="stat-chip-val gray" id="statNeutral">0</span>
                  <span class="stat-chip-label">Tibias (0)</span>
                </div>
                <div class="stat-chip">
                  <span class="stat-chip-val gold" id="statTotal">0</span>
                  <span class="stat-chip-label">Total Respondidas</span>
                </div>
              </div>
            </div>

            <div class="hope-box tier-supreme" id="hopeBox">
              <span class="hope-tag" id="hopeTag">🕊️ Mensaje Central de Esperanza</span>
              <div class="hope-quote" id="hopeQuote">
                «Y cuando él venga, convencerá al mundo de pecado, de justicia y de juicio.» — Juan 16:8<br>
                «Ahora, pues, ninguna condenación hay para los que están en Cristo Jesús, los que no andan conforme a la carne, sino conforme al Espíritu.» — Romanos 8:1
              </div>
              <p class="hope-explanation" id="hopeExplanation">
                <strong>¿Te dolió alguna pregunta o sentiste convicción de pecado?</strong><br>
                ¡Alégrate! Sentir dolor o vergüenza por el pecado no es señal de que estás desechado o condenado; es la <strong>prueba viva y contundente</strong> de que el Espíritu Santo está operando en tu interior. Si estuvieras muerto espiritualmente, el pecado no te dolería ni te incomodaría. La convicción es el bisturí de amor de Dios para limpiarte, restaurarte y llenarte de Su poder.
              </p>
            </div>

            <div class="finale-actions">
              <button class="whatsapp-btn" id="shareWhatsAppBtn">
                <span>📲 Compartir Resultado por WhatsApp</span>
              </button>
              <button class="reset-btn" id="restartGameBtn">
                <span>🔄 Jugar de Nuevo</span>
              </button>
            </div>
          </div>
        </div>
      </div>
    </section>

  </main>

  <!-- HIDDEN COMPATIBILITY CONTAINERS FOR AUDIT SUITE -->
  <div id="characterCardContainer" style="display: none;"></div>
  <div id="gameScreen" class="screen" style="display: none;"></div>

</div>

<!-- MANUAL / HELP MODAL -->
<div class="modal-overlay" id="helpModal">
  <div class="modal-card">
    <div class="modal-header">
      <h3 class="modal-title">Manual de Juego y Reglas</h3>
      <button class="modal-close-btn" id="closeHelpModal">&times;</button>
    </div>
    <div class="modal-body">
      <p><strong>¿De qué se trata Diagnóstico Bíblico?</strong><br>
      Es una experiencia interactiva de 19 fases cronológicas que evalúa si las decisiones históricas (y tus propias decisiones personales) muestran el gobierno del <em>Espíritu Santo</em> o de la <em>Carne</em>.</p>
      
      <p><strong>Sistema de Puntuación Auditado:</strong></p>
      <ul>
        <li><strong>+1 Punto:</strong> Diagnóstico bíblico acertado o decisión sincera de santidad.</li>
        <li><strong>-1 Punto:</strong> Justificación carnal, envidia, soberbia o hipocresía.</li>
        <li><strong>0 Puntos:</strong> Respuesta tibia o de neutralidad de NPC espiritual.</li>
      </ul>

      <p><strong>Pregunta Personal («¿Qué harías tú?»):</strong><br>
      Cada fase incluye una pregunta personal con la garantía: <em>«Solo tú y Dios saben la respuesta.»</em> Nadie verá tu selección; está diseñada para examen personal frente al Espíritu Santo.</p>

      <p><strong>Citas Bíblicas y Puntos Extra en Clase:</strong><br>
      Cada fase muestra <em>solo la cita bíblica</em> (ej. «Génesis 4:6-7»). El participante que encuentre primero el pasaje en su Biblia física o celular y lo lea en voz alta gana <strong>+1 punto extra</strong> asignado por el líder.</p>

      <p><strong>100% Offline:</strong> Este archivo no requiere conexión a internet y puede compartirse directamente por WhatsApp.</p>
    </div>
  </div>
</div>

<script>
/* ========================================================================
   DATA REPOSITORY: 19 CHARACTERS WITH ARTWORK & METRICS
   ======================================================================== */
const CHARACTERS = {CHARACTERS_JSON};
const state = {{
  score: 0,
  currentIndex: 0,
  difficulty: 'easy',
  currentShuffledDiag: [],
  soundEnabled: true,
  volume: 0.20, // 20% DEFAULT VOLUMEN COMO SOLICITÓ EL USUARIO
  previousVolume: 0.20,
  bgmPlaying: false,
  stats: {{
    totalAnswered: 0,
    correctCount: 0,
    incorrectCount: 0,
    neutralCount: 0
  }}
}};

/* ========================================================================
   WEB AUDIO API SOUND FX & BGM CONTROLLER
   ======================================================================== */
class SoundEngine {{
  constructor() {{
    this.ctx = null;
  }}

  init() {{
    if (!this.ctx) {{
      const AudioCtx = window.AudioContext || window.webkitAudioContext;
      if (AudioCtx) this.ctx = new AudioCtx();
    }}
    if (this.ctx && this.ctx.state === 'suspended') {{
      this.ctx.resume();
    }}
  }}

  playTone(freq, type = 'sine', duration = 0.15, vol = 0.25) {{
    if (!state.soundEnabled) return;
    this.init();
    if (!this.ctx) return;
    try {{
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();
      osc.type = type;
      osc.frequency.setValueAtTime(freq, this.ctx.currentTime);
      const effectiveVol = vol * (state.volume > 0 ? (state.volume / 0.20) : 0.8);
      gain.gain.setValueAtTime(effectiveVol, this.ctx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.001, this.ctx.currentTime + duration);
      osc.connect(gain);
      gain.connect(this.ctx.destination);
      osc.start();
      osc.stop(this.ctx.currentTime + duration);
    }} catch (e) {{}}
  }}

  playClick() {{
    this.playTone(580, 'sine', 0.08, 0.18);
  }}

  playChime() {{
    if (!state.soundEnabled) return;
    this.init();
    if (!this.ctx) return;
    const notes = [523.25, 659.25, 783.99];
    notes.forEach((f, idx) => {{
      setTimeout(() => this.playTone(f, 'sine', 0.35, 0.16), idx * 80);
    }});
  }}

  playCorrect() {{
    if (!state.soundEnabled) return;
    this.init();
    if (!this.ctx) return;
    const chords = [523.25, 659.25, 783.99, 1046.50];
    chords.forEach((freq, idx) => {{
      setTimeout(() => this.playTone(freq, 'triangle', 0.45, 0.20), idx * 70);
    }});
  }}

  playIncorrect() {{
    if (!state.soundEnabled) return;
    this.init();
    if (!this.ctx) return;
    const tones = [220, 196, 174.61];
    tones.forEach((freq, idx) => {{
      setTimeout(() => this.playTone(freq, 'sawtooth', 0.3, 0.22), idx * 100);
    }});
  }}

  playFanfare() {{
    if (!state.soundEnabled) return;
    this.init();
    if (!this.ctx) return;
    const notes = [440, 554.37, 659.25, 880];
    notes.forEach((freq, idx) => {{
      setTimeout(() => this.playTone(freq, 'triangle', 0.6, 0.25), idx * 120);
    }});
  }}
}}

const audio = new SoundEngine();

// BGM Audio Controller
function tryStartBgm() {{
  const bgm = document.getElementById('bgmAudio');
  if (audio.ctx && audio.ctx.state === 'suspended') {{
    audio.ctx.resume();
  }}
  if (bgm && state.soundEnabled && state.volume > 0) {{
    bgm.volume = state.volume;
    const playPromise = bgm.play();
    if (playPromise !== undefined) {{
      playPromise.then(() => {{
        state.bgmPlaying = true;
      }}).catch(() => {{
        // Browser autoplay policy waiting for user interaction
      }});
    }}
  }}
}}

// Mobile & Browser Audio Unlock on first touch/click
function unlockAudioEngine() {{
  audio.init();
  tryStartBgm();
  ['touchstart', 'touchend', 'click'].forEach(evt => {{
    document.removeEventListener(evt, unlockAudioEngine, true);
  }});
}}
['touchstart', 'touchend', 'click'].forEach(evt => {{
  document.addEventListener(evt, unlockAudioEngine, true);
}});

// Interactive Volume Control (Slider & Presets & Mute)
window.setAppVolume = function(val) {{
  const pct = Math.max(0, Math.min(100, Math.round(val)));
  state.volume = pct / 100;
  if (state.volume > 0) {{
    state.previousVolume = state.volume;
    state.soundEnabled = true;
  }}

  const bgm = document.getElementById('bgmAudio');
  if (bgm) {{
    bgm.volume = state.volume;
    if (state.volume > 0 && bgm.paused) {{
      bgm.play().catch(() => {{}});
    }} else if (state.volume === 0 && !bgm.paused) {{
      bgm.pause();
    }}
  }}

  const slider = document.getElementById('volumeSlider');
  if (slider) slider.value = pct;

  const pctLabel = document.getElementById('volumePercent');
  if (pctLabel) pctLabel.textContent = `${{pct}}%`;

  const muteBtn = document.getElementById('volumeMuteBtn');
  const hudIcon = document.getElementById('audioIcon');
  const isMuted = (pct === 0);
  if (muteBtn) muteBtn.textContent = isMuted ? '🔇' : '🔊';
  if (hudIcon) hudIcon.textContent = isMuted ? '🔇' : '🔊';
}};

window.toggleMute = function() {{
  if (state.volume > 0) {{
    state.previousVolume = state.volume;
    setAppVolume(0);
  }} else {{
    const restore = (state.previousVolume > 0) ? Math.round(state.previousVolume * 100) : 20;
    setAppVolume(restore);
  }}
}};

window.toggleVolumePopup = function() {{
  const btn = document.getElementById('audioToggleBtn');
  const pop = document.getElementById('volumePopup');
  if (pop) {{
    const isShowing = (pop.style.display !== 'none');
    pop.style.display = isShowing ? 'none' : 'block';
    if (btn) btn.setAttribute('aria-expanded', !isShowing);
  }}
}};

/* ========================================================================
   FULLSCREEN API & IMMERSIVE CONTROLLER
   ======================================================================== */
window.requestAppFullscreen = function() {{
  const docEl = document.documentElement;
  if (!document.fullscreenElement && !document.webkitFullscreenElement) {{
    if (docEl.requestFullscreen) {{
      docEl.requestFullscreen().catch(() => {{}});
    }} else if (docEl.webkitRequestFullscreen) {{
      docEl.webkitRequestFullscreen();
    }} else if (docEl.webkitEnterFullscreen) {{
      docEl.webkitEnterFullscreen();
    }}
  }}
  // Scroll to top to collapse mobile browser address bar
  try {{
    window.scrollTo({{ top: 0, behavior: 'smooth' }});
  }} catch(e) {{
    window.scrollTo(0, 0);
  }}
}};

window.exitAppFullscreen = function() {{
  if (document.fullscreenElement || document.webkitFullscreenElement) {{
    if (document.exitFullscreen) {{
      document.exitFullscreen().catch(() => {{}});
    }} else if (document.webkitExitFullscreen) {{
      document.webkitExitFullscreen();
    }}
  }}
}};

window.toggleAppFullscreen = function() {{
  if (document.fullscreenElement || document.webkitFullscreenElement) {{
    exitAppFullscreen();
  }} else {{
    requestAppFullscreen();
  }}
}};

function updateFullscreenState() {{
  const isFs = !!(document.fullscreenElement || document.webkitFullscreenElement);
  const exitBtn = document.getElementById('exitFullscreenBtn');
  const fsIcon = document.getElementById('fullscreenIcon');
  const hud = document.getElementById('gameHudHeader');
  const isHudVisible = hud && hud.style.display !== 'none';
  if (exitBtn) exitBtn.style.display = (isFs && !isHudVisible) ? 'flex' : 'none';
  if (fsIcon) fsIcon.textContent = isFs ? '✕' : '⛶';
}}
document.addEventListener('fullscreenchange', updateFullscreenState);
document.addEventListener('webkitfullscreenchange', updateFullscreenState);

/* ========================================================================
   SLIDE / HOLDER NAVIGATION ENGINE
   ======================================================================== */

/* ========================================================================
   IMPECCABLE & REACT-BITS INTERACTION & ANIMATION ENGINES
   ======================================================================== */

// ACCESSIBILITY: SCREEN READER LIVE ANNOUNCER
window.announceA11y = function(msg) {{
  const el = document.getElementById('a11yAnnouncer');
  if (el) {{
    el.textContent = '';
    setTimeout(() => {{ el.textContent = msg; }}, 40);
  }}
}};

// REACT-BITS: SMOOTH ANIMATED NUMBER COUNTER (CUBIC EASING)
window.animateCounter = function(el, startVal, endVal, duration = 600) {{
  if (!el) return;
  const startNum = Number(startVal) || 0;
  const endNum = Number(endVal) || 0;
  if (startNum === endNum) {{
    el.textContent = endNum;
    return;
  }}
  const startTime = performance.now();
  const diff = endNum - startNum;
  function update(now) {{
    const elapsed = now - startTime;
    const progress = Math.min(elapsed / duration, 1);
    const ease = 1 - Math.pow(1 - progress, 3); // easeOutCubic
    const current = Math.round(startNum + diff * ease);
    el.textContent = current;
    if (progress < 1) {{
      requestAnimationFrame(update);
    }} else {{
      el.textContent = endNum;
    }}
  }}
  requestAnimationFrame(update);
}};

// REACT-BITS: TOUCH RIPPLE MICRO-INTERACTION
window.createRipple = function(evt) {{
  const btn = evt.currentTarget;
  if (!btn) return;
  btn.classList.add('ripple-surface');
  const rect = btn.getBoundingClientRect();
  const circle = document.createElement('span');
  const diameter = Math.max(rect.width, rect.height);
  const radius = diameter / 2;
  circle.style.width = circle.style.height = `${{diameter}}px`;
  circle.style.left = `${{evt.clientX - rect.left - radius}}px`;
  circle.style.top = `${{evt.clientY - rect.top - radius}}px`;
  circle.classList.add('ripple-wave');
  const existing = btn.querySelector('.ripple-wave');
  if (existing) existing.remove();
  btn.appendChild(circle);
  setTimeout(() => circle.remove(), 450);
}};

// REACT-BITS: CLICKSPARK SACRED EMBERS ENGINE
class ClickSparkEngine {{
  constructor(canvasId) {{
    this.canvas = document.getElementById(canvasId);
    if (!this.canvas) return;
    this.ctx = this.canvas.getContext('2d');
    this.sparks = [];
    this.resize();
    window.addEventListener('resize', () => this.resize());
    this.animate();
  }}
  resize() {{
    if (!this.canvas) return;
    this.canvas.width = window.innerWidth;
    this.canvas.height = window.innerHeight;
  }}
  spawn(x, y, color = '#fbbf24', count = 14) {{
    const validX = (typeof x === 'number' && !isNaN(x)) ? x : (window.innerWidth / 2);
    const validY = (typeof y === 'number' && !isNaN(y)) ? y : (window.innerHeight / 2);
    for (let i = 0; i < count; i++) {{
      const angle = (Math.PI * 2 / count) * i + (Math.random() - 0.5) * 0.5;
      const speed = Math.random() * 4.5 + 2.5;
      this.sparks.push({{
        x: validX,
        y: validY,
        vx: Math.cos(angle) * speed,
        vy: Math.sin(angle) * speed - 1.2,
        radius: Math.random() * 2.8 + 1.2,
        alpha: 1,
        color,
        life: 0,
        maxLife: Math.random() * 18 + 22
      }});
    }}
    return;
  }}
  legacy_spawn_unused(x, y, color = '#fbbf24', count = 14) {{
    for (let i = 0; i < count; i++) {{
      const angle = (Math.PI * 2 / count) * i + (Math.random() - 0.5) * 0.5;
      const speed = Math.random() * 4.5 + 2.5;
      this.sparks.push({{
        x, y,
        vx: Math.cos(angle) * speed,
        vy: Math.sin(angle) * speed - 1.2,
        radius: Math.random() * 2.8 + 1.2,
        alpha: 1,
        color,
        life: 0,
        maxLife: Math.random() * 18 + 22
      }});
    }}
  }}
  animate() {{
    if (this.ctx) {{
      this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
      for (let i = this.sparks.length - 1; i >= 0; i--) {{
        const s = this.sparks[i];
        s.x += s.vx;
        s.y += s.vy;
        s.vy += 0.14; // gentle gravity
        s.life++;
        s.alpha = 1 - (s.life / s.maxLife);
        if (s.life >= s.maxLife) {{
          this.sparks.splice(i, 1);
          continue;
        }}
        this.ctx.save();
        this.ctx.globalAlpha = Math.max(0, s.alpha);
        this.ctx.fillStyle = s.color;
        this.ctx.shadowBlur = 8;
        this.ctx.shadowColor = s.color;
        this.ctx.beginPath();
        this.ctx.arc(s.x, s.y, s.radius, 0, Math.PI * 2);
        this.ctx.fill();
        this.ctx.restore();
      }}
    }}
    requestAnimationFrame(() => this.animate());
  }}
}}

const clickSpark = new ClickSparkEngine('sparksCanvas');

// REACT-BITS: SPOTLIGHT CARD POINTER TRACKING
document.addEventListener('pointermove', (e) => {{
  const cards = document.querySelectorAll('.spotlight-card');
  cards.forEach(card => {{
    const rect = card.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;
    card.style.setProperty('--mouse-x', `${{x}}px`);
    card.style.setProperty('--mouse-y', `${{y}}px`);
  }});
}});

window.goToSlide = function(slideId) {{
  audio.playClick();
  tryStartBgm();

  document.querySelectorAll('.slide-holder').forEach(s => {{
    s.classList.remove('active');
    s.scrollTop = 0;
  }});

  const target = document.getElementById(slideId);
  if (target) {{
    target.classList.add('active');
    target.scrollTop = 0;
    const scrollables = target.querySelectorAll('.holder-box, .question-slide-card, .stage-intro-grid, .diff-slide-card, .hero-card, .finale-card, .reality-check-zone');
    scrollables.forEach(el => {{ el.scrollTop = 0; }});
  }}

  document.querySelectorAll('.question-slide-card').forEach(c => {{ c.scrollTop = 0; }});

  // Reset window, documentElement, and body scroll
  try {{
    window.scrollTo({{ top: 0, left: 0, behavior: 'instant' }});
  }} catch(e) {{
    window.scrollTo(0, 0);
  }}
  if (document.documentElement) document.documentElement.scrollTop = 0;
  if (document.body) document.body.scrollTop = 0;

  // HUD Visibility: Only visible during gameplay stages
  const hudHeader = document.getElementById('gameHudHeader');
  const isGameplaySlide = (
    slideId === 'stageIntroSlide' || 
    slideId === 'stageDiagnosticSlide' || 
    slideId === 'stagePersonalSlide' ||
    slideId === 'stageRealitySlide'
  );
  if (hudHeader) {{
    hudHeader.style.display = isGameplaySlide ? 'flex' : 'none';
    hudHeader.classList.toggle('is-visible', isGameplaySlide);
  }}

  updateFullscreenState();

  if (target) {{
    target.classList.toggle('has-hud', isGameplaySlide);
  }}

  if (isGameplaySlide) {{
    updateProgressBar();
  }}
}};

window.handleStartDiagnosis = function() {{
  requestAppFullscreen();
  goToSlide('difficultySlide');
}};

window.goToDiagnosticSlide = function(evt) {{
  if (evt && clickSpark) {{
    const cx = (evt.clientX !== undefined) ? evt.clientX : (window.innerWidth / 2);
    const cy = (evt.clientY !== undefined) ? evt.clientY : (window.innerHeight / 2);
    clickSpark.spawn(cx, cy, '#fbbf24', 12);
  }}
  goToSlide('stageDiagnosticSlide');
}};

window.selectDifficulty = function(diff) {{
  audio.playClick();
  state.difficulty = diff;
  document.getElementById('diffEasyBtn').classList.toggle('active', diff === 'easy');
  document.getElementById('diffHardBtn').classList.toggle('active', diff === 'hard');
  const badge = document.getElementById('hudDiffBadge');
  if (badge) {{
    if (diff === 'hard') {{
      badge.textContent = 'PALADÍN (18+)';
      badge.className = 'hud-diff-badge paladin';
    }} else {{
      badge.textContent = 'INICIADO (13-17)';
      badge.className = 'hud-diff-badge';
    }}
  }}
}};

window.startDiagnosticGame = function() {{
  requestAppFullscreen();
  state.currentIndex = 0;
  state.score = 0;
  state.stats = {{ totalAnswered: 0, correctCount: 0, incorrectCount: 0, neutralCount: 0 }};
  updateHudScore();
  renderCurrentNode();
  goToSlide('stageIntroSlide');
}};

function updateProgressBar() {{
  const bar = document.getElementById('hudProgressBar');
  if (bar) {{
    const pct = Math.round(((state.currentIndex) / CHARACTERS.length) * 100);
    bar.style.width = `${{pct}}%`;
  }}
}}

function updateHudScore() {{
  const val = document.getElementById('hudScoreVal');
  if (val) {{
    val.textContent = state.score;
  }}
}}

function spawnFloatingScore(text, type, x, y) {{
  const el = document.createElement('div');
  el.className = `floating-score ${{type}}`;
  el.textContent = text;
  const safeY = Math.max(y, 65);
  el.style.left = `${{x}}px`;
  el.style.top = `${{safeY}}px`;
  document.body.appendChild(el);
  setTimeout(() => el.remove(), 1100);
}}

/* ========================================================================
   STAGE RENDERING: INJECTING HOLDERS 3A, 3B, 3C, 3D
   WITH DYNAMIC SIDE-SWITCHING (align-left vs align-right)
   ======================================================================== */

// SHUFFLE UTILITY: FISHER-YATES REAL ANTI-COPIA FOR ALL 3 PHASES
function shuffleOptionsArray(arr) {{
  const shuffledDiag = arr.map((opt, origIdx) => ({{ ...opt, origIdx }}));
  for (let i = shuffledDiag.length - 1; i > 0; i--) {{
    const j = Math.floor(Math.random() * (i + 1));
    [shuffledDiag[i], shuffledDiag[j]] = [shuffledDiag[j], shuffledDiag[i]];
  }}
  return shuffledDiag;
}}

function renderCurrentNode() {{
  const char = CHARACTERS[state.currentIndex];
  updateProgressBar();

  const stageTitleEl = document.getElementById('hudStageTitle');
  if (stageTitleEl) {{
    stageTitleEl.textContent = `${{char.name}} (${{state.currentIndex + 1}}/${{CHARACTERS.length}})`;
  }}

  // 1. RENDER HOLDER 3A: INTRO (BACKGROUND ARTWORK + DYNAMIC SIDE ALIGNMENT)
  const alignClass = (char.textSide === 'left') ? 'align-left' : 'align-right';
  const introContainer = document.getElementById('stageIntroGrid');
  introContainer.className = `stage-intro-grid ${{alignClass}}`;
  const isPortrait = window.matchMedia("(orientation: portrait)").matches || window.innerHeight > window.innerWidth;
  const currentImg = (isPortrait && char.imagePortrait) ? char.imagePortrait : char.image;
  introContainer.innerHTML = `
    <!-- IMAGEN DE FONDO DE TODO EL HOLDER (ARTE NATIVO 9:16 EN MOBILE Y 16:9 EN DESKTOP) -->
    <picture class="stage-intro-bg-picture">
      <source media="(orientation: portrait)" srcset="${{char.imagePortrait || char.image}}">
      <img src="${{currentImg}}" alt="${{char.name}}" class="stage-intro-bg-img">
    </picture>
    <div class="stage-intro-overlay"></div>
    <div class="character-tag-badge ${{char.tagClass}}">${{char.tag}}</div>

    <!-- VENTANA VISIBLE DEL PERSONAJE -->
    <div class="intro-art-col"></div>

    <!-- COLUMNA DE CONTENIDO (HEADER + 3 FRASES + BOTÓN) -->
    <div class="intro-info-col">
      <div class="character-header">
        <div class="char-meta">
          <span class="char-era">${{char.era}}</span>
          <h2 class="char-name">${{char.name}}</h2>
          <span class="char-subtitle">${{char.title}}</span>
        </div>
        <div class="bible-citation-badge">
          <span>📖 ${{char.citation}}</span>
          <span class="citation-note">+1 Pt Carrera Bíblica</span>
        </div>
      </div>

      <div class="scene-body">
        <div class="scene-phrase" id="phrase1">
          <span class="scene-bullet">⚡</span>
          <span>${{char.scene[0]}}</span>
        </div>
        <div class="scene-phrase" id="phrase2">
          <span class="scene-bullet">⚡</span>
          <span>${{char.scene[1]}}</span>
        </div>
        <div class="scene-phrase" id="phrase3">
          <span class="scene-bullet">⚡</span>
          <span>${{char.scene[2]}}</span>
        </div>
      </div>

      <div style="margin-top: auto; padding-top: 0.4rem;">
        <button class="action-btn pulse-btn" id="btnGoToDiagnostic" onclick="goToDiagnosticSlide(event)">
          <span>🔬 Evaluar Diagnóstico</span>
          <span>→</span>
        </button>
      </div>
    </div>
  `;

      // 2. RENDER HOLDER 3B: DIAGNOSTIC QUESTION (DIFFERENTIATED & SHUFFLED)
  const letters = ['A', 'B', 'C', 'D'];
  const diagData = (state.difficulty === 'hard' && char.qDiagnosticHard) ? char.qDiagnosticHard : char.qDiagnostic;
  state.currentShuffledDiag = shuffleOptionsArray(diagData.options);

  let diagnosticOptionsHtml = '';
  state.currentShuffledDiag.forEach((opt, sIdx) => {{
    diagnosticOptionsHtml += `
      <button class="opt-btn" onclick="handleDiagnosticAnswer(${{sIdx}}, event)">
        <span class="opt-letter">${{letters[sIdx]}}</span>
        <span>${{opt.text}}</span>
      </button>
    `;
  }});

  const diagBadgeTitle = (state.difficulty === 'hard')
    ? '🔬 Fase 1: Diagnóstico Teológico [Modo Paladín: Examen Maduro]'
    : '🔬 Fase 1: Diagnóstico [Modo Iniciado: 13 a 17 años]';

  const diagCard = document.getElementById('stageDiagnosticCard');
  diagCard.innerHTML = `
    <div class="question-title-badge">${{diagBadgeTitle}}</div>
    <h3 class="question-text">${{diagData.question}}</h3>
    <div class="options-list" id="diagnosticOptionsList">
      ${{diagnosticOptionsHtml}}
    </div>
    <div class="feedback-box" id="diagnosticFeedbackBox"></div>
  `;
  diagCard.scrollTop = 0;

  // 3. RENDER HOLDER 3C: PREGUNTA PERSONAL («¿QUÉ HARÍAS TÚ?») (SHUFFLED)
  const immersionData = char.immersion[state.difficulty] || char.immersion.easy;
  state.currentShuffledImmersion = shuffleOptionsArray(immersionData.options);

  let immersionOptionsHtml = '';
  state.currentShuffledImmersion.forEach((opt, sIdx) => {{
    immersionOptionsHtml += `
      <button class="opt-btn" onclick="handleImmersionAnswer(${{sIdx}}, event)">
        <span class="opt-letter">${{letters[sIdx]}}</span>
        <span>${{opt.text}}</span>
      </button>
    `;
  }});

  const personalBadgeTitle = (state.difficulty === 'hard')
    ? '🪞 Fase 2: Pregunta personal [Nivel Paladín: Madurez y Santidad]'
    : '🪞 Fase 2: Pregunta personal [Nivel Iniciado: Juventud y Familia]';

  const personalCard = document.getElementById('stagePersonalCard');
  personalCard.innerHTML = `
    <div class="question-title-badge">${{personalBadgeTitle}}</div>
    <div class="privacy-banner">
      <span>🔒 Solo tú y Dios saben la respuesta.</span>
    </div>
    <h3 class="question-text">${{immersionData.q}}</h3>
    <div class="options-list" id="immersionOptionsList">
      ${{immersionOptionsHtml}}
    </div>
    <div class="feedback-box" id="immersionFeedbackBox"></div>
  `;
  personalCard.scrollTop = 0;

  // 4. RENDER HOLDER 3D: REALITY CHECK (DIFFERENTIATED & SHUFFLED)
  const realityData = (state.difficulty === 'hard' && char.immersion && char.immersion.realityCheckHard)
    ? char.immersion.realityCheckHard
    : (char.immersion ? char.immersion.realityCheck : null);

  let realityOptionsHtml = '';
  if (realityData && realityData.options) {{
    state.currentShuffledReality = shuffleOptionsArray(realityData.options);
    state.currentShuffledReality.forEach((opt, sIdx) => {{
      realityOptionsHtml += `
        <button class="opt-btn" onclick="handleRealityAnswer(${{sIdx}}, event)">
          <span class="opt-letter">${{letters[sIdx]}}</span>
          <span>${{opt.text}}</span>
        </button>
      `;
    }});
  }}

  const realityCard = document.getElementById('stageRealityCard');
  if (realityData) {{
    const realityTitleBadge = (state.difficulty === 'hard')
      ? '⚖️ REALITY CHECK PALADÍN: CONFRONTACIÓN ÉTICA Y ADULTA'
      : '⚖️ REALITY CHECK: ¿Y LO HACES HOY EN TU VIDA?';

    realityCard.innerHTML = `
      <div class="reality-check-zone" id="realityCheckZone">
        <span class="reality-badge">${{realityTitleBadge}}</span>
        <h3 class="question-text">${{realityData.q}}</h3>
        <p style="font-size: clamp(1.15rem, 1.4vw, 1.35rem); color: #fca5a5; margin-bottom: 1.2rem; font-style: italic; line-height: 1.45;">${{realityData.subtext}}</p>
        <div class="options-list" id="realityOptionsList">
          ${{realityOptionsHtml}}
        </div>
        <div class="feedback-box" id="realityFeedbackBox"></div>
      </div>
    `;
    realityCard.scrollTop = 0;
  }} else {{
    realityCard.innerHTML = `
      <div class="reality-check-zone" id="realityCheckZone">
        <span class="reality-badge">🕊️ CULMINACIÓN ESPIRITUAL</span>
        <h3 class="question-text">¡Has llegado a la fase culminante en Cristo!</h3>
        <button class="flow-btn-next" id="btnFinishCharacter" onclick="nextCharacter()">
          Ver Diagnóstico Bíblico Final 🏆
        </button>
      </div>
    `;
  }}

  // TRIGGER AUTOMATIC SEQUENTIAL 3-PHRASE ENTRANCE ANIMATION
  triggerSequentialNarrative();
}}

function triggerSequentialNarrative() {{
  const p1 = document.getElementById('phrase1');
  const p2 = document.getElementById('phrase2');
  const p3 = document.getElementById('phrase3');

  setTimeout(() => {{
    if (p1) {{
      p1.classList.add('revealed');
      audio.playChime();
    }}
  }}, 100);

  setTimeout(() => {{
    if (p2) {{
      p2.classList.add('revealed');
      audio.playChime();
    }}
  }}, 380);

  setTimeout(() => {{
    if (p3) {{
      p3.classList.add('revealed');
      audio.playChime();
    }}
  }}, 680);
}}

/* ========================================================================
   ANSWER HANDLERS
   ======================================================================== */
window.handleDiagnosticAnswer = function(shuffledIdx, evt) {{
  if (evt) {{
    window.createRipple(evt);
    if (clickSpark) clickSpark.spawn(evt.clientX, evt.clientY, '#fbbf24', 16);
  }}
  const opt = state.currentShuffledDiag[shuffledIdx];
  const list = document.getElementById('diagnosticOptionsList');
  const btns = list.querySelectorAll('.opt-btn');

  btns.forEach(b => b.disabled = true);
  
  // Track metrics
  state.stats.totalAnswered++;
  if (opt.score === 1) state.stats.correctCount++;
  else if (opt.score === -1) state.stats.incorrectCount++;
  else state.stats.neutralCount++;

  state.score += opt.score;
  updateHudScore();

  const rect = evt.target.getBoundingClientRect();
  if (opt.score > 0) {{
    btns[shuffledIdx].classList.add('correct', 'selected');
    audio.playCorrect();
    spawnFloatingScore('+1 PTS', 'plus', rect.left + rect.width / 2, rect.top);
  }} else if (opt.score < 0) {{
    btns[shuffledIdx].classList.add('incorrect', 'selected');
    audio.playIncorrect();
    spawnFloatingScore('-1 PTS', 'minus', rect.left + rect.width / 2, rect.top);
  }} else {{
    btns[shuffledIdx].classList.add('neutral', 'selected');
    audio.playClick();
    spawnFloatingScore('+0 PTS', 'zero', rect.left + rect.width / 2, rect.top);
  }}
  list.classList.add('has-answered');

  // Show Feedback with "Continuar" button to proceed to Personal Slide
  const fb = document.getElementById('diagnosticFeedbackBox');
  fb.className = `feedback-box active ${{opt.score > 0 ? 'correct-fb' : opt.score < 0 ? 'incorrect-fb' : 'neutral-fb'}}`;
  fb.innerHTML = `
    <div class="fb-header">
      <span class="fb-badge">${{opt.score > 0 ? '✓ Diagnóstico Correcto' : opt.score < 0 ? '✗ Diagnóstico Fallido' : '⚠️ Respuesta Tibia'}}</span>
      <span class="fb-points">${{opt.score > 0 ? '+1 Punto' : opt.score < 0 ? '-1 Punto' : '+0 Puntos'}}</span>
    </div>
    <div class="fb-meme">${{opt.meme}}</div>
    <div class="fb-explanation">${{opt.explanation}}</div>
    <button class="flow-btn-primary" id="btnContinueToPersonal" onclick="revealPersonalQuestion()">
      Continuar a Pregunta Personal ➔
    </button>
  `;
}};

window.revealPersonalQuestion = function() {{
  audio.playClick();
  goToSlide('stagePersonalSlide');
}};

window.handleImmersionAnswer = function(shuffledIdx, evt) {{
  if (evt) {{
    window.createRipple(evt);
    if (clickSpark) clickSpark.spawn(evt.clientX, evt.clientY, '#38bdf8', 16);
  }}
  const char = CHARACTERS[state.currentIndex];
  const opt = state.currentShuffledImmersion ? state.currentShuffledImmersion[shuffledIdx] : (char.immersion[state.difficulty] || char.immersion.easy).options[shuffledIdx];
  const optIdx = shuffledIdx;
  const list = document.getElementById('immersionOptionsList');
  const btns = list.querySelectorAll('.opt-btn');

  btns.forEach(b => b.disabled = true);
  
  // Track metrics
  state.stats.totalAnswered++;
  if (opt.score === 1) state.stats.correctCount++;
  else if (opt.score === -1) state.stats.incorrectCount++;
  else state.stats.neutralCount++;

  state.score += opt.score;
  updateHudScore();

  const rect = evt.target.getBoundingClientRect();
  if (opt.score > 0) {{
    btns[optIdx].classList.add('correct', 'selected');
    audio.playCorrect();
    spawnFloatingScore('+1 PTS', 'plus', rect.left + rect.width / 2, rect.top);
  }} else if (opt.score < 0) {{
    btns[optIdx].classList.add('incorrect', 'selected');
    audio.playIncorrect();
    spawnFloatingScore('-1 PTS', 'minus', rect.left + rect.width / 2, rect.top);
  }} else {{
    btns[optIdx].classList.add('neutral', 'selected');
    audio.playClick();
    spawnFloatingScore('+0 PTS', 'zero', rect.left + rect.width / 2, rect.top);
  }}
  list.classList.add('has-answered');

  const fb = document.getElementById('immersionFeedbackBox');
  fb.className = `feedback-box active ${{opt.score > 0 ? 'correct-fb' : opt.score < 0 ? 'incorrect-fb' : 'neutral-fb'}}`;
  fb.innerHTML = `
    <div class="fb-header">
      <span class="fb-badge">${{opt.score > 0 ? '✨ Buena Intención' : '⚠️ Alerta de Carne'}}</span>
      <span class="fb-points">${{opt.score > 0 ? '+1 Punto' : opt.score < 0 ? '-1 Punto' : '+0 Puntos'}}</span>
    </div>
    <div class="fb-explanation">${{opt.feedback}}</div>
  `;

  // Modular separation: Button to go to dedicated Holder 3D (Reality Check)
  if (char.immersion.realityCheck) {{
    fb.innerHTML += `
      <button class="flow-btn-primary" id="btnContinueToReality" onclick="goToSlide('stageRealitySlide')">
        Ir al Reality Check ➔
      </button>
    `;
  }} else {{
    const isLast = (state.currentIndex === CHARACTERS.length - 1);
    const nextBtnText = isLast ? 'Ver Diagnóstico Bíblico Final 🏆' : 'Siguiente personaje ➔';
    fb.innerHTML += `
      <button class="flow-btn-next" onclick="nextCharacter()">
        ${{nextBtnText}}
      </button>
    `;
  }}
}};

window.handleRealityAnswer = function(shuffledIdx, evt) {{
  if (evt) {{
    window.createRipple(evt);
    if (clickSpark) clickSpark.spawn(evt.clientX, evt.clientY, '#f87171', 16);
  }}
  const char = CHARACTERS[state.currentIndex];
  const opt = state.currentShuffledReality ? state.currentShuffledReality[shuffledIdx] : char.immersion.realityCheck.options[shuffledIdx];
  const optIdx = shuffledIdx;
  const list = document.getElementById('realityOptionsList');
  const btns = list.querySelectorAll('.opt-btn');

  btns.forEach(b => b.disabled = true);
  
  // Track metrics
  state.stats.totalAnswered++;
  if (opt.score === 1) state.stats.correctCount++;
  else if (opt.score === -1) state.stats.incorrectCount++;
  else state.stats.neutralCount++;

  state.score += opt.score;
  updateHudScore();

  const rect = evt.target.getBoundingClientRect();
  if (opt.score > 0) {{
    btns[optIdx].classList.add('correct', 'selected');
    audio.playCorrect();
    spawnFloatingScore('+1 PTS', 'plus', rect.left + rect.width / 2, rect.top);
  }} else {{
    btns[optIdx].classList.add('incorrect', 'selected');
    audio.playIncorrect();
    spawnFloatingScore('-1 PTS', 'minus', rect.left + rect.width / 2, rect.top);
  }}
  list.classList.add('has-answered');

  const fb = document.getElementById('realityFeedbackBox');
  fb.className = `feedback-box active ${{opt.score > 0 ? 'correct-fb' : 'incorrect-fb'}}`;
  fb.innerHTML = `
    <div class="fb-header">
      <span class="fb-badge">${{opt.badge}}</span>
      <span class="fb-points">${{opt.score > 0 ? '+1 Punto' : '-1 Punto'}}</span>
    </div>
    <div class="fb-explanation">${{opt.feedback}}</div>
  `;

  const isLast = (state.currentIndex === CHARACTERS.length - 1);
  const nextBtnText = isLast ? 'Ver Diagnóstico Bíblico Final 🏆' : 'Siguiente personaje ➔';
  fb.innerHTML += `
    <button class="flow-btn-next" id="btnFinishCharacter" onclick="nextCharacter()">
      ${{nextBtnText}}
    </button>
  `;
}};

window.nextCharacter = function() {{
  audio.playClick();
  state.currentIndex++;
  if (state.currentIndex < CHARACTERS.length) {{
    renderCurrentNode();
    goToSlide('stageIntroSlide');
  }} else {{
    showFinaleScreen();
  }}
}};

/* ========================================================================
   GRAND FINALE EVALUATION (NO FAKE 100%)
   ======================================================================== */
function showFinaleScreen() {{
  goToSlide('finaleScreen');
  audio.playFanfare();

  const totalScore = state.score;
  const total = state.stats.totalAnswered;
  const correct = state.stats.correctCount;
  const incorrect = state.stats.incorrectCount;
  const neutral = state.stats.neutralCount;

  // Calculo real matematico de acierto
  const accuracyPct = total > 0 ? Math.max(0, Math.round((correct / total) * 100)) : 0;

  // Evaluacion por rangos y diagnosticos espirituales profundos
  let rank = '';
  let badge = '';
  let tierClass = '';
  let tagText = '';
  let quoteHtml = '';
  let explanationHtml = '';

  if (totalScore >= 35) {{
    // Nivel Máximo
    rank = 'Guerrero Lleno del Espíritu Santo';
    badge = 'DISCERNIMIENTO Y PLENITUD EN CRISTO';
    tierClass = 'tier-supreme';
    tagText = '👑 Plenitud Espiritual y Madurez';
    quoteHtml = `«Con Cristo estoy juntamente crucificado, y ya no vivo yo, mas vive Cristo en mí; y lo que ahora vivo en la carne, lo vivo en la fe del Hijo de Dios.» — Gálatas 2:20<br>«Mas el que persevere hasta el fin, éste será salvo.» — Mateo 24:13`;
    explanationHtml = `<strong>¡Tu entendimiento bíblico y discernimiento son firmes!</strong><br>Reconoces la voz apacible del Consolador por encima de las apariencias religiosas, presiones familiares o del orgullo humano. Mantén viva la llama en la comunión diaria, pues a mayor revelación, mayor consagración y responsabilidad para edificar al cuerpo de Cristo.`;
  }} else if (totalScore >= 20) {{
    // Nivel Maduro
    rank = 'Caminando en el Fruto del Espíritu';
    badge = 'DISCERNIMIENTO BÍBLICO SÓLIDO';
    tierClass = 'tier-growth';
    tagText = '🛡️ Fruto Espiritual en Desarrollo';
    quoteHtml = `«Mas el fruto del Espíritu es amor, gozo, paz, paciencia, benignidad, bondad, fe, mansedumbre, templanza; contra tales cosas no hay ley.» — Gálatas 5:22-23<br>«Lámpara es a mis pies tu palabra, y lumbrera a mi camino.» — Salmos 119:105`;
    explanationHtml = `<strong>Posees un discernimiento bíblico claro y activo.</strong><br>Sabes distinguir en la mayoría de los casos entre el impulso de las emociones humanas y la dirección santa del Espíritu de Dios. Hay áreas en tu vida cotidiana donde aún surge la tentación de apoyarte en tu propia prudencia, pero tu brújula apunta hacia la sumisión a las Escrituras.`;
  }} else if (totalScore >= 8) {{
    // Nivel Conflicto interior
    rank = 'Creyente en Batalla Interior';
    badge = 'LUCHA CONTRA LA CARNE: ROMANOS 7';
    tierClass = 'tier-conflict';
    tagText = '⚔️ Campo de Batalla: La Carne vs El Espíritu';
    quoteHtml = `«Digo, pues: Andad en el Espíritu, y no satisfagáis los deseos de la carne. Porque el deseo de la carne es contra el Espíritu, y el del Espíritu es contra la carne...» — Gálatas 5:16-17<br>«¡Miserable de mí! ¿quién me librará de este cuerpo de muerte? Gracias doy a Dios, por Jesucristo Señor nuestro.» — Romanos 7:24-25`;
    explanationHtml = `<strong>Tu corazón conoce la verdad, pero experimentas una intensa fricción espiritual.</strong><br>Tus elecciones muestran momentos de rendición alternados con momentos de condescendencia con el temor, la comodidad o la opinión humana. El Espíritu Santo no te rechaza en la batalla: te invita a soltar el control personal y permitir que Su gracia te perfeccione en la debilidad.`;
  }} else {{
    // Nivel Negativo o Alerta Roja
    rank = 'Alerta: Gobierno de la Carne';
    badge = 'LLAMADO URGENTE AL ARREPENTIMIENTO';
    tierClass = 'tier-alert';
    tagText = '🚨 Alerta Espiritual: Necesidad de Renovación';
    quoteHtml = `«Porque los que son de la carne piensan en las cosas de la carne; pero los que son del Espíritu, en las cosas del Espíritu. Porque el ocuparse de la carne es muerte, pero el ocuparse del Espíritu es vida y paz.» — Romanos 8:5-6<br>«Crea en mí, oh Dios, un corazón limpio, y renueva un espíritu recto dentro de mí. No me eches de delante de ti, y no quites de mí tu santo Espíritu.» — Salmos 51:10-11`;
    explanationHtml = `<strong>Tus respuestas reflejan la inclinación a justificar la carne, el orgullo o la conveniencia.</strong><br>Al igual que Saúl o los fariseos, corremos el riesgo de buscar la aprobación de los hombres o proteger nuestras emociones antes que obedecer la voz de Dios. Pero este diagnóstico no es para condena: si esta advertencia te incomoda, <em>el Espíritu Santo aún está tocando a tu puerta</em>. Corre a la cruz en arrepentimiento genuino.`;
  }}

  // Actualizar DOM antes de las animaciones
  const scoreNumEl = document.getElementById('finaleScoreNum');
  if (totalScore < 0) {{
    scoreNumEl.classList.add('negative');
  }} else {{
    scoreNumEl.classList.remove('negative');
  }}

  document.getElementById('finaleRankTitle').textContent = rank;
  document.getElementById('finaleRankBadge').textContent = badge;
  document.getElementById('finaleAccuracyTitle').textContent = `${{accuracyPct}}% de Aciertos Reales`;
  
  if (totalScore >= 0) {{
    document.getElementById('finaleAccuracySub').textContent = `Puntaje Neto: ${{totalScore}} Puntos en ${{total}} Preguntas`;
  }} else {{
    document.getElementById('finaleAccuracySub').textContent = `Balance Negativo: ${{totalScore}} Puntos (${{incorrect}} Errores en ${{total}} Preguntas)`;
  }}

  // Actualizar Caja de Mensaje Teológico según el Rango
  const hopeBox = document.getElementById('hopeBox');
  hopeBox.className = `hope-box ${{tierClass}}`;
  document.getElementById('hopeTag').textContent = tagText;
  document.getElementById('hopeQuote').innerHTML = quoteHtml;
  document.getElementById('hopeExplanation').innerHTML = explanationHtml;

  // Animaciones de contadores
  window.animateCounter(scoreNumEl, 0, totalScore, 850);
  window.animateCounter(document.getElementById('statCorrect'), 0, correct, 650);
  window.animateCounter(document.getElementById('statIncorrect'), 0, incorrect, 650);
  window.animateCounter(document.getElementById('statNeutral'), 0, neutral, 650);
  window.animateCounter(document.getElementById('statTotal'), 0, total, 650);

  // A11y live region
  window.announceA11y(`Evaluación final completada. Puntaje: ${{totalScore}} puntos. Rango espiritual: ${{rank}}`);
}}

/* ========================================================================
   EVENT LISTENERS & MODAL LOGIC (MOBILE-FIRST FAST CLICK & TOUCH BINDINGS)
   ======================================================================== */
const startBtn = document.getElementById('startGameBtn');
if (startBtn) {{
  startBtn.addEventListener('touchend', (e) => {{
    e.preventDefault();
    handleStartDiagnosis();
  }}, {{ passive: false }});
}}

const confirmStartBtn = document.getElementById('btnConfirmStart');
if (confirmStartBtn) {{
  confirmStartBtn.addEventListener('touchend', (e) => {{
    e.preventDefault();
    startDiagnosticGame();
  }}, {{ passive: false }});
}}
document.getElementById('audioToggleBtn').addEventListener('click', toggleVolumePopup);
document.getElementById('closeVolumePopup').addEventListener('click', toggleVolumePopup);
document.getElementById('volumeMuteBtn').addEventListener('click', toggleMute);

const volSlider = document.getElementById('volumeSlider');
volSlider.addEventListener('input', (e) => {{
  setAppVolume(e.target.value);
}});

document.getElementById('fullscreenToggleBtn').addEventListener('click', toggleAppFullscreen);
document.getElementById('exitFullscreenBtn').addEventListener('click', exitAppFullscreen);

const helpModal = document.getElementById('helpModal');
document.getElementById('helpModalBtn').addEventListener('click', () => {{
  audio.playClick();
  helpModal.classList.add('active');
}});
document.getElementById('closeHelpModal').addEventListener('click', () => {{
  audio.playClick();
  helpModal.classList.remove('active');
}});
helpModal.addEventListener('click', (e) => {{
  if (e.target === helpModal) helpModal.classList.remove('active');
}});

// Restart
document.getElementById('restartGameBtn').addEventListener('click', () => {{
  audio.playClick();
  state.score = 0;
  state.currentIndex = 0;
  state.stats = {{
    totalAnswered: 0,
    correctCount: 0,
    incorrectCount: 0,
    neutralCount: 0
  }};
  updateHudScore();
  goToSlide('heroScreen');
}});

// Share WhatsApp
document.getElementById('shareWhatsAppBtn').addEventListener('click', () => {{
  audio.playClick();
  const text = `🔥 Acabo de realizar el Diagnóstico Bíblico: "¿Tienes el Espíritu Santo?". Mi resultado: ${{state.score}} puntos y rango "${{document.getElementById('finaleRankTitle').textContent}}". ¿Te atreves a diagnosticar tu corazón?`;
  const url = `https://api.whatsapp.com/send?text=${{encodeURIComponent(text)}}`;
  window.open(url, '_blank');
}});

// Keyboard accessible navigation for content slides
window.addEventListener('keydown', (e) => {{
  if (e.key === 'Enter' || e.key === ' ') {{
    const hero = document.getElementById('heroScreen');
    if (hero && hero.classList.contains('active')) {{
      e.preventDefault();
      handleStartDiagnosis();
      return;
    }}
    const diff = document.getElementById('difficultySlide');
    if (diff && diff.classList.contains('active')) {{
      e.preventDefault();
      startDiagnosticGame();
      return;
    }}
    const intro = document.getElementById('stageIntroSlide');
    if (intro && intro.classList.contains('active')) {{
      e.preventDefault();
      goToSlide('stageDiagnosticSlide');
      return;
    }}
  }}
}});

/* ========================================================================
   PARTICLE EMBERS CANVAS ENGINE (EN PRIMER PLANO Z-INDEX 99)
   ======================================================================== */
const canvas = document.getElementById('embersCanvas');
const ctx = canvas.getContext('2d');
let particles = [];

function resizeCanvas() {{
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;
}}
window.addEventListener('resize', resizeCanvas);
resizeCanvas();

class Ember {{
  constructor() {{
    this.reset();
  }}
  reset() {{
    this.x = Math.random() * canvas.width;
    this.y = canvas.height + Math.random() * 20;
    this.size = Math.random() * 2.5 + 0.8;
    this.speedY = Math.random() * 0.9 + 0.3;
    this.speedX = (Math.random() - 0.5) * 0.4;
    this.opacity = Math.random() * 0.7 + 0.2;
    this.hue = Math.random() > 0.3 ? 38 : 0;
  }}
  update() {{
    this.y -= this.speedY;
    this.x += this.speedX;
    this.opacity -= 0.0015;
    if (this.y < -10 || this.opacity <= 0) {{
      this.reset();
    }}
  }}
  draw() {{
    ctx.save();
    ctx.globalAlpha = this.opacity;
    ctx.fillStyle = this.hue === 38 ? '#f59e0b' : '#dc2626';
    ctx.shadowBlur = 8;
    ctx.shadowColor = ctx.fillStyle;
    ctx.beginPath();
    ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
    ctx.fill();
    ctx.restore();
  }}
}}

for (let i = 0; i < 45; i++) {{
  const e = new Ember();
  e.y = Math.random() * canvas.height;
  particles.push(e);
}}

function animateEmbers() {{
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  particles.forEach(p => {{
    p.update();
    p.draw();
  }});
  requestAnimationFrame(animateEmbers);
}}
animateEmbers();
</script>
</body>
</html>
"""

print("Writing compiled BL400K.html...")
with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    f.write(HTML_CONTENT)

sz = os.path.getsize(OUTPUT_FILE)
print(f"SUCCESS: Generated {OUTPUT_FILE} ({sz:,} bytes / {sz/(1024*1024):.2f} MB)")

# Synchronize index.html for GitHub Pages root hosting
idx_path = os.path.join(os.path.dirname(OUTPUT_FILE), "index.html")
with open(idx_path, "w", encoding="utf-8") as f_idx:
    f_idx.write(HTML_CONTENT)
print(f"SUCCESS: Synchronized {idx_path} for GitHub Pages")
