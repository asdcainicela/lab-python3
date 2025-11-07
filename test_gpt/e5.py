"""
Desarrolla un sistema completo de gestión de préstamos de libros que cumpla lo siguiente:

1. Almacena un catálogo de libros en 'catalogo.json'. Cada libro debe tener:
   - título
   - autor
   - estado (disponible o prestado)

2. Almacena un registro de usuarios y sus préstamos en 'prestamos.json'.
   Cada préstamo debe incluir:
   - nombre del usuario
   - libro prestado (título)
   - fecha (puede ser texto)
   - devuelto: sí o no

3. El programa debe mostrar un menú con opciones:
   1. Registrar nuevo libro
   2. Mostrar catálogo de libros
   3. Prestar libro
   4. Ver historial de préstamos
   5. Marcar libro como devuelto
   6. Salir

4. Restricciones:
   - No se puede prestar un libro que ya está prestado.
   - Solo se pueden devolver libros que están en estado "prestado".
   - Debe actualizarse el estado del libro según los préstamos.
   - Todo cambio debe guardarse en los archivos.
"""

