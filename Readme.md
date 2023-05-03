# Scripts for iot labs

### inicializar el servicio mosquito

```bash
net start mosquitto

net stop mosquitto
```

***deviceSub1.py***

Este es el script para el corredor local, se suscribe y publica datos, tiene un ciclo while para iterar una impresión en la consola y ver el tránsito de datos.

***localTOaws.py***

This script connect local broker and aws broker, then configure the client for aws iot core

### local devices emulator

Devices emulating broker servers sensors "...ping Device ## local... [###]"
local_devices -> device10.py, device20.py & device30.py

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