import gym
env = gym.make("FrozenLake-v0")
observation = env.reset()


class _Getch:
    def __call__(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(3)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

inkey = _Getch()

LEFT = 0
DOWN = 1
RIGHT = 2
UP = 3

arrow_keys = {
        '\x1b[A': UP,
        '\x1b[B': DOWN,
        '\x1b[C': RIGHT,
        '\x1b[D': LEFT,
        }


for _ in range(1000):
  env.render()
  action = env.action_space.sample()
  observation, reward, done, info = env.step(action)

