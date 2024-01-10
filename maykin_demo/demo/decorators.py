from django.shortcuts import redirect

#can be used with views to limited page access
def authenticated_user(view_func):
    def wrapper_func(response, *args, **kwargs):
        if response.user.is_authenticated == False:
            return redirect('/home')
        else:
            return view_func(response, *args, **kwargs)

    return wrapper_func

def unauthenticated_user(view_func):
    def wrapper_func(response, *args, **kwargs):
        if response.user.is_authenticated:
            return redirect('/home')
        else:
            return view_func(response, *args, **kwargs)

    return wrapper_func
