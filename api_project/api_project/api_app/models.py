from django.db import models

# Create your models here.
class Autor(models.Model):
    id_autor = models.AutoField(primary_key=True, editable=False, db_column='T001IdAutor')
    nombre = models.CharField(max_length=100, db_column='T001Nombre')
    apellido = models.CharField(max_length=100, db_column='T001Apellido')
    biografia = models.CharField(blank=True, db_column='T001Biografia')

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
    class Meta:
        db_table = 'T001Autor'
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
    
class Editorial(models.Model):
    id_editorial = models.AutoField(primary_key=True, editable=False,db_column='T002IdLibro')
    nombre = models.CharField(max_length=100, db_column='T002Nombre')
    direccion = models.TextField(max_length=100, db_column='T002Direccion')
    telefono = models.CharField(max_length= 10,db_column='T002Telefono', blank=True,null=True)

    def _str_(self):
        return self.nombre

    class Meta:
        db_table = 'T002Editorial'
        verbose_name = 'Editorial'
        verbose_name_plural='Editoriales'

class Libro(models.Model):
    id_libro = models.AutoField(primary_key=True, editable=False,db_column='T003IdLibro')
    titulo = models.CharField(max_length=100, db_column='T003Titulo')
    resumen = models.TextField( db_column='T003Resumen')
    isbm = models.CharField(max_length= 20,db_column='T003Isbn', unique=True)
    publicacion = models.DateField(db_column='T003Publicacion')
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE,related_name='libros', db_column='T003IdAutor')
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE, related_name='libros',db_column='T003IdEditorial')

    def _str_(self):
        return self.titulo

    class Meta:
        db_table = 'T003Libro'
        verbose_name = 'Libro'
        verbose_name_plural='Libros'

class Miembro(models.Model):
    id_miembro = models.AutoField(primary_key=True, editable=False,db_column='T004IdMiembro')
    nombre = models.CharField(max_length=40, db_column='T004Nombre')
    apellido = models.TextField(max_length=40, db_column='T004Apellido')
    email = models.EmailField(db_column='T004Email', unique=True)
    fecha_membresia = models.DateField(db_column='T004FechaMembresia',auto_now_add=True)
    

    def _str_(self):
        return self.nombre

    class Meta:
        db_table = 'T004Miembro'
        verbose_name = 'miembro'
        verbose_name_plural='miembros'

class Prestamo(models.Model):
    id_prestamo = models.AutoField(primary_key=True, editable=False,db_column='T005Prestamo')
    fecha_prestamo = models.DateField(db_column='T005FechaPrestamo',auto_now_add=True)
    fecha_devolucion = models.DateField(db_column='T005FechaDevolucion',blank=True, null=True)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE,related_name='prestamos', db_column='T005IdLibro')
    miembro = models.ForeignKey(Miembro, on_delete=models.CASCADE, related_name='prestamos',db_column='T005IdMiembro')

    def _str_(self):
        return self.titulo

    class Meta:
        db_table = 'T005Prestamo'
        verbose_name = 'prestamo'
        verbose_name_plural='prestamos'