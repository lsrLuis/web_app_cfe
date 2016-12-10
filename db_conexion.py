import web

db = web.database(dbn='mysql', db='cfe', user='root', pw='')

def get_user(username):
    return db.select('usuarios', where='nombre=$username',vars=locals())

def get_pagos(id):
    return db.select('pagos', where='id_usuario='+id)

def get_new(direccion, num_medidor, lec_actual, periodo_consumo, fecha_pago, total_pago, id_usuario):
    db.insert('pagos',direccion=direccion,num_medidor=num_medidor,lec_actual=lec_actual,periodo_consumo=periodo_consumo,fecha_pago=fecha_pago,total_pago=total_pago,id_usuario=id_usuario)

def get_data(id):
    try:
        return db.select('pagos', where='id_pago=$id', vars=locals())[0]
    except IndexError:
        return None

def delete(id):
    db.query("DELETE FROM `cfe`.`pagos` WHERE `id_pago`="+id)

def update(direccion, num_medidor, lec_actual, periodo_consumo, fecha_pago, total_pago, id):
    db.update('pagos', where="id_pago="+id,direccion=direccion,num_medidor=num_medidor,lec_actual=lec_actual,periodo_consumo=periodo_consumo,fecha_pago=fecha_pago,total_pago=total_pago)
