


def verbosedFeedback(exc):
    accepted = ['email', 'name']
    err = str(exc).strip().replace("'", '')
    if err in accepted: 
        return err 
    else: 
        return 'unknown error'