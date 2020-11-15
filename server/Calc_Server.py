from concurrent import futures
import time

import grpc

import Calc_pb2
import Calc_pb2_grpc

_ONE_DAY_IN_SECONDS = 60*60*24

class Calculator(Calc_pb2_grpc.CalculatorServicer):

    def Add(self, request, context):
        return Calc_pb2.AddReply(n1=request.n1 + request.n2)

    def Substract(self, request, context):
        return Calc_pb2.SubstractReply(n1=request.n1 + request.n2)

    def Multiply(self, request, context):
        return Calc_pb2.MultiplyReply(n1=request.n1 * request.n2)

    def Divide(self, request, context):
        return Calc_pb2.DivideReply(n1=request.n1 // request.n2)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    Calc_pb2_grpc.add_CalculatorServicer_to_server(Calculator(), server)
    server.add_insecure_port('[::]:50050')

    server.start()
    print('Server started at 50050')
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
