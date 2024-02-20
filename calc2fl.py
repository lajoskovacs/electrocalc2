# electro calculator, with Flet modul
# version 0.1  2024.02.17.-
import flet as ft
from math import pi
from math import sqrt
#from math import atan			 

def main(page: ft.Page):
		
        def xl_f_click(e):			# xl-tab 'f' változását lekezelő függvény	
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
                        L = float(tf_xl_L.value)   # 'L' beolvasása szövegmezőből
                        if L <= 0:
                                ok = False
                                tf_xl_L.value = tf_xl_L.value + ' ?'   # nem jó érték !               
                except:
                        ok = False
                        tf_xl_L.value = tf_xl_L.value + ' ?'   # nem jó érték !
                if ok:
                        f = 1000*xl/(2*pi*L)        #  f   Hz-ben !!
                        tf_xl_f.value = str(f)   # 'f' kiírása szövegmezőbe
                else:
                        tf_xl_f.value = "hiba!!"   

                page.update()			#  grafikus felület frissítése

        ###########################################################################################

        def xl_L_click(e):			# xl-tab 'L' változását lekezelő függvény	
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
                        tf_xl_L.value = "hiba!!"   

                page.update()			#  grafikus felület frissítése

       ###########################################################################################

        def xl_XL_click(e):			# xl-tab XL változását lekezelő függvény	
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
                        tf_xl_XL.value = "hiba!!"   

                page.update()			#  grafikus felület frissítése

       ###########################################################################################

        def xc_f_click(e):			#  xc-tab 'f' változását lekezelő függvény	
                ok = True
                try:
                        xc = float(tf_xc_XC.value)   # 'XC' beolvasása szövegmezőből
                        if xc <= 0:
                                ok = False
                                tf_xc_XC.value = tf_xc_XC.value + ' ?'   # nem jó érték !
                except:
                        ok = False
                        tf_xc_XC.value = tf_xc_XC.value + ' ?'   # nem jó érték !
                try:
                        C = float(tf_xc_C.value)   # 'C' beolvasása szövegmezőből
                        if C <= 0:
                                ok = False
                                tf_xc_C.value = tf_xc_C.value + ' ?'   # nem jó érték !
                except:
                        ok = False
                        tf_xc_C.value = tf_xc_C.value + ' ?'   # nem jó érték !
                if ok:
                        f = 1000000000/(2*pi*C*xc)        #  f   Hz-ben !!
                        tf_xc_f.value = str(f)   # 'f' kiírása szövegmezőbe
                else:
                        tf_xc_f.value = "hiba!!"        

                page.update()			#  grafikus felület frissítése

       ###########################################################################################

        def xc_C_click(e):			#  xc-tab 'C' változását lekezelő függvény	
                ok = True
                try:
                        xc = float(tf_xc_XC.value)   # 'XC' beolvasása szövegmezőből
                        if xc <= 0:
                                ok = False
                                tf_xc_XC.value = tf_xc_XC.value + ' ?'   # nem jó érték !
                except:
                        ok = False
                        tf_xc_XC.value = tf_xc_XC.value + ' ?'   # nem jó érték !
                try:
                        f = float(tf_xc_f.value)   # 'f' beolvasása szövegmezőből
                        if f <= 0:
                                ok = False
                                tf_xc_f.value = tf_xc_f.value + ' ?'   # nem jó érték !               
                except:
                        ok = False
                        tf_xc_f.value = tf_xc_f.value + ' ?'   # nem jó érték !
                if ok:
                        C = 1000000000/(2*pi*f*xc)        #  C   nF-ban !!
                        tf_xc_C.value = str(C)   # 'C' kiírása szövegmezőbe
                else:
                        tf_xc_C.value = "hiba!!"   

                page.update()			#  grafikus felület frissítése

       ###########################################################################################

        def xc_XC_click(e):			#  xc-tab 'XC' változást lekezelő függvény	
                ok = True
                try:
                        C = float(tf_xc_C.value)   # 'C' beolvasása szövegmezőből
                        if C <= 0:
                                ok = False
                                tf_xc_C.value = tf_xc_C.value + ' ?'   # nem jó érték !
                except:
                        ok = False
                        tf_xc_C.value = tf_xc_C.value + ' ?'   # nem jó érték !
                try:
                        f = float(tf_xc_f.value)   # 'f' beolvasása szövegmezőből
                        if f <= 0:
                                ok = False
                                tf_xc_f.value = tf_xc_f.value + ' ?'   # nem jó érték !               
                except:
                        ok = False
                        tf_xc_f.value = tf_xc_f.value + ' ?'   # nem jó érték !
                if ok:
                        xc = 1000000000/(2*pi*f*C)        #  XC   Ohm-ban !!
                        tf_xc_XC.value = str(xc)   # 'XL' kiírása szövegmezőbe
                else:
                        tf_xc_XC.value = "hiba!!"   

                page.update()			#  grafikus felület frissítése

       ###########################################################################################

        def fo_f_click(e):			#  fo-tab 'f' változását lekezelő függvény
                ok = True
                try:
                        L = float(tf_fo_L.value)   # 'L' beolvasása szövegmezőből
                        if L <= 0:
                                ok = False
                                tf_fo_L.value = tf_fo_L.value + ' ?'   # nem jó érték !               
                except:
                        ok = False
                        tf_fo_L.value = tf_fo_L.value + ' ?'   # nem jó érték !
                try:
                        C = float(tf_fo_C.value)   # 'C' beolvasása szövegmezőből
                        if C <= 0:
                                ok = False
                                tf_fo_C.value = tf_fo_C.value + ' ?'   # nem jó érték !
                except:
                        ok = False
                        tf_fo_C.value = tf_fo_C.value + ' ?'   # nem jó érték !
                if ok:
                        f = 1000000/(2*pi*sqrt(C*L))        #  f   Hz-ben !!
                        tf_fo_f.value = str(f)   # 'f' kiírása szövegmezőbe
                else:
                        tf_fo_f.value = "hiba!!"        

                page.update()			#  grafikus felület frissítése

       ###########################################################################################

        def fo_L_click(e):			#  fo-tab 'L' változását lekezelő függvény
                ok = True
                try:
                        f = float(tf_fo_f.value)   # 'f' beolvasása szövegmezőből
                        if f <= 0:
                                ok = False
                                tf_fo_f.value = tf_fo_f.value + ' ?'   # nem jó érték !               
                except:
                        ok = False
                        tf_fo_f.value = tf_fo_f.value + ' ?'   # nem jó érték !
                try:
                        C = float(tf_fo_C.value)   # 'C' beolvasása szövegmezőből
                        if C <= 0:
                                ok = False
                                tf_fo_C.value = tf_fo_C.value + ' ?'   # nem jó érték !
                except:
                        ok = False
                        tf_fo_C.value = tf_fo_C.value + ' ?'   # nem jó érték !
                if ok:
                        L = 1000000000000/(4*pi*pi*f*f*C)       #  L  mH-ben !!
                        tf_fo_L.value = str(L)   # 'f' kiírása szövegmezőbe
                else:
                        tf_fo_L.value = "hiba!!"        

                page.update()			#  grafikus felület frissítése

       ###########################################################################################

        def fo_C_click(e):			#  fo-tab 'C' változását lekezelő függvény
                ok = True
                try:
                        f = float(tf_fo_f.value)   # 'f' beolvasása szövegmezőből
                        if f <= 0:
                                ok = False
                                tf_fo_f.value = tf_fo_f.value + ' ?'   # nem jó érték !               
                except:
                        ok = False
                        tf_fo_f.value = tf_fo_f.value + ' ?'   # nem jó érték !
                try:
                        L = float(tf_fo_L.value)   # 'L' beolvasása szövegmezőből
                        if L <= 0:
                                ok = False
                                tf_fo_L.value = tf_fo_L.value + ' ?'   # nem jó érték !
                except:
                        ok = False
                        tf_fo_L.value = tf_fo_L.value + ' ?'   # nem jó érték !
                if ok:
                        C = 1000000000000/(4*pi*pi*f*f*L)       #  C  nF-ban !!
                        tf_fo_C.value = str(C)   # 'f' kiírása szövegmezőbe
                else:
                        tf_fo_C.value = "hiba!!"        

                page.update()			#  grafikus felület frissítése


       ###########################################################################################

        def rlc_Ze_click(e):			#  rlc-tab 'Ze' változását lekezelő függvény
                ok = True  

        
       ###########################################################################################

        txt_cim= ft.Text(
                value=" Elektrotechnikai számítások ", 
                color=ft.colors.WHITE, 
                bgcolor=ft.colors.ORANGE_800, 
                size=30,
                theme_style=ft.TextThemeStyle.TITLE_LARGE, 
                width = 800
        )	  #  egy cimke

        buttstyle1 = ft.ButtonStyle(bgcolor=ft.colors.YELLOW)   # button style
        textstyle1 = ft.TextStyle(size=30,color="pink600",weight=ft.FontWeight.W_900)

       ###########################################################################################
                # tab1-XL  buttons, textfields
        tb_xl_f = ft.TextButton(
                content= ft.Text(value="Frekvencia, f (Hz)",size=20),
                style= buttstyle1,
                on_click=xl_f_click
        )
        tb_xl_L = ft.TextButton(
                content= ft.Text(value="Induktivitás, L (mH)",size=20),
                style= buttstyle1, 
                on_click=xl_L_click
        )
        tb_xl_XL = ft.TextButton(
                content= ft.Text(value="XL = 2*pi*f*L (ohm)",size=20),
                style= buttstyle1,
                on_click=xl_XL_click
        )
        tf_xl_f = ft.TextField(value=" ", width = 200)
        tf_xl_L = ft.TextField(value=" ", width = 200)
        tf_xl_XL = ft.TextField(value=" ", width = 200)

        data_xlf = ft.Row(controls=[tb_xl_f,tf_xl_f])
        data_xlL = ft.Row(controls=[tb_xl_L,tf_xl_L])
        data_xlXL = ft.Row(controls=[tb_xl_XL,tf_xl_XL])

       ###########################################################################################
              # tab2-XC  buttons, textfields
        tb_xc_f = ft.TextButton(
                content= ft.Text(value="Frekvencia, f (Hz)",size=20), 
                style= buttstyle1,
                on_click=xc_f_click
        )
        tb_xc_C = ft.TextButton(
                content= ft.Text(value="Kapacitás, C (nF)",size=20), 
                style= buttstyle1, 
                on_click=xc_C_click
        )
        tb_xc_XC = ft.TextButton(
                content= ft.Text(value="XC = 1/(2*pi*f*C)  (ohm)",size=20), 
                style= buttstyle1, 
                on_click=xc_XC_click
        )
        tf_xc_f = ft.TextField(value=" ", width = 200)
        tf_xc_C = ft.TextField(value=" ", width = 200)
        tf_xc_XC = ft.TextField(value=" ", width = 200)

        data_xcf = ft.Row(controls=[tb_xc_f,tf_xc_f])
        data_xcC = ft.Row(controls=[tb_xc_C,tf_xc_C])
        data_xcXC = ft.Row(controls=[tb_xc_XC,tf_xc_XC])

       ###########################################################################################
                # tab3-fo  buttons, textfields
        tb_fo_f = ft.TextButton(
                content= ft.Text(value="Rezonancia frekvencia, fo (Hz)",size=20), 
                style= buttstyle1,  
                on_click=fo_f_click
        )
        tb_fo_L = ft.TextButton(
                content= ft.Text(value="Induktivitás, L (mH)",size=20),
                style= buttstyle1,  
                on_click=fo_L_click
        )
        tb_fo_C = ft.TextButton(
                content= ft.Text(value="Kapacitás, C (nF)",size=20), 
                style= buttstyle1, 
                on_click=fo_C_click
        )
        tf_fo_f = ft.TextField(value=" ", width = 200)
        tf_fo_L = ft.TextField(value=" ", width = 200)
        tf_fo_C = ft.TextField(value=" ", width = 200)

        data_fof = ft.Row(controls=[tb_fo_f,tf_fo_f])
        data_foL = ft.Row(controls=[tb_fo_L,tf_fo_L])
        data_foC = ft.Row(controls=[tb_fo_C,tf_fo_C])

       ###########################################################################################
                # tab4-RLC  buttons, textfields
        tb_rlc_f = ft.TextButton(
                content= ft.Text(value="Frekvencia, f (Hz)",size=20), 
                style= buttstyle1,  
               # on_click=rlc_f_click
        )
        tb_rlc_L = ft.TextButton(
                content= ft.Text(value="Induktivitás, L (mH)",size=20),
                style= buttstyle1,  
              #  on_click=rlc_L_click
        )
        tb_rlc_C = ft.TextButton(
                content= ft.Text(value="Kapacitás, C (nF)",size=20), 
                style= buttstyle1, 
             #  on_click=rlc_C_click
        )
        tb_rlc_R = ft.TextButton(
                content= ft.Text(value="Ellenállás, R (ohm)",size=20), 
                style= buttstyle1, 
             #  on_click=rlc_R_click
        )
        tb_rlc_Ze = ft.TextButton(
                content= ft.Text(value="Impedancia, Ze (ohm)",size=20), 
                style= buttstyle1, 
                on_click=rlc_Ze_click
        )
        tb_rlc_fi = ft.TextButton(
                content= ft.Text(value="Fázisszög, fi (fok)",size=20), 
                style= buttstyle1, 
             #  on_click=rlc_fi_click
        )
        tb_rlc_fo = ft.TextButton(
                content= ft.Text(value="Rezonancia frekvencia, fo (Hz)",size=20), 
                style= buttstyle1, 
             #  on_click=rlc_fo_click
        )

        tf_rlc_f = ft.TextField(value=" ", width = 200)
        tf_rlc_L = ft.TextField(value=" ", width = 200)
        tf_rlc_C = ft.TextField(value=" ", width = 200)
        tf_rlc_R = ft.TextField(value=" ", width = 200)
        tf_rlc_Ze = ft.Text(value=" ", width = 200)
        tf_rlc_fi = ft.Text(value=" ", width = 200)
        tf_rlc_fo = ft.Text(value=" ", width = 200)

        data_rlcf = ft.Row(controls=[tb_rlc_f,tf_rlc_f])
        data_rlcL = ft.Row(controls=[tb_rlc_L,tf_rlc_L])
        data_rlcC = ft.Row(controls=[tb_rlc_C,tf_rlc_C])
        data_rlcR = ft.Row(controls=[tb_rlc_R,tf_rlc_R])
        data_rlcZe = ft.Row(controls=[tb_rlc_Ze,tf_rlc_Ze])
        data_rlcfi = ft.Row(controls=[tb_rlc_fi,tf_rlc_fi])
        data_rlcfo = ft.Row(controls=[tb_rlc_fo,tf_rlc_fo])

       ###########################################################################################
                # tabs
        lapok = ft.Tabs(
                selected_index=0,  
                animation_duration=300,	# váltás a nézetek között ms
                tabs=[
                        ft.Tab(
                                text="XL",
                                content=ft.Column(
                                        controls=[
                                                ft.Text("Induktív reaktancia számítása",style=textstyle1), 
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
                                                ft.Text("Kapacitív reaktancia számítása",style=textstyle1), 
                                                data_xcf, 
                                                data_xcC, 
                                                data_xcXC
                                        ]
                                ),
                        ),
                        ft.Tab(
                                text="fo",
                                content=ft.Column(
                                        controls=[
                                                ft.Text("Rezonancia fekvencia számítása",style=textstyle1),
                                                data_foC, 
                                                data_foL, 
                                                data_fof
                                        ]
                                )
                        ),
                        ft.Tab(
                                text="RLC",
                                content=ft.Column(
                                        controls=[
                                                ft.Text("soros RLC számítása",style=textstyle1),
                                                data_rlcf,      
                                                data_rlcL,
                                                data_rlcC,
                                                data_rlcR,
                                                data_rlcZe,
                                                data_rlcfi,
                                                data_rlcfo,
                                        ]
                                )
                        ),
                        ft.Tab(text="R",content=ft.Container(
                                content=ft.Text("Ellenállás számítása"), alignment=ft.alignment.center),
                        ),
                ],
                expand=1,
        )

       ###########################################################################################

        page.add(
                txt_cim,
                lapok
        )


        

ft.app(target=main)		#  fő ablak/alkalmazás példány létrehozása
