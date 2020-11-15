from __future__ import print_function

import grpc

# import Calc_pb2_grpc
# import Calc_pb2

from .proto import Calc_pb2_grpc, Calc_pb2

def run():
    channel = grpc.insecure_channel('localhost:50050')
    stub = Calc_pb2_grpc.CalculatorStub(channel)

    # 20 + 10
    response = stub.Add(Calc_pb2.AddRequest(n1=20,n2=10))
    print(response.n1)

    # 20 - 10
    response = stub.Substract(Calc_pb2.SubstractRequest(n1=20,n2=10))
    print(response.n1)

    response = stub.Multiply(Calc_pb2.MultiplyRequest(n1=20,n2=10))
    print(response.n1)

    response = stub.Divide(Calc_pb2.DivideRequest(n1=20,n2=10))
    print(response.n1)

if __name__ == '__main__':
    run()
