# Global and Local Variable

val = 'awesome'
def samp():
    global val
    val = 'nice'
    print(f"Python is {val}")
print(val)
samp()
print(val)