
# snake and food
snake = [(4, 4), (4, 3), (4, 2)]
food = (6, 6)

win.addch(food[0], food[1], '♡')
# game logic
score = 0

ESC = 27
key = curses.KEY_RIGHT

while key != ESC:
    win.addstr(0, 2, 'Score ' + str(score) + ' ')
    win.timeout(150 - (len(snake)) // 5 + len(snake)//10 % 120) # increase speed

    prev_key = key
    event = win.getch()
    key = event if event != -1 else prev_key

    if key not in [curses.KEY_LEFT, curses.KEY_RIGHT, curses.KEY_UP, curses.KEY_DOWN, ESC]:
        key = prev_key

    # calculate the next coordinates
    y = snake[0][0]
    x = snake[0][1]
    if key == curses.KEY_DOWN:
        y += 1
    if key == curses.KEY_UP:
        y -= 1
    if key == curses.KEY_LEFT:
        x -= 1
    if key == curses.KEY_RIGHT:
        x += 1

    snake.insert(0, (y, x)) # append O(n)

    # check if we hit the border
    if y == 0: break
    if y == WINDOW_HEIGHT-1: break
    if x == 0: break
    if x == WINDOW_WIDTH -1: break

    # if snake runs over itself
    if snake[0] in snake[1:]: break

    if snake[0] == food:
        # eat the food
        score += 1
        food = ()
        while food == ():
            food = (randint(1,WINDOW_HEIGHT-2), randint(1,WINDOW_WIDTH -2))
            if food in snake:
                food = ()
        win.addch(food[0], food[1], '♡')
    else:
        # move snake
        last = snake.pop()
        win.addch(last[0], last[1], ' ')

    win.addch(snake[0][0], snake[0][1], '*')

curses.endwin()
print(f"Final score = {score}")
