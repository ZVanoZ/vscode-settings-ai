import json
import sys
import subprocess

def run_pwd_command():
    """Выполняет команду 'pwd' и возвращает вывод."""
    try:
        result = subprocess.run(["pwd"], capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"Error executing pwd: {e.stderr.strip()}"

def handle_request(request):
    """Обрабатывает входящий JSON-RPC запрос."""
    method = request.get("method")
    params = request.get("params")
    id = request.get("id")

    if method == "getTools":
        # MCP-сервер должен сообщить Continue, какие инструменты он предоставляет
        tools = [
            {
                "name": "get_current_directory",
                "description": "Получает текущий рабочий каталог, используя команду 'pwd'.",
                "parameters": {
                    "type": "object",
                    "properties": {} # Инструмент не требует параметров
                }
            }
        ]
        return {"jsonrpc": "2.0", "result": {"tools": tools}, "id": id}
    elif method == "runTool":
        # Continue просит выполнить один из инструментов
        tool_name = params.get("name")
        if tool_name == "get_current_directory":
            pwd_output = run_pwd_command()
            return {"jsonrpc": "2.0", "result": pwd_output, "id": id}
        else:
            return {"jsonrpc": "2.0", "error": {"code": -32601, "message": f"Tool '{tool_name}' not found"}, "id": id}
    
    # Обработка неизвестных методов
    return {"jsonrpc": "2.0", "error": {"code": -32601, "message": f"Method '{method}' not found"}, "id": id}

def main():
    """Основной цикл сервера: читает stdin, пишет в stdout."""
    # Убедимся, что буферизация выключена для stdin/stdout
    sys.stdin = open(sys.stdin.fileno(), 'r', buffering=1)
    sys.stdout = open(sys.stdout.fileno(), 'w', buffering=1)

    while True:
        try:
            line = sys.stdin.readline()
            if not line: # EOF
                break
            
            request = json.loads(line)
            response = handle_request(request)
            sys.stdout.write(json.dumps(response) + "\n")
            sys.stdout.flush()
        except json.JSONDecodeError:
            sys.stderr.write("Invalid JSON received. Skipping.\n")
            sys.stderr.flush()
        except Exception as e:
            sys.stderr.write(f"MCP Server Error: {e}\n")
            sys.stderr.flush()
            # Можно отправить ошибку в Continue, но для простоты просто логируем

if __name__ == "__main__":
    main()