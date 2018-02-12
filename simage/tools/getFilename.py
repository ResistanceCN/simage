def get_filename(path, insert_str=''):
    """Get the single path and filename."""
    path_tmp = path.split('/')
    single_path = '/'.join(path_tmp[:-1]) + '/'
    if len(path_tmp) == 1:
        filename = path_tmp[0]
    else:
        filename = path_tmp[-1]
    if insert_str == '':
        single_filename = filename
    else:
        single_filename = insert_str + '.' + filename

    return single_path, single_filename
