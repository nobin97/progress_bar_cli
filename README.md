# Progress Bar for CLIs

### A simple Progress Bar written in python 3 for CLIs.

## Usage:
```
  from progress_bar import ProgressBar
  pbr = ProgressBar()
  for i in range(10):
      pbr.progress_bar(value=i, final=10)                 // shows progress using progress bar
      or
      pbr.progress_bar(value=i, final=10, delay="random") // shows progress with a random delay
      or
      pbr.progress_bar(value=i, final=10, delay=1)        // shows progress with a 1 sec delay
```
## Customising Bar:
Default Bar length is 100 chars, you can override it by:
```
  pbr = ProgressBar(bar_length=50,   # A 50 chars long progress bar gets initialised
    in_progress_color="green",       # The color of the in_progress_character can be set like this
    incomplete_color="red",          # The color of the incomplete_character can be set like this
    in_progress_character="+",       # The value of the in_progress_character can be set like this
    incomplete_character="_",        # The value of the incomplete_character can be set like this
    theme_color="light-yellow")      # A theme color for title and completion info can be set like this
```
Default Title is "Progress Bar", override it by:
  ```
  pbr.title = "New Title"
  ```

By default title is shown, you can make it invisible by:
  ```
  pbr.show_title = False
  ```

By default progress bar doesn't clear the screen while updating, override it by:
  ```
  pbr.clear_screen = False
  ```
