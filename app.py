# encoding: utf-8
import web
from web import form
import cfe_data
import db_conexion

data = cfe_data.Cfe_data()
data.data_read('data/data_cfe2.csv')
db = db_conexion

render = web.template.render('views/', base='index')
urls = ('/', 'index',
        '/cfe_data','cfe_data',
        '/cfe_data/cfematicos(.*)','cfematicos',
        '/login','login',
        '/historial_pagos', 'historial_pagos',
        '/historial_pagos/new','new',
        '/historial_pagos/edit(.*)','edit',
        '/historial_pagos/delete(.*)','delete')
app = web.application(urls, globals())

data_cfe = form.Form(
        form.Dropdown('Estado', data.data_state()))

sesion = form.Form(
        form.Textbox('Username'),
        form.Password('Password')
    )
nuevo = form.Form(
        form.Textbox('Direccion'),
        form.Textbox('Numero de medidor'),
        form.Textbox('Lectura actual'),
        form.Textbox('Periodo de consumo'),
        form.Textbox('Fecha de pago'),
        form.Textbox('Total del pago')
    )

class index:
    def GET(self):
        return render.intro()

class cfe_data:
    city = []

    def GET(self):
        form = data_cfe()
        return render.cfe_data(form,self.city)

    def POST(self):
        form = data_cfe()
        if not form.validates():
            return render.cfe_data(form,self.city)
        else:
            self.city = data.data_city(str(form.d.Estado))
            return render.cfe_data(form,self.city)

class cfematicos:
    cfematicos = []
    def GET(self, city):
        i = web.input(city = city)
        self.cfematicos = data.data_cfematicos(str(i.city))
        return render.cfematicos(self.cfematicos)
    def POST(self):
        if not form.validates():
            return render.cfematicos(self.cfematicos)
        else:
            return render.cfematicos(self.cfematicos)

class login:
    def GET(self):
        form = sesion()
        return render.login(form)

    def POST(self):
        form = sesion()
        if not form.validates():
            return render.login(form)
        else:
            username = ''
            password = ''
            for row in db.get_user(form.d.Username):
                username = row.nombre
                password = row.contrasena
            if username == form.d.Username and password == form.d.Password:
                raise web.seeother('/cfe_data')
            else:
                return render.login(form)

class historial_pagos:
    def GET(self):
        return render.historial_pagos(db.get_pagos(str(1)))

class new:
    def GET(self):
        form = nuevo()
        return render.new(form)

    def POST(self):
        form = nuevo()
        if not form.validates():
            return render.new(form)
        else:
            db.get_new(form['Direccion'].value,
                 form['Numero de medidor'].value,
                 form['Lectura actual'].value,
                 form['Periodo de consumo'].value,
                 form['Fecha de pago'].value,
                 form['Total del pago'].value,1)
            raise web.seeother('/historial_pagos')

class edit:
    def GET(self, id):
        i = web.input(id = id)
        post = db.get_data(i.id)
        form = nuevo()
        form.fill(post)
        return render.edit(form,i.id)

    def POST(self,id):
        i = web.input(id = id)
        post = db.get_data(i.id)
        form = nuevo()
        if not form.validates():
            return render.new(form,i.id)
        else:
            db.update(form['Direccion'].value,
                 form['Numero de medidor'].value,
                 form['Lectura actual'].value,
                 form['Periodo de consumo'].value,
                 form['Fecha de pago'].value,
                 form['Total del pago'].value,i.id)
            raise web.seeother('/historial_pagos')

class delete:
    def POST(self,id):
        i = web.input(id = id)
        db.delete(i.id)
        raise web.seeother('/historial_pagos')


if __name__=="__main__":
    web.internalerror = web.debugerror
    app.run()
