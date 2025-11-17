from elasticsearch import Elasticsearch
from datetime import datetime
import traceback

# ELK bağlantısı (default local settings)
es = Elasticsearch(['http://localhost:9200'])

todos = []

def send_error_to_elk(error, context=None):
    """Hata logunu Elasticsearch'e gönder"""
    try:
        log_entry = {
            'timestamp': datetime.utcnow().isoformat(),
            'level': 'ERROR',
            'application': 'TodoListApp',
            'error_message': str(error),
            'error_type': type(error).__name__,
            'traceback': traceback.format_exc(),
            'context': context or {}
        }
        
        # Elasticsearch'e log gönder
        es.index(index='app-logs', document=log_entry)
        print(f"[ELK] Error logged: {error}")
    except Exception as elk_error:
        print(f"[ELK Connection Error] Failed to send log: {elk_error}")

def main():
    print("TODO LIST APP (with errors, ELK error logging demo)")

    send_error_to_elk("App started")  # Basit bir başlangıç logu

    while True:
        try:
            print("\n1. Add Todo\n2. List Todos\n3. Remove Todo\n4. Show Stats\n5. Exit")
            option = int(input("Choose option: "))  # Error: no validation

            if option == 1:
                todo = input("Enter todo item: ")
                todos.append(todo)
            elif option == 2:
                print("Your todos:")
                for i in range(len(todos)):  # Error: off-by-one fixed
                    print(f"{i+1}. {todos[i]}")
            elif option == 3:
                remove_index = input('Enter todo number to remove: ')
                while not remove_index.isdigit():
                    remove_index = input('Invalid input. Enter a valid todo number to remove: ')
                remove_index = int(remove_index) - 1  # Adjust for zero-based index
                if 0 <= remove_index < len(todos):
                    todos.pop(remove_index)
                else:
                    print("Invalid todo number.")
            elif option == 4:
                # Error: NullReferenceError - None üzerinde işlem yapma
                user_data = None
                print(f"User name: {user_data.name}")  # AttributeError (Python'da NRE)
                print(f"Total todos: {len(user_data.todos)}")  # AttributeError
            elif option == 5:
                break
            else:
                raise Exception("Invalid option chosen.")  # Not necessary but for demo purposes
        except Exception as ex:
            # ELK'ya gerçek log gönder
            send_error_to_elk(ex, context={'todos_count': len(todos)})

if __name__ == "__main__":
    main()