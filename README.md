# amatuerCTF_Censorship
amatuerCTF 2023  misc/Censorship expoit   (unintended solve)


Im using a python if else statement to leak the flag!!!  :)


data = f"if chr({ord(str(i))}) in _[{len(found)}]: ord(2)"  <<<  this line


if true it will try to ord(2)  which will result in an error since we can't ord integers  in this case error means character exists


flag : amateursCTF{i_l0v3_overwr1t1nG_functions..:D}
