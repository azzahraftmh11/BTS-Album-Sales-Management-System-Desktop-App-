# Memasukkan library flet ke aplikasi
import flet
from flet import *

class FormCRUD(UserControl):
    def build(catatan):

        # Buat variabel untuk inputan
        catatan.inputan_Kode = TextField(
            label="Kode",
            hint_text="Masukkan Kode",
            expand=True
        )
        # membuat Dropdown
        catatan.inputan_nama_album = Dropdown(
            label="Nama Album",
            hint_text="Pilih Album",
            options=[
                dropdown.Option("The Most Beautiful Moment in Life, Pt. 1"),
                dropdown.Option("Love Yourself: Tear"),
                dropdown.Option("Map of the Soul: 7 ~ The Journey ~"),
                dropdown.Option("MAP OF THE SOUL: PERSONA"),
            ],
            expand=True
        )
        catatan.inputan_jumlah = TextField(
            label="Jumlah Album",
            hint_text="Masukkan Jumlah Album",
            expand=True,
            input_filter=InputFilter(allow=True, regex_string=r"[0-9]", replacement_string="")
        )
        catatan.inputan_harga = TextField(
            label="Harga",
            hint_text="Masukkan Harga barang",
            prefix_text="Rp. ",
            expand=True,
            input_filter=InputFilter(allow=True, regex_string=r"[0-9]", replacement_string="")
        )
        catatan.inputan_nama_user = TextField(
            label="Nama Pelanggan",
            hint_text="Masukkan Nama Pelanggan",
            expand=True
        )
        catatan.inputan_jenis_pembayaran = Dropdown(
            label="Jenis Pembayaran",
            hint_text="Pilih Bayar",
            options=[
                dropdown.Option("Cash"),
                dropdown.Option("Transfer"),
            ],
            expand=True
        )

        #buat variabel notif snackbar
        catatan.snack_bar= SnackBar(
            content=Text("Silahkan isi terlebih dahulu!"),
            bgcolor=colors.BLACK,
            close_icon_color=colors.RED,
            show_close_icon=True
        )
        catatan.judul_rekap= Text("Data Penjualan",
                            size=20,
                            color='black',
                            weight= "BOLD",
                            text_align=TextAlign.CENTER,
                            visible=False
        )

        # Buat variabel untuk layout data rekapan
        catatan.layout_data = Column()

        columnku = Column(
            controls=[
                Row(
                    controls=[
                        catatan.inputan_Kode,
                    ]
                ),
                Row(
                    controls=[
                        catatan.inputan_nama_album,
                    ]
                ),
                Row(
                    controls=[
                        catatan.inputan_jumlah,
                    ]
                ),
                Row(
                    controls=[
                        catatan.inputan_harga,
                    ]
                ),
                Row(
                    controls=[
                        catatan.inputan_nama_user,
                    ]
                ),
                Row(
                    controls=[
                        catatan.inputan_jenis_pembayaran,
                    ]
                ),
                Row(
                    controls=[
                        FloatingActionButton(
                            icon=icons.SAVE_AS,
                            text = "Simpan Data",
                            bgcolor="PURPLE",
                            width=390,
                            on_click=catatan.tambah_catatan
                        )
                    ]
                ),
                Row(
                    controls=[
                        catatan.judul_rekap,
                    ]
                ),
                


                # layout rekapan data
                catatan.layout_data,
                #snackbar
                catatan.snack_bar,
            ]
        )
        return Card(content=Container(content=columnku, padding=10))
    
    # Fungsi untuk perintah tambah data
    def tambah_catatan(catatan, e):
        if catatan.inputan_Kode.value=="" or catatan.inputan_nama_album.value=="" or catatan.inputan_jumlah.value=="" or catatan.inputan_harga.value=="" or catatan.inputan_nama_user.value=="" or catatan.inputan_jenis_pembayaran.value=="":
            catatan.snack_bar.open=True
            catatan.update()

        elif catatan.inputan_Kode.value!="" or catatan.inputan_nama_album.value!="" or catatan.inputan_jumlah.value!="" or catatan.inputan_harga.value!="" or catatan.inputan_nama_user.value=="" or catatan.inputan_jenis_pembayaran.value=="":
            data_catatan_baru= FormdataCRUD(catatan.inputan_Kode.value, catatan.inputan_nama_album.value, catatan.inputan_jumlah.value, catatan.inputan_harga.value, catatan.inputan_nama_user.value, catatan.inputan_jenis_pembayaran.value, catatan.hapus_catatan)
            catatan.layout_data.controls.append(data_catatan_baru)
            catatan.inputan_Kode.value=""
            catatan.inputan_nama_album.value=""
            catatan.inputan_jumlah.value=""
            catatan.inputan_harga.value=""
            catatan.inputan_nama_user.value=""
            catatan.inputan_jenis_pembayaran.value=""
            catatan.judul_rekap.visible=True
            catatan.update()

    # Fungsi untuk perintah hapus data
    def hapus_catatan(catatan, data_catatan_masuk):
        catatan.layout_data.controls.remove(data_catatan_masuk)
        catatan.update()

# Buat class form data rekapan/histori catatan
class FormdataCRUD(UserControl):
    def __init__(catatan, Kode_catatan,nama_album_catatan, jumlah_catatan, harga_catatan, nama_user_catatan, jenis_pembayaran_catatan, hapus_catatan):
        super().__init__()
        catatan.Kode_catatan = Kode_catatan
        catatan.nama_album_catatan = nama_album_catatan
        catatan.jumlah_catatan = jumlah_catatan
        catatan.harga_catatan = harga_catatan
        catatan.nama_user_catatan = nama_user_catatan
        catatan.jenis_pembayaran_catatan = jenis_pembayaran_catatan
        catatan.hapus_catatan = hapus_catatan

    def build(catatan):
        # Buat variabel untuk DATA TAMPILAN
        catatan.data_catatan = Text(catatan.Kode_catatan +  catatan.nama_album_catatan + ", " + catatan.jumlah_catatan + catatan.harga_catatan)
        catatan.Kode_ubah = Text(catatan.Kode_catatan)
        catatan.nama_album_ubah = Text(catatan.nama_album_catatan)
        catatan.jumlah_ubah = Text(catatan.jumlah_catatan)
        catatan.harga_ubah = Text(catatan.harga_catatan)
        catatan.nama_user_ubah = Text(catatan.nama_user_catatan)
        catatan.jenis_pembayaran_ubah = Text(catatan.jenis_pembayaran_catatan)

        #buat variabel untuk inputan/field ubah data
        catatan.inputan_catatan_ubah = TextField( expand = True)
        catatan.inputan_Kode_ubah = TextField (expand=True, label="Kode")
        catatan.inputan_jumlah_ubah = TextField (expand=True, label="Jumlah", input_filter=InputFilter(allow=True, regex_string=r"[0-9]", replacement_string=""))
        catatan.inputan_harga_ubah = TextField (expand=True, label="Harga", input_filter=InputFilter(allow=True, regex_string=r"[0-9]", replacement_string=""), prefix_text="Rp. ")
        catatan.inputan_nama_album_ubah = Dropdown(
            label="Nama Album",
            hint_text="Pilih Album",
            options=[
                dropdown.Option("The Most Beautiful Moment in Life, Pt. 1"),
                dropdown.Option("Love Yourself: Tear"),
                dropdown.Option("Map of the Soul: 7 ~ The Journey ~"),
                dropdown.Option("MAP OF THE SOUL: PERSONA"),
            ],
            expand=True
        )
        catatan.inputan_nama_user_ubah = TextField (expand=True, label="Nama Pelanggan")
        catatan.inputan_jenis_pembayaran_ubah = Dropdown(
            label="Jenis Pembayaran",
            hint_text="Pilih Bayar",
            options=[
                dropdown.Option("Cash"),
                dropdown.Option("Transfer"),
            ],
            expand=True
        )

        # Buat form rekapan data yang berhasil di simpan
        catatan.tampil_data = Column(
            
            controls=[
                #catatan.data_catatan,
                Row(
                    controls=[
                        catatan.Kode_ubah,
                        catatan.nama_album_ubah,
                        catatan.jumlah_ubah,
                        catatan.harga_ubah,
                        catatan.nama_user_ubah,
                        catatan.jenis_pembayaran_ubah,
        
                        
                        IconButton(
                            icon=icons.CREATE_OUTLINED,
                            tooltip="Ubah",
                            on_click = catatan.ubah_data,
                        ),
                        IconButton(
                            icon=icons.DELETE_OUTLINE,
                            tooltip="Hapus",
                            on_click = catatan.hapus_data,
                        ),
                    ],
                ),
            ],
        )

        #buat form entri untuk perubahan data
        catatan.tampil_ubahdata = Column(
            visible = False,
            controls = [
                #field / inputan catatan
                #catatan.inputan_catatan_ubah,
                Text("Edit Data",
                     size=20,
                     color='black',
                     weight='bold',
                     text_align=TextAlign.CENTER
                     ),
                Row(
                    controls=[
                        catatan.inputan_Kode_ubah,
                    ]
                ),
                Row(
                    controls=[
                        catatan.inputan_nama_album_ubah,
                    ]
                ),
                Row(
                    controls=[
                        catatan.inputan_jumlah_ubah,
                    ]
                ),
                Row(
                    controls=[
                        catatan.inputan_harga_ubah,
                    ]
                ),
                Row(
                    controls=[
                        catatan.inputan_nama_user_ubah,
                    ]
                ),
                Row(
                    controls=[
                        catatan.inputan_jenis_pembayaran_ubah,
                    ]
                ),
                Row(
                    controls=[
                        #tombol ubah data
                        IconButton(
                            icon = icons.DONE_OUTLINE_OUTLINED,
                            icon_color = colors.BLACK,
                            tooltip = "Simpan Perubahan",
                            on_click = catatan.simpan_ubah_data,
                        ),
                    ]
                ),
            ],
        )
        return Column(controls=[catatan.tampil_data, catatan.tampil_ubahdata])

    #fungsi utk perintah simpan data
    def simpan_ubah_data(catatan, e):
        catatan.Kode_ubah.value = catatan.inputan_Kode_ubah.value
        catatan.nama_album_ubah.value = catatan.inputan_nama_album_ubah.value
        catatan.jumlah_ubah.value = catatan.inputan_jumlah_ubah.value
        catatan.harga_ubah.value = catatan.inputan_harga_ubah.value
        catatan.nama_user_ubah.value = catatan.inputan_nama_user_ubah.value
        catatan.jenis_pembayaran_ubah.value = catatan.inputan_jenis_pembayaran_ubah.value
        catatan.tampil_data.visible = True
        catatan.tampil_ubahdata.visible = False
        catatan.update()

    #fungsi utk perintah ubah data
    def ubah_data(catatan, e):
        catatan.inputan_Kode_ubah.value = catatan.Kode_ubah.value
        catatan.inputan_nama_album_ubah.value = catatan.nama_album_ubah.value
        catatan.inputan_jumlah_ubah.value = catatan.jumlah_ubah.value
        catatan.inputan_harga_ubah.value = catatan.harga_ubah.value
        catatan.inputan_nama_user_ubah.value = catatan.nama_user_ubah.value
        catatan.inputan_jenis_pembayaran_ubah.value = catatan.jenis_pembayaran_ubah.value
        catatan.tampil_data.visible = True
        catatan.tampil_ubahdata.visible = True
        catatan.update()

    #fungsi utk perintah hapus data
    def hapus_data(catatan, e):
        catatan.hapus_catatan(catatan)


# Function / fungsi utama
def main(page: Page):
    # Mengatur halaman
    page.title = "ALBUM BTS"
    page.window_width = 450
    page.window_height = 612
    page.window_resizable = True
    page.window_maximizable = True
    page.window_minimizable = True
    page.scroll = "adaptive"
    page.theme_mode = ThemeMode.LIGHT

    # Menampilkan objek teks
    judul_aplikasi_1 = 'ALBUM'
    judul_aplikasi_2 = 'BTS'

    # Buat variabel untuk memanggil class form catatan
    form_aplikasi_note = FormCRUD()

    page.add(
        Row(
            controls=[
                Text(judul_aplikasi_1,
                     size=30,
                     weight='bold',
                     color='black',
                     ),
                Text(judul_aplikasi_2,
                     size=30,
                     weight='bold',
                     color='purple',
                     )
            ],
            alignment='center'
        ),
        form_aplikasi_note
    )

# Mengatur output aplikasi
flet.app(target=main)
#ft.app(target = main, view = ft.AppView.WEB_BROWSER)