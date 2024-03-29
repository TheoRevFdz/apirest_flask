from flask_restful import request


def check(form_class):
    def warpper(func):
        def decorated(*args, **kwargs):
            form = form_class(request.form)
            if not form.validate():
                print(form.errors)
                res = {'status': 'ERROR', 'missing': []}
                for field, error in form.errors.items():
                    temp = {'field': field, 'info': getattr(form, field).label.text,
                            'errors': error}
                    res['missing'].append(temp)
                return res, 400

            # return 'ok', 200
            return func(*args, **kwargs)

        return decorated

    return warpper
