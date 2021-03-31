import grpc
from .grpclib import DhiGRPC_pb2
from .grpclib import DhiGRPC_pb2_grpc
from concurrent import futures

class Servicer(DhiGRPC_pb2_grpc.DhiGRPCServicer):
    
    def Ping(self, request, context):
        response =DhiGRPC_pb2.Echo
        response.value=request.value
        return response



def serve(port):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    DhiGRPC_pb2_grpc.add_DhiGRPCServicer_to_server(Servicer(), server)
    server.add_insecure_port('[::]:%s' % port)
    server.start()
    server.wait_for_termination()