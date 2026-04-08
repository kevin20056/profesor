# Sistema de Mensajería con Salas (Chat Rooms)

## Descripción del Trabajo

El objetivo de este trabajo es desarrollar un sistema de mensajería concurrente basado en salas (rooms), donde múltiples usuarios puedan conectarse a un servidor y comunicarse entre sí de manera organizada.

Cada usuario podrá unirse a una sala específica, y los mensajes enviados serán visibles únicamente para los usuarios que se encuentren en esa misma sala.

Este tipo de arquitectura es común en aplicaciones reales como chats grupales, plataformas colaborativas y sistemas de comunicación en tiempo real.

## Objetivos de Aprendizaje

Con este proyecto, el estudiante deberá:

* Comprender el funcionamiento de la comunicación cliente-servidor
* Implementar concurrencia mediante hilos usando threading
* Utilizar sockets de red con el módulo socket
* Aplicar conceptos de Programación Orientada a Objetos
* Gestionar múltiples clientes conectados simultáneamente
* Diseñar lógica para manejo de salas y difusión de mensajes

## Flujo de Comunicación

El sistema debe seguir el siguiente flujo básico:

```bash
CLIENTE                                  SERVIDOR
   │                                         │
   ├────────── CONEXIÓN ──────────────────►  │
   │         (socket.connect)                │
   │                                         │
   ├────────── NICKNAME ──────────────────►  │
   │                                         │
   ├────────── "join general" ─────────────► │
   │          (unirse a sala)                │
   │                                         │
   ├────────── "Hola mundo" ──────────────►  │
   │          (mensaje)                      │────► Broadcast solo a Room "general"
   │                                         │
   │◄──────── "Usuario1: Hola mundo" ────────┤
   │                                         │
   ├────────── "join tech" ────────────────► │
   │          (cambiar de sala)              │
   │                                         │
```

## Comandos del Cliente

El cliente deberá soportar los siguientes comandos:

| Comando | Descripción |
|--------------|--------------|
| /join <sala> | Unirse a una sala |
| /leave | Salir de la sala actual |
| /rooms | Listar salas disponibles |
| /msg <texto> | Enviar mensaje |
| /quit | Desconectarse Servidor |

> El usuario solo puede estar en una sala a la vez.

## Ejemplo de Ejecución

```bash
=== SERVIDOR ===
[INFO] Servidor iniciado en 127.0.0.1:5555
[+] Cliente1 se unió a sala 'general'
[+] Cliente2 se unido a sala 'general'
[+] Cliente3 se unió a sala 'tech'
[Cliente1] Hola todos!
[INFO] Mensaje broadcast a sala 'general'
[-] Cliente1 desconectado
=== CLIENTE 1 (terminal 1) ===
> Ingresa tu nombre: Juan
> /join general
> Hola todos!
> /join tech
>Error: No puedes estar en dos salas
=== CLIENTE 2 (terminal 2) ===
> Ingresa tu nombre: Maria
> /join general
< Juan: Hola todos!
=== CLIENTE 3 (terminal 3) ===
> Ingresa tu nombre: Pedro
> /join tech
< (no ve el mensaje de Juan)
```

## Requisitos Técnicos

El proyecto debe desarrollarse utilizando únicamente módulos estándar de Python:

| Requisito | Módulo Python |
| --------- | ------------- |
| Sockets | socket |
| Hilos | threading |
| POO | (nativo de Python) |

> No necesita librerías externas, todo estea en la parte del la explicacion

## Requerimientos Funcionales

El sistema debe:

* Permitir múltiples clientes conectados simultáneamente
* Manejar correctamente la concurrencia mediante hilos
* Gestionar salas dinámicamente
* Enviar mensajes únicamente a los usuarios de la misma sala
* Manejar desconexiones de forma controlada
* Validar comandos ingresados por el cliente
