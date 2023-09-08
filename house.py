name = input("whats your name")
if (name == "harry" or "perry" or "veera"):
    print("gryyfin")
elif name == "peroy":
    print("veera")
else:
    print("juo")


#case

match name:
    case "veer" | "sek" | "ii":
        print("he")
    case "harty":
        print("svghd")
    case "patty":
        print("koi")
    case "juu":
        print("slyother")
    case _:
        print("who?")