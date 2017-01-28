def remove_duplicates(string):
    prefix = "abcdefghijklmnopqrstuvwxyz"
    out = ""
    dof = ""
    c = 0
    if (type(string) == str):
        for char in string:
            if char in prefix:
                c+=1
            else:
                c-=1
    if c== len(string):
          for i in string:
              if i not in out:
                  out += i
              else:
                  dof += i
          return ("".join(sorted(out)), len(dof))


print remove_duplicates('reesstrf')
