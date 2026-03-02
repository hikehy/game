from .clearconsole import clearconsole
def dodgeresult(name, result):
    clearconsole()
    if name == "player":
        print("you used dodge used dodge...")
        input("press enter to see result")
        print("your dodge ", result)
        input("press enter to continue")
    else:
        print("enemy used dodge...")
        input("press enter to see result")
        print("enemy dodge ", result)
        input("press enter to continue")
    clearconsole()
