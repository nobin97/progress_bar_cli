# Progress Bar for CLIs

### A simple progress bar for CLIs written in Python 3.

## Usage:
```
  from progress_bar import ProgressBar
  pbr = ProgressBar()
  limit = 10
  for i in range(limit + 1):
      pbr.progress_bar(value=i, final=limit)                 // shows progress using progress bar
      or
      pbr.progress_bar(value=i, final=limit, delay="random") // shows progress with a random delay
      or
      pbr.progress_bar(value=i, final=limit, delay=1)        // shows progress with a 1 sec delay
```
## Customising Bar:
Default Bar length is 100 chars, you can override it by:
```
  pbr = ProgressBar(bar_length=50,   # A 50 chars long progress bar gets initialised
    description="Test description",  # A description can be added like this
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
  pbr.clear_screen = True
  ```
## Theme colors:
A theme color can be set as a string or as a list of strings.
```
pbr = ProgressBar(
    theme_color="yellow"
    or
    theme_color=["light-cyan", "italic", "bold"]
)
```
You should provide the desired color first in the list and then the formatters.

If you give multiple colors, the last one will be applied.

#### The following colors and formatting can be used:
```
Colors:
    'red',
    'yellow',
    'green',
    'dim',
    'blue',
    'magenta',
    'cyan',
    'light-gray',
    'dark-gray',
    'light-red',
    'light-green',
    'light-yellow,
    'light-blue',
    'light-magenta',
    'light-cyan',
    'white'

For extra formatting:
    'italic',
    'invisible',
    'bold',
    'underlined',
    'reverse',
    'hidden'
```
