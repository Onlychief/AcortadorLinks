from src import app
from src.config.db import DB

class UsuariosModel():
    
    def ver_links(self,id_usuario):
    
        cursor = DB.cursor()
        cursor.execute('select * from enlaces where id_usuario= ?',[id_usuario])
        links = cursor.fetchall()
        cursor.close()
        return(links)
        

    def insertar_link(self, link,aleatorio,id_usuario):

        cursor = DB.cursor()
        cursor.execute('insert into enlaces(enlace, aleatorio, id_usuario) values(?,?,?)', (link, aleatorio, id_usuario))
        cursor.close()
    
    def consultar_link(self, codigo):
    
        cursor = DB.cursor()
        cursor.execute('select enlace from enlaces WHERE aleatorio=?',[codigo])
        link = cursor.fetchall()
        cursor.close()
        enlace = str(link)

        caracteres = (")","(","'",",","[","]")
        enlaceLimpio = ""

        for letters in enlace:
            if letters not in caracteres:
                enlaceLimpio = enlaceLimpio + letters

        return(enlaceLimpio)

    def registrar_usuario(self, nombre,correo, clave):
    
        cursor = DB.cursor()
        cursor.execute('insert into usuarios(nombre,email,clave) values(?,?,?)', (nombre,correo,clave))
        cursor.close() 

    def ingreso_usuarios(self, correo, clave):
        
        cursor = DB.cursor()
        cursor.execute('select id from usuarios WHERE Email=? AND Clave =?', (correo,clave))
        id_usuario = cursor.fetchall()
        cursor.close()
        elid = str(id_usuario)

        caracteres = (")","(","'",",","[","]")
        id_limpio = ""

        for letters in elid:
            if letters not in caracteres:
                id_limpio = id_limpio + letters

        return (id_limpio)

    def eliminar_link(self, id_link):
        
        cursor = DB.cursor()
        cursor.execute('delete from enlaces where id = ?', [id_link])
        cursor.close()     
    
    def actualizar_link(self,id_links,nuevo_enlace):
        cursor = DB.cursor()
        cursor.execute('update enlaces set enlace = ? WHERE id = ?', (nuevo_enlace, id_links))
        cursor.close()

          
        
        