


def  chekr(command_name, **kwargs):
    print(command_name)
    print(kwargs["flagname"])


val = "-l"
chekr("wc", filename = "tt.txt", flagname= val)