"""
Determina si un número es primo y permite listar primos en un rango.
Menú interactivo por línea de comandos.
"""

import math
import sys


def es_primo(n: int) -> bool:
    """Devuelve True si n es primo, False en caso contrario."""
    if n < 2:
        return False
    limite = int(math.isqrt(n))
    for i in range(2, limite + 1):
        if n % i == 0:
            return False
    return True


def primos_en_rango(inicio: int, fin: int) -> list[int]:
    """Devuelve la lista de números primos en [inicio, fin]."""
    return [n for n in range(inicio, fin + 1) if es_primo(n)]


# ───── helpers ─────

def _leer_entero(mensaje: str) -> int | None:
    """Lee un entero del usuario. Retorna None si no es válido."""
    try:
        return int(input(mensaje))
    except ValueError:
        print("❌ Eso no es un número entero válido.")
        return None


def _pausa() -> None:
    input("\nPresioná Enter para volver al menú...")


# ───── opciones del menú ─────

def _opcion_verificar() -> None:
    n = _leer_entero("Ingresá un número entero: ")
    if n is None:
        _pausa()
        return
    msg = "✅ es primo." if es_primo(n) else "❌ NO es primo."
    print(f"{n} {msg}")
    _pausa()


def _opcion_rango() -> None:
    inicio = _leer_entero("Inicio del rango: ")
    if inicio is None:
        _pausa()
        return
    fin = _leer_entero("Fin del rango: ")
    if fin is None:
        _pausa()
        return
    if inicio > fin:
        print("⚠️  El inicio no puede ser mayor que el fin.")
        _pausa()
        return

    primos = primos_en_rango(inicio, fin)
    print(f"\n🔢 Primos entre {inicio} y {fin}:")
    if primos:
        # mostrar de a 15 por línea
        for i in range(0, len(primos), 15):
            print("  " + "  ".join(str(p) for p in primos[i:i+15]))
        print(f"\n📊 Total: {len(primos)} primos encontrados.")
    else:
        print("  (ninguno)")
    _pausa()


# ───── menú principal ─────

MENU = """
═══════════════════════════════
   VERIFICADOR DE NÚMEROS PRIMOS
═══════════════════════════════
   1. Verificar si un número es primo
   2. Listar primos en un rango
   3. Salir
"""


def main() -> None:
    while True:
        print(MENU)
        opcion = input("Elegí una opción [1-3]: ").strip()

        if opcion == "1":
            _opcion_verificar()
            continue
        if opcion == "2":
            _opcion_rango()
            continue
        if opcion == "3":
            print("👋 ¡Chau!")
            sys.exit(0)

        print("❌ Opción inválida. Elegí 1, 2 o 3.")
        _pausa()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 ¡Chau!")
        sys.exit(0)
