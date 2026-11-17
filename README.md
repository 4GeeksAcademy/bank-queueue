# Bank Queue - Banking Operations Management System

A Python application that implements a **priority queue system for managing banking operations**. This system processes financial transactions (transfers, deposits, withdrawals, payments) with an intelligent priority-based queue.

## Project Overview

This banking system demonstrates:
- **Priority Queue Implementation** using Python's `heapq` module
- **Data Validation** with frozen dataclasses
- **Operation Management** with atomic queue operations
- **Real-time Statistics** on pending operations

## Features

✨ **Core Features:**
- Add banking operations with client name, operation type, amount, and priority level
- Automatic priority-based processing (1=High, 2=Medium, 3=Low)
- View all pending operations in priority order
- Peek at the next operation without removing it
- Real-time statistics on queue status by priority level
- Input validation and error handling

## Project Structure

```
bank-queueue/
├── main.py              # Main application with queue implementation and CLI
├── README.md           # This file (English documentation)
├── README.es.md        # Spanish documentation
├── learn.json          # Learning resources metadata
└── server.py           # Optional Flask development server
```

## Key Files

### `main.py`
Contains the complete banking operations queue system:

- **BankOperation class**: Dataclass representing a single banking operation with:
  - `client_name` (str): Customer name
  - `operation_type` (str): Type of operation (transfer, deposit, withdrawal, payment)
  - `amount` (float): Transaction amount
  - `priority` (int): Priority level (1-3)
  - `created_at` (datetime): Operation creation timestamp

- **BankOperationQueue class**: Manages operations using a min-heap with methods:
  - `enqueue(operation)`: Add a new operation to the queue
  - `dequeue()`: Remove and return the highest-priority operation
  - `peek()`: View the next operation without removing it
  - `list_queue()`: Get all operations sorted by priority
  - `stats()`: Get count of operations by priority level

- **Main Menu Interface**: Interactive CLI with options to:
  1. Add new operations
  2. Process next operation
  3. View entire queue
  4. Display statistics
  5. Peek at next operation
  6. Exit

## How to Run

### Prerequisites
Ensure Python 3.8+ is installed on your system.

### Execution

```bash
$ python main.py
```

A menu will appear allowing you to interact with the banking operations queue.

## Example Usage

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

## Technical Details

### Priority Queue Behavior
The queue sorts operations by:
1. **Priority level** (1=highest, 3=lowest)
2. **Arrival time** (FIFO for same priority)
3. **Sequence number** (ensures stability)

### Thread Safety Note
For multi-threaded or multi-server environments, this implementation uses a simple heap. For production:
- Use thread locks for single-process, multi-threaded scenarios
- Implement database transactions for distributed systems
- Consider message brokers (RabbitMQ, Redis) for scaling

### Data Validation
All inputs are validated:
- Client names cannot be empty
- Amounts must be positive numbers
- Priority must be 1, 2, or 3
- Timestamps include timezone information

## Error Handling

The system includes proper exception handling:
- `EmptyQueueError`: Attempting to access empty queue
- `ValueError`: Invalid input data
- `TypeError`: Wrong data type provided

## Requirements

- Python 3.8 or higher
- No external dependencies required

## Learning Outcomes

This project teaches:
- Python dataclasses and immutability
- Heap-based priority queue implementation
- DateTime and timezone handling
- Input validation and error handling
- Atomic operations in queue management
- Interactive CLI applications

## Contributors

Built as a practical example of Python data structures and banking system concepts.

## License

Open source for educational purposes.

