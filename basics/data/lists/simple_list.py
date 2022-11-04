def directions():
  directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
  return directions

def run():
  print(directions())

if __name__ == "__main__": # Remember, you can always add the following code to call your function run.  The if statement ensures that the function is only called when the file is executed directly and not when it is imported into another module.
    run()