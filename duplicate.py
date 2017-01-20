def remove_duplicates(string):
    out = " "
    dof = " "
    for i in string:
        if i not in out:
            out += i
        else:
            dof += i

    return (out, len(dof))