# Scripts para iot labs

### inicializar el servicio mosquito

```bash
net start mosquitto

net stop mosquitto
```

### local devices emulator

Dispositivos que emulan dispositivos o servidores intermediarios "...ping Device ## local... [###]"
-> device10.py, device20.py & device30.py

### to verificate trafic:

```bash
Terminal command:

mosquitto_sub -h localhost -p 1883 -t "local/#"
```

***aws_conexion/publicateToAWS.py***

Nuevo archivo con la logica para tranferir el mensaje del broker mqtt mosquitto hacia aws iot core


### Condicional para diferentes topicos

***conditionalToAWS.py***

este script configura una suscripcion de escucha a los topicos locales y republica en aws iot core según corresponda al topico de origen local.

***publicateToAWS.py***

este script configura una suscripcion de escucha a los solo el topico de device10.py y republica en aws iot core al kael/topic