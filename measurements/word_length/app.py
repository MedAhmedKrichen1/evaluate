import evaluate
from evaluate.utils import launch_gradio_widget


module = evaluate.load("word_length")
launch_gradio_widget(module)
