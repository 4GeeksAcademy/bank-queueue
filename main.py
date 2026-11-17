"""Sistema de Gestión de Operaciones Bancarias con Cola de Prioridades.

Implementa una cola de prioridades para procesar operaciones bancarias.
Cada operación tiene un nivel de prioridad (1=alta, 2=media, 3=baja).

Consideraciones importantes:
- Mantener un registro de operaciones en proceso, actualizarlo dentro del
mismo bloqueo. Después liberar el bloqueo y realizar la operación.

- No utilizar peek() seguido de dequeue() como operaciones
independientes para reservar una operación.

- Si una operación de alta prioridad se inserta antes de la extracción atómica,
tendrá prioridad. Si llega después, será la siguiente: no
interrumpe una operación ya retirada para su procesamiento.

- Para varios procesos o servidores, un Lock de hilos no basta:
haría falta una cola compartida con operaciones atómicas o una
transacción en base de datos.
"""

from dataclasses import dataclass, field
from datetime import datetime, timezone
import heapq
from itertools import count


class EmptyQueueError(IndexError):
    """Se intentó consultar o extraer de una cola vacía."""


@dataclass(frozen=True)
class BankOperation:
    client_name: str
    operation_type: str
    amount: float
    priority: int
    created_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    def __post_init__(self):
        if not isinstance(self.client_name, str) or not self.client_name.strip():
            raise ValueError("El nombre del cliente no puede estar vacío.")

        if not isinstance(self.operation_type, str) or not self.operation_type.strip():
            raise ValueError("El tipo de operación no puede estar vacío.")

        if not isinstance(self.amount, (int, float)) or self.amount <= 0:
            raise ValueError("El monto debe ser un número positivo.")

        if (
            type(self.priority) is not int
            or self.priority not in (1, 2, 3)
        ):
            raise ValueError("La prioridad debe ser un entero entre 1 (alta) y 3 (baja).")

        if not isinstance(self.created_at, datetime):
            raise ValueError("La fecha debe ser un datetime.")

        if (
            self.created_at.tzinfo is None
            or self.created_at.utcoffset() is None
        ):
            raise ValueError("La fecha debe incluir zona horaria.")

        object.__setattr__(self, "client_name", self.client_name.strip())
        object.__setattr__(self, "operation_type", self.operation_type.strip())
        object.__setattr__(
            self,
            "created_at",
            self.created_at.astimezone(timezone.utc),
        )


class BankOperationQueue:
    def __init__(self):
        self._heap = []
        self._sequence = count()

    def enqueue(self, operation: BankOperation) -> None:
        if not isinstance(operation, BankOperation):
            raise TypeError("Debes proporcionar una operación bancaria válida.")

        heapq.heappush(
            self._heap,
            (
                operation.priority,
                operation.created_at,
                next(self._sequence),
                operation,
            ),
        )

    def dequeue(self) -> BankOperation:
        if not self._heap:
            raise EmptyQueueError("No hay operaciones en espera.")
        return heapq.heappop(self._heap)[3]

    def peek(self) -> BankOperation:
        if not self._heap:
            raise EmptyQueueError("No hay operaciones en espera.")
        return self._heap[0][3]

    def list_queue(self) -> list[BankOperation]:
        return [entry[3] for entry in sorted(self._heap)]

    def stats(self) -> dict[int, int]:
        result = {1: 0, 2: 0, 3: 0}
        for entry in self._heap:
            result[entry[3].priority] += 1
        return result


def show_operation(operation: BankOperation) -> str:
    created = operation.created_at.strftime("%Y-%m-%d %H:%M:%S UTC")
    return (
        f"{operation.client_name} | {operation.operation_type} | "
        f"${operation.amount:.2f} | Prioridad {operation.priority} | "
        f"Creada: {created}"
    )


def main() -> None:
    queue = BankOperationQueue()

    menu = """
--- Cola de Operaciones Bancarias ---
1. Añadir operación
2. Procesar siguiente operación
3. Ver cola
4. Ver estadísticas
5. Consultar siguiente sin procesarla
0. Salir
"""

    while True:
        try:
            print(menu)
            option = input("Elige una opción: ").strip()

            if option == "1":
                client_name = input("Nombre del cliente: ")
                operation_type = input("Tipo de operación (transferencia/depósito/retiro/pago): ")
                amount = float(input("Monto: $"))
                priority = int(input("Prioridad (1 alta, 2 media, 3 baja): "))
                operation = BankOperation(client_name, operation_type, amount, priority)
                queue.enqueue(operation)
                print(f"Operación añadida: {show_operation(operation)}")

            elif option == "2":
                operation = queue.dequeue()
                print(f"Procesando: {show_operation(operation)}")
                print("✓ Operación completada.\n")

            elif option == "3":
                operations = queue.list_queue()
                if not operations:
                    print("No hay operaciones en espera.\n")
                else:
                    for position, op in enumerate(operations, start=1):
                        print(f"{position}. {show_operation(op)}")
                    print()

            elif option == "4":
                stats = queue.stats()
                print("--- Estadísticas de Prioridad ---")
                print(f"Alta (1): {stats[1]}")
                print(f"Media (2): {stats[2]}")
                print(f"Baja (3): {stats[3]}")
                print(f"Total: {sum(stats.values())}\n")

            elif option == "5":
                print(f"Siguiente operación: {show_operation(queue.peek())}\n")

            elif option == "0":
                print("Programa finalizado.")
                break

            else:
                print("Opción no válida.\n")

        except EmptyQueueError as error:
            print(f"⚠ {error}\n")
        except ValueError as error:
            print(f"❌ Entrada no válida: {error}\n")
        except (EOFError, KeyboardInterrupt):
            print("\nPrograma finalizado.")
            break


if __name__ == "__main__":
    main()


if __name__ == "__main__":
    main()