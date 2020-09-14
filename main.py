import os

def hello(request):
    return f"What's up, {os.environ.get('name')}!"

# functions-framework --target=main --port=2222 --debug