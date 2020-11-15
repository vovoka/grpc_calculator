### example grpc calculator

Install gRPC and gRPC-tools:
```
python -m pip install grpcio  
python -m pip install grpcio-tools  
npm install grpc --global  
```

If you change Calc.proto file then do not forget to re-create `Calc_pb2.py` and `Calc_pb2_grpc.py` by executing:  
```
python -m grpc.tools.protoc  --python_out=. --grpc_python_out=. --proto_path=. Calc.proto
```
  
Update these two files in all directories (server and clients) with new.  
