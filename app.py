import streamlit as st
import os
import datetime

# Page configuration for browser tab and layout
st.set_page_config(
    page_title="RoastTrack - Sistem Pakar Pemilihan Biji Kopi Pasca Roasting",
    page_icon="☕",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load CSS stylesheet
def load_css(css_file_path):
    if os.path.exists(css_file_path):
        with open(css_file_path, "r") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    else:
        # Fallback inline basic styles if style.css is not found
        st.markdown("""
            <style>
                .stApp { background-color: #120e0b; color: #f7f3ef; }
                h1, h2, h3 { color: #e6a15c !important; }
            </style>
        """, unsafe_allow_html=True)

# Path to CSS
CSS_PATH = os.path.join(os.path.dirname(__file__), "style.css")
load_css(CSS_PATH)

# ==========================================
# METADATA & DATA RULES SYSTEM
# ==========================================

CIRI_INFO = {
    "C01": "Bentuk biji kopi lonjong dan pipih",
    "C02": "Memiliki aroma buah atau bunga",
    "C03": "Memiliki tekstur lebih halus",
    "C04": "Memiliki garis agak berliku",
    "C05": "Kadar kafein sekitar 0,8 - 1,4%",
    "C06": "Bentuk biji kopi bulat dan padat",
    "C07": "Memiliki aroma buah",
    "C08": "Memiliki garis tengah lurus dan cembung",
    "C09": "Memiliki tekstur agak kasar",
    "C10": "Kadar kafein sekitar 1,7 - 4,0%",
    "C11": "Bentuk biji kopi yang besar",
    "C12": "Memiliki garis tidak simetris",
    "C13": "Bentuknya seperti air mata",
    "C14": "Kadar kafein sekitar 0,7 - 1,2%",
    "C15": "Biji kopi berwarna sangat hitam (gosong)",
    "C16": "Terdapat bercak hitam",
    "C17": "Memiliki warna lebih muda dari yang lain"
}

JURUSAN_INFO = {
    "J01": {
        "nama": "Biji Kopi Arabika Berkualitas",
        "deskripsi": "Biji kopi Arabika Anda tergolong berkualitas tinggi. Karakteristik ini didukung oleh bentuk lonjong pipih yang khas, aroma floral/fruity yang tajam, tekstur permukaan yang halus, celah garis tengah berliku, serta kadar kafein rendah alami khas Arabika (0.8 - 1.4%). Sangat cocok untuk pasar specialty coffee.",
        "rekomendasi": "Pertahankan profil roasting light-to-medium untuk menonjolkan keasaman (acidity) alami dan aroma buah/bunganya. Simpan dalam wadah kedap udara dengan katup satu arah (one-way degas valve).",
        "kategori": "Berkualitas",
        "tipe": "Arabika",
        "warna": "#2e7d32"
    },
    "J02": {
        "nama": "Biji Kopi Robusta Berkualitas",
        "deskripsi": "Biji kopi Robusta Anda memiliki kualitas yang baik. Ditandai dengan bentuk bulat padat, tekstur permukaan agak kasar, garis tengah lurus cembung, aroma buah yang kuat, serta kadar kafein tinggi (1.7 - 4.0%) yang memberikan rasa tebal (bold body).",
        "rekomendasi": "Sangat direkomendasikan untuk roasting medium-to-dark. Sangat baik sebagai bahan dasar espresso blend, kopi susu kekinian, atau kopi tubruk tradisional yang memerlukan body tebal.",
        "kategori": "Berkualitas",
        "tipe": "Robusta",
        "warna": "#2e7d32"
    },
    "J03": {
        "nama": "Biji Kopi Liberika Berkualitas",
        "deskripsi": "Biji kopi Liberika Anda teridentifikasi berkualitas baik. Memiliki karakteristik fisik biji yang sangat besar, bentuk menyerupai tetesan air (air mata) tidak simetris, aroma buah nangka yang khas, serta kadar kafein rendah (0.7 - 1.2%). Jenis kopi ini langka dan eksotis.",
        "rekomendasi": "Roasting dengan profil medium untuk menjaga keunikan aroma buah nangka (jackfruit-like) dan rasa rempah (spicy notes). Pasarkan sebagai kopi gourmet unik.",
        "kategori": "Berkualitas",
        "tipe": "Liberika",
        "warna": "#2e7d32"
    },
    "J04": {
        "nama": "Biji Kopi Arabika Memiliki Cacat (Defect)",
        "deskripsi": "Biji kopi Arabika Anda teridentifikasi memiliki cacat mutu pasca pemanggangan. Bentuk dasar mengarah ke Arabika, namun terdapat cacat berupa biji gosong (burnt/over-roasted), bercak hitam (black spot), atau warna terlalu muda yang tidak merata (quaker/under-roasted).",
        "rekomendasi": "Lakukan penyortiran manual (hand picking) untuk memisahkan biji cacat/gosong dari biji yang bagus. Biji cacat ini dapat merusak cita rasa seduhan (menimbulkan rasa pahit hangus atau asam kimia tidak sedap). Sesuaikan temperatur mesin roasting.",
        "kategori": "Cacat",
        "tipe": "Arabika",
        "warna": "#d84315"
    },
    "J05": {
        "nama": "Biji Kopi Robusta Memiliki Cacat (Defect)",
        "deskripsi": "Biji kopi Robusta Anda teridentifikasi memiliki cacat mutu pasca pemanggangan. Ciri fisik menunjukkan tipe Robusta, namun terdapat cacat pembakaran seperti bercak hitam akibat pemanasan tidak merata, biji gosong pekat, atau biji terlalu muda yang lolos sortasi pasca panen.",
        "rekomendasi": "Lakukan kalibrasi mesin sangrai kopi Anda. Pastikan sirkulasi udara panas (airflow) mengalir baik agar biji tidak gosong sebagian. Sortir biji kopi cacat ini sebelum diproduksi massal.",
        "kategori": "Cacat",
        "tipe": "Robusta",
        "warna": "#d84315"
    },
    "J06": {
        "nama": "Biji Kopi Liberika Memiliki Cacat (Defect)",
        "deskripsi": "Biji kopi Liberika Anda teridentifikasi memiliki cacat mutu pasca pemanggangan. Ukuran biji besar namun mengalami kegosongan berlebih (sangat hitam) atau memiliki bercak gelap akibat serangan hama saat di kebun yang tampak jelas setelah disangrai.",
        "rekomendasi": "Sortir biji secara ketat. Biji kopi Liberika cacat cenderung menimbulkan aroma busuk tanah (earthy defect) yang mengganggu aroma nangka alami kopi. Kurangi suhu awal pengisian biji (charge temperature) pada mesin roasting.",
        "kategori": "Cacat",
        "tipe": "Liberika",
        "warna": "#d84315"
    }
}

# Decision Tree Graph Representation for Step-by-Step Questionnaire
DECISION_TREE = {
    "C01": {"yes": "C02", "no": "C06", "tanya": "Apakah biji kopi pasca roasting memiliki bentuk fisik yang cenderung LONJONG dan PIPIH?"},
    "C02": {"yes": "C03", "no": "J0", "tanya": "Apakah biji kopi mengeluarkan aroma yang harum seperti BUAH-BUAHAN atau BUNGA (floral/fruity)?"},
    "C03": {"yes": "C04", "no": "J0", "tanya": "Ketika diraba, apakah permukaan biji kopi memiliki tekstur yang HALUS?"},
    "C04": {"yes": "C05", "no": "J0", "tanya": "Apakah garis tengah (celah belahan) biji kopi tampak AGAK BERLIKU (tidak lurus rata)?"},
    "C05": {"yes": "J01", "no": "C15_arabika", "tanya": "Berdasarkan uji lab/karakteristik varietas, apakah kadar kafein rendah berkisar antara 0,8% hingga 1,4%?"},
    
    # Arabika Defect check branch
    "C15_arabika": {"yes": "J04", "no": "C16_arabika", "tanya": "Apakah ditemukan biji kopi yang berwarna sangat hitam pekat alias GOSONG akibat over-roasting?"},
    "C16_arabika": {"yes": "J04", "no": "C17_arabika", "tanya": "Apakah terdapat BERCAK-BERCAK HITAM atau lubang hitam kecil pada permukaan biji kopi?"},
    "C17_arabika": {"yes": "J04", "no": "J0", "tanya": "Apakah ada biji kopi yang berwarna LEBIH MUDA/pucat kekuningan dibandingkan biji lainnya (quaker/under-roasted)?"},

    # Robusta branch
    "C06": {"yes": "C07", "no": "C11", "tanya": "Apakah bentuk fisik biji kopi cenderung BULAT dan PADAT?"},
    "C07": {"yes": "C08", "no": "J0", "tanya": "Apakah biji kopi mengeluarkan aroma harum BUAH-BUAHAN yang khas?"},
    "C08": {"yes": "C09", "no": "J0", "tanya": "Apakah celah garis tengah biji kopi berbentuk LURUS dan CEMBUNG pada kedua sisinya?"},
    "C09": {"yes": "C10", "no": "J0", "tanya": "Ketika diraba, apakah permukaan biji kopi terasa AGAK KASAR?"},
    "C10": {"yes": "J02", "no": "C15_robusta", "tanya": "Apakah kadar kafein biji kopi cenderung tinggi, berkisar antara 1,7% hingga 4,0%?"},

    # Robusta Defect check branch
    "C15_robusta": {"yes": "J05", "no": "C16_robusta", "tanya": "Apakah ditemukan biji kopi yang berwarna sangat hitam pekat alias GOSONG?"},
    "C16_robusta": {"yes": "J05", "no": "C17_robusta", "tanya": "Apakah terdapat BERCAK-BERCAK HITAM atau cacat fisik berlubang pada permukaan biji?"},
    "C17_robusta": {"yes": "J05", "no": "J0", "tanya": "Apakah ada biji kopi yang berwarna LEBIH MUDA/pucat dibandingkan dengan profil roasting rata-rata?"},

    # Liberika branch
    "C11": {"yes": "C12", "no": "J0", "tanya": "Apakah ukuran fisik biji kopi cenderung sangat BESAR dibandingkan biji kopi biasa?"},
    "C12": {"yes": "C13", "no": "J0", "tanya": "Apakah celah garis tengah biji kopi tampak TIDAK SIMETRIS?"},
    "C13": {"yes": "C14", "no": "J0", "tanya": "Apakah bentuk ujung biji kopi cenderung lancip menyerupai TETESAN AIR MATA?"},
    "C14": {"yes": "J03", "no": "C15_liberika", "tanya": "Apakah kadar kafein biji kopi sangat rendah, berkisar antara 0,7% hingga 1,2%?"},

    # Liberika Defect check branch
    "C15_liberika": {"yes": "J06", "no": "C16_liberika", "tanya": "Apakah ditemukan biji kopi yang berwarna sangat hitam pekat alias GOSONG?"},
    "C16_liberika": {"yes": "J06", "no": "C17_liberika", "tanya": "Apakah terdapat BERCAK-BERCAK HITAM pada permukaan biji?"},
    "C17_liberika": {"yes": "J06", "no": "J0", "tanya": "Apakah ada biji kopi yang memiliki warna LEBIH MUDA/pucat dari yang lain?"}
}

NODE_TO_CIRI = {
    "C01": "C01", "C02": "C02", "C03": "C03", "C04": "C04", "C05": "C05",
    "C06": "C06", "C07": "C07", "C08": "C08", "C09": "C09", "C10": "C10",
    "C11": "C11", "C12": "C12", "C13": "C13", "C14": "C14",
    "C15_arabika": "C15", "C16_arabika": "C16", "C17_arabika": "C17",
    "C15_robusta": "C15", "C16_robusta": "C16", "C17_robusta": "C17",
    "C15_liberika": "C15", "C16_liberika": "C16", "C17_liberika": "C17"
}

# ==========================================
# INFERENCE LOGIC (FORWARD CHAINING)
# ==========================================

def run_forward_chaining(facts):
    """
    Evaluates the input facts using the production rules of the expert system.
    Returns the list of conclusions and evaluation logs.
    """
    firing_logs = []
    inferred = set()
    known_facts = set(facts)
    
    rules = [
        {
            "id": "R1", 
            "cond": {"C01", "C02", "C03", "C04", "C05"}, 
            "conclusion": "J01", 
            "nama": "Kaidah Biji Arabika Berkualitas"
        },
        {
            "id": "R2", 
            "cond": {"C06", "C07", "C08", "C09", "C10"}, 
            "conclusion": "J02", 
            "nama": "Kaidah Biji Robusta Berkualitas"
        },
        {
            "id": "R3", 
            "cond": {"C11", "C12", "C13", "C14"}, 
            "conclusion": "J03", 
            "nama": "Kaidah Biji Liberika Berkualitas"
        },
        # Defect rules for Arabica
        {
            "id": "R4a", "cond": {"C01", "C02", "C03", "C04", "C15"}, "conclusion": "J04",
            "nama": "Kaidah Cacat Arabika - Gosong"
        },
        {
            "id": "R4b", "cond": {"C01", "C02", "C03", "C04", "C16"}, "conclusion": "J04",
            "nama": "Kaidah Cacat Arabika - Bercak Hitam"
        },
        {
            "id": "R4c", "cond": {"C01", "C02", "C03", "C04", "C17"}, "conclusion": "J04",
            "nama": "Kaidah Cacat Arabika - Quaker (Warna Muda)"
        },
        # Defect rules for Robusta
        {
            "id": "R5a", "cond": {"C06", "C07", "C08", "C09", "C15"}, "conclusion": "J05",
            "nama": "Kaidah Cacat Robusta - Gosong"
        },
        {
            "id": "R5b", "cond": {"C06", "C07", "C08", "C09", "C16"}, "conclusion": "J05",
            "nama": "Kaidah Cacat Robusta - Bercak Hitam"
        },
        {
            "id": "R5c", "cond": {"C06", "C07", "C08", "C09", "C17"}, "conclusion": "J05",
            "nama": "Kaidah Cacat Robusta - Quaker"
        },
        # Defect rules for Liberica
        {
            "id": "R6a", "cond": {"C11", "C12", "C13", "C15"}, "conclusion": "J06",
            "nama": "Kaidah Cacat Liberika - Gosong"
        },
        {
            "id": "R6b", "cond": {"C11", "C12", "C13", "C16"}, "conclusion": "J06",
            "nama": "Kaidah Cacat Liberika - Bercak Hitam"
        },
        {
            "id": "R6c", "cond": {"C11", "C12", "C13", "C17"}, "conclusion": "J06",
            "nama": "Kaidah Cacat Liberika - Quaker"
        }
    ]
    
    loop = True
    iteration = 1
    firing_logs.append("⚙️ **Memulai Proses Forward Chaining...**")
    firing_logs.append(f"Fakta Awal Terdeteksi: `{list(known_facts)}`")
    
    while loop:
        fired_in_this_loop = False
        firing_logs.append(f"--- **Iterasi {iteration}** ---")
        
        for rule in rules:
            rule_id = rule["id"]
            conds = rule["cond"]
            conclusion = rule["conclusion"]
            rule_name = rule["nama"]
            
            if conclusion not in known_facts:
                # Check if all conditions are satisfied
                if conds.issubset(known_facts):
                    known_facts.add(conclusion)
                    inferred.add(conclusion)
                    fired_in_this_loop = True
                    firing_logs.append(
                        f"🔥 **{rule_id} ({rule_name}) fired!** Kondisi {list(conds)} cocok dengan fakta. "
                        f"Kesimpulan baru didapat: **{conclusion}** ({JURUSAN_INFO[conclusion]['nama']})"
                    )
        
        if not fired_in_this_loop:
            firing_logs.append("⏸️ Tidak ada aturan lain yang terpenuhi. Proses selesai.")
            loop = False
        else:
            iteration += 1
            
    return list(inferred), firing_logs

# ==========================================
# STATE MANAGEMENT
# ==========================================

if 'step' not in st.session_state:
    st.session_state.step = 'homepage'

if 'user_nama' not in st.session_state:
    st.session_state.user_nama = ''

if 'user_usaha' not in st.session_state:
    st.session_state.user_usaha = ''

if 'wizard_node' not in st.session_state:
    st.session_state.wizard_node = 'C01'

if 'wizard_answers' not in st.session_state:
    st.session_state.wizard_answers = {}

if 'wizard_history' not in st.session_state:
    st.session_state.wizard_history = []

if 'riwayat' not in st.session_state:
    st.session_state.riwayat = []

# ==========================================
# LAYOUT & SIDEBAR
# ==========================================

with st.sidebar:
    st.markdown('<div style="text-align: center;"><h1 style="margin-bottom:0px; font-size: 2.2rem;">☕ RoastTrack</h1><p style="color: #8c7362; font-style: italic; font-size: 0.9rem; margin-top:0px;">Sistem Pakar Kopi Pasca Roasting</p></div>', unsafe_allow_html=True)
    st.markdown("---")
    
    # Sidebar Navigation Menu
    menu = st.radio(
        "Navigasi Menu",
        ["🔍 Konsultasi Pakar", "📋 Daftar Aturan & Metode", "🔤 Kamus Kode Indikator", "📖 Ensiklopedia Kopi", "🕒 Riwayat Tes"],
        index=0
    )
    
    st.markdown("---")
    
    # User Profile Section
    if st.session_state.user_nama:
        st.markdown(f"### 👤 Profil Pengguna")
        st.markdown(f"**Nama:** {st.session_state.user_nama}")
        if st.session_state.user_usaha:
            st.markdown(f"**Kedai/Usaha:** {st.session_state.user_usaha}")
        
        # Reset button in sidebar
        if st.button("Reset Identitas & Sesi"):
            st.session_state.step = 'homepage'
            st.session_state.user_nama = ''
            st.session_state.user_usaha = ''
            st.session_state.wizard_node = 'C01'
            st.session_state.wizard_answers = {}
            st.session_state.wizard_history = []
            st.rerun()
            
    st.markdown("""
        <div style="font-size: 0.75rem; color: #5c4a3c; margin-top: 5rem; border-top: 1px solid #33271f; padding-top: 1rem;">
            RoastTrack App v1.0.0<br>
            Metode: Forward Chaining<br>
            Berdasarkan Jurnal Sistem Informasi, Mei 2024
        </div>
    """, unsafe_allow_html=True)

# ==========================================
# VIEW ROUTER
# ==========================================

# 1. ATURAN & METODE VIEW
if menu == "📋 Daftar Aturan & Metode":
    st.markdown('<div class="header-badge">Metode Inferensi</div>', unsafe_allow_html=True)
    st.title("Metode Forward Chaining & Aturan Keputusan")
    
    st.markdown("""
    Sistem pakar ini menggunakan metode **Forward Chaining**, yaitu teknik pelacakan ke depan yang dimulai dari fakta-fakta yang diinputkan oleh pengguna (ciri fisik, aroma, kadar kafein) untuk kemudian mencari kaidah/aturan yang cocok untuk menarik kesimpulan jenis kualitas biji kopi.
    
    Di bawah ini adalah 6 Aturan Utama (Production Rules) dari sistem pakar yang diadaptasi dari hasil wawancara pakar sangrai kopi (*Coffee Roaster*):
    """)
    
    # Display rules elegantly
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="coffee-card">
            <h3 style="margin-top:0px; color:#ffb77d !important;">☕ Kategori Kopi Layak (Berkualitas)</h3>
            <ul style="margin-bottom:0px; padding-left: 20px; color: #dfd0c6;">
                <li style="margin-bottom: 1rem;"><b>Kaidah 1 (Arabika Berkualitas - J01)</b>:<br>
                    <span style="font-size:0.9rem; color:#bfa593;">IF Lonjong Pipih (<code>C01</code>) <b>AND</b> Aroma Buah/Bunga (<code>C02</code>) <b>AND</b> Tekstur Halus (<code>C03</code>) <b>AND</b> Garis Tengah Berliku (<code>C04</code>) <b>AND</b> Kafein 0.8-1.4% (<code>C05</code>)<br>
                    THEN <b>Biji Kopi Arabika Berkualitas</b> (<code>J01</code>)</span>
                </li>
                <li style="margin-bottom: 1rem;"><b>Kaidah 2 (Robusta Berkualitas - J02)</b>:<br>
                    <span style="font-size:0.9rem; color:#bfa593;">IF Bulat Padat (<code>C06</code>) <b>AND</b> Aroma Buah (<code>C07</code>) <b>AND</b> Garis Tengah Lurus Cembung (<code>C08</code>) <b>AND</b> Tekstur Agak Kasar (<code>C09</code>) <b>AND</b> Kafein 1.7-4.0% (<code>C10</code>)<br>
                    THEN <b>Biji Kopi Robusta Berkualitas</b> (<code>J02</code>)</span>
                </li>
                <li style="margin-bottom: 0px;"><b>Kaidah 3 (Liberika Berkualitas - J03)</b>:<br>
                    <span style="font-size:0.9rem; color:#bfa593;">IF Biji Besar (<code>C11</code>) <b>AND</b> Garis Tengah Tidak Simetris (<code>C12</code>) <b>AND</b> Bentuk Air Mata (<code>C13</code>) <b>AND</b> Kafein 0.7-1.2% (<code>C14</code>)<br>
                    THEN <b>Biji Kopi Liberika Berkualitas</b> (<code>J03</code>)</span>
                </li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
        <div class="coffee-card">
            <h3 style="margin-top:0px; color:#ff8a65 !important;">⚠️ Kategori Kopi Cacat (Defect)</h3>
            <ul style="margin-bottom:0px; padding-left: 20px; color: #dfd0c6;">
                <li style="margin-bottom: 1rem;"><b>Kaidah 4 (Arabika Cacat - J04)</b>:<br>
                    <span style="font-size:0.9rem; color:#bfa593;">IF Lonjong Pipih (<code>C01</code>) <b>AND</b> Aroma Buah/Bunga (<code>C02</code>) <b>AND</b> Tekstur Halus (<code>C03</code>) <b>AND</b> Garis Tengah Berliku (<code>C04</code>) <b>AND</b> (Gosong (<code>C15</code>) <b>OR</b> Bercak (<code>C16</code>) <b>OR</b> Warna Muda (<code>C17</code>))<br>
                    THEN <b>Biji Kopi Arabika Cacat</b> (<code>J04</code>)</span>
                </li>
                <li style="margin-bottom: 1rem;"><b>Kaidah 5 (Robusta Cacat - J05)</b>:<br>
                    <span style="font-size:0.9rem; color:#bfa593;">IF Bulat Padat (<code>C06</code>) <b>AND</b> Aroma Buah (<code>C07</code>) <b>AND</b> Garis Tengah Lurus (<code>C08</code>) <b>AND</b> Tekstur Agak Kasar (<code>C09</code>) <b>AND</b> (Gosong (<code>C15</code>) <b>OR</b> Bercak (<code>C16</code>) <b>OR</b> Warna Muda (<code>C17</code>))<br>
                    THEN <b>Biji Kopi Robusta Cacat</b> (<code>J05</code>)</span>
                </li>
                <li style="margin-bottom: 0px;"><b>Kaidah 6 (Liberika Cacat - J06)</b>:<br>
                    <span style="font-size:0.9rem; color:#bfa593;">IF Biji Besar (<code>C11</code>) <b>AND</b> Garis Tidak Simetris (<code>C12</code>) <b>AND</b> Bentuk Air Mata (<code>C13</code>) <b>AND</b> (Gosong (<code>C15</code>) <b>OR</b> Bercak (<code>C16</code>) <b>OR</b> Warna Muda (<code>C17</code>))<br>
                    THEN <b>Biji Kopi Liberika Cacat</b> (<code>J06</code>)</span>
                </li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    # Visual Demonstration of Forward Chaining Simulator
    st.markdown("### 🧪 Simulator Forward Chaining Mandiri")
    st.markdown("Pilih ciri-ciri yang teramati di bawah ini untuk melihat bagaimana mesin inferensi bekerja menarik kesimpulan:")
    
    selected_symptoms = []
    sc1, sc2, sc3 = st.columns(3)
    
    with sc1:
        st.markdown("**Bentuk Fisik & Tekstur**")
        if st.checkbox("C01 - Bentuk lonjong dan pipih", key="sim_c01"): selected_symptoms.append("C01")
        if st.checkbox("C03 - Permukaan bertekstur lebih halus", key="sim_c03"): selected_symptoms.append("C03")
        if st.checkbox("C06 - Bentuk bulat dan padat", key="sim_c06"): selected_symptoms.append("C06")
        if st.checkbox("C09 - Permukaan bertekstur agak kasar", key="sim_c09"): selected_symptoms.append("C09")
        if st.checkbox("C11 - Bentuk biji sangat besar", key="sim_c11"): selected_symptoms.append("C11")
        if st.checkbox("C13 - Bentuk seperti tetesan air mata", key="sim_c13"): selected_symptoms.append("C13")
        
    with sc2:
        st.markdown("**Garis Tengah & Aroma & Kafein**")
        if st.checkbox("C04 - Celah garis tengah berliku", key="sim_c04"): selected_symptoms.append("C04")
        if st.checkbox("C08 - Garis tengah lurus dan cembung", key="sim_c08"): selected_symptoms.append("C08")
        if st.checkbox("C12 - Garis tengah tidak simetris", key="sim_c12"): selected_symptoms.append("C12")
        if st.checkbox("C02 - Aroma harum buah atau bunga", key="sim_c02"): selected_symptoms.append("C02")
        if st.checkbox("C07 - Aroma harum buah saja", key="sim_c07"): selected_symptoms.append("C07")
        if st.checkbox("C05 - Kafein rendah (0.8 - 1.4%)", key="sim_c05"): selected_symptoms.append("C05")
        if st.checkbox("C10 - Kafein tinggi (1.7 - 4.0%)", key="sim_c10"): selected_symptoms.append("C10")
        if st.checkbox("C14 - Kafein liberika (0.7 - 1.2%)", key="sim_c14"): selected_symptoms.append("C14")
        
    with sc3:
        st.markdown("**Cacat Fisik Pasca Roasting**")
        if st.checkbox("C15 - Berwarna sangat hitam (gosong)", key="sim_c15"): selected_symptoms.append("C15")
        if st.checkbox("C16 - Terdapat bercak-bercak hitam", key="sim_c16"): selected_symptoms.append("C16")
        if st.checkbox("C17 - Warna lebih muda dari rata-rata", key="sim_c17"): selected_symptoms.append("C17")

    if st.button("Jalankan Inferensi Forward Chaining", type="primary"):
        if not selected_symptoms:
            st.warning("Silakan pilih minimal satu ciri di atas.")
        else:
            conclusions, logs = run_forward_chaining(selected_symptoms)
            
            st.markdown("#### 🔄 Trace Log Evaluasi:")
            for log in logs:
                st.write(log)
                
            st.markdown("#### 🎯 Hasil Kesimpulan:")
            if conclusions:
                for res in conclusions:
                    info = JURUSAN_INFO[res]
                    st.success(f"**TERDETEKSI: {info['nama']} ({res})** - {info['deskripsi']}")
            else:
                st.error("**TIDAK TERIDENTIFIKASI:** Kombinasi ciri tidak memenuhi kriteria aturan mana pun (J01-J06).")

# 2. KAMUS KODE INDIKATOR VIEW
elif menu == "🔤 Kamus Kode Indikator":
    st.markdown('<div class="header-badge">Kamus Kode</div>', unsafe_allow_html=True)
    st.title("Kamus Kode Gejala & Kesimpulan")
    st.markdown("Berikut adalah tabel referensi kode-kode ciri fisik (gejala) dan kesimpulan keputusan yang digunakan dalam sistem pakar ini:")
    
    # 1. CIRI CODES BY CATEGORY
    st.header("1. Daftar Kode Ciri (C01 - C17)")
    
    # We can present it categorized in columns or custom styling cards
    cat1, cat2 = st.columns(2)
    
    with cat1:
        st.markdown("""
        <div class="coffee-card" style="height: 100%;">
            <h3 style="margin-top:0px; color:#ffb77d !important;">📐 Ciri Bentuk Fisik & Garis</h3>
            <table style="width:100%; border-collapse: collapse; color: #dfd0c6;">
                <tr style="border-bottom: 1px solid rgba(230, 161, 92, 0.15); font-weight:bold;">
                    <td style="padding: 8px 5px; width: 20%;">Kode</td>
                    <td style="padding: 8px 5px;">Deskripsi Indikator Fisik</td>
                </tr>
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.03);">
                    <td style="padding: 8px 5px; font-weight:bold; color:#e6a15c;">C01</td>
                    <td style="padding: 8px 5px;">Bentuk lonjong dan pipih</td>
                </tr>
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.03);">
                    <td style="padding: 8px 5px; font-weight:bold; color:#e6a15c;">C03</td>
                    <td style="padding: 8px 5px;">Permukaan bertekstur lebih halus</td>
                </tr>
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.03);">
                    <td style="padding: 8px 5px; font-weight:bold; color:#e6a15c;">C04</td>
                    <td style="padding: 8px 5px;">Garis tengah celah agak berliku</td>
                </tr>
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.03);">
                    <td style="padding: 8px 5px; font-weight:bold; color:#e6a15c;">C06</td>
                    <td style="padding: 8px 5px;">Bentuk bulat dan padat</td>
                </tr>
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.03);">
                    <td style="padding: 8px 5px; font-weight:bold; color:#e6a15c;">C08</td>
                    <td style="padding: 8px 5px;">Garis tengah lurus dan cembung</td>
                </tr>
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.03);">
                    <td style="padding: 8px 5px; font-weight:bold; color:#e6a15c;">C09</td>
                    <td style="padding: 8px 5px;">Permukaan bertekstur agak kasar</td>
                </tr>
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.03);">
                    <td style="padding: 8px 5px; font-weight:bold; color:#e6a15c;">C11</td>
                    <td style="padding: 8px 5px;">Ukuran biji sangat besar</td>
                </tr>
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.03);">
                    <td style="padding: 8px 5px; font-weight:bold; color:#e6a15c;">C12</td>
                    <td style="padding: 8px 5px;">Garis tengah tidak simetris</td>
                </tr>
                <tr style="border-bottom: 0px;">
                    <td style="padding: 8px 5px; font-weight:bold; color:#e6a15c;">C13</td>
                    <td style="padding: 8px 5px;">Bentuk ujung menyerupai tetesan air mata</td>
                </tr>
            </table>
        </div>
        """, unsafe_allow_html=True)
        
    with cat2:
        st.markdown("""
        <div class="coffee-card" style="height: 100%;">
            <h3 style="margin-top:0px; color:#ffd3b0 !important;">🌸 Ciri Aroma, Kafein & Defect</h3>
            <table style="width:100%; border-collapse: collapse; color: #dfd0c6;">
                <tr style="border-bottom: 1px solid rgba(230, 161, 92, 0.15); font-weight:bold;">
                    <td style="padding: 8px 5px; width: 20%;">Kode</td>
                    <td style="padding: 8px 5px;">Deskripsi Indikator Non-Fisik</td>
                </tr>
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.03);">
                    <td style="padding: 8px 5px; font-weight:bold; color:#e6a15c;">C02</td>
                    <td style="padding: 8px 5px;">Memiliki aroma buah atau bunga (Arabika)</td>
                </tr>
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.03);">
                    <td style="padding: 8px 5px; font-weight:bold; color:#e6a15c;">C07</td>
                    <td style="padding: 8px 5px;">Memiliki aroma buah saja (Robusta)</td>
                </tr>
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.03);">
                    <td style="padding: 8px 5px; font-weight:bold; color:#e6a15c;">C05</td>
                    <td style="padding: 8px 5px;">Kadar kafein rendah (0.8% - 1.4%)</td>
                </tr>
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.03);">
                    <td style="padding: 8px 5px; font-weight:bold; color:#e6a15c;">C10</td>
                    <td style="padding: 8px 5px;">Kadar kafein tinggi (1.7% - 4.0%)</td>
                </tr>
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.03);">
                    <td style="padding: 8px 5px; font-weight:bold; color:#e6a15c;">C14</td>
                    <td style="padding: 8px 5px;">Kadar kafein liberika (0.7% - 1.2%)</td>
                </tr>
                <tr style="border-top: 1px solid rgba(230,161,92,0.1); border-bottom: 1px solid rgba(255,255,255,0.03); background-color: rgba(216, 67, 21, 0.05);">
                    <td style="padding: 8px 5px; font-weight:bold; color:#ff8a65;">C15</td>
                    <td style="padding: 8px 5px;">Biji kopi berwarna sangat hitam (gosong)</td>
                </tr>
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.03); background-color: rgba(216, 67, 21, 0.05);">
                    <td style="padding: 8px 5px; font-weight:bold; color:#ff8a65;">C16</td>
                    <td style="padding: 8px 5px;">Terdapat bercak-bercak hitam (cacat fisik)</td>
                </tr>
                <tr style="border-bottom: 0px; background-color: rgba(216, 67, 21, 0.05);">
                    <td style="padding: 8px 5px; font-weight:bold; color:#ff8a65;">C17</td>
                    <td style="padding: 8px 5px;">Warna biji lebih muda dari rata-rata (quaker)</td>
                </tr>
            </table>
        </div>
        """, unsafe_allow_html=True)
        
    st.markdown("<br>", unsafe_allow_html=True)
    
    # 2. RESULT CODES (J01 - J06)
    st.header("2. Daftar Kode Hasil Keputusan (J01 - J06)")
    
    st.markdown("""
    <div class="coffee-card">
        <table style="width:100%; border-collapse: collapse; color: #dfd0c6;">
            <tr style="border-bottom: 1px solid rgba(230, 161, 92, 0.15); font-weight:bold;">
                <td style="padding: 10px 5px; width: 12%;">Kode</td>
                <td style="padding: 10px 5px; width: 35%;">Hasil Klasifikasi</td>
                <td style="padding: 10px 5px; width: 15%;">Kategori Kopi</td>
                <td style="padding: 10px 5px;">Deskripsi Ringkas</td>
            </tr>
            <tr style="border-bottom: 1px solid rgba(255,255,255,0.03);">
                <td style="padding: 10px 5px; font-weight:bold; color:#81c784;">J01</td>
                <td style="padding: 10px 5px; font-weight:bold; color:#81c784;">Arabika Berkualitas</td>
                <td style="padding: 10px 5px; color:#81c784;">Berkualitas</td>
                <td style="padding: 10px 5px; font-size:0.9rem;">Biji Arabika dalam kondisi fisik mulus, rasa seimbang, kafein rendah alami.</td>
            </tr>
            <tr style="border-bottom: 1px solid rgba(255,255,255,0.03);">
                <td style="padding: 10px 5px; font-weight:bold; color:#81c784;">J02</td>
                <td style="padding: 10px 5px; font-weight:bold; color:#81c784;">Robusta Berkualitas</td>
                <td style="padding: 10px 5px; color:#81c784;">Berkualitas</td>
                <td style="padding: 10px 5px; font-size:0.9rem;">Biji Robusta bulat padat, tebal (bold), kadar kafein tinggi (1.7-4.0%).</td>
            </tr>
            <tr style="border-bottom: 1px solid rgba(255,255,255,0.03);">
                <td style="padding: 10px 5px; font-weight:bold; color:#81c784;">J03</td>
                <td style="padding: 10px 5px; font-weight:bold; color:#81c784;">Liberika Berkualitas</td>
                <td style="padding: 10px 5px; color:#81c784;">Berkualitas</td>
                <td style="padding: 10px 5px; font-size:0.9rem;">Biji Liberika sangat besar, berujung lancip air mata, aroma nangka eksotis.</td>
            </tr>
            <tr style="border-bottom: 1px solid rgba(255,255,255,0.03); background-color: rgba(216, 67, 21, 0.03);">
                <td style="padding: 10px 5px; font-weight:bold; color:#ff8a65;">J04</td>
                <td style="padding: 10px 5px; font-weight:bold; color:#ff8a65;">Arabika Memiliki Cacat</td>
                <td style="padding: 10px 5px; color:#ff8a65;">Memiliki Cacat</td>
                <td style="padding: 10px 5px; font-size:0.9rem;">Tipe biji Arabika tetapi memiliki defect gosong, berbercak hitam, atau warna belang.</td>
            </tr>
            <tr style="border-bottom: 1px solid rgba(255,255,255,0.03); background-color: rgba(216, 67, 21, 0.03);">
                <td style="padding: 10px 5px; font-weight:bold; color:#ff8a65;">J05</td>
                <td style="padding: 10px 5px; font-weight:bold; color:#ff8a65;">Robusta Memiliki Cacat</td>
                <td style="padding: 10px 5px; color:#ff8a65;">Memiliki Cacat</td>
                <td style="padding: 10px 5px; font-size:0.9rem;">Tipe biji Robusta bulat padat tetapi cacat gosong, pecah berlubang, atau quaker pucat.</td>
            </tr>
            <tr style="border-bottom: 0px; background-color: rgba(216, 67, 21, 0.03);">
                <td style="padding: 10px 5px; font-weight:bold; color:#ff8a65;">J06</td>
                <td style="padding: 10px 5px; font-weight:bold; color:#ff8a65;">Liberika Memiliki Cacat</td>
                <td style="padding: 10px 5px; color:#ff8a65;">Memiliki Cacat</td>
                <td style="padding: 10px 5px; font-size:0.9rem;">Tipe biji Liberika tetapi mengalami defect akibat over-roasted gosong, bercak, dll.</td>
            </tr>
        </table>
    </div>
    """, unsafe_allow_html=True)

# 3. ENSIKLOPEDIA KOPI VIEW
elif menu == "📖 Ensiklopedia Kopi":
    st.markdown('<div class="header-badge">Edukasi Kopi</div>', unsafe_allow_html=True)
    st.title("Ensiklopedia Tiga Jenis Biji Kopi Utama")
    st.markdown("Ketahui lebih dalam mengenai klasifikasi varietas kopi yang diidentifikasi oleh sistem pakar ini:")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="coffee-card" style="height: 480px;">
            <h3 style="margin-top:0px; color:#ffb77d !important;">👑 Kopi Arabika</h3>
            <p><b>Arabika</b> adalah jenis kopi paling populer di dunia karena profil rasanya yang kompleks dan kaya.</p>
            <ul style="color: #dfd0c6; padding-left: 20px;">
                <li><b>Karakter Fisik</b>: Biji lonjong, pipih, dengan garis tengah berliku.</li>
                <li><b>Cita Rasa</b>: Memiliki rasa asam (<i>acidity</i>) manis alami yang segar, dengan aroma buah, bunga, atau cokelat yang kaya.</li>
                <li><b>Kadar Kafein</b>: Rendah (0.8% - 1.4%).</li>
                <li><b>Sensitivitas</b>: Tumbuh optimal di dataran tinggi (di atas 1000 mdpl) dengan suhu sejuk. Lebih rentan terhadap hama karat daun.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
        <div class="coffee-card" style="height: 480px;">
            <h3 style="margin-top:0px; color:#e6a15c !important;">⚡ Kopi Robusta</h3>
            <p><b>Robusta</b> terkenal karena kekuatan rasanya yang tebal (<i>bold body</i>) dan ketahanan penyakit yang baik.</p>
            <ul style="color: #dfd0c6; padding-left: 20px;">
                <li><b>Karakter Fisik</b>: Biji berbentuk bulat, padat, berukuran lebih kecil, dengan garis tengah lurus cembung.</li>
                <li><b>Cita Rasa</b>: Rasa pahit yang tebal (cokelat pahit, kacang-kacangan) dengan aroma earthy. Keasaman sangat rendah.</li>
                <li><b>Kadar Kafein</b>: Tinggi (1.7% - 4.0%), memberikan dorongan energi yang kuat.</li>
                <li><b>Sensitivitas</b>: Sangat kuat, tumbuh baik di dataran rendah (di bawah 800 mdpl).</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with col3:
        st.markdown("""
        <div class="coffee-card" style="height: 480px;">
            <h3 style="margin-top:0px; color:#ffab91 !important;">🍃 Kopi Liberika</h3>
            <p><b>Liberika</b> adalah varietas kopi eksotis asal Liberia dengan ukuran biji yang sangat masif.</p>
            <ul style="color: #dfd0c6; padding-left: 20px;">
                <li><b>Karakter Fisik</b>: Ukuran biji sangat besar (bisa dua kali lipat Arabika), asimetris, berbentuk runcing air mata.</li>
                <li><b>Cita Rasa</b>: Profil rasa buah nangka matang dengan sensasi rempah (<i>smoky</i>) yang khas dan unik.</li>
                <li><b>Kadar Kafein</b>: Sangat rendah (0.7% - 1.2%).</li>
                <li><b>Sensitivitas</b>: Tumbuh optimal di tanah gambut basah dan dataran rendah.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# 3. RIWAYAT TES VIEW
elif menu == "🕒 Riwayat Tes":
    st.markdown('<div class="header-badge">Riwayat Sesi</div>', unsafe_allow_html=True)
    st.title("Riwayat Tes Konsultasi")
    st.markdown("Daftar hasil identifikasi biji kopi yang dilakukan selama sesi aplikasi ini:")
    
    if not st.session_state.riwayat:
        st.info("Belum ada riwayat konsultasi pada sesi ini. Silakan masuk ke menu **🔍 Konsultasi Pakar** untuk memulai analisis.")
    else:
        # Display history in a clean table
        for i, item in enumerate(reversed(st.session_state.riwayat)):
            card_class = "result-success" if item["kategori"] == "Berkualitas" else "result-warning"
            st.markdown(f"""
                <div class="{card_class}">
                    <div style="display:flex; justify-content:space-between; align-items:center;">
                        <h4 style="margin:0px; color:#fff !important;">Hasil #{len(st.session_state.riwayat) - i}: {item['hasil']}</h4>
                        <span style="font-size:0.8rem; opacity:0.8;">{item['waktu']}</span>
                    </div>
                    <p style="margin: 5px 0 0 0; font-size: 0.9rem;">
                        <strong>Penguji:</strong> {item['nama']} ({item['usaha']}) <br>
                        <strong>Tipe Biji:</strong> Kopi {item['tipe']} | <strong>Status Kualitas:</strong> {item['kategori']} <br>
                        <strong>Ciri Terpilih:</strong> {', '.join(item['ciri'])}
                    </p>
                </div>
            """, unsafe_allow_html=True)

# 4. KONSULTASI PAKAR (MAIN FLOW)
else:
    # Homepage step
    if st.session_state.step == 'homepage':
        st.markdown('<div class="header-badge">Sistem Pakar Forward Chaining</div>', unsafe_allow_html=True)
        st.title("Sistem Pakar Pemilihan Biji Kopi Pasca Roasting")
        
        col1, col2 = st.columns([3, 2])
        
        with col1:
            # Aksen gambar biji kopi premium
            if os.path.exists("roasted_coffee_beans.jpg"):
                st.image("roasted_coffee_beans.jpg", use_container_width=True)
                
            st.markdown("""
            <div class="coffee-card" style="margin-bottom: 1.5rem !important;">
                <h3 style="margin-top:0px; color:#e6a15c !important;">☕ Selamat Datang di RoastTrack</h3>
                <p style="font-size: 1rem; line-height: 1.6;">Aplikasi ini dirancang untuk mengidentifikasi jenis biji kopi pasca penyangraian (<i>roasting</i>) serta menganalisis kelas mutunya apakah layak/berkualitas atau cacat (<i>defect</i>) berdasarkan 17 ciri fisik.</p>
                <p style="font-size: 1rem; margin-top: 1rem;">Sistem menggunakan mesin inferensi <b>Forward Chaining</b> untuk mengevaluasi:</p>
                <ul style="color: #dfd0c6; padding-left: 20px; font-size: 0.95rem; line-height: 1.7; margin-bottom: 0px;">
                    <li>📐 <b>Bentuk Fisik</b>: Memeriksa bentuk lonjong pipih, bulat padat, atau ukuran biji besar.</li>
                    <li>🌸 <b>Karakter Aroma</b>: Mendeteksi profil aroma fruity (buah) atau floral (bunga/nangka).</li>
                    <li>🧪 <b>Kadar Kafein</b>: Estimasi kimiawi persentase kafein berdasarkan varietas biji.</li>
                    <li>⚠️ <b>Defect Pemanggangan</b>: Menguji adanya biji gosong, bercak hama, atau warna belang quaker.</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button("Mulai Konsultasi Kopi", type="primary", use_container_width=True):
                st.session_state.step = 'identitas'
                st.rerun()
                
        with col2:
            st.markdown("""
            <div class="coffee-card" style="text-align: center; border-color: rgba(230, 161, 92, 0.25) !important;">
                <h3 style="margin-top:0px; color:#e6a15c !important;">🏆 Akurasi Uji Pakar</h3>
                <h1 style="font-size: 3.8rem; margin: 15px 0px; background: linear-gradient(135deg, #ffd3b0 0%, #e6a15c 50%, #b86f34 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">90.4%</h1>
                <p style="color: #bfa593; font-size: 0.9rem;">Tingkat penerimaan tampilan sistem berdasarkan pengujian User Acceptance Testing (UAT)</p>
                <hr style="margin: 1.5rem 0 !important; border-color: rgba(230, 161, 92, 0.1) !important;">
                <h3 style="color:#e6a15c !important;">📊 Klasifikasi Biji</h3>
                <h4 style="color:#ffb77d !important; margin: 5px 0px;">3 Varietas & 6 Kelas Mutu</h4>
                <p style="color: #dfd0c6; font-size: 0.9rem;">Arabika, Robusta, & Liberika (Berkualitas / Cacat)</p>
            </div>
            """, unsafe_allow_html=True)

    # Identitas step
    elif st.session_state.step == 'identitas':
        st.markdown('<div class="header-badge">QC Profile</div>', unsafe_allow_html=True)
        st.title("Profil Penguji Kualitas Kopi")
        st.markdown("Silakan isi nama dan informasi usaha Anda terlebih dahulu untuk mendokumentasikan laporan identifikasi.")
        
        with st.form("profil_penguji_form"):
            nama = st.text_input("Nama Lengkap Penguji", value=st.session_state.user_nama, placeholder="Masukkan nama Anda (contoh: Adeltya)")
            usaha = st.text_input("Nama Usaha / Kedai Kopi (Opsional)", value=st.session_state.user_usaha, placeholder="Masukkan nama kedai (contoh: Kopi Krema Jaya)")
            
            # Submit button inside st.form
            submit = st.form_submit_button("Lanjutkan Analisis", type="primary", use_container_width=True)
            
            if submit:
                if not nama.strip():
                    st.error("Nama wajib diisi sebelum melanjutkan.")
                else:
                    st.session_state.user_nama = nama.strip()
                    st.session_state.user_usaha = usaha.strip()
                    # Initialize wizard variables
                    st.session_state.wizard_node = 'C01'
                    st.session_state.wizard_answers = {}
                    st.session_state.wizard_history = []
                    st.session_state.step = 'wizard'
                    st.rerun()
                    
        col_cancel1, col_cancel2, col_cancel3 = st.columns([1, 2, 1])
        with col_cancel2:
            if st.button("⬅️ Batal & Kembali ke Beranda", use_container_width=True):
                st.session_state.step = 'homepage'
                st.rerun()

    # Wizard step
    elif st.session_state.step == 'wizard':
        current_node = st.session_state.wizard_node
        node_data = DECISION_TREE[current_node]
        
        # Calculate progress estimation
        total_wizard_steps = 17
        answered_count = len(st.session_state.wizard_history)
        progress_percentage = min((answered_count / 10) * 100, 100.0) # Approx max 10 questions per path
        
        st.markdown('<div class="header-badge">Diagnosa Interaktif</div>', unsafe_allow_html=True)
        st.title("Analisis Karakter Fisik Biji Kopi")
        st.markdown("Jawablah pertanyaan mengenai ciri fisik biji kopi pasca roasting di bawah ini secara teliti.")
        
        # Custom progress bar
        st.markdown(f"""
            <div class="progress-container">
                <div class="progress-label">
                    <span>Estimasi Diagnosa</span>
                    <span>Pertanyaan Ke-{answered_count + 1}</span>
                </div>
                <div class="progress-bar-bg">
                    <div class="progress-bar-fill" style="width: {progress_percentage}%;"></div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
            <div class="wizard-box" style="text-align: center;">
                <div style="font-size: 1.1rem; color: #ffb77d; margin-bottom: 0.75rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.08em;">Kode Ciri: {NODE_TO_CIRI[current_node]}</div>
                <h2 style="font-size: 2.1rem; line-height: 1.4; color: #ffffff !important; margin: 0 0 1.5rem 0; font-weight: 700;">{node_data['tanya']}</h2>
                <p style="color: #bfa593; font-size: 0.95rem; margin: 0;">Silakan amati kondisi fisik biji kopi pasca roasting Anda secara teliti sebelum menjawab.</p>
            </div>
        """, unsafe_allow_html=True)
        
        # Action Buttons (Ya / Tidak) in equal-width column pairs for symmetry
        col_act1, col_act2 = st.columns(2)
        
        with col_act1:
            if st.button("❌ TIDAK (KONDISI NEGATIF)", type="secondary", use_container_width=True):
                # Save answer
                ciri_code = NODE_TO_CIRI[current_node]
                st.session_state.wizard_answers[ciri_code] = False
                st.session_state.wizard_history.append(current_node)
                
                next_node = node_data['no']
                if next_node.startswith('J'):
                    st.session_state.wizard_node = next_node
                    st.session_state.step = 'result'
                else:
                    st.session_state.wizard_node = next_node
                st.rerun()
                
        with col_act2:
            if st.button("✅ YA (KONFIRMASI CIRI)", type="primary", use_container_width=True):
                # Save answer
                ciri_code = NODE_TO_CIRI[current_node]
                st.session_state.wizard_answers[ciri_code] = True
                st.session_state.wizard_history.append(current_node)
                
                next_node = node_data['yes']
                if next_node.startswith('J'):
                    st.session_state.wizard_node = next_node
                    st.session_state.step = 'result'
                else:
                    st.session_state.wizard_node = next_node
                st.rerun()
                
        # Center the Back button below the primary choice panel
        st.markdown("<div style='margin-top: 1rem;'></div>", unsafe_allow_html=True)
        col_back1, col_back2, col_back3 = st.columns([1, 2, 1])
        with col_back2:
            if len(st.session_state.wizard_history) > 0:
                if st.button("⬅️ Kembali ke Pertanyaan Sebelumnya", use_container_width=True):
                    # Go back to previous node
                    prev_node = st.session_state.wizard_history.pop()
                    # Remove from answers
                    prev_ciri = NODE_TO_CIRI[prev_node]
                    st.session_state.wizard_answers.pop(prev_ciri, None)
                    st.session_state.wizard_node = prev_node
                    st.rerun()
            else:
                if st.button("⬅️ Batal & Kembali ke Profil", use_container_width=True):
                    st.session_state.step = 'identitas'
                    st.rerun()
                
        # Display list of currently selected features
        if st.session_state.wizard_answers:
            st.markdown("#### 🔍 Ringkasan Ciri Teramati:")
            badges_html = '<div class="badge-container">'
            for k, v in st.session_state.wizard_answers.items():
                status_text = "Ya" if v else "Tidak"
                status_color = "#81c784" if v else "#e57373"
                badges_html += f'<span class="ciri-badge">{k}: {CIRI_INFO[k]} (<b style="color:{status_color};">{status_text}</b>)</span>'
            badges_html += '</div>'
            st.markdown(badges_html, unsafe_allow_html=True)

    # Result step
    elif st.session_state.step == 'result':
        result_code = st.session_state.wizard_node
        
        st.markdown('<div class="header-badge">Hasil Diagnosis Pakar</div>', unsafe_allow_html=True)
        st.title("Hasil Klasifikasi Kualitas Biji Kopi")
        st.markdown("Berikut adalah laporan hasil klasifikasi sistem pakar berdasarkan ciri fisik biji kopi Anda:")
        
        # Check if result matches anything
        if result_code == "J0" or result_code not in JURUSAN_INFO:
            st.markdown("""
                <div class="result-warning" style="border-color: #ffb74d;">
                    <h3>⚠️ Biji Kopi Tidak Teridentifikasi Secara Pasti</h3>
                    <p style="font-size: 1.1rem; line-height: 1.6;">
                        Berdasarkan kombinasi ciri-ciri yang Anda masukkan, sistem tidak dapat menentukan kesimpulan kualitas yang tepat secara otomatis sesuai aturan paper. Hal ini terjadi karena kombinasi ciri tersebut tidak cocok dengan 6 Aturan Pakar standar yang terdaftar.
                    </p>
                    <p>
                        <strong>Analisis Alternatif:</strong> Kemungkinan biji kopi Anda merupakan jenis campuran (blend) atau memiliki kecacatan lain yang tidak spesifik di dalam database sistem kami saat ini.
                    </p>
                </div>
            """, unsafe_allow_html=True)
            
            # Save "Unknown" result to session history if not already saved
            history_key = f"hist_{len(st.session_state.riwayat)}"
            if 'last_saved_key' not in st.session_state or st.session_state.last_saved_key != history_key:
                active_symptoms = [k for k, v in st.session_state.wizard_answers.items() if v]
                st.session_state.riwayat.append({
                    "nama": st.session_state.user_nama,
                    "usaha": st.session_state.user_usaha if st.session_state.user_usaha else "Perseorangan",
                    "hasil": "Tidak Teridentifikasi",
                    "kategori": "Cacat / Campuran",
                    "tipe": "Tidak Diketahui",
                    "ciri": active_symptoms if active_symptoms else ["Tidak ada ciri positif"],
                    "waktu": datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
                })
                st.session_state.last_saved_key = history_key
                
        else:
            info = JURUSAN_INFO[result_code]
            card_class = "result-success" if info["kategori"] == "Berkualitas" else "result-warning"
            icon = "✅" if info["kategori"] == "Berkualitas" else "⚠️"
            
            st.markdown(f"""
                <div class="{card_class}">
                    <h2 style="color: #fff !important; margin-top: 0px; font-size: 2.2rem;">{icon} {info['nama']} ({result_code})</h2>
                    <p style="font-size: 1.15rem; line-height: 1.6; margin-bottom: 1.5rem;">
                        {info['deskripsi']}
                    </p>
                    <hr style="border-color: rgba(255,255,255,0.1); margin: 1.5rem 0;">
                    <h4 style="color: #fff !important; margin-bottom: 0.5rem;">💡 Rekomendasi Roaster Ahli:</h4>
                    <p style="font-size: 1.05rem; line-height: 1.6;">
                        {info['rekomendasi']}
                    </p>
                </div>
            """, unsafe_allow_html=True)
            
            # Save correct result to session history if not already saved
            history_key = f"hist_{len(st.session_state.riwayat)}"
            if 'last_saved_key' not in st.session_state or st.session_state.last_saved_key != history_key:
                active_symptoms = [k for k, v in st.session_state.wizard_answers.items() if v]
                st.session_state.riwayat.append({
                    "nama": st.session_state.user_nama,
                    "usaha": st.session_state.user_usaha if st.session_state.user_usaha else "Perseorangan",
                    "hasil": info["nama"],
                    "kategori": info["kategori"],
                    "tipe": info["tipe"],
                    "ciri": active_symptoms,
                    "waktu": datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
                })
                st.session_state.last_saved_key = history_key

        # Fact list display
        st.markdown("### 🔍 Fakta Diagnosa Terpilih")
        col_f1, col_f2 = st.columns(2)
        with col_f1:
            st.markdown("**Ciri yang Terdeteksi Positif (YA):**")
            yes_found = False
            for k, v in st.session_state.wizard_answers.items():
                if v:
                    st.write(f"- `{k}`: {CIRI_INFO[k]}")
                    yes_found = True
            if not yes_found:
                st.write("*Tidak ada ciri fisik yang terdeteksi positif.*")
                
        with col_f2:
            st.markdown("**Ciri yang Dinyatakan Negatif (TIDAK):**")
            no_found = False
            for k, v in st.session_state.wizard_answers.items():
                if not v:
                    st.write(f"- `{k}`: {CIRI_INFO[k]}")
                    no_found = True
            if not no_found:
                st.write("*Tidak ada ciri fisik yang terdeteksi negatif.*")

        st.markdown("---")
        
        # Action controls for starting over
        col_res1, col_res2 = st.columns(2)
        with col_res1:
            if st.button("Ulangi Tes Kopi Lain", type="primary", use_container_width=True):
                st.session_state.wizard_node = 'C01'
                st.session_state.wizard_answers = {}
                st.session_state.wizard_history = []
                st.session_state.step = 'wizard'
                st.rerun()
        with col_res2:
            if st.button("Kembali ke Halaman Utama", use_container_width=True):
                st.session_state.step = 'homepage'
                st.rerun()
