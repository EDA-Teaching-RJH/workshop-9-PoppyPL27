#main entry point
def main():
    from email import CheckEmailValid
    try:
        assert CheckEmailValid("qvahxzeueq@word.nhs.net") == "Valid NHS Email"
    except AssertionError:
        print("Something is wrong this should have returned : Valid NHS Email")
    
    try:
        assert CheckEmailValid("rwvqhptft@thing.nhs.net") == "Valid NHS Email"
    except AssertionError:
        print("Something is wrong this should have returned : Valid NHS Email")

    try:
        assert CheckEmailValid("njvun@word.nhs.net") == "Valid NHS Email"
    except AssertionError:
        print("Something is wrong this should have returned : Valid NHS Email")

    try:
        assert CheckEmailValid("omkueltb@word.govv.uk") == "invalid due to unaccepted email type"
    except AssertionError:
        print("Something is wrong this should have returned : invalid due to unaccepted email type")

    try:
        assert CheckEmailValid("qpzyqnlaq@word.nhs.net") == "Valid NHS Email"
    except AssertionError:
        print("Something is wrong this should have returned : Valid NHS Email")

    try:
        assert CheckEmailValid("dkf*ggnu@word.gov.uk") == "invalid due to unaccepted character"
    except AssertionError:
        print("Something is wrong this should have returned : invalid due to unaccepted character")

    try:
        assert CheckEmailValid("mtnurpnn@word.gov.uk") == "Valid Government Email"
    except AssertionError:
        print("Something is wrong this should have returned : Valid Government Email")

    try:
        assert CheckEmailValid("wiq)jadaa@word.nhs.net") == "invalid due to unaccepted character"
    except AssertionError:
        print("Something is wrong this should have returned : invalid due to unaccepted character")

    try:
        assert CheckEmailValid("fph@jp@word.ac.uk") == "invalid due to unaccepted character"
    except AssertionError:
        print("Something is wrong this should have returned : invalid due to unaccepted character")

    try:
        assert CheckEmailValid("euktfrzm@word.gov.uk") == "Valid Government Email"
    except AssertionError:
        print("Something is wrong this should have returned : Valid Government Email")

if __name__ == "__main__":
    main()