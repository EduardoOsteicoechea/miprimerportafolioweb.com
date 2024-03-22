for i in range(1, 20):
   filename = f"sesion_{i}.html"
   with open(filename, "w") as file:
       text = """
<!DOCTYPE html>
<html lang="en">
   <head>
       <meta charset="utf-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <title>miprimerportafolioweb.com</title>
       <link rel="stylesheet" href="_/css/global.css">
       <link rel="stylesheet" href="_/css/header.css">
       <link rel="stylesheet" href="_/css/footer.css">
       <link rel="stylesheet" href="_/css/main_navigation.css">
   </head>
   <body>
       <nav>
           	<ul>
               <h3>Sesiones del tutorial</h3>
               <li><a href="index.html">Inicio</a></li>
               <li><a href="sesion_1.html">Sesi&#243;n 1</a></li>
               <li><a href="sesion_2.html">Sesi&#243;n 2</a></li>  
               <li><a href="sesion_3.html">Sesi&#243;n 3</a></li>  
               <li><a href="sesion_4.html">Sesi&#243;n 4</a></li>  
               <li><a href="sesion_5.html">Sesi&#243;n 5</a></li>  
               <li><a href="sesion_6.html">Sesi&#243;n 6</a></li>  
               <li><a href="sesion_7.html">Sesi&#243;n 7</a></li>  
               <li><a href="sesion_8.html">Sesi&#243;n 8</a></li>  
               <li><a href="sesion_9.html">Sesi&#243;n 9</a></li>  
               <li><a href="sesion_10.html">Sesi&#243;n 10</a></li>  
               <li><a href="sesion_11.html">Sesi&#243;n 11</a></li>  
               <li><a href="sesion_12.html">Sesi&#243;n 12</a></li>  
               <li><a href="sesion_13.html">Sesi&#243;n 13</a></li>  
               <li><a href="sesion_14.html">Sesi&#243;n 14</a></li>  
               <li><a href="sesion_15.html">Sesi&#243;n 15</a></li>  
               <li><a href="sesion_16.html">Sesi&#243;n 16</a></li>  
               <li><a href="sesion_17.html">Sesi&#243;n 17</a></li>  
               <li><a href="sesion_18.html">Sesi&#243;n 18</a></li>  
               <li><a href="sesion_19.html">Sesi&#243;n 19</a></li>  
               <li><a href="sesion_20.html">Sesi&#243;n 20</a></li>  
				</ul>
       </nav>
   </body>
</html>
"""
       file.write(text)
