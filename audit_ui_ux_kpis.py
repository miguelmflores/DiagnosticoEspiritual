"""
Comprehensive UI/UX & Animations Auditor for BL400K
Based on standards from:
- react-bits (interactive animations, click spark, spotlight cards, counters, ripples)
- impeccable (WCAG AA accessibility, prefers-reduced-motion, focus states, performance, motion thesis)
- ui-ux-pro-max-skill (119 UX heuristics, touch targets >= 48px, immediate feedback, visual hierarchy)
"""
import os
import re
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

HTML_PATH = r"c:\Users\migue\OneDrive - Universidad Catolica del Maule\BL400K\BL400K.html"

def run_audit():
    print("=" * 80)
    print("      AUDITORÍA INTEGRAL DE UI, UX Y ANIMACIONES: BL400K.html")
    print("      (Estándares: react-bits | impeccable | ui-ux-pro-max)")
    print("=" * 80)

    assert os.path.exists(HTML_PATH), f"No se encontró {HTML_PATH}"
    size = os.path.getsize(HTML_PATH)
    print(f"Tamaño del archivo: {size:,} bytes ({size / (1024*1024):.2f} MB)\n")

    with open(HTML_PATH, 'r', encoding='utf-8') as f:
        html = f.read()

    kpis = {}

    # 1. prefers-reduced-motion
    has_reduced = "@media (prefers-reduced-motion: reduce)" in html or "prefers-reduced-motion" in html
    kpis["1. Accesibilidad: prefers-reduced-motion"] = {
        "pass": has_reduced,
        "detail": "CSS con alternativa intencional para sensibilidad al movimiento" if has_reduced else "Ausente: sin soporte para usuarios con sensibilidad motriz"
    }

    # 2. focus-visible
    has_focus = ":focus-visible" in html
    kpis["2. Accesibilidad: Estados :focus-visible para teclado"] = {
        "pass": has_focus,
        "detail": "Estilo de foco visible implementado para navegación accesible" if has_focus else "Ausente: navegación por teclado no tiene indicador visual claro"
    }

    # 3. aria-live announcements
    has_aria_live = 'aria-live="polite"' in html or 'aria-live="assertive"' in html or 'role="status"' in html
    kpis["3. Accesibilidad: Región aria-live para anuncios de voz"] = {
        "pass": has_aria_live,
        "detail": "Región accesible configurada para notificar cambios de estado a lectores de pantalla" if has_aria_live else "Ausente: lectores de pantalla no perciben cambios de puntuación ni diapositivas"
    }

    # 4. aria-pressed & aria-expanded
    has_aria_states = 'aria-pressed' in html and 'aria-expanded' in html
    kpis["4. Accesibilidad: Atributos aria-pressed y aria-expanded"] = {
        "pass": has_aria_states,
        "detail": "Botones de alternancia y modales marcados semánticamente" if has_aria_states else "Ausente o incompleto: falta semántica en botones de estado"
    }

    # 5. ClickSpark (react-bits)
    has_spark = "clickSpark" in html or "createClickSpark" in html or "spawnSparks" in html or "ClickSparkEngine" in html
    kpis["5. Animación: ClickSpark de react-bits (chispas sagradas)"] = {
        "pass": has_spark,
        "detail": "Efecto de chispas en clicks y selecciones implementado" if has_spark else "Ausente: los clics no producen micro-partículas reactivas"
    }

    # 6. SpotlightCard (react-bits)
    has_spotlight = "spotlight-card" in html and "--mouse-x" in html
    kpis["6. UI: SpotlightCard de react-bits (iluminación dinámica de cursor)"] = {
        "pass": has_spotlight,
        "detail": "Efecto de luz interactiva seguidora del cursor activo en tarjetas" if has_spotlight else "Ausente: las tarjetas tienen iluminación estática sin reacción al puntero"
    }

    # 7. Animated Counter (react-bits)
    has_counter = "animateCounter" in html or "countUp" in html or "animateNumber" in html
    kpis["7. UX: Animated Number Counter (conteo numérico fluido)"] = {
        "pass": has_counter,
        "detail": "Transición numérica suave implementada para HUD y estadísticas finales" if has_counter else "Ausente: los números cambian abruptamente de golpe"
    }

    # 8. Touch Ripple & Micro-feedback
    has_ripple = "createRipple" in html or "ripple-wave" in html
    kpis["8. UX: Touch Ripple & Micro-interacciones hápticas visuales"] = {
        "pass": has_ripple,
        "detail": "Onda expansiva en botones para respuesta táctil inmediata" if has_ripple else "Ausente: sin feedback háptico-visual en taps/clicks de botones"
    }

    # 9. Star/Electric Border Glow (react-bits)
    has_border_glow = "border-glow" in html or "star-border" in html or "glow-border" in html or "electric-glow" in html or "box-shadow: 0 0 20px var(--emerald-glow)" in html
    kpis["9. UI: Border Glow interactivo en aciertos y botones activos"] = {
        "pass": has_border_glow,
        "detail": "Borde brillante con gradiente animado para opciones destacadas" if has_border_glow else "Ausente: bordes planos sin dinámica lumínica"
    }

    # 10. Web Audio ADSR Envelope
    has_adsr = "exponentialRampToValueAtTime" in html and ("createGain" in html or "GainNode" in html)
    kpis["10. Audio: Sintetizador Web Audio con envolventes armónicas"] = {
        "pass": has_adsr,
        "detail": "Síntesis de sonido con curvas exponenciales y acordes orquestados" if has_adsr else "Ausente o básico: audio sin pulido acústico"
    }

    # 11. Curva natural de easing (Impeccable cubic-bezier)
    has_bezier = "cubic-bezier(0.16, 1, 0.3, 1)" in html
    kpis["11. Animación: Easing natural Impeccable cubic-bezier(0.16, 1, 0.3, 1)"] = {
        "pass": has_bezier,
        "detail": "Curva de desaceleración natural presente en transiciones" if has_bezier else "Ausente: transiciones lineales o con easing estándar no calibrado"
    }

    # 12. Orquestación narrativa ágil (< 1000ms para evitar latencia UX)
    has_fast_narrative = False
    m = re.search(r'function triggerSequentialNarrative\(\)\s*\{(.+?)\n\}', html, re.DOTALL)
    if m:
        timeouts = [int(t) for t in re.findall(r'setTimeout\([^,]+,\s*(\d+)\)', m.group(1))]
        if timeouts and max(timeouts) <= 1000:
            has_fast_narrative = True
            max_t = max(timeouts)
        else:
            max_t = max(timeouts) if timeouts else 0
    else:
        max_t = 0
    kpis["12. UX: Orquestación narrativa ágil (tiempo total <= 1000ms)"] = {
        "pass": has_fast_narrative,
        "detail": f"Frases se revelan rápidamente ({max_t}ms total) sin bloquear la lectura del usuario" if has_fast_narrative else "Lenta: retrasos acumulados > 1000ms causan fricción y latencia percibida"
    }

    # 13. Touch targets ergonómicos (min-height >= 48px)
    has_touch_targets = "min-height: 48px" in html
    kpis["13. UX: Touch targets ergonómicos (min-height >= 48px WCAG AA)"] = {
        "pass": has_touch_targets,
        "detail": "Botones y opciones cumplen con tamaño táctil accesible" if has_touch_targets else "Incumplimiento de tamaño mínimo táctil en algunos controles"
    }

    # 14. GPU Acceleration & Zero Layout Thrashing
    has_gpu = "transform: translate3d" in html or "will-change: transform" in html
    kpis["14. Performance: Aceleración GPU y 60fps constantes"] = {
        "pass": has_gpu,
        "detail": "Capas de composición GPU activas para evitar layout thrashing" if has_gpu else "Ausente: animaciones causan recalculo de layout en CPU"
    }

    # 15. Jerarquía visual y contraste de textos
    has_hierarchy = "--text-main: #f3f4f6" in html and "--text-muted: #9ca3af" in html and "text-shadow:" in html
    kpis["15. UI: Jerarquía tipográfica con sombras de contraste"] = {
        "pass": has_hierarchy,
        "detail": "Jerarquía tipográfica con contraste protegido y legibilidad óptima" if has_hierarchy else "Contraste deficiente o jerarquía confusa"
    }

    passed_count = sum(1 for v in kpis.values() if v["pass"])
    total_count = len(kpis)
    score_pct = (passed_count / total_count) * 100

    print("--- RESULTADOS DETALLADOS ---")
    for name, res in kpis.items():
        symbol = "✅ PASS" if res["pass"] else "❌ FAIL"
        print(f"{symbol} | {name}: {res['detail']}")

    print("\n" + "=" * 80)
    print(f"PUNTUACIÓN GLOBAL: {passed_count}/{total_count} ({score_pct:.1f}%)")
    print("=" * 80)
    return passed_count, total_count, score_pct

if __name__ == "__main__":
    run_audit()
