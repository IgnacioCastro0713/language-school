from sweetify import warning


def form_invalid_decorator(function):
    def wrap(request, form):
        warning(request, 'Verifique la información ingresada.', toast=True, position='top', timer=3000)
        return function(request, form)
    return wrap
