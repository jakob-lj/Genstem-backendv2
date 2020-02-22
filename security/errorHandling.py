


def verbosedFeedback(exc):
    accepted = ['email', 'name', 'id', 'token']
    err = str(exc).strip().replace("'", '')
    if err in accepted: 
        return err 
    else: 
        return 'unknown error'