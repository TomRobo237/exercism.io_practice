def handle_error_by_throwing_exception():
    raise Exception('Heres a General Error')


def handle_error_by_returning_none(input_data):
    if input_data == '1':
        return(1)

def handle_error_by_returning_tuple(input_data):
    if input_data == '1':
        return (True,1)
    return (False,1)
    


def filelike_objects_are_closed_on_exception(filelike_object):
    filelike_object.open()
    try:
        filelike_object.do_something()
    except:
        filelike_object.close()
        raise Exception('Error')
    filelike_object.close()
