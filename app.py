import mouse
import time
import keyboard as kb

class App:
  def __init__(self) -> None:
    self.quit = False
    self.running = False

    self.quit_kbd = kb.add_hotkey('q', lambda: self.stop())
    self.toggle_kbd = kb.add_hotkey('s', lambda: self.toggle())

  def run(self):
    print('Started auto clicker')
    while not self.quit:
      if self.running:
        mouse.double_click()
        mouse.double_click()
        mouse.double_click()
        time.sleep(0.001)

  def start(self):
    self.quit = False
    self.running = True

  def stop(self):
    self.quit = True

  def toggle(self):
    self.running = not self.running
    print(f'Is running: {self.running}')

  def resume(self):
    self.running = True

  def pause(self):
    self.running = False