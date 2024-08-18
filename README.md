# gRPC FastAPI services

---

### API FastAPI Gateway
```python
    uvicorn api_gateway.api:app --reload
```

### To compile protobuf files
```python
    python -m grpc_tools.protoc --python_out=. --grpc_python_out=. --pyi_out=. --proto_path=. ./protos/*.proto 
```

## Services

### For starting Book service
```python
    python book_server.py
```

### For starting Author service
```python
    python author_server.py
```
