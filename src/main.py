from person import Autor
from book import LibroDigital, Libro, LibroImpreso, AudioLibro

def main() -> None:
    libro1 = LibroImpreso(
        titulo = "Death Metal",
        isbn = "1234",
        genero = "Novela",
        formato = "Pasta dura",
        paginas = 100,
        valor = 100000,
        num_ejemplares = 5
    )

    libro1 = AudioLibro(
        titulo = "Back in Black",
        isbn = "7842",
        genero = "Novela",
        formato = ".mp4",
        valor = 80000,
        duracion = 200
    )

if __name__ == '__main__':
    main()