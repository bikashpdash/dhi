import grpc
from .grpclib import Service_pb2
from .grpclib import Service_pb2_grpc
from concurrent import futures
# add the following import statement to use server reflection
from grpc_reflection.v1alpha import reflection
from . import app
from .utils import match_check


class Servicer(Service_pb2_grpc.ServiceServicer):
    
    def Ping(self, request, context):
        response =Service_pb2.Pong()
        response.msg="Congrats, Service Working !!"
        return response
    
    def Match(self, request, context):
        response=Service_pb2.MatchResponse()      
        
        
        if request.level== Service_pb2.MatchRequest.MatchLevel.simple:
            response.ratio=match_check.simple_match(request.content,request.tokens)
        elif request.level== Service_pb2.MatchRequest.MatchLevel.partial:
            response.ratio=match_check.partial_match(request.content,request.tokens)
        elif request.level== Service_pb2.MatchRequest.MatchLevel.token:
            response.ratio=match_check.relevant_match(request.content,request.tokens)
        
        return response


def serve(port):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    Service_pb2_grpc.add_ServiceServicer_to_server(Servicer(), server)
    
    if app.config['dev']=='true':
        # the reflection service will be aware of "Service" and "ServerReflection" services.
        SERVICE_NAMES = (
            Service_pb2.DESCRIPTOR.services_by_name['Service'].full_name,
            reflection.SERVICE_NAME,
        )
        reflection.enable_server_reflection(SERVICE_NAMES, server)
    
    server.add_insecure_port('[::]:%s' % port)
    server.start()
    server.wait_for_termination()
