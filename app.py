import streamlit as st
from PIL import Image
from lorem_text import lorem
# import altair with an abbreviated alias
import altair as alt
# load a sample dataset as a pandas DataFrame
from vega_datasets import data

# Atur halaman
st.set_page_config(
    page_title="Mari belajar Streamlit",
    layout='wide'
)

tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9 = st.tabs(["Text", "Button", "Slider & text input", "Date & Color", "Image & Audio", "video", "Kolom", "Expand", "Data"])


with tab1: # Text

    st.write("hello world")

    """Teks tanpa menggunakan st.write"""
    """
    _Lorem ipsum dolor sit amet_,\n
    **consectetur adipiscing elit**,\n
    sed do eiusmod tempor incididunt ut labore et dolore magn
    """

    # Memasukkan teks dengan metode markdown
    st.markdown ("Tulisan ini menggunakan _Markdown_")
    # Menulis teks dengan style Title
    st.title("Ini adalah judul") # atau bisa "# adhaldas"
    # Menulis teks dengan style Header
    st.header ("Ini adalah header") # atau bisa "## adhaldas"
    # Menulis teks dengan style Subheader
    st.subheader ("Ini adalah subheader")
    # Menulis teks dengan preformatted-text/teks biasa
    st.text ("Ini adalah preformatted text")
    # Menulis teks dengan style caption
    st.caption ("Ini adalah caption")
    # Menulis teks kode
    st.code ("import streamlit as st")
    # Menulis teks kode multibaris
    st.code ("""
    # import library streamlit
    import streamlit as st
    """)
    # Menulis teks Latex
    st.latex("ax^2 + bx + c = 0")

with tab2: # Button
    # WIDGET
    # output: True/False
    tombol = st.button ("Tekan tombol ini")
    st.write(tombol) # tanpa st.write juga bisa, langsung nama variabelnya

    # output: True/False
    agree = st.checkbox("Apakah kamu setuju?")
    if agree:
        st.write("Anda setuju untuk belajar lebih giat")
    else:
        st.write("Ayo Belajar")

    # radio button, memilih salah satu opsi dari sekian opsi
    genre = st.radio (
        "Pilih genre musik favoritmu", 
        ("Pop", "Rock", "Metal", "Indie")
    )
    st.write(genre)

    kota = st.selectbox(
        "Pilih kota tujuan",
        ("Bandung", "Jakarta", "Surabaya", "Padang") # bisa list[] atau tuple()
    )
    st.write(kota)

    multi_kota = st.multiselect (
        "Pilih kota tujuan",
        ("Bandung", "Jakarta", "Surabaya", "Padang") # bisa list[] atau tuple()
    )
    st.write(multi_kota)

with tab3:
    x = st.slider(
        "Masukkan nilai parameter X",
        min_value=0, 
        max_value=100, 
        step=1,
        value=10 # nilai default
    )
    st.write(x)

    size = st.select_slider(
        "Masukkan ukuran baju",
        ("XS" , "S" , "M", "L", "XL", "XXL"), 
        value="L" # nilai default
    )
    st.write(size)

    y = st.number_input(
        "Masukkan nilai parameter Y",
        min_value=0, 
        max_value=10, 
        step=1,
        value=3 # nilai default
    )
    st.write(y)

    nama = st.text_input(
        "Masukkan nama kamu"
        )
    st.write(nama)

    komentar = st.text_area (
        "Tulis komentar di sini"
        )
    st.write(komentar)

with tab4:
    tanggal_lahir = st.date_input (
        "Masukkan tanggal lahir kamu"
    )
    st.write(tanggal_lahir)

    awal_meeting = st.time_input (
        "Masukkan waktu meeting"
    )
    st.write(awal_meeting)

    warna = st.color_picker(
        "Masukkan warna yang disukai"
    )
    st.write(warna)

with tab5:
    image = Image.open('media/sunrise.jpeg')

    st.image(
        image,
        caption="Ini adalah pemandangan matahari terbit"
    )

    audio_file = open('media/opening.mp3','rb')
    audio_bytes = audio_file.read()

    st.audio(audio_bytes, format='audio/mp3')

with tab6:
    video_file = open ('media/dqlab.mp4', 'rb')
    video_bytes = video_file. read ()
    st.video (video_bytes)

with tab7:
    # Membuat 3 buah kolom sama lebar
    coll, col2, col3 = st. columns (3)
    with coll:
        st.title("Kolom 1")
        lahir_saya = st.date_input("Tanggal lahir kamu")
    with col2:
        st.title("Kolom 2")
        lahir_gebetan = st.date_input("Tanggal lahir dia")
    with col3:
        st.title("Kolom 3")
        jadian = st.date_input("Tanggal jadian")
    st.button("Hitung")
    # Membuat dua buah kolom dengan lebar 1/4 dan 3/4
    kol1, kol2 = st. columns ( [1,3])
    with kol1:
        st.title("Kolom 1")
        lahir_aku = st.date_input("Tanggal lahir aku")
    with kol2:
        st.title("Kolom 2")
        lahir_dia = st.date_input("Tanggal lahir dirinya")

with tab8:
    with st.expander("See Lorem Ipsum"):
        text = lorem.paragraphs (3)
        st.write(text)

with tab9:
    cars = data.cars()
    # make the chart
    chart1 = alt.Chart(cars).mark_point().encode(
        x='Horsepower',
        y='Miles_per_Gallon',
        color='Origin',
    ).interactive()
    chart2 = alt.Chart(data).mark_bar().encode(
        alt.Y('a', type='nominal'),
        alt.X('b', type='quantitative',aggregate='average') 
    )

    source = data.cars()

    chart = alt.Chart(source).mark_circle().encode(
        x='Horsepower',
        y='Miles_per_Gallon',
        color='Origin',
    ).interactive()

    tab1, tab2, tab3 = st.tabs(["Streamlit theme (default)", "Altair native theme", "tetris"])

    with tab1:
        # Use the Streamlit theme.
        # This is the default. So you can also omit the theme argument.
        st.altair_chart(chart, theme="streamlit", use_container_width=True)
    with tab2:
        # Use the native Altair theme.
        st.altair_chart(chart, theme=None, use_container_width=True)
    with tab3:
        coll, col2 = st. columns (2)
        with coll:
            st.title("Container=True")
            st.altair_chart(chart1, theme=None, use_container_width=True)
        with col2:
            st.title("Without Container")
            st.altair_chart(chart1, theme=None)

    

with st.sidebar:
    st.title("SideBar Nih")
    st.write("Ini adalah sidebar")
    user = st.text_input("Masukkan user kamu")
    with st.expander("See Lorem Ipsum"):
        text = lorem.paragraphs (3)
        st.write(text)
    with st.container(): # secara visual ga kelihatan tapi sebenarnya memberikan wadah, dan juga biar mudah dilipet kalau
        #codenya panjang
        st.write('ini di dalam kontainer')

    st.write('ini di luar kontainer')


