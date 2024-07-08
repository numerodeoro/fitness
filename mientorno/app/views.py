from flask import jsonify, request # retorna una respuesta en un archivo json
from app.models import Suscripcion

def index(): # --> aca usamos la funcion "index", que luego si queremos usarla en otro archivo, debemos
    return jsonify({"message": "Suscripciones Fitness-360"}) 


def create_suscripcion():
    data = request.json
    new_suscripcion = Suscripcion(nombre=data['nombre'], edad=data['edad'], mail=data['mail'], telefono=data['telefono'])
    new_suscripcion.save()
    return jsonify({'message': 'Suscripción creada satisfactoriamente'}), 201

def get_all_suscripciones():
    suscripciones = Suscripcion.get_all()
    return jsonify([suscripcion.serialize() for suscripcion in suscripciones])

def get_suscripcion(id_suscripcion):
    suscripcion = Suscripcion.get_by_id(id_suscripcion)
    if not suscripcion:
        return jsonify({'message': 'Suscripción no encontrada'}), 404
    return jsonify(suscripcion.serialize())

def update_suscripcion(id_suscripcion):
    suscripcion = Suscripcion.get_by_id(id_suscripcion)
    if not suscripcion:
        return jsonify({'message': 'Suscripción no encontrada'}), 404
    data = request.json
    suscripcion.nombre = data['nombre']
    suscripcion.edad = data['edad']
    suscripcion.mail = data['mail']
    suscripcion.telefono = data['telefono']
    suscripcion.save()
    return jsonify({'message': 'Suscripción actualizada satisfactoriamente'})

def delete_suscripcion(id_suscripcion):
    suscripcion = Suscripcion.get_by_id(id_suscripcion)
    if not suscripcion:
        return jsonify({'message': 'Suscripción no encontrada'}), 404
    suscripcion.delete()
    return jsonify({'message': 'Suscripción eliminada satisfactoriamente'})
