# Basci error handling with a try/except block

def divider(num, den, alt):

    try:
        return num / den
    except ZeroDivisionError:
        return f'Cannot divide by: {alt}!'
    except TypeError:
        return f'Numerator and denominator must be numbers!'
    finally:
        return 'Exiting'