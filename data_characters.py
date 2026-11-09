"""
Data repository for BL400K: 19 Characters and 21 NanoBanana Base64 artworks.
"""
import os
import json
import base64
import io
from PIL import Image

BRAIN_DIR = r"C:\Users\migue\.gemini\antigravity-ide\brain\a12232b8-9dbc-4def-85d8-8800cc7a85d5"

IMAGE_FILES = {
    "hero": "hero_cover_bl400k_1790917964562.jpg",
    "cain": "cain_wrath_1790918296039.jpg",
    "abraham_hagar": "abraham_hagar_1790918321982.jpg",
    "abraham_isaac": "abraham_isaac_1790918378734.jpg",
    "joseph": "joseph_egypt_1790918409467.jpg",
    "pharaoh": "pharaoh_hardened_1790918469972.jpg",
    "moses": "moses_sinai_1790918523265.jpg",
    "bezaleel": "bezaleel_tabernacle_1790964358281.jpg",
    "saul": "saul_tormented_1790918660569.jpg",
    "david_goliath": "david_goliath_1790918719511.jpg",
    "david_repentance": "david_repentance_1790918829673.jpg",
    "elijah": "elijah_carmel_1790918985141.jpg",
    "micaiah": "micaiah_prophet_1790964468254.jpg",
    "daniel": "daniel_lions_1790919059799.jpg",
    "john_baptist": "john_baptist_nb_1790951120756.jpg",
    "judas": "judas_nb_1790951335570.jpg",
    "peter_pentecost": "peter_pentecost_nb_1790951457646.jpg",
    "ananias_sapphira": "ananias_sapphira_nb_1790951535909.jpg",
    "stephen_paul": "stephen_paul_nb_1790951705411.jpg",
    "jesus": "jesus_anointed_1790966969526.jpg",
    "hope_finale": "hope_finale_nb_1790951801215.jpg",
}

def img_to_b64(path, max_w=900, q=80):
    img = Image.open(path)
    if img.mode != 'RGB':
        img = img.convert('RGB')
    w, h = img.size
    if w > max_w:
        new_h = int(h * (max_w / w))
        img = img.resize((max_w, new_h), Image.Resampling.LANCZOS)
    buf = io.BytesIO()
    img.save(buf, format='JPEG', quality=q, optimize=True)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode('utf-8')

# Calibration coordinates: exact pixel crop for 9:16 vertical mobile portrait
CROP_LEFTS = {
    'cain': 620,
    'abraham_hagar': 585,
    'abraham_isaac': 300,
    'joseph': 472,
    'pharaoh': 736,
    'moses': 736,
    'bezaleel': 614,
    'saul': 430,
    'david_goliath': 170,
    'david_repentance': 614,
    'elijah': 623,
    'micaiah': 283,
    'daniel': 623,
    'john_baptist': 151,
    'judas': 340,
    'peter_pentecost': 642,
    'ananias_sapphira': 330,
    'stephen_paul': 660,
    'jesus': 434,
}

def img_portrait_to_b64(path, left_px, max_w=432, q=78):
    img = Image.open(path)
    if img.mode != 'RGB':
        img = img.convert('RGB')
    w, h = img.size
    crop_w = int(h * (9 / 16))
    cropped = img.crop((left_px, 0, left_px + crop_w, h))
    if crop_w > max_w:
        new_h = int(h * (max_w / crop_w))
        cropped = cropped.resize((max_w, new_h), Image.Resampling.LANCZOS)
    buf = io.BytesIO()
    cropped.save(buf, format='JPEG', quality=q, optimize=True)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode('utf-8')

print("Loading NanoBanana artworks to Base64...")
ASSETS = {}
for key, fname in IMAGE_FILES.items():
    fpath = os.path.join(BRAIN_DIR, fname)
    if os.path.exists(fpath):
        ASSETS[key] = img_to_b64(fpath)
    else:
        raise FileNotFoundError(f"Missing {fpath}")

print("Loading dedicated 9:16 Portrait artworks to Base64...")
ASSETS_PORTRAIT = {}
for key, fname in IMAGE_FILES.items():
    if key in CROP_LEFTS:
        fpath = os.path.join(BRAIN_DIR, fname)
        ASSETS_PORTRAIT[key] = img_portrait_to_b64(fpath, CROP_LEFTS[key])

# Load the 16 characters from compile_phase2.py
with open('compile_phase2.py', 'r', encoding='utf-8') as f:
    code = f.read()

start = code.find('CHARACTERS = [')
end = code.find('def generate_html_phase2():')
char_block = code[start:end]

scope = {"ASSETS": ASSETS}
exec(char_block, scope)
p2_chars = scope["CHARACTERS"]

BEZALEEL = {
    "id": "bezaleel",
    "era": "Éxodo / Tabernáculo en el Desierto",
    "name": "Bezaleel",
    "title": "El Espíritu Santo en la Excelencia Práctica y la Creatividad",
    "citation": "Éxodo 31:1-5 y 35:30-35",
    "image": ASSETS["bezaleel"],
    "alignment": "espiritu",
    "tag": "GUIADO POR EL ESPÍRITU",
    "tagClass": "tag-green",
    "scene": [
        "Dios no solo derrama su Espíritu para profetizar o guiar ejércitos: llama a Bezaleel y lo llena del Espíritu de Dios en sabiduría, inteligencia y pericia manual.",
        "Recibe la unción celestial para labrar oro, plata, engastar piedras, tallar madera y diseñar el Arca del Pacto según el patrón exacto del cielo.",
        "Demuestra que todo talento técnico y creativo consagrado al Señor es una obra sagrada inspirada y respaldada por el Espíritu Santo."
    ],
    "qDiagnostic": {
        "question": "¿Qué revela bíblicamente que Bezaleel fuera lleno del Espíritu Santo para edificar el Tabernáculo?",
        "options": [
            {
                "text": "Revela que el Espíritu Santo capacita tanto para la adoración litúrgica como para el trabajo técnico, artístico y profesional con suprema excelencia.",
                "score": 1,
                "meme": "1000 de IQ espiritual. El Espíritu Santo no solo es para orar en lenguas, ¡también para programar, diseñar y edificar con santidad!",
                "explanation": "Éxodo 31:2-3 es la primera vez en la Biblia que se describe a alguien 'lleno del Espíritu de Dios': fue un artesano y arquitecto. Toda excelencia para Dios proviene de su Santo Espíritu."
            },
            {
                "text": "El Espíritu Santo en el Antiguo Testamento solo intervenía en milagros y batallas militares; la obra de Bezaleel fue mera habilidad técnica humana sin unción.",
                "score": -1,
                "meme": "Cringe teológico monumental. Ignorar Éxodo 31:3 es recortar las Escrituras.",
                "explanation": "Incorrecto. Éxodo 31:3 dice explícitamente: 'Lo he llenado del Espíritu de Dios, en sabiduría y en inteligencia, en ciencia y en todo arte'."
            },
            {
                "text": "Fue un nombramiento sindical honorífico de albañiles de la época sin relevancia espiritual para el creyente hoy.",
                "score": 0,
                "meme": "Análisis tibio de sociólogo secular sin discernimiento bíblico.",
                "explanation": "La construcción del Tabernáculo representaba el trono de Dios en la tierra; nada en la presencia del Señor se edifica por simple capacidad carnal."
            }
        ]
    },
    "immersion": {
        "easy": {
            "q": "POV: Te piden colaborar en el equipo de multimedia, audio, limpieza o logística del templo, pero nadie te aplaude ni te da las gracias.",
            "options": [
                { "text": "Lo hago con toda mi excelencia y oración: el Espíritu Santo guía cada cable, gráfico y detalle para la gloria de Dios.", "score": 1, "feedback": "¡Basado! Espíritu de Bezaleel: la excelencia para Dios no busca likes ni aplausos humanos.", "triggerRealityCheck": True },
                { "text": "Si no me dan el micrófono principal en el altar, que lo haga otro; mi unción es 'demasiado elevada' para limpiar o conectar cables.", "score": -1, "feedback": "Farisáico total. El ego de la carne arruina el servicio a Dios." },
                { "text": "Hago lo mínimo posible para que no me digan nada y me pongo a ver TikTok en la cabina.", "score": 0, "feedback": "Tibieza carnal. Servir al Rey de reyes merece tu 100% de dedicación." }
            ]
        },
        "hard": {
            "q": "En tu profesión, oficio o carrera secular en el mundo contemporáneo:",
            "options": [
                { "text": "Consagro mi destreza técnica, honestidad y trabajo diario como un altar gobernado por el Espíritu Santo.", "score": 1, "feedback": "Excelente discernimiento teológico: no hay división entre secular y sagrado para el creyente (Colosenses 3:23).", "triggerRealityCheck": True },
                { "text": "Separo mi fe de mi trabajo: en la oficina utilizo atajos morales y en el templo canto alabanzas.", "score": -1, "feedback": "Doble ánimo corrosivo: la carne gobernando tus horas más productivas de la semana." },
                { "text": "Trabajo mecánicamente solo por el sueldo, sin considerar que Dios es mi verdadero Señor y testigo de mi conducta.", "score": 0, "feedback": "Mentalidad mundana que apaga la influencia del Reino en la sociedad." }
            ]
        },
        "realityCheck": {
            "q": "¿Y lo estás haciendo hoy en tu día a día?",
            "subtext": "Cuando tienes una tarea escolar, universitaria o laboral que nadie supervisa a fondo... ¿la haces con excelencia para Dios o al 'ahí se va'?",
            "options": [
                { "text": "A veces la pereza me tienta, pero el Espíritu Santo me redarguye a ser diligente y le pido su gracia.", "score": 1, "badge": "CONVICCIÓN PRÁCTICA", "feedback": "¡Gloria a Dios! El fruto del Espíritu produce fidelidad en lo poco (Mateo 25:21)." },
                { "text": "Yo siempre hago todo impecable y sin fallas, no necesito mejorar en nada.", "score": -1, "badge": "ORGULLO DETECTADO", "feedback": "'El que se enaltece será humillado' (Lucas 14:11). El Espíritu Santo enseña humildad continua." }
            ]
        }
    }
}

MICAIAH = {
    "id": "micaiah",
    "era": "Monarquía Dividida / Reyes",
    "name": "Micaías hijo de Imla",
    "title": "El Espíritu de Verdad contra 400 Falsos Profetas",
    "citation": "1 Reyes 22:13-28",
    "image": ASSETS["micaiah"],
    "alignment": "espiritu",
    "tag": "GUIADO POR EL ESPÍRITU",
    "tagClass": "tag-green",
    "scene": [
        "El rey impío Acab y el rey Josafat preparan la guerra; 400 profetas asalariados prometen victoria unánime adulando los oídos de la realeza.",
        "Los emisarios presionan a Micaías: 'Todos los profetas a una voz anuncian bien al rey; que tu palabra sea como la de ellos'. Micaías responde: 'Vive Jehová, que lo que Jehová me dijere, eso hablaré'.",
        "Revela la visión del trono celestial y el juicio sobre Acab; es abofeteado por Sedequías y encarcelado a pan y agua, pero su profecía se cumple exactamente cuando Acab muere en la batalla."
    ],
    "qDiagnostic": {
        "question": "¿Qué demuestra la solitaria postura de Micaías frente al consenso de los 400 profetas de la corte?",
        "options": [
            {
                "text": "El Espíritu Santo habla la verdad inmutable de Dios sin concesiones, aun cuando contradiga a la mayoría religiosa popular y conlleve prisión y rechazo.",
                "score": 1,
                "meme": "Gigachad espiritual definitivo. 1 contra 400 respaldado por el Dios todopoderoso.",
                "explanation": "1 Reyes 22:14. La llenura del Espíritu no busca consensos políticos ni aplausos humanos, sino proclamar fielmente lo que Dios ha dicho."
            },
            {
                "text": "Micaías fue divisivo y terco; debió buscar un término medio pacífico para mantener la unidad ecuménica de Israel.",
                "score": -1,
                "meme": "Mucho cringe pastoral complaciente. La verdad del Espíritu no negocia con espíritus de mentira.",
                "explanation": "Falso. La falsa paz construida sobre la mentira es apostasía. 2 Corintios 6:14 enseña que no hay comunión entre la luz y las tinieblas."
            },
            {
                "text": "Fue un debate ordinario sobre estrategias militares sin implicación doctrinal alguna.",
                "score": 0,
                "meme": "Ceguera espiritual. Había un espíritu de engaño en boca de los 400 falsos profetas.",
                "explanation": "1 Reyes 22:21-23 revela la dimensión espiritual invisible: un espíritu de mentira operando en los profetas que no temían al Señor."
            }
        ]
    },
    "immersion": {
        "easy": {
            "q": "POV: Todo tu círculo de amigos o compañeros apoya una moda o conducta contraria a la Palabra de Dios y se burlan de ti si no participas.",
            "options": [
                { "text": "Me mantengo firme en la verdad de Dios con mansedumbre, aunque me dejen solo o me critiquen en las redes sociales.", "score": 1, "feedback": "¡Aura celestial inquebrantable! El Espíritu de Verdad mora en quienes no se doblan ante la presión social.", "triggerRealityCheck": True },
                { "text": "Cedo y hago lo mismo que el grupo para no sentirme rechazado o impopular.", "score": -1, "feedback": "Espíritu de los 400 profetas: cambiar la santidad por aceptación humana pasajera." },
                { "text": "Finjo que participo pero por dentro me justifico diciendo que 'en mi corazón sigo a Dios'.", "score": 0, "feedback": "Hipocresía que apaga el testimonio del Espíritu en tu vida." }
            ]
        },
        "hard": {
            "q": "Cuando una enseñanza o movimiento popular en el liderazgo religioso contradice las Escrituras:",
            "options": [
                { "text": "Examino todo a la luz de la Palabra y defiendo la verdad con amor, aunque pierda privilegios, contactos influyentes o reputación.", "score": 1, "feedback": "Madurez apostólica genuina: es necesario obedecer a Dios antes que a los hombres (Hechos 5:29).", "triggerRealityCheck": True },
                { "text": "Guardo silencio cómplice para proteger mi estatus ministerial y mis relaciones de conveniencia.", "score": -1, "feedback": "Peligro de Balaam y de los profetas de Acab: mercantilizar el ministerio por tranquilidad carnal." },
                { "text": "Murmuro en secreto contra los líderes pero en público finjo sumisión absoluta.", "score": 0, "feedback": "Cobardía corrosiva que daña el cuerpo de Cristo." }
            ]
        },
        "realityCheck": {
            "q": "¿Y lo estás haciendo hoy en tu día a día?",
            "subtext": "Cuando una conversación en tu círculo se convierte en chisme, burla o difamación... ¿tienes la valentía de pararla o te sumas a las risas?",
            "options": [
                { "text": "A veces la cobardía me asalta, pero reconozco que el Espíritu Santo me llama a la integridad y decido callar la burla.", "score": 1, "badge": "VALENTÍA EN EL ESPÍRITU", "feedback": "¡Aleluya! Esa convicción interna es el Espíritu Santo guiándote a ser sal y luz." },
                { "text": "Yo siempre tengo el valor perfecto y jamás tengo miedo a la opinión de nadie.", "score": -1, "badge": "AUTOENGAÑO DETECTADO", "feedback": "La carne presume autosuficiencia. El creyente maduro sabe que su fuerza proviene del Espíritu." }
            ]
        }
    }
}

JESUS = {
    "id": "jesus",
    "era": "Evangelios / Cumbre de la Salvación",
    "name": "Jesucristo: El Ungido de Dios",
    "title": "El Máximo Ejemplo, Buen Pastor y Plenitud del Espíritu Santo",
    "citation": "Lucas 4:1-14 / Isaías 61:1-2 / Hebreos 9:14",
    "image": ASSETS["jesus"],
    "alignment": "espiritu",
    "tag": "PLENITUD DEL ESPÍRITU SANTO",
    "tagClass": "tag-gold",
    "scene": [
        "Bautizado en las aguas del Jordán, el Espíritu Santo desciende en forma corporal como paloma sobre Él, y la voz del Padre declara: 'Este es mi Hijo amado, en quien tengo complacencia'.",
        "Lleno del Espíritu Santo y llevado por el Espíritu al desierto, resiste cuarenta días de ayuno y derrota a Satanás usando la espada viva de la Palabra: 'Escrito está'.",
        "Regresa en el poder del Espíritu Santo a Galilea, proclama libertad a los cautivos, da vista a los ciegos y se ofrece por el Espíritu eterno como sacrificio sin mancha para redimir a la humanidad."
    ],
    "qDiagnostic": {
        "question": "¿Por qué Jesús es el modelo supremo e insuperable de una vida gobernada por el Espíritu Santo?",
        "options": [
            {
                "text": "Porque vivió en total sumisión al Padre y en el poder del Espíritu: venció la tentación con las Escrituras, ministró en amor sacrificial y se ofreció por el Espíritu eterno para salvarnos.",
                "score": 1,
                "meme": "¡AMÉN Y AMÉN! Él es el Autor y Consumador de la fe. En Él habita corporalmente toda la plenitud de la Deidad.",
                "explanation": "Lucas 4:14 y Hebreos 9:14. Jesús no actuó en autonomía de la carne, sino que cada palabra, milagro y entrega en la cruz fue en perfecta comunión con el Espíritu Santo."
            },
            {
                "text": "Jesús no dependía del Espíritu Santo porque siendo Dios operaba con facultades mágicas automáticas sin experimentar debilidad humana real.",
                "score": -1,
                "meme": "Herejía docetista histórica. Filipenses 2:7 enseña que se despojó a sí mismo y dependió del Padre y del Espíritu.",
                "explanation": "Incorrecto. Jesús fue plenamente Dios y plenamente hombre; fue tentado en todo según nuestra semejanza pero sin pecado, dependiendo de la unción del Espíritu (Hechos 10:38)."
            },
            {
                "text": "Fue únicamente un filósofo moral inspirador similar a Sócrates o Gandhi sin trascendencia redentora sobrenatural.",
                "score": 0,
                "meme": "Error garrafal del liberalismo teológico. Jesús es el Mesías Ungido, el Salvador y único Mediador.",
                "explanation": "1 Timoteo 2:5 y Juan 14:6. Jesús no vino a dar lecciones éticas de autosuperación, sino a vencer el pecado y derramar el Espíritu Santo sobre su pueblo."
            }
        ]
    },
    "immersion": {
        "easy": {
            "q": "POV: La tentación te asedia con furia (en tu mente, celular, o en la soledad) y sientes que estás al borde de caer.",
            "options": [
                { "text": "Sigo el ejemplo de Jesús en el desierto: clamo al Espíritu Santo, me aferro a un versículo bíblico y huyo de la ocasión de pecar.", "score": 1, "feedback": "¡Victoria sobrenatural en Cristo! 'Someteos a Dios, resistid al diablo, y huirá de vosotros' (Santiago 4:7).", "triggerRealityCheck": True },
                { "text": "Confío en mi propia fuerza de voluntad diciendo 'yo lo tengo controlado', y termino tropezando otra vez.", "score": -1, "feedback": "La carne siempre fracasa. Separados de Jesús nada podéis hacer (Juan 15:5)." },
                { "text": "Pienso que es imposible resistir y me rindo de antemano.", "score": 0, "feedback": "Incredulidad carnal. El mismo Espíritu que levantó a Cristo de los muertos mora en ti (Romanos 8:11)." }
            ]
        },
        "hard": {
            "q": "Ante el sufrimiento, la incomprensión y el llamado a tomar tu cruz diariamente por causa del Reino:",
            "options": [
                { "text": "Rindo mi voluntad como Cristo en Getsemaní: 'No se haga mi voluntad, sino la tuya', fortalecido por el Consolador eterno.", "score": 1, "feedback": "La cima de la madurez espiritual: el Espíritu Santo te capacita para amar, perdonar y obedecer hasta las últimas consecuencias.", "triggerRealityCheck": True },
                { "text": "Busco un evangelio cómodo sin Getsemaní, sin renuncia y adaptado a mis conveniencias temporales.", "score": -1, "feedback": "El evangelio adulterado de la carne: pretender la resurrección sin pasar por la cruz." },
                { "text": "Me debato en amargura y resentimiento contra Dios por permitir pruebas en mi vida.", "score": 0, "feedback": "Ceguera espiritual: las pruebas producen paciencia y carácter probado por el Espíritu." }
            ]
        },
        "realityCheck": {
            "q": "¿Y lo estás haciendo hoy en tu día a día?",
            "subtext": "Al concluir este diagnóstico bíblico frente al testimonio de Jesucristo... ¿está tu corazón verdaderamente rendido a su Señorío y a la guía de su Espíritu Santo?",
            "options": [
                { "text": "Señor Jesús, reconozco mis faltas y caídas; rindo mi vida entera a Ti para que tu Santo Espíritu sea mi guía, consuelo y poder cada día.", "score": 1, "badge": "ENTREGA TOTAL A CRISTO", "feedback": "¡GLORIA A DIOS! Este es el fruto supremo de todo este diagnóstico: que Cristo sea formado en ti por el Espíritu Santo (Gálatas 4:19)." },
                { "text": "Yo ya tengo una espiritualidad perfecta y no necesito aprender ni cambiar nada.", "score": -1, "badge": "FARISÍSMO CEGADOR", "feedback": "'Si decimos que no tenemos pecado, nos engañamos a nosotros mismos' (1 Juan 1:8). El Espíritu Santo nos lleva siempre al quebrantamiento y a la cruz." }
            ]
        }
    }
}

TEXT_SIDES = {
    "cain": "left",             # User: Caín texto al lado izquierdo
    "abraham_hagar": "left",    # User: Abraham con Agar texto al lado izquierdo
    "abraham_isaac": "right",   # User: Abraham con Sara e Isaac ok (texto al lado derecho)
    "joseph": "left",           # José texto al lado izquierdo
    "pharaoh": "left",          # User: Faraón texto al lado izquierdo
    "moses": "left",            # User: Moisés texto al lado izquierdo
    "bezaleel": "left",         # User: Bezaleel texto al lado izquierdo
    "saul": "right",            # Saúl texto al lado derecho
    "david_goliath": "right",   # David texto al lado derecho
    "david_repentance": "left", # David arrepentimiento texto al lado izquierdo
    "elijah": "right",          # Elías texto al lado derecho
    "micaiah": "right",         # Micaías texto al lado derecho
    "daniel": "left",           # Daniel en el foso texto al lado izquierdo
    "john_baptist": "right",    # Juan el Bautista texto al lado derecho
    "judas": "right",           # Judas texto al lado derecho
    "peter_pentecost": "left",  # Pedro en Pentecostés texto al lado izquierdo
    "ananias_sapphira": "right",# Ananías y Safira texto al lado derecho
    "stephen_paul": "left",     # Esteban y Pablo texto al lado izquierdo
    "jesus": "right"            # Jesucristo texto al lado derecho
}

PORTRAIT_POSITIONS = {
    "cain": "68% 22%",             # Caín de rodillas con ira ante el altar
    "abraham_hagar": "62% 20%",    # Abraham y Agar en aflicción en la tienda
    "abraham_isaac": "32% 18%",    # Abraham ante el altar con el carnero y la luz
    "joseph": "50% 18%",           # José con resplandor en el palacio egipcio
    "pharaoh": "78% 18%",          # Faraón en su trono de piedra y el Nilo de sangre
    "moses": "78% 20%",            # Moisés descendiendo de Sinaí con las tablas
    "bezaleel": "65% 20%",         # Bezaleel tallando el Arca del Pacto
    "saul": "46% 18%",             # Saúl atormentado en su trono con corona
    "david_goliath": "18% 18%",    # David con la honda resplandeciente
    "david_repentance": "65% 25%", # David llorando postrado ante su corona
    "elijah": "66% 22%",           # Elías con brazos en alto y el fuego del cielo
    "micaiah": "30% 20%",          # Micaías encadenado con la visión celestial arriba
    "daniel": "66% 22%",           # Daniel orando con el ángel resplandeciente
    "john_baptist": "16% 18%",     # Juan el Bautista predicando en la roca
    "judas": "36% 18%",            # Judas en Getsemaní con la bolsa de plata
    "peter_pentecost": "68% 18%",  # Pedro en Pentecostés con la llama sobre su cabeza
    "ananias_sapphira": "35% 25%", # Ananías cayendo fulminado con las monedas
    "stephen_paul": "70% 20%",     # Esteban apedreado mirando al cielo abierto
    "jesus": "46% 18%",            # Jesucristo con brazos abiertos y la paloma santa
}

CHARACTERS = []
for c in p2_chars:
    c["textSide"] = TEXT_SIDES.get(c["id"], "right")
    c["portraitPos"] = PORTRAIT_POSITIONS.get(c["id"], "50% 20%")
    c["imagePortrait"] = ASSETS_PORTRAIT.get(c["id"], c["image"])
    CHARACTERS.append(c)
    if c["id"] == "moses":
        BEZALEEL["textSide"] = TEXT_SIDES.get("bezaleel", "left")
        BEZALEEL["portraitPos"] = PORTRAIT_POSITIONS.get("bezaleel", "65% 20%")
        BEZALEEL["imagePortrait"] = ASSETS_PORTRAIT.get("bezaleel", BEZALEEL["image"])
        CHARACTERS.append(BEZALEEL)
    elif c["id"] == "elijah":
        MICAIAH["textSide"] = TEXT_SIDES.get("micaiah", "right")
        MICAIAH["portraitPos"] = PORTRAIT_POSITIONS.get("micaiah", "30% 20%")
        MICAIAH["imagePortrait"] = ASSETS_PORTRAIT.get("micaiah", MICAIAH["image"])
        CHARACTERS.append(MICAIAH)

JESUS["textSide"] = TEXT_SIDES.get("jesus", "right")
JESUS["portraitPos"] = PORTRAIT_POSITIONS.get("jesus", "46% 18%")
JESUS["imagePortrait"] = ASSETS_PORTRAIT.get("jesus", JESUS["image"])
CHARACTERS.append(JESUS)
print(f"Total characters ready: {len(CHARACTERS)}")



# -------------------------------------------------------------------------
# PALADIN MODE DEEP THEOLOGICAL DILEMMAS & ADULT REALITY CHECKS (18+)
# -------------------------------------------------------------------------
PALADIN_DATA = {'cain': {'qDiagnosticHard': {'question': '¿Cuál es la raíz teológica por la cual Dios rechazó la ofrenda de Caín y su posterior reacción?', 'options': [{'text': 'La ofrenda de Caín carecía de fe y reverencia espiritual (Hebreos 11:4); su corazón operaba en autosuficiencia carnal y rechazó airadamente la advertencia redentora de Dios.', 'score': 1, 'meme': 'Discernimiento supremo. La religión de la carne intenta comprar a Dios sin rendir el corazón.', 'explanation': 'Exacto. Génesis 4:5-7 y 1 Juan 3:12 revelan que las obras de Caín eran malas porque nacían de un espíritu autosuficiente que no tolera la corrección del Espíritu Santo.'}, {'text': 'Dios rechazó su ofrenda porque Caín era agricultor y no pastor, careciendo de corderos para una expiación ceremonial estricta.', 'score': -1, 'meme': 'Trampa legalista. Dios acepta frutos de la tierra (Levítico 2); el problema era el corazón de Caín.', 'explanation': 'Falso. La ley mosaica incluía ofrendas de grano. Dios mira primero al oferente y luego a la ofrenda (Génesis 4:4).'}, {'text': 'Caín tenía buena intención inicial, pero la presión de la herencia adámica lo obligó a matar sin tener libre albedrío.', 'score': -1, 'meme': "Error fatalista. Dios le dijo explícitamente: 'el pecado está a la puerta... pero tú te enseñorearás de él'.", 'explanation': 'Dios advirtió a Caín que podía gobernar sobre el pecado mediante la sumisión a Él, pero Caín prefirió dar rienda suelta a la carne.'}, {'text': 'Fue una desavenencia civil entre hermanos que no guarda relación con la doctrina de la pneumatología ni la santidad.', 'score': 0, 'meme': 'Ceguera espiritual. Toda la Escritura usa a Caín como el arquetipo del hombre no regenerado.', 'explanation': "Judas 1:11 condena 'el camino de Caín' como la senda de rebelión contra el gobierno del Espíritu."}]}, 'realityCheckHard': {'q': '¿Cómo reaccionas cuando Dios bendice o promueve a un hermano o colega que tú consideras menos calificado que tú?', 'subtext': 'Frente al éxito visible de otro en el ministerio, empresa o familia... ¿qué fruto brota en el silencio de tu mente?', 'options': [{'text': 'Me humillo ante Dios, renuncio a toda envidia oculta y oro con alegría por el respaldo divino sobre mi hermano.', 'score': 1, 'badge': 'CORAZÓN CRUCIFICADO', 'feedback': 'Victoria en el Espíritu. Solo quien tiene la plenitud de Dios se alegra genuinamente en el fruto ajeno.'}, {'text': 'Finjo felicitaciones en público pero en privado resalto sutilmente sus defectos para restarle mérito ante los demás.', 'score': -1, 'badge': 'VENENO DE CAÍN', 'feedback': 'Peligro mortal: la murmuración y el menosprecio son el cuchillo espiritual de Caín desangrando al hermano.'}, {'text': "Me resiento, me repliego en amargura y reduzco mi servicio alegando que 'el liderazgo no tiene discernimiento'.", 'score': -1, 'badge': 'EGO HERIDO', 'feedback': 'La carne buscando victimizarse antes que reconocer su necesidad urgente de arrepentimiento.'}]}}, 'abraham_hagar': {'qDiagnosticHard': {'question': '¿Qué distinción espiritual establece Gálatas 4 entre engendrar con Agar y esperar en la promesa?', 'options': [{'text': 'Agar representa el pacto de la carne intentando ayudar a Dios mediante obras humanas; engendra esclavitud espiritual y rivalidad con el Espíritu.', 'score': 1, 'meme': 'Teología pura de Pablo. El esfuerzo carnal jamás consuma las promesas de la gracia.', 'explanation': 'Gálatas 4:22-29 contrasta al nacido según la carne (Ismael) con el nacido según el Espíritu (Isaac). El apuro humano produce persecución interna.'}, {'text': 'Fue un acto de fe práctica y obediencia pragmática considerando que la promesa divina exigía intervención biológica inmediata.', 'score': -1, 'meme': 'Confundir pragmatismo con fe. La fe verdadera sabe esperar el tiempo de Dios.', 'explanation': 'Abraham no consultó al Señor ni esperó en el Espíritu; escuchó la voz del temor y la desesperación humana.'}, {'text': 'Dios ordenó explícitamente a Abraham tomar a Agar para demostrar la complejidad de los pactos patriarcales.', 'score': -1, 'meme': 'Falsificación bíblica. Dios jamás ordenó el concubinato con Agar; fue sugerencia de Sara en su crisis de fe.', 'explanation': 'Génesis 16:2 muestra que fue Sara quien propuso la idea y Abraham consintió según el razonamiento de la carne.'}, {'text': 'Un error cultural de la época sin ninguna trascendencia teológica para el creyente bajo el Nuevo Pacto.', 'score': 0, 'meme': 'Análisis superficial. Ignora que Pablo dedica un capítulo entero a este evento en Gálatas.', 'explanation': "Todo creyente corre el riesgo de engendrar 'Ismaeles' ministeriales cuando abandona la dependencia del Consolador."}]}, 'realityCheckHard': {'q': 'Ante la aparente demora de una respuesta divina en tu ministerio, finanzas o matrimonio:', 'subtext': "¿Has tomado atajos éticos, deudas imprudentes o manipulaciones emocionales para 'ayudar a Dios'?", 'options': [{'text': "Confieso que he sentido la tentación de forzar puertas, pero renuncio a 'engendrar Ismaeles' y descanso en la soberanía de Dios.", 'score': 1, 'badge': 'PACIENCIA DEL ESPÍRITU', 'feedback': 'La paciencia (fruto del Espíritu) es la prueba de fuego de quien no confía en su propia fuerza.'}, {'text': "Utilizo presiones, omisiones convenientes o deudas diciendo: 'Dios bendecirá el fin aunque el medio sea dudoso'.", 'score': -1, 'badge': 'ATRAPADO EN EL VALLE DE AGAR', 'feedback': 'Alerta solemne: lo que se engendra en la carne traerá conflicto continuo a tu casa espiritual.'}]}}, 'abraham_isaac': {'qDiagnosticHard': {'question': '¿Por qué la disposición de Abraham de entregar a Isaac en el Monte Moriah es la cima de la fe pneumatológica?', 'options': [{'text': 'Porque Abraham rindió la promesa misma al Prometedor, confiando en que el Espíritu de Dios tenía poder aun para resucitarlo de los muertos (Hebreos 11:19).', 'score': 1, 'meme': 'Comprensión apostólica perfecta. Moriah es la sombra profética del Calvario.', 'explanation': 'Abraham no amó la bendición por encima del Bendecidor. Su fe fue perfeccionada en la rendición incondicional.'}, {'text': 'Porque Abraham sabía de antemano que Dios enviaría un carnero, por lo que nunca hubo un riesgo ni dolor real.', 'score': -1, 'meme': 'Teología barata. Abraham subió con el cuchillo en mano dispuesto a obedecer hasta el fin.', 'explanation': 'Génesis 22 y Santiago 2:21 muestran que la fe de Abraham se demostró en el acto real de ofrecer a su hijo amado.'}, {'text': 'Demuestra que la relación con Dios es un contrato transaccional donde se intercambian sacrificios extremos por favores celestiales.', 'score': -1, 'meme': 'Paganismo encubierto. Dios no negocia favores; prueba y purifica la fidelidad del corazón.', 'explanation': 'Dios detesta los sacrificios paganos; la prueba de Abraham reveló que su tesoro supremo era Dios mismo.'}, {'text': 'Fue un relato mitológico para justificar el rechazo del sacrificio infantil en el culto semítico antiguo.', 'score': 0, 'meme': "Racionalismo sin fe. Cristo mismo testificó: 'Abraham se gozó de que había de ver mi día; y lo vio, y se gozó'.", 'explanation': 'En Moriah, Abraham vio la provisión sustitutoria del Cordero de Dios que quita el pecado del mundo.'}]}, 'realityCheckHard': {'q': 'Si el Espíritu Santo te pide hoy soltar aquello que se ha convertido en tu mayor ídolo funcional:', 'subtext': 'Tu reputación profesional, una relación no alineada a Dios, el control sobre tus hijos o tu seguridad económica...', 'options': [{'text': 'Subo a mi Moriah personal: declaro que Cristo es superior a cualquier tesoro y pongo mi ídolo en el altar.', 'score': 1, 'badge': 'RENDICIÓN TOTAL', 'feedback': 'El Espíritu Santo desciende con fuego purificador sobre los altares donde nada se reserva.'}, {'text': 'Le entrego a Dios mis sobras de tiempo y dinero, pero aquello que sostiene mi ego es intocable.', 'score': -1, 'badge': 'IDOLATRÍA RELIGIOSA', 'feedback': "'El que ama padre o madre más que a mí, no es digno de mí' (Mateo 10:37). La carne siempre busca conservar a su Isaac."}]}}, 'joseph': {'qDiagnosticHard': {'question': '¿Qué capacitó a José para rechazar el pecado sexual con la mujer de Potifar y perdonar a sus hermanos?', 'options': [{'text': 'La presencia moradora del Espíritu Santo, que produjo en él un temor reverente a Dios por encima del placer temporal y una perspectiva de redención sobre el agravio.', 'score': 1, 'meme': "Génesis 41:38 confirmado por Faraón: '¿Acaso hallaremos a otro hombre como este, en quien esté el espíritu de Dios?'", 'explanation': "José no dijo '¿cómo pecaré contra mi jefe?', sino '¿cómo haría yo este gran mal, y pecaría contra Dios?'. Su pureza y perdón emanaban de la presencia divina."}, {'text': 'Su rígido código moral egipcio y el miedo a ser decapitado si Potifar descubría la infidelidad.', 'score': -1, 'meme': "Miopía bíblica. El texto bíblico enfatiza repetidamente que 'Jehová estaba con José'.", 'explanation': 'El temor humano no produce santidad secreta ni perdón hacia verdugos; solo la unción de Dios transforma el alma.'}, {'text': 'Una fría estrategia política para ganar simpatía y eventualmente ascender al trono de Egipto.', 'score': -1, 'meme': 'Cinismo secular. José pasó años en el calabozo sin perder su integridad ni su fe en Dios.', 'explanation': 'José rechazó la tentación perdiendo su manto y su libertad; el costo de la santidad fue la cárcel, no el ascenso inmediato.'}, {'text': 'La mujer de Potifar no era atractiva, por lo que no existió una tentación real en sus años de juventud.', 'score': 0, 'meme': 'Minimizar la lucha contra el pecado es ceguera espiritual total.', 'explanation': "Génesis 39:10 dice que ella le insistía 'día tras día'; la victoria de José fue fruto de una comunión inquebrantable con Dios."}]}, 'realityCheckHard': {'q': 'En la oscuridad de tu habitación, cuando nadie te ve, o frente a la pantalla de tu ordenador o teléfono:', 'subtext': '¿Gobierna en tu mirada el temor santo de Dios o consientes pensamientos y consumos que apagan al Espíritu Santo?', 'options': [{'text': 'Huyo de la tentación como José: cuido mis ojos y rindo cuentas en santidad ante el Dios que todo lo escudriña.', 'score': 1, 'badge': 'SANTIDAD EN LO SECRETO', 'feedback': 'Bienaventurados los de limpio corazón, porque ellos verán a Dios. Esa victoria invisible es la gloria del Espíritu.'}, {'text': 'Mantengo una fachada irreprochable en la congregación mientras mantengo hábitos secretos de inmoralidad.', 'score': -1, 'badge': 'HIPOCRESÍA EN TINIEBLAS', 'feedback': "'No os engañéis; Dios no puede ser burlado' (Gálatas 6:7). Necesitas confesar y cortar hoy mismo."}]}}, 'pharaoh': {'qDiagnosticHard': {'question': '¿Cuál es la lección teológica fundamental sobre la interacción entre la soberanía divina y la obstinación de Faraón?', 'options': [{'text': 'Faraón endureció reiteradamente su corazón contra la revelación de Dios; consecuentemente, el juicio divino lo confirmó en su propia soberbia para manifestar la gloria del Señor.', 'score': 1, 'meme': 'Romanos 9:17 en su máxima expresión. El mismo sol que derrite la cera, endurece el barro obstinado.', 'explanation': 'Éxodo muestra que Faraón endureció su corazón primero (Éxodo 7:13, 8:15). Quien resiste persistentemente la voz del Espíritu queda cautivo en su propia dureza.'}, {'text': 'Faraón era un hombre noble que deseaba liberar a Israel, pero Dios lo obligó mágicamente a actuar con crueldad contra su voluntad.', 'score': -1, 'meme': 'Deformación herética de la soberanía. Dios no infunde maldad en corazones puros.', 'explanation': 'La Escritura enseña que Dios entrega al hombre rebelde a la impureza y a una mente reprobada cuando rechaza la verdad (Romanos 1:28).'}, {'text': 'Faraón no cometió ningún pecado espiritual, únicamente defendía los intereses geopolíticos del imperio nilótico.', 'score': -1, 'meme': 'Justificación humanista que ignora la rebelión cósmica de Faraón contra el Dios creador.', 'explanation': "Faraón desafió: '¿Quién es Jehová para que yo oiga su voz?' (Éxodo 5:2), manifestando el arquetipo de la soberbia satánica."}, {'text': 'Las plagas fueron fenómenos climáticos ordinarios magnificados por los sacerdotes hebreos sin milagro divino.', 'score': 0, 'meme': "Naturalismo incrédulo. Los mismos hechiceros de Faraón confesaron: 'Dedo de Dios es este' (Éxodo 8:19).", 'explanation': 'El Espíritu de Dios desmanteló a cada uno de los dioses del panteón egipcio con poder incontestable.'}]}, 'realityCheckHard': {'q': 'Cuando el Espíritu Santo o la predicación bíblica expone una conducta soberbia o pecaminosa en tu vida:', 'subtext': '¿Te quebrantas de inmediato o levantas argumentos para defender tu postura y resistir la corrección?', 'options': [{'text': 'Caigo de rodillas: tiemblo ante su Palabra, reconozco mi necedad y pido un corazón contrito y humillado.', 'score': 1, 'badge': 'CORAZÓN DE CARNE', 'feedback': "'Al corazón contrito y humillado no despreciarás tú, oh Dios' (Salmo 51:17). El Espíritu habita con el quebrantado."}, {'text': 'Busco justificaciones intelectuales o errores en quien me corrigió para no tener que arrepentirme.', 'score': -1, 'badge': 'SÍNDROME DE FARAÓN', 'feedback': "'El hombre que reprendido endurece la cerviz, de repente será quebrantado, y todo sin remedio' (Proverbios 29:1)."}]}}, 'moses': {'qDiagnosticHard': {'question': '¿Por qué a Moisés se le negó la entrada a la Tierra Prometida al golpear la roca en Meriba (Números 20)?', 'options': [{'text': 'Porque no santificó a Dios ante el pueblo; actuó con ira carnal distorsionando el carácter de la gracia divina y alterando la tipología profética de la Roca que era Cristo.', 'score': 1, 'meme': 'Discernimiento ministerial riguroso. A quien más se le revela el Espíritu, más estricto es su juicio de santidad.', 'explanation': '1 Corintios 10:4 aclara que la Roca era Cristo, herida una sola vez (Éxodo 17). En Meriba debía hablarle, no golpearla. Moisés deshonró la santidad del Espíritu.'}, {'text': 'Porque Moisés ya era anciano y físicamente incompetente para librar las batallas militares de Canaán.', 'score': -1, 'meme': "Falso: Deuteronomio 34:7 dice que 'sus ojos nunca se oscurecieron, ni perdió su vigor'.", 'explanation': 'El impedimento no fue biológico ni estratégico, sino estrictamente espiritual y disciplinario.'}, {'text': 'Dios fue injusto y desproporcionado castigando a su más grande siervo por una simple equivocación menor de impaciencia.', 'score': -1, 'meme': 'Blasfemia sutil. Dios es perfecto en todos sus caminos; el líder espiritual no puede arrogarse la gloria del milagro.', 'explanation': "Moisés dijo: '¿Os hemos de hacer salir aguas de esta peña?'. Arrogarse la obra del Espíritu es anatema."}, {'text': 'Moisés decidió voluntariamente quedarse en el monte Nebo para meditar sin involucrarse en la conquista territorial.', 'score': 0, 'meme': 'Invención novelesca que contradice la súplica insistente de Moisés para cruzar el Jordán (Deut. 3:25).', 'explanation': 'Dios le ordenó callar sobre el asunto, demostrando que el gobierno del Espíritu demanda reverencia suprema.'}]}, 'realityCheckHard': {'q': 'En el ejercicio de tu liderazgo o servicio espiritual cuando la congregación o familia te agota con quejas:', 'subtext': "¿Ministras con la mansedumbre del Espíritu Santo o explotas en amargura 'golpeando la roca' con tus palabras?", 'options': [{'text': 'Velo sobre mi espíritu: reconozco que la ira del hombre no obra la justicia de Dios y busco la santidad del Señor.', 'score': 1, 'badge': 'MANSEDUMBRE MINISTERIAL', 'feedback': 'Moisés aprendió la lección y fue el hombre más manso sobre la tierra. El Espíritu doma la lengua del siervo.'}, {'text': "Descargo mi frustración con sermones airados o desplantes en casa, justificándome en que 'la gente es insoportable'.", 'score': -1, 'badge': 'IRA EN EL ALTAR', 'feedback': 'Cuidado solemne: golpear la roca con tu amargura puede costarte entrar en la plenitud de lo que Dios preparó para ti.'}]}}, 'bezaleel': {'qDiagnosticHard': {'question': "¿Qué implicación teológica tiene que la primera persona descrita en la Biblia como 'llena del Espíritu de Dios' fuera un artesano (Éxodo 31:3)?", 'options': [{'text': 'Desmantela la falsa dicotomía entre lo sagrado y lo secular: el Espíritu Santo consagra y unge las habilidades manuales, técnicas y creativas para reflejar la gloria y orden del Creador.', 'score': 1, 'meme': '1000 de IQ teológico. El Espíritu Santo llena tanto el púlpito como el taller, el diseño y la programación.', 'explanation': "Éxodo 31:3 une 'Espíritu de Dios' con 'sabiduría, inteligencia, ciencia y todo arte'. Toda excelencia dedicada al Señor es una obra pneumatológica."}, {'text': 'Significa que la unción profética y la salvación del alma son secundarias frente al desarrollo de la estética material en el culto.', 'score': -1, 'meme': 'Desviación estética idolátrica. El tabernáculo apuntaba a Cristo, no al culto a los objetos.', 'explanation': 'El arte de Bezaleel estaba estrictamente subordinado al diseño revelado por Dios en el monte; no era arte autónomo.'}, {'text': 'Fue un error de traducción de los escribas; en el texto original solo se refería a talento genético heredado de la tribu de Judá.', 'score': -1, 'meme': "Negar el texto bíblico explícito: 'lo he llenado del Espíritu de Dios' (Ruaj Elohim).", 'explanation': 'El texto hebreo es enfático e inconfundible: la creatividad de Bezaleel fue una dotación sobrenatural del Espíritu Santo.'}, {'text': 'Una mención gremial histórica sin relevancia para la vida del cristiano profesional hoy en día.', 'score': 0, 'meme': 'Reduccionismo espiritual que limita al Consolador a los cuatro muros del templo.', 'explanation': 'Colosenses 3:23 y 1 Corintios 10:31 confirman que todo lo que hacemos de palabra o de hecho debe ser para la gloria de Dios.'}]}, 'realityCheckHard': {'q': 'En tu profesión, trabajo secular, estudios o proyectos cotidianos:', 'subtext': "¿Haces tu labor con la excelencia de Bezaleel para Dios, o entregas mediocridad diciendo 'al fin que es solo un trabajo secular'?", 'options': [{'text': 'Ofrezco mi trabajo como un acto de adoración al Espíritu Santo: con honestidad, puntualidad y excelencia intachable.', 'score': 1, 'badge': 'EXCELENCIA DE BEZALEEL', 'feedback': '¡Amén! Tu oficina, taller o pantalla de código es un púlpito de testimonio vivo del Reino de Dios.'}, {'text': 'Hago lo mínimo necesario para que no me despidan y me justifico diciendo que en el mundo todos son mediocres.', 'score': -1, 'badge': 'TESTIMONIO MANCHADO', 'feedback': 'La pereza y la mediocridad deshonran al Espíritu Santo. El creyente debe ser el trabajador más íntegro de la empresa.'}]}}, 'saul': {'qDiagnosticHard': {'question': '¿Por qué el Espíritu Santo se apartó de Saúl mientras que no se apartó definitivamente de David tras sus pecados?', 'options': [{'text': 'Porque Saúl solo buscó proteger su trono, su imagen pública y la aprobación del pueblo sin jamás arrepentirse ante Dios; David quebrantó su alma en genuina contrición rogando no perder el Espíritu Santo (Salmo 51:11).', 'score': 1, 'meme': 'La diferencia irreconciliable entre el remordimiento que teme al castigo y el arrepentimiento que llora por haber ofendido a Dios.', 'explanation': "Saúl le suplicó a Samuel: 'Hónrame ahora delante de los ancianos' (1 Sam 15:30). Su dios era la reputación. David clamó: 'Contra ti, contra ti solo he pecado'."}, {'text': 'Porque Dios era caprichoso y prefería a David por su aspecto físico sin importar sus actos morales.', 'score': -1, 'meme': "Blasfemia descomunal. Dios no hace acepción de personas; 'el hombre mira lo que está delante de sus ojos, pero Jehová mira el corazón'.", 'explanation': '1 Samuel 16:7 refuta directamente este error. Saúl fue desechado por su desobediencia obstinada y corazón no arrepentido.'}, {'text': 'Porque los pecados de Saúl fueron objetivamente más sangrientos y monstruosos que el homicidio y adulterio cometidos por David.', 'score': -1, 'meme': 'Cálculo carnal. A los ojos humanos, perdonar al ganado de Amalec parecía menos grave que enviar a Urías a la muerte.', 'explanation': "Para Dios, la rebelión de Saúl fue 'como pecado de adivinación, y como ídolos la obstinación' (1 Sam 15:23). El problema era su raíz de insumisión."}, {'text': 'Saúl nunca tuvo el Espíritu Santo en ningún momento; su unción como rey fue meramente política y decorativa.', 'score': 0, 'meme': "Ignorancia bíblica: 1 Samuel 10:6 profetizó: 'el Espíritu de Jehová vendrá sobre ti... y serás mudado en otro hombre'.", 'explanation': 'Saúl experimentó la unción, pero la despreció gobernando por el temor a los hombres y la brujería final de Endor.'}]}, 'realityCheckHard': {'q': 'Cuando cometes un pecado o falta grave que pone en riesgo tu imagen pública:', 'subtext': '¿Te duele haber entristecido al Espíritu Santo o te aterra que los demás se enteren y pierdas estatus o seguidores?', 'options': [{'text': 'Me quebranta haber ofendido la santidad de Dios: confieso con vergüenza y busco restauración sin maquillar mi falta.', 'score': 1, 'badge': 'CORAZÓN CONTRITO', 'feedback': "'El que encubre sus pecados no prosperará; mas el que los confiesa y se aparta alcanzará misericordia' (Proverbios 28:13)."}, {'text': "Oculto todo, manipulo a quienes saben y me concentro en armar una narrativa para proteger mi imagen de 'líder intachable'.", 'score': -1, 'badge': 'ESPÍRITU DE SAÚL', 'feedback': 'Cuidado: el camino de Saúl termina en soledad, tormento espiritual y juicio inexorable.'}]}}, 'david_goliath': {'qDiagnosticHard': {'question': '¿Cuál fue el verdadero fundamento teológico de la victoria de David sobre Goliat en el valle de Ela?', 'options': [{'text': 'La batalla pertenecía a Jehová: David operaba bajo el celo del Espíritu Santo por la gloria de Dios, desenmascarando que Goliat había desafiado al Dios vivo y no a un ejército humano.', 'score': 1, 'meme': "1 Samuel 17:45-47 grabado en fuego. 'Tú vienes a mí con espada y lanza; mas yo vengo a ti en el nombre de Jehová de los ejércitos'.", 'explanation': 'David no confió en la armadura carnal de Saúl. La victoria fue el fruto de la fe pneumatológica que vindica el honor de Dios frente a la soberbia del mundo.'}, {'text': 'Su puntería balística superior adquirida como pastor, convirtiéndolo en un francotirador militar de élite frente a un gigante miope.', 'score': -1, 'meme': 'Racionalismo que despoja al milagro de su gloria sobrenatural.', 'explanation': "Si bien David usó su honda, el texto enfatiza: 'no con espada ni con lanza salva Jehová; porque de Jehová es la batalla'."}, {'text': 'El deseo de David de casarse con la hija del rey, obtener exención de impuestos y ganar prestigio en Israel.', 'score': -1, 'meme': "Atribuirle ambición carnal a quien fue llamado 'un varón conforme al corazón de Dios'.", 'explanation': "El motor de David fue la indignación santa: '¿Quién es este filisteo incircunciso, para que provoque a los escuadrones del Dios viviente?'."}, {'text': 'Goliat sufrió una crisis médica de gigantismo hipofisario que le impidió defenderse.', 'score': 0, 'meme': 'Explicaciones seculares ridículas para no reconocer el poder del Espíritu de Dios.', 'explanation': 'La Escritura declara que David venció por la mano todopoderosa del Señor.'}]}, 'realityCheckHard': {'q': "Frente a los 'gigantes' contemporáneos que se burlan de la fe bíblica (leyes anticristianas, burlas en la universidad o presiones en el trabajo):", 'subtext': '¿Te repliegas cobardemente como el ejército de Saúl o te levantas con valentía y mansedumbre en el nombre de Jesús?', 'options': [{'text': 'No me avergüenzo del Evangelio: con sabiduría y gracia del Espíritu Santo doy testimonio firme de la Verdad sin transigir.', 'score': 1, 'badge': 'VALENTÍA DE DAVID', 'feedback': "'Porque no nos ha dado Dios espíritu de cobardía, sino de poder, de amor y de dominio propio' (2 Timoteo 1:7)."}, {'text': 'Oculto que soy creyente, me río de los chistes impíos y transijo con el pecado para no ser cancelado ni marginado.', 'score': -1, 'badge': 'COBARDÍA EN EL CAMPAMENTO', 'feedback': "'Cualquiera que se avergonzare de mí y de mis palabras... el Hijo del Hombre se avergonzará también de él' (Marcos 8:38)."}]}}, 'david_repentance': {'qDiagnosticHard': {'question': "¿Qué revela el Salmo 51:11 ('No quites de mí tu santo Espíritu') sobre el entendimiento de David acerca de la gracia y el juicio?", 'options': [{'text': 'Comprendió que el mayor castigo no era perder el trono o la salud, sino la comunión con el Espíritu Santo; reconoció su culpa sin excusas y buscó la regeneración de su ser interior.', 'score': 1, 'meme': 'La joya del arrepentimiento genuino. David vio lo que le pasó a Saúl y temió por encima de todo perder la gloria de Dios.', 'explanation': 'David no pidió conservar riquezas ni palacios. Su clamor supremo fue la purificación con hisopo y la permanencia del Santo Espíritu en su vida.'}, {'text': 'David recitó un poema protocolar exigido por los sacerdotes para limpiar su récord penal ante el tribunal levítico.', 'score': -1, 'meme': "Ceguera litúrgica. El Salmo 51 declara: 'Los sacrificios de Dios son el espíritu quebrantado'.", 'explanation': 'David sabía que los holocaustos externos no agradaban a Dios sin un corazón sinceramente contrito.'}, {'text': 'David culpó a Betsabé por bañarse a la vista del palacio, demostrando que su arrepentimiento fue solo parcial.', 'score': -1, 'meme': "Falsedad absoluta. En todo el Salmo 51 David asume la responsabilidad total: 'mi pecado está siempre delante de mí'.", 'explanation': 'El hombre guiado por el Espíritu no culpa a la tentación ni a su prójimo; se hace 100% responsable de su iniquidad.'}, {'text': 'Una oración privada que no tuvo ninguna consecuencia práctica en las leyes del reino de Israel.', 'score': 0, 'meme': 'Análisis político desconectado del dolor y las disciplinas providenciales que marcaron la casa de David.', 'explanation': 'El arrepentimiento de David fue auténtico y Dios lo perdonó, aunque las consecuencias de su pecado afectaron a su familia.'}]}, 'realityCheckHard': {'q': 'Cuando el Espíritu Santo te confronta a solas con un pecado deliberado que cometiste:', 'subtext': "¿Buscas excusas atenuantes ('es que estaba estresado', 'la carne es débil') o te humillas reconociendo la gravedad de tu ofensa?", 'options': [{'text': 'No pongo excusas: confieso mi maldad, me acojo a la sangre de Cristo y ruego que su Espíritu limpie mi corazón.', 'score': 1, 'badge': 'QUEBRANTAMIENTO GENUINO', 'feedback': "'Crea en mí, oh Dios, un corazón limpio, y renueva un espíritu recto dentro de mí'. Esta es la marca de un verdadero hijo de Dios."}, {'text': "Minimizo mi falta diciendo que 'otros hacen cosas peores' y continúo mi vida sin un cambio real de conducta.", 'score': -1, 'badge': 'AUTOJUSTIFICACIÓN PELIGROSA', 'feedback': 'La autojustificación es el veneno que endurece el corazón y apaga la voz del Consolador.'}]}}, 'elijah': {'qDiagnosticHard': {'question': "¿Por qué el fuego del cielo en el Carmelo y el 'silbo apacible' en Horeb revelan la plenitud del obrar del Espíritu Santo?", 'options': [{'text': 'Porque el Espíritu Santo se manifiesta con poder destructor sobre los altares de idolatría pública, pero transforma y pastorea el corazón del siervo en la intimidad apacible de su comunión personal.', 'score': 1, 'meme': '1 Reyes 18 y 19 en sublime armonía pneumatológica. Dios no estaba en el terremoto ni en el viento, sino en el silbo apacible.', 'explanation': 'Elías aprendió que los grandes despliegues de fuego no sustituyen la voz susurrante del Espíritu que renueva las fuerzas y redarguye en lo secreto.'}, {'text': 'Porque Elías demostró que la violencia y el espectáculo mediático son los únicos instrumentos válidos para revivir a una nación apóstata.', 'score': -1, 'meme': 'Error carnal. Dios llevó a Elías al desierto precisamente para liberarlo de la dependencia del espectáculo.', 'explanation': 'Tras el Carmelo, Jezabel siguió amenazando y Elías cayó en depresión; el verdadero sostenimiento vino del pan del cielo y la presencia íntima de Dios.'}, {'text': 'El fuego en el Carmelo fue un fenómeno pirotécnico provocado con nafta oculta por los discípulos de los profetas.', 'score': -1, 'meme': 'Racionalismo impío. El altar fue empapado con cuatro cántaros de agua tres veces consecutivas antes de que cayera el fuego.', 'explanation': '1 Reyes 18:33-35 prueba que toda posibilidad de fraude humano fue eliminada para que solo el Espíritu Santo recibiera la gloria.'}, {'text': 'Elías fue desechado por Dios en Horeb debido a su cobardía al huir de Jezabel.', 'score': 0, 'meme': 'Interpretación legalista y despiadada. Dios consoló a Elías, lo alimentó con ángeles y le dio sucesor.', 'explanation': 'Dios trata con ternura las flaquezas de sus siervos cuando estos se refugian en su monte sagrado.'}]}, 'realityCheckHard': {'q': 'Tras una gran victoria espiritual o servicio exitoso, cuando llega el lunes y te sientes solo, agotado o deprimido:', 'subtext': '¿Buscas el susurro apacible del Espíritu Santo en oración o buscas llenar tu vacío con desahogos carnales y quejas?', 'options': [{'text': 'Me refugio en el silbo apacible: descanso en Dios, permito que su Espíritu renueve mis fuerzas y escucho sus instrucciones.', 'score': 1, 'badge': 'SILBO APACIBLE EN EL ALMA', 'feedback': "'Venid a mí todos los que estáis trabajados y cargados, y yo os haré descansar'. El Espíritu es tu eterno Consolador."}, {'text': 'Me hundo en autocompasión, me aíslo con pensamientos de muerte y culpo a Dios de haberme abandonado.', 'score': -1, 'badge': 'DEPRESIÓN EN LA CUEVA', 'feedback': 'Sal de la cueva de la amargura: Dios tiene aún 7.000 que no han doblado sus rodillas ante Baal y tiene propósito para ti.'}]}}, 'micaiah': {'qDiagnosticHard': {'question': '¿Qué revela 1 Reyes 22 sobre el discernimiento espiritual de Micaías frente a los 400 profetas que profetizaban éxito al rey Acab?', 'options': [{'text': 'Que el consenso masivo religioso no es garantía de verdad: Micaías discernió en el consejo celestial que un espíritu de mentira operaba en los profetas complacientes para juicio de Acab.', 'score': 1, 'meme': 'Discernimiento profético supremo. Es preferible estar solo con el Espíritu de Verdad que acompañado de 400 aduladores del poder.', 'explanation': "Micaías declaró: 'Vive Jehová, que lo que Jehová me dijere, eso hablaré' (1 Reyes 22:14). El Espíritu Santo no se somete a encuestas de popularidad ni a reyes impíos."}, {'text': 'Que Micaías era un opositor político amargado y rebelde que disfrutaba llevarle la contra a la autoridad real.', 'score': -1, 'meme': "Acab pensaba exactamente eso: 'le aborrezco, porque nunca me profetiza bien'. Confundir lealtad a Dios con amargura.", 'explanation': 'Micaías amaba la verdad de Dios; fue abofeteado y encarcelado a pan y agua por no vender su mensaje.'}, {'text': 'Los 400 profetas tenían razón teológica, pero Acab cometió un error táctico de camuflaje en la batalla.', 'score': -1, 'meme': "Ceguera flagrante: Acab murió traspasado por una flecha disparada 'al azar' cumpliendo la profecía exacta de Micaías.", 'explanation': 'La Palabra respaldada por el Espíritu Santo jamás cae a tierra; el juicio anunciado se cumplió con precisión milimétrica.'}, {'text': 'Micaías negoció su liberación prometiendo cambiar su profecía si Acab regresaba victorioso de Ramot de Galaad.', 'score': 0, 'meme': "Contradice 1 Reyes 22:28: 'Si llegas a volver en paz, Jehová no ha hablado por mí. Oíd, pueblos todos'.", 'explanation': 'Micaías selló su testimonio ante todo el pueblo como testigo inquebrantable de la verdad divina.'}]}, 'realityCheckHard': {'q': 'Cuando en tu entorno cristiano o social surge una moda, doctrina errónea o práctica pecaminosa respaldada por la mayoría:', 'subtext': "¿Te atreves a sostener la Verdad bíblica con mansedumbre aunque te llamen 'anticuado', 'intolerante' o te aíslen?", 'options': [{'text': 'Me mantengo firme como Micaías: mi lealtad es al Espíritu de Verdad y a las Escrituras, no a los aplausos de la multitud.', 'score': 1, 'badge': 'CONVICCIÓN PROFÉTICA', 'feedback': "'Porque ¿busco ahora el favor de los hombres, o el de Dios?... si todavía agradara a los hombres, no sería siervo de Cristo' (Gálatas 1:10)."}, {'text': 'Me callo, acomodo mi discurso y sonrío para no incomodar a la mayoría ni perder privilegios o amistades.', 'score': -1, 'badge': 'PROCURADOR DE ACAB', 'feedback': 'La tibieza que transige con el error terminará arrastrada por el mismo juicio que consumirá a los falsos profetas.'}]}}, 'daniel': {'qDiagnosticHard': {'question': "¿Cuál fue la clave pneumatológica por la cual Daniel mantuvo un 'espíritu superior' en medio del imperio babilónico y persa?", 'options': [{'text': 'Su disciplina innegociable de santidad y oración continua en dependencia del Espíritu Santo, sin contaminarse con la mesa ni los edictos idolátricos de los gobernantes terrenales.', 'score': 1, 'meme': "Daniel 6:10 y Daniel 1:8: 'propuso en su corazón no contaminarse'. El Espíritu Santo habita en quienes no transigen con el sistema babilónico.", 'explanation': "Los mismos sátrapas persas reconocieron: 'No hallaremos contra este Daniel ocasión alguna, para acusarle, si no la hallamos contra él en relación con la ley de su Dios'."}, {'text': 'Su astucia política bilingüe que le permitió adular hábilmente a Nabucodonosor, Belsasar y Darío sin contradecir sus religiones.', 'score': -1, 'meme': "Insulto a la integridad de Daniel. Daniel le dijo a Belsasar en su cara: 'Tus dones sean para ti, y da tus recompensas a otros' (Daniel 5:17).", 'explanation': 'Daniel confrontó a los reyes más poderosos del planeta con los juicios del Dios Altísimo; no fue un cortesano sumiso.'}, {'text': 'El foso de los leones fue una alegoría poética sin peligro biológico; los leones eran mascotas dóciles del palacio.', 'score': -1, 'meme': 'Racionalismo que desestima Daniel 6:24: los acusadores fueron arrojados después y los leones quebraron todos sus huesos antes de llegar al suelo.', 'explanation': 'El ángel de Dios cerró la boca de las fieras porque Daniel fue hallado inocente y lleno del Espíritu de vida.'}, {'text': 'Daniel dependía de horóscopos caldeos que combinaba de forma sincretista con el culto monoteísta hebreo.', 'score': 0, 'meme': 'Grave error: Daniel 2 desmintió rotundamente a todos los magos, astrólogos y adivinos de Babilonia.', 'explanation': "Daniel afirmó: 'Hay un Dios en los cielos, el cual revela los misterios'. Su sabiduría no era oculta sino celestial."}]}, 'realityCheckHard': {'q': 'Cuando el sistema profesional, político o cultural donde vives presiona para comprometer tu ética cristiana:', 'subtext': 'Fraudes tributarios, mentiras en reportes corporativos o aplaudir ideologías contrarias a la Palabra de Dios...', 'options': [{'text': 'Abro mis ventanas como Daniel hacia el cielo: me mantengo irreprochable cueste lo que cueste y confío en la protección divina.', 'score': 1, 'badge': 'ESPÍRITU SUPERIOR', 'feedback': 'El Dios a quien tú continuamente sirves, Él te librará. La integridad es el sello de los nacidos del Espíritu.'}, {'text': "Cedo diciendo que 'los negocios son negocios' y que 'en el mundo laboral hay que ensuciarse las manos para sobrevivir'.", 'score': -1, 'badge': 'CIUDADANO DE BABILONIA', 'feedback': "'¿No sabéis que la amistad del mundo es enemistad contra Dios?' (Santiago 4:4). No puedes beber de la copa del Señor y de la mesa de Babilonia."}]}}, 'john_baptist': {'qDiagnosticHard': {'question': '¿Por qué Jesús declaró que Juan el Bautista era el mayor entre los nacidos de mujer, pero que el menor en el Reino de los Cielos es mayor que él?', 'options': [{'text': 'Juan fue el culminador del Antiguo Pacto, lleno del Espíritu desde el vientre para señalar al Cordero; pero el creyente del Nuevo Pacto participa de la plenitud del Espíritu morador por la obra consumada de Cristo.', 'score': 1, 'meme': 'Mateo 11:11 y Juan 1:29 en suprema revelación. Juan anunció el Reino; la Iglesia habita en el misterio del Espíritu derramado.', 'explanation': "Juan no vio la cruz ni la resurrección; selló su testimonio con su martirio. Su grandeza residió en su suprema humildad: 'Es necesario que él crezca, pero que yo mengüe'."}, {'text': "Porque Juan cometió apostasía irreparable cuando envió a preguntar desde la cárcel: '¿Eres tú aquel que había de venir, o esperaremos a otro?'.", 'score': -1, 'meme': 'Juicio despiadado contra el heraldo. Jesús no lo reprochó, sino que elogió su firmeza de caña no sacudida por el viento.', 'explanation': 'La duda de Juan en la prisión de Maqueronte fue la angustia de un profeta sufriente; Jesús le respondió con las señales mesiánicas de Isaías 35.'}, {'text': 'Porque Juan fundó una secta rival de bautistas en el desierto que rechazaba la autoridad teológica de Jesús.', 'score': -1, 'meme': 'Invento histórico infundado. Juan instruyó a sus propios discípulos a seguir a Jesús (Juan 1:35-37).', 'explanation': "Juan se gozó de ser 'el amigo del esposo' que oye la voz del Novio; su misión fue preparar el camino, no retener discípulos."}, {'text': 'Juan era un anacoreta excéntrico que sobrevivió comiendo langostas sin mayor impacto en la historia bíblica.', 'score': 0, 'meme': 'Miopía que no entiende el cumplimiento de la profecía de Elías anunciada en Malaquías 4:5.', 'explanation': 'Juan bautizó al Hijo de Dios en el Jordán donde el Padre habló y el Espíritu Santo descendió en forma de paloma.'}]}, 'realityCheckHard': {'q': 'Cuando otra persona, iglesia o ministerio empieza a crecer y recibir los elogios y recursos que tú anhelabas:', 'subtext': "¿Puedes decir con el corazón sincero de Juan: 'Es necesario que él crezca, pero que yo mengüe'?", 'options': [{'text': 'Me gozo en que Cristo sea proclamado: menguo con alegría para que el único exaltado sea el Cordero de Dios.', 'score': 1, 'badge': 'CORAZÓN DE HERALDO', 'feedback': 'La humildad es el sello del Espíritu Santo. Quien no busca su propia gloria entra en el gozo del Esposo.'}, {'text': "Siento envidia disimulada, critico su método ministerial y busco retener 'mi territorio' y mis seguidores a toda costa.", 'score': -1, 'badge': 'CELO CARNAL', 'feedback': 'El ministerio que busca promoverse a sí mismo apaga al Espíritu Santo y terminará en esterilidad espiritual.'}]}}, 'judas': {'qDiagnosticHard': {'question': '¿Cuál es la advertencia pneumatológica más aterradora del caso de Judas Iscariote para la iglesia contemporánea?', 'options': [{'text': 'Se puede caminar cerca de Jesús, predicar el Evangelio, echar fuera demonios e integrar el liderazgo eclesial sin haber nacido jamás del Espíritu Santo, dominado por la codicia y el engaño de la carne.', 'score': 1, 'meme': 'Alerta roja ministerial de Mateo 7:22-23 y Juan 12:6. La cercanía litúrgica no equivale a regeneración del corazón.', 'explanation': 'Judas llevó la bolsa, vio los milagros y participó de la misión de los doce, pero era ladrón e incrédulo. Su traición demostró que la carne religiosa es capaz de vender al Hijo de Dios.'}, {'text': 'Judas era un héroe incomprendido que intentó acelerar la revolución militar de Jesús contra el imperio romano.', 'score': -1, 'meme': "Herejía gnóstica del falso 'evangelio de Judas'. La Escritura lo llama 'hijo de perdición' (Juan 17:12).", 'explanation': 'Jesús conocía desde el principio quién lo había de entregar; Satanás entró en él tras consentir con la avaricia de 30 piezas de plata.'}, {'text': 'Judas no tuvo ninguna culpa moral porque estaba predestinado maquinalmente sin poder elegir ni arrepentirse.', 'score': -1, 'meme': "Deformación teológica: Hechos 1:25 declara que Judas cayó 'por transgresión, para irse a su propio lugar'.", 'explanation': 'Judas experimentó la gracia, las advertencias de Jesús en el aposento alto y el bocado de amor, pero prefirió el beso de traición.'}, {'text': 'Su pecado fue únicamente financiero y no guarda relación con la apostasía ni la condenación del alma.', 'score': 0, 'meme': 'Minimizar la traición al Santo de Israel es ceguera espiritual total.', 'explanation': 'El amor al dinero fue la raíz de todos los males que ahogó la semilla de la Palabra en el corazón de Judas.'}]}, 'realityCheckHard': {'q': 'En tu administración del dinero, negocios y finanzas personales y eclesiales:', 'subtext': '¿Has traicionado principios bíblicos, estafado o retenido lo que pertenece a Dios por amor a la ganancia deshonesta?', 'options': [{'text': 'Examino mis cuentas con temor de Dios: renuncio a toda avaricia y declaro que mi tesoro está en los cielos.', 'score': 1, 'badge': 'MAYORDOMÍA TRANSPARENTE', 'feedback': "'Porque raíz de todos los males es el amor al dinero' (1 Timoteo 6:10). El Espíritu produce contentamiento y generosidad."}, {'text': "Uso la fe como un negocio lucrativo, desvío fondos o hago trampas fiscales justificando que 'el fin justifica los medios'.", 'score': -1, 'badge': 'LA BOLSA DE JUDAS', 'feedback': 'Peligro supremo: no puedes servir a Dios y a las riquezas. Quien vende a Jesús por plata termina en desolación.'}]}}, 'peter_pentecost': {'qDiagnosticHard': {'question': '¿Qué distinción fundamental operó el bautismo del Espíritu Santo en Pentecostés en la vida y predicación del apóstol Pedro?', 'options': [{'text': 'Pasó de una valentía emocional basada en la fuerza de su propia carne (que colapsó ante una criada en la noche de la traición) a una convicción inquebrantable capacitada por el Espíritu que proclamó a Cristo ante el Sanedrín.', 'score': 1, 'meme': "Hechos 2 y Hechos 4:8: 'Pedro, lleno del Espíritu Santo, les dijo...'. El Espíritu transforma cobardes en columnas de fuego.", 'explanation': 'Pedro juró que moriría por Jesús en su fuerza carnal y fracasó tres veces. En Pentecostés recibió poder de lo alto (Lucas 24:49) y no temió la cruz.'}, {'text': 'Pedro simplemente aprendió retórica helenística en las escuelas de oratoria de Jerusalén para debatir con los fariseos.', 'score': -1, 'meme': "Hechos 4:13 lo refuta categóricamente: los líderes 'viendo el denuedo de Pedro y de Juan, y sabiendo que eran hombres sin letras y del vulgo, se maravillaban; y les reconocían que habían estado con Jesús'.", 'explanation': 'La unción del Espíritu Santo no proviene de la elocuencia humana, sino del poder de la resurrección.'}, {'text': 'Pedro continuó teniendo el mismo nivel de cobardía y fue Pablo quien realmente dirigió el avance apostólico sin su concurso.', 'score': -1, 'meme': 'Ignorancia de los primeros 12 capítulos de Hechos: Pedro abrió la puerta del Evangelio a judíos, samaritanos y gentiles (Cornelio).', 'explanation': 'Las llaves del Reino otorgadas a Pedro fueron ejercidas bajo la soberanía del Espíritu Santo.'}, {'text': 'El hablar en lenguas en Pentecostés fue un éxtasis místico ininteligible sin mensaje de arrepentimiento ni cristocéntrico.', 'score': 0, 'meme': "Contradice Hechos 2:11: 'les oímos hablar en nuestras lenguas las maravillas de Dios', seguido del sermón cristológico más poderoso.", 'explanation': 'Pentecostés no fue ruido emocional, sino la investidura de poder para ser testigos hasta lo último de la tierra.'}]}, 'realityCheckHard': {'q': 'Ante la orden del mundo de silenciar tu voz sobre el pecado, el juicio y la salvación exclusiva en Jesucristo:', 'subtext': "¿Callas para evitar problemas o respondes como Pedro: 'Es menester obedecer a Dios antes que a los hombres' (Hechos 5:29)?", 'options': [{'text': 'Ruego por denuedo al Espíritu Santo: predico el Evangelio completo con amor y firmeza sin adulterar la Verdad.', 'score': 1, 'badge': 'FUEGO DE PENTECOSTÉS', 'feedback': "'Y cuando hubieron orado, el lugar en que estaban congregados tembló; y todos fueron llenos del Espíritu Santo, y hablaban con denuedo la palabra de Dios'."}, {'text': "Acomodo el mensaje para no ofender a nadie; predico un evangelio 'motivacional' sin cruz, sin arrepentimiento y sin juicio.", 'score': -1, 'badge': 'NEGACIÓN EN EL PATIO', 'feedback': 'El evangelio adulterado no salva a nadie y avergüenza al Espíritu de gracia. Vuelve a Pentecostés.'}]}}, 'ananias_sapphira': {'qDiagnosticHard': {'question': "¿Por qué el apóstol Pedro confrontó a Ananías diciendo: '¿Por qué llenó Satanás tu corazón para que mintieses al Espíritu Santo?' (Hechos 5:3)?", 'options': [{'text': 'Porque fingieron una consagración radical que no tenían, pretendiendo comprar prestigio ministerial mediante una mentira premeditada al Espíritu Santo en la comunidad del pacto.', 'score': 1, 'meme': 'La lección más temible sobre la santidad del Espíritu. Mentir a los hombres es grave; mentir al Espíritu Santo es apostasía mortal.', 'explanation': 'La propiedad era suya y no estaban obligados a venderla (Hechos 5:4). Su pecado fue la hipocresía teatral: querer la gloria de Bernabé reteniendo el corazón en la avaricia.'}, {'text': 'Porque la iglesia primitiva era un régimen comunista obligatorio donde la propiedad privada estaba castigada con la pena de muerte.', 'score': -1, 'meme': "Anacronismo ideológico absurdo. Pedro dijo claramente: 'Reteniéndola, ¿no se te quedaba a ti? y vendida, ¿no estaba en tu poder?'.", 'explanation': 'La ofrenda era 100% voluntaria. La sentencia divina castigó la mentira descarada al Espíritu de Santidad.'}, {'text': 'Fue un accidente cardíaco simultáneo producto del estrés de la asamblea y no un juicio sobrenatural de Dios.', 'score': -1, 'meme': "Racionalismo que ignora la profecía de Pedro a Safira: 'He aquí a la puerta los pies de los que han sepultado a tu marido, y te sacarán a ti'.", 'explanation': "El juicio fue inmediato y produjo 'gran temor sobre toda la iglesia' (Hechos 5:11), guardando la pureza del avivamiento."}, {'text': 'Ananías y Safira fueron víctimas de una conspiración de los apóstoles para confiscar sus bienes.', 'score': 0, 'meme': 'Blasfemia contra el testimonio apostólico inspirado por el Espíritu Santo en el libro de los Hechos.', 'explanation': 'Los apóstoles no codiciaban bienes; vivían en continua oración y en la comunión del Espíritu.'}]}, 'realityCheckHard': {'q': 'En tu testimonio público, redes sociales y vida eclesial:', 'subtext': '¿Aparentas una estatura espiritual, generosidad y devoción íntima que no practicas en lo absoluto a solas?', 'options': [{'text': 'Renuncio a toda máscara de hipocresía: prefiero ser transparente con mis debilidades que fingir una santidad artificial ante los hombres.', 'score': 1, 'badge': 'TRANSPARENCIA EN EL ESPÍRITU', 'feedback': 'La integridad es la coincidencia exacta entre lo que eres a solas y lo que dices ser en el púlpito.'}, {'text': "Proyecto una imagen de 'supercristiano lleno de unción' en mis publicaciones mientras mantengo una vida carnal y fría en lo privado.", 'score': -1, 'badge': 'LEVADURA DE ANANÍAS', 'feedback': 'Ten temor de Dios: el Espíritu Santo no puede ser engañado por filtros, títulos ni apariencias teatrales.'}]}}, 'stephen_paul': {'qDiagnosticHard': {'question': '¿Cómo se conecta la plenitud del Espíritu en el martirio de Esteban (Hechos 7) con la posterior conversión y teología de Pablo?', 'options': [{'text': 'Esteban, lleno del Espíritu Santo, vio los cielos abiertos y oró por sus asesinos; esa oración y testimonio perforaron la conciencia de Saulo, preparándolo para ser derribado por la luz de Cristo en Damasco.', 'score': 1, 'meme': "Hechos 7:55-60 y Hechos 9. 'La sangre de los mártires es la semilla de la Iglesia'. La intercesión de Esteban engendró al apóstol Pablo.", 'explanation': "Saulo guardaba las ropas de los apedreadores. Escuchar a Esteban clamar 'Señor, no les tomes en cuenta este pecado' reveló la estatura incomprensible del fruto del Espíritu Santo."}, {'text': 'Esteban murió maldiciendo al Sanedrín, lo cual enfureció a Saulo y retrasó el avance del Evangelio varios decenios.', 'score': -1, 'meme': 'Falsificación del texto bíblico: Esteban dobló sus rodillas y clamó perdón con la misma gloria de Cristo en la cruz.', 'explanation': 'El Espíritu Santo reproduce el carácter de Jesús en sus mártires; Esteban murió amando y perdonando a sus verdugos.'}, {'text': 'Pablo se convirtió por estudiar a fondo la filosofía griega en Tarso y no por una intervención sobrenatural del Espíritu.', 'score': -1, 'meme': "Pablo testificó: 'Cuando agradó a Dios... revelar a su Hijo en mí' (Gálatas 1:15-16).", 'explanation': "Pablo persiguió a la iglesia hasta que el Resucitado lo confrontó: 'Saulo, Saulo, ¿por qué me persigues?'."}, {'text': 'Esteban era un simple administrador de mesas que se extralimitó al predicar teología a los rabinos de Jerusalén.', 'score': 0, 'meme': "Hechos 6:8 dice: 'Esteban, lleno de gracia y de poder, hacía grandes prodigios y señales entre el pueblo'.", 'explanation': 'El Espíritu Santo derriba el clericalismo: un diácono lleno del Espíritu desafió a los teólogos más encumbrados de la nación.'}]}, 'realityCheckHard': {'q': 'Cuando sufres persecución, calumnias, despidos injustos o traiciones dolorosas por causa de tu fe o integridad:', 'subtext': '¿Maldices y planeas venganza en tu carne o tienes la gracia del Espíritu para orar por la salvación de tus ofensores?', 'options': [{'text': 'Oro por quienes me ultrajan: bendigo y perdono en el nombre de Jesús, dejando la vindicación en las manos del Juez Justo.', 'score': 1, 'badge': 'CORONA DE ESTEBAN', 'feedback': "'Amad a vuestros enemigos, bendecid a los que os maldicen... para que seáis hijos de vuestro Padre que está en los cielos' (Mateo 5:44)."}, {'text': 'Alimento el rencor, hablo pestes de mis agresores y deseo en secreto que les sobrevenga una desgracia para celebrar.', 'score': -1, 'badge': 'ESPÍRITU DE VENGANZA', 'feedback': "'Mía es la venganza, yo pagaré, dice el Señor' (Romanos 12:19). Quien guarda rencor tiene bloqueada la comunión con el Consolador."}]}}, 'jesus': {'qDiagnosticHard': {'question': '¿Por qué la vida, ministerio y resurrección de Jesucristo constituyen el canon supremo de una vida gobernada por el Espíritu Santo?', 'options': [{'text': 'Porque Cristo fue concebido por el Espíritu, ungido en el Jordán, llevado al desierto para vencer a Satanás, ministró en el poder del Espíritu, se ofreció a sí mismo sin mancha por el Espíritu eterno y fue resucitado por el Espíritu de santidad.', 'score': 1, 'meme': 'La cumbre de la Pneumatología bíblica (Hechos 10:38, Hebreos 9:14, Romanos 1:4). Jesús es el modelo perfecto del Siervo ungido.', 'explanation': 'Jesús no operó como un mago autónomo; en su encarnación vivió en perfecta y constante sumisión al Padre mediante la comunión del Espíritu Santo.'}, {'text': 'Porque Jesús prescindió del Espíritu Santo al poseer divinidad intrínseca, siendo el bautismo en el Jordán una mera pantomima simbólica.', 'score': -1, 'meme': 'Herejía que niega la kenosis y la pneumatología del Nuevo Testamento. Jesús fue ungido para inaugurar el Año Agradable del Señor (Lucas 4:18).', 'explanation': "Hechos 10:38 afirma taxativamente: 'Dios ungió con el Espíritu Santo y con poder a Jesús de Nazaret, y cómo este anduvo haciendo bienes'."}, {'text': 'Jesús fue únicamente un sabio maestro ético que alcanzó iluminación mística mediante ejercicios de meditación esenia.', 'score': -1, 'meme': "Paganismo gnóstico moderno que niega al Mesías prometido en Isaías 11:2 ('Y reposará sobre él el Espíritu de Jehová').", 'explanation': 'Jesús es el Verbo hecho carne, el Cordero de Dios que bautiza con el Espíritu Santo y con fuego.'}, {'text': 'El ministerio de Jesús dependió de la aprobación rabínica del Templo de Jerusalén.', 'score': 0, 'meme': 'El Templo corrupto lo rechazó y crucificó; su autoridad provenía directamente del cielo.', 'explanation': 'La unción del Espíritu Santo en Cristo desenmascaró la esterilidad del sistema religioso carnal.'}]}, 'realityCheckHard': {'q': 'Al culminar este diagnóstico frente a la majestuosidad de Jesucristo el Ungido de Dios:', 'subtext': '¿Estás dispuesto a tomar tu cruz diariamente, renunciar a tu propio ego y permitir que el Espíritu Santo gobierne cada área de tu vida?', 'options': [{'text': 'Señor Jesús: renuncio a gobernarme a mí mismo; me rindo a tu Señorío y clamo para que tu Santo Espíritu sea mi guía, mi poder y mi vida entera.', 'score': 1, 'badge': 'CORONA DE GLORIA EN CRISTO', 'feedback': '¡GLORIA A DIOS EN LAS ALTURAS! Este es el fruto supremo de todo el examen: que Cristo viva en ti por su Santo Espíritu (Gálatas 2:20).'}, {'text': 'Prefiero un cristianismo cómodo, de domingo por la mañana, sin cruz, sin Getsemaní y sin que el Espíritu incomode mis placeres carnales.', 'score': -1, 'badge': 'CRISTIANISMO TIBIO', 'feedback': "'Por cuanto eres tibio, y no frío ni caliente, te vomitaré de mi boca' (Apocalipsis 3:16). Despierta, tú que duermes, y te alumbrará Cristo."}]}}}

for c in CHARACTERS:
    cid = c.get("id")
    if cid in PALADIN_DATA:
        c["qDiagnosticHard"] = PALADIN_DATA[cid]["qDiagnosticHard"]
        if "immersion" in c:
            c["immersion"]["realityCheckHard"] = PALADIN_DATA[cid]["realityCheckHard"]

print(f"Paladin mode deep dilemmas injected into all 19 characters.")
