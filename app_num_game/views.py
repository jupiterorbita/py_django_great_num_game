from django.shortcuts import render, redirect
import random # import the random module

# ----------------------------------------------
# ----              INDEX                   ----
# ----------------------------------------------
def index(request):
  print("\n-------- index '/'")
  
  rand_num = request.session.get('the_random_num_in_session', random.randint(1,100))
  # request.session['the_random_num_in_session'] = random.randint(1,100)
  request.session['the_random_num_in_session'] = rand_num
  
  print('\n -- rand int in session? -> ', rand_num , '\n')
  
  # set a default result to display
  if 'result' in request.session:
    pass
  else:
    request.session['result'] = ''
    
  # # set default color
  # if 'color' in request.session:
  #   pass
  # else:
  #   request.session['color'] = 'aqua'
  # alt way:
  request.session.get('color', 'aqua')
  
  
  print(request.session)
  print('the_random_num_in_session = ', request.session['the_random_num_in_session'])
  
  return render(request, 'index.html')

# ----------------------------------------------
# ----       PROCCESS FORM                  ----
# ----------------------------------------------
def process_form(request):
  print("\n-------- process_form '/process_form'")
  if request.method == "POST":
    print('\n --- got POST ---')
    
    # alt put 'required' inside input
    # catch if user doesn't enter a value:
    if 'user_guessed_num' in request.POST:
      if request.POST['user_guessed_num'].isdigit():
      
        # print('request.POST =', request.POST)
        print("* * * user guessed => ", request.POST['user_guessed_num'])
        cpu_num = request.session['the_random_num_in_session']
        user_guess = int(request.POST['user_guessed_num'])
        
        # edge cases
        if user_guess > 100 or user_guess < 0:
          request.session['result'] = "let's not get too crazy 🤪"
          request.session['color'] = 'orange'
          
        elif user_guess < cpu_num:
          print(f'TOO LOW! user:{user_guess} < {cpu_num}')
          request.session['result'] = "too low!"
          request.session['color'] = 'red'
        
        elif user_guess > cpu_num:
          print(f'TOO HIGH! user:{user_guess} > {cpu_num}')
          request.session['result'] = "too high!"
          request.session['color'] = 'blue'
        
        elif user_guess == cpu_num:
          print(f'you WON! user:{user_guess} = {cpu_num}')
          request.session['result'] = "you won!! 🎊🥳"
          request.session['color'] = 'green'
          # request.session.clear()

      else:
        # user did not input a number!
        request.session['result'] = "ENTER a number from 1-100"

  return redirect('/')

# ----------------------------------------------
# ----          CLEAR SESSION               ----
# ----------------------------------------------
def clear_session(request):
  request.session.clear()
  if "the_random_num_in_session" in request.session:
    del request.session['the_random_num_in_session']
  return redirect('/')
    