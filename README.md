# Trabajo Integrador - Gestión Automatizada de Solicitud de Vacaciones

## Descripción

Proyecto desarrollado para modelar y automatizar el proceso de solicitud de vacaciones mediante un chatbot implementado en Python.

## Objetivos

- Modelar el proceso AS-IS y TO-BE utilizando BPMN 2.0.
- Automatizar la validación de solicitudes.
- Implementar reglas de negocio.
- Integrar persistencia de datos mediante archivos CSV.
- Gestionar aprobaciones y rechazos por parte del supervisor.

## Tecnologías utilizadas

- Python 3
- BPMN 2.0
- GitHub
- CSV

## Estructura del proyecto

- scripts/: código fuente
- datos/: almacenamiento de información
- diagramas/: modelos BPMN
- documentacion/: Matias Perez Romo TPIOE.pdf
- 
MANUAL DE USUARIO (GUÍA RÁPIDA)
Este manual describe los comandos y la lógica de interacción para los dos roles que operan con el Chatbot de Gestión de Vacaciones.
1. Perspectiva del Empleado (Solicitante)
   El solicitante interactúa con el sistema mediante mensajes de texto directos o comandos en la interfaz para gestionar su licencia anual:
   Inicio del Trámite (/start): Activa el bot. El sistema saluda al usuario y le solicita el ingreso de su número de legajo de manera automática.
   Identificación: El usuario debe digitar su número de legajo (Ej: 1024). Si el dato no es numérico o no existe, el bot reportará el error.
   Carga de Solicitud: Tras validar el legajo, el bot solicita la cantidad de días deseados. El usuario debe ingresar un número entero (Ej: 7).
   Espera de Resolución: Si el saldo es disponible, el bot informará que el trámite pasó a revisión del supervisor y pausará la sesión.
2. Perspectiva del Supervisor (Autorizador)
   El líder de equipo valida y dictamina el veredicto de los flujos pre-aprobados por el filtro automático del chatbot:
   Recepción de Alertas: El supervisor recibe una notificación en su interfaz indicando el nombre, legajo y días solicitados por el empleado a cargo.
   Comandos de Decisión: El sistema habilita dos botones interactivos o palabras clave de respuesta estricta:
     Botón / Comando SI: Aprueba las vacaciones. Modifica el saldo en el archivo de persistencia (empleados.csv) (Matias Per... p. 6) y dispara la notificación de éxito al empleado
     Botón / Comando NO: Rechaza la solicitud. Finaliza el proceso inmediatamente sin alterar los registros físicos (Matias Per... p. 6).
   
## Ejecución

```bash
python chatbot.py
