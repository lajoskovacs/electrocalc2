# electro calculator, with Flet modul

import flet as ft
from math import pi
#from math import sqrt
#from math import atan			 

def main(page: ft.Page):
		
        def xl_f_clicked(e):			#  'f' változását lekezelő függvény	
	        pass
	        page.update()			#  grafikus felület frissítése


        def xl_L_clicked(e):			#  'L' változását lekezelő függvény	
                ok = True
                try:
                        xl = float(tf_xl_XL.value)   # 'XL' beolvasása szövegmezőből
                        if xl <= 0:
                                ok = False
                                tf_xl_XL.value = tf_xl_XL.value + ' ?'   # nem jó érték !
                except:
                        ok = False
                        tf_xl_XL.value = tf_xl_XL.value + ' ?'   # nem jó érték !
                try:
                        f = float(tf_xl_f.value)   # 'f' beolvasása szövegmezőből
                        if f <= 0:
                                ok = False
                                tf_xl_f.value = tf_xl_f.value + ' ?'   # nem jó érték !               
                except:
                        ok = False
                        tf_xl_f.value = tf_xl_f.value + ' ?'   # nem jó érték !
                if ok:
                        L = 1000*xl/(2*pi*f)        #  L   mH-ben !!
                        tf_xl_L.value = str(L)   # 'L' kiírása szövegmezőbe
                else:
                        tf_xl_L.value = "hiba!!"   # 'L' kiírása szövegmezőbe 

                page.update()			#  grafikus felület frissítése



        def xl_XL_clicked(e):			#  XL változását lekezelő függvény	
                ok = True
                try:
                        L = float(tf_xl_L.value)   # 'L' beolvasása szövegmezőből
                        if L <= 0:
                                ok = False
                                tf_xl_L.value = tf_xl_L.value + ' ?'   # nem jó érték !
                except:
                        ok = False
                        tf_xl_L.value = tf_xl_L.value + ' ?'   # nem jó érték !
                try:
                        f = float(tf_xl_f.value)   # 'f' beolvasása szövegmezőből
                        if f <= 0:
                                ok = False
                                tf_xl_f.value = tf_xl_f.value + ' ?'   # nem jó érték !               
                except:
                        ok = False
                        tf_xl_f.value = tf_xl_f.value + ' ?'   # nem jó érték !
                if ok:
                        xl = 2*pi*f*L/1000         #  XL   Ohm-ban !!
                        tf_xl_XL.value = str(xl)   # 'XL' kiírása szövegmezőbe
                else:
                        tf_xl_XL.value = "hiba!!"   # 'XL' kiírása szövegmezőbe 

                page.update()			#  grafikus felület frissítése


        def xc_f_clicked(e):			#  'f' változását lekezelő függvény	
	        pass
	        page.update()			#  grafikus felület frissítése


        def xc_C_clicked(e):			#  'C' változását lekezelő függvény	
	        pass
	        page.update()			#  grafikus felület frissítése


        def xc_XC_clicked(e):			#  'XC' változást lekezelő függvény	
	        pass
	        page.update()			#  grafikus felület frissítése


        txt_cim= ft.Text(
                value=" Elektrotechnikai számítások ", 
                color=ft.colors.WHITE, 
                bgcolor=ft.colors.ORANGE_800, 
                theme_style=ft.TextThemeStyle.TITLE_LARGE, 
                width = 300
        )	  #  egy cimke

        tb_xl_f = ft.TextButton("frekvencia, f (Hz)", on_click=xl_f_clicked)
        tb_xl_L = ft.TextButton("Induktivitás, L (mH)", on_click=xl_L_clicked)
        tb_xl_XL = ft.TextButton("XL = 2*pi*f*L (ohm)", on_click=xl_XL_clicked)
        tf_xl_f = ft.TextField(value=" ", width = 100)
        tf_xl_L = ft.TextField(value=" ", width = 100)
        tf_xl_XL = ft.TextField(value=" ", width = 100)

        data_xlf = ft.Row(controls=[tb_xl_f,tf_xl_f])
        data_xlL = ft.Row(controls=[tb_xl_L,tf_xl_L])
        data_xlXL = ft.Row(controls=[tb_xl_XL,tf_xl_XL])

        tb_xc_f = ft.TextButton("frekvencia, f (Hz)", on_click=xc_f_clicked)
        tb_xc_C = ft.TextButton("Kapacitás, C (nF)", on_click=xc_C_clicked)
        tb_xc_XC = ft.TextButton("XC = 1/(2*pi*f*C)  (ohm)", on_click=xc_XC_clicked)
        tf_xc_f = ft.TextField(value=" ", width = 100)
        tf_xc_C = ft.TextField(value=" ", width = 100)
        tf_xc_XC = ft.TextField(value=" ", width = 100)

        data_xcf = ft.Row(controls=[tb_xc_f,tf_xc_f])
        data_xcC = ft.Row(controls=[tb_xc_C,tf_xc_C])
        data_xcXC = ft.Row(controls=[tb_xc_XC,tf_xc_XC])


        lapok = ft.Tabs(
                selected_index=0,  
                animation_duration=300,	# váltás a nézetek között ms
                tabs=[
                        ft.Tab(
                                text="XL",
                                content=ft.Column(
                                        controls=[
                                                ft.Text("Induktív reaktancia számítása"), 
                                                data_xlf, 
                                                data_xlL, 
                                                data_xlXL
                                        ]
                                ),
                        ),
                        ft.Tab(
                                text="XC",
                                content=ft.Column(
                                        controls=[
                                                ft.Text("Kapacitív reaktancia számítása"), 
                                                data_xcf, 
                                                data_xcC, 
                                                data_xcXC
                                        ]
                                ),
                        ),
                        ft.Tab(text="R",content=ft.Container(
                                content=ft.Text("R számítása"), alignment=ft.alignment.center),
                        ),
                        ft.Tab(text="RLC",content=ft.Container(
                                content=ft.Text("soros RLC számítása"), alignment=ft.alignment.center),
                        ),
                ],
                expand=1,
        )

        page.add(
                txt_cim,
                lapok
        )


        

ft.app(target=main)		#  fő ablak/alkalmazás példány létrehozása
