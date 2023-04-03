# python3 chapter-6/backwardForward.py

current_state_url = ''

forward_stack = []
backward_stack = []

def visit_new_url(url):
    global current_state_url

    if (current_state_url != ''):
        backward_stack.append(current_state_url)
    
    current_state_url = url

def forward():
    if (len(forward_stack) == 0 or current_state_url == forward_stack[-1]):
        print('Not Available')
        return
    else:
        backward_stack.append(current_state_url)
        current_state_url = forward_stack[-1]
        forward_stack.pop()

def backward():
    if(len(backward_stack) != 0 or current_state_url == backward_stack[-1]):
        print('Not Available')
        return
    else:
        forward_stack.append(current_state_url)
        current_state_url = backward_stack[-1]
        backward_stack[-1]

def simulatorFunction():
  # Current URL
  url = "ajay.com"
  
  # Visit the current URL
  visit_new_url(url)
  
  # Print the current URL
  print("Current URL is: " + current_state_url)
  
  # New current URL
  url = "abc.com"
  
  # Visit the current URL
  visit_new_url(url)
  
  # Print the current URL
  print("Current URL is: " + current_state_url)
  
  # Pressed backward button
  backward()
  
  # Print the current URL
  print("Current URL after pressing" + " Backward button is: " + current_state_url)
  
  # Pressed forward button
  forward()
  
  # Print the current URL
  print("Current URL after pressing" + " Forward button is: " + current_state_url)
  
  # New current URL
  url = "nikhil.com"
  
  # Visit the current URL
  visit_new_url(url)
  
  # Print the current URL
  print("Current URL is: " + current_state_url)
  
  # Pressed forward button
  forward()
  
  # Print the current URL
  print("Current URL after pressing" + " Forward button is: " + current_state_url)
  # Pressed backward button
  backward()
  
  # Print the current URL
  print("Current URL after pressing" + " Backward button is: " + current_state_url)
   
# Function to simulate process of
# pressing forward & backward button

if __name__ == "__main__":
    simulatorFunction()
 