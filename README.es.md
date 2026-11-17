# Bank Queue - Sistema de Gestión de Operaciones Bancarias

Una aplicación en Python que implementa un **sistema de cola con prioridades para gestionar operaciones bancarias**. Este sistema procesa transacciones financieras (transferencias, depósitos, retiros, pagos) con una cola inteligente basada en niveles de prioridad.

## Descripción del Proyecto

Este sistema bancario demuestra:
- **Implementación de Cola con Prioridades** usando el módulo `heapq` de Python
- **Validación de Datos** con dataclasses congeladas
- **Gestión de Operaciones** con operaciones atómicas en cola
- **Estadísticas en Tiempo Real** sobre operaciones pendientes

## Características

✨ **Características Principales:**
- Añadir operaciones bancarias con nombre del cliente, tipo de operación, monto y nivel de prioridad
- Procesamiento automático basado en prioridades (1=Alta, 2=Media, 3=Baja)
- Ver todas las operaciones pendientes ordenadas por prioridad
- Consultar la siguiente operación sin removerla
- Estadísticas en tiempo real del estado de la cola por nivel de prioridad
- Validación de entrada y manejo de errores

## Estructura del Proyecto

```
bank-queueue/
├── main.py              # Aplicación principal con implementación de cola e interfaz CLI
├── README.md           # Documentación en inglés
├── README.es.md        # Documentación en español (este archivo)
├── learn.json          # Metadatos de recursos de aprendizaje
└── server.py           # Servidor Flask opcional para desarrollo
```

## Archivos Clave

### `main.py`
Contiene el sistema completo de cola de operaciones bancarias:

- **Clase BankOperation**: Dataclass que representa una operación bancaria con:
  - `client_name` (str): Nombre del cliente
  - `operation_type` (str): Tipo de operación (transferencia, depósito, retiro, pago)
  - `amount` (float): Monto de la transacción
  - `priority` (int): Nivel de prioridad (1-3)
  - `created_at` (datetime): Marca de tiempo de creación

- **Clase BankOperationQueue**: Gestiona operaciones usando un min-heap con métodos:
  - `enqueue(operation)`: Añade una nueva operación a la cola
  - `dequeue()`: Extrae y retorna la operación de mayor prioridad
  - `peek()`: Consulta la siguiente operación sin removerla
  - `list_queue()`: Obtiene todas las operaciones ordenadas por prioridad
  - `stats()`: Obtiene conteos de operaciones por nivel de prioridad

- **Interfaz de Menú Interactivo**: CLI con opciones para:
  1. Añadir nuevas operaciones
  2. Procesar siguiente operación
  3. Ver cola completa
  4. Mostrar estadísticas
  5. Consultar siguiente operación
  6. Salir

## Cómo Ejecutar

### Requisitos Previos
Asegúrate de tener Python 3.8+ instalado en tu sistema.

### Ejecución

```bash
$ python main.py
```

Aparecerá un menú que te permitirá interactuar con la cola de operaciones bancarias.

## Ejemplo de Uso

```
--- Cola de Operaciones Bancarias ---
1. Añadir operación
2. Procesar siguiente operación
3. Ver cola
4. Ver estadísticas
5. Consultar siguiente sin procesarla
0. Salir

Elige una opción: 1
Nombre del cliente: Juan García
Tipo de operación (transferencia/depósito/retiro/pago): transferencia
Monto: $5000
Prioridad (1 alta, 2 media, 3 baja): 2
Operación añadida: Juan García | transferencia | $5000.00 | Prioridad 2 | Creada: 2026-11-17 13:40:37 UTC
```

## Detalles Técnicos

### Comportamiento de la Cola de Prioridades
La cola ordena las operaciones por:
1. **Nivel de prioridad** (1=máxima, 3=mínima)
2. **Hora de llegada** (FIFO para la misma prioridad)
3. **Número de secuencia** (garantiza estabilidad)

### Nota sobre Seguridad en Hilos
Para entornos multi-hilo o multi-servidor, esta implementación usa un heap simple. Para producción:
- Usa locks de hilos para escenarios de un solo proceso con múltiples hilos
- Implementa transacciones de base de datos para sistemas distribuidos
- Considera sistemas de colas de mensajes (RabbitMQ, Redis) para escalabilidad

### Validación de Datos
Todas las entradas se validan:
- Los nombres de clientes no pueden estar vacíos
- Los montos deben ser números positivos
- La prioridad debe ser 1, 2 o 3
- Las marcas de tiempo incluyen información de zona horaria

## Manejo de Errores

El sistema incluye manejo apropiado de excepciones:
- `EmptyQueueError`: Intento de acceder a cola vacía
- `ValueError`: Datos de entrada inválidos
- `TypeError`: Tipo de dato incorrecto

## Requisitos

- Python 3.8 o superior
- Sin dependencias externas requeridas

## Resultados de Aprendizaje

Este proyecto enseña:
- Dataclasses de Python e inmutabilidad
- Implementación de cola de prioridades basada en heap
- Manejo de DateTime y zonas horarias
- Validación de entrada y manejo de errores
- Operaciones atómicas en gestión de colas
- Aplicaciones CLI interactivas

## Contribuidores

Construido como un ejemplo práctico de estructuras de datos de Python y conceptos de sistemas bancarios.

## Licencia

Código abierto para propósitos educativos.

